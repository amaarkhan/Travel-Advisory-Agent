from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('GEMINI_API_KEY')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def get_weather(city, start_date, end_date):
    weather_info = []
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    
    while current_date <= end_date_obj:
        date_str = current_date.strftime('%Y-%m-%d')
        today = datetime.now().date()
        current_date_obj = current_date.date()
        
        # Use forecast API for future dates, history API for past dates
        if current_date_obj >= today:
            url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&dt={date_str}"
        else:
            url = f"http://api.weatherapi.com/v1/history.json?key={WEATHER_API_KEY}&q={city}&dt={date_str}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if 'error' in data:
                print(f"Error fetching weather for {date_str}: {data['error']['message']}")
                current_date += timedelta(days=1)
                continue
            
            # Handle both forecast and history API responses
            if 'forecast' in data:
                daily_data = data['forecast']['forecastday'][0]
            else:
                daily_data = data['forecast']['forecastday'][0]
            
            weather_info.append({
                'date': date_str,
                'condition': daily_data['day']['condition']['text'],
                'avg_temp_c': daily_data['day']['avgtemp_c'],
                'max_temp_c': daily_data['day']['maxtemp_c'],
                'min_temp_c': daily_data['day']['mintemp_c'],
                'humidity': daily_data['day']['avghumidity']
            })
        
        except Exception as e:
            print(f"Error fetching weather data for {date_str}: {e}")
        
        current_date += timedelta(days=1)
    
    return weather_info

def get_places_from_gemini(city):
    """Use Gemini API to get places to visit for any city"""
    try:
        import google.generativeai as genai
        
        # Configure Gemini API
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        # Create prompt for places to visit
        prompt = f"""
        List the top 10 most popular and must-visit tourist attractions, landmarks, and places of interest in {city}.
        Include famous museums, historical sites, parks, monuments, religious sites, and cultural attractions.
        Please provide only the names of the places, one per line, without descriptions or numbers.
        Make sure these are real, well-known places that actually exist in {city}.
        """
        
        response = model.generate_content(prompt)
        
        if response and response.text:
            # Parse the response to extract place names
            places = []
            lines = response.text.strip().split('\n')
            
            for line in lines:
                # Clean up the line (remove bullets, numbers, etc.)
                place = line.strip()
                place = place.lstrip('•-*123456789. ')
                place = place.strip()
                
                if place and len(place) > 3:  # Filter out very short strings
                    places.append(place)
            
            # Limit to top 10 places
            return places[:10] if places else None
        
    except Exception as e:
        print(f"Error getting places from Gemini: {e}")
    
    return None

def get_places_to_visit(city):
    # First try to get places using Gemini API
    places = get_places_from_gemini(city)
    if places:
        return places
    
    # If Gemini fails, try OpenStreetMap Nominatim API
    osm_places = []
    try:
        # Get coordinates using Nominatim
        nominatim_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
        headers = {'User-Agent': 'Travel-Advisory-Agent/1.0'}
        
        response = requests.get(nominatim_url, headers=headers)
        if response.status_code == 200:
            geo_data = response.json()
            if geo_data:
                lat = float(geo_data[0]['lat'])
                lon = float(geo_data[0]['lon'])
                
                # Use Overpass API to get places of interest
                overpass_url = "https://overpass-api.de/api/interpreter"
                
                # Query for tourist attractions, museums, monuments, etc.
                overpass_query = f"""
                [out:json][timeout:25];
                (
                  node["tourism"~"attraction|museum|monument|castle|viewpoint|artwork|gallery"]["name"](around:15000,{lat},{lon});
                  node["historic"~"monument|castle|building|ruins"]["name"](around:15000,{lat},{lon});
                  node["leisure"~"park|garden"]["name"](around:15000,{lat},{lon});
                  node["amenity"~"place_of_worship"]["name"](around:15000,{lat},{lon});
                );
                out center;
                """
                
                response = requests.post(overpass_url, data=overpass_query, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    
                    for element in data.get('elements', []):
                        name = element.get('tags', {}).get('name', '')
                        if name and name not in osm_places:
                            osm_places.append(name)
                    
                    # Limit to top 10 places
                    if osm_places:
                        return osm_places[:10]
    
    except Exception as e:
        print(f"Error fetching places from OpenStreetMap: {e}")
    
    # If both Gemini and OpenStreetMap fail, return None
    # This will indicate that we couldn't find specific places for this city
    return None

def get_packing_suggestions(weather_info):
    suggestions = []
    for day in weather_info:
        temp = day['avg_temp_c']
        condition = day['condition'].lower()
        
        # Base clothing suggestions based on temperature
        if temp < 10:
            clothes = "warm clothes like jackets, sweaters, and long pants"
        elif 10 <= temp < 20:
            clothes = "light layers like long sleeves and a light jacket"
        elif 20 <= temp < 30:
            clothes = "comfortable clothes like t-shirts and light pants"
        else:
            clothes = "light summer clothes like t-shirts and shorts"
        
        # Add weather-specific suggestions
        weather_extras = []
        if any(word in condition for word in ['rain', 'shower', 'drizzle', 'storm']):
            weather_extras.append("umbrella or raincoat")
        if any(word in condition for word in ['snow', 'blizzard']):
            weather_extras.append("warm boots and winter gear")
        if any(word in condition for word in ['sunny', 'clear']):
            weather_extras.append("sunglasses and sunscreen")
        if any(word in condition for word in ['cloud', 'overcast']):
            weather_extras.append("light jacket in case it gets cooler")
        
        # Combine suggestions
        suggestion = f"On {day['date']} ({day['condition']}, {temp}°C), pack {clothes}"
        if weather_extras:
            suggestion += f" and bring {', '.join(weather_extras)}"
        suggestion += "."
        
        suggestions.append(suggestion)
    
    return suggestions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        city = data.get('city', '').strip()
        start_date = data.get('startDate', '').strip()
        end_date = data.get('endDate', '').strip()
        
        if not city or not start_date or not end_date:
            return jsonify({'error': 'Please provide all required fields'}), 400
        
        # Validate dates
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
            
            if start_date_obj > end_date_obj:
                return jsonify({'error': 'Start date must be before end date'}), 400
        except ValueError:
            return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD'}), 400
        
        # Check API key
        if not WEATHER_API_KEY:
            return jsonify({'error': 'Weather API key not configured'}), 500
        
        # Get weather information
        weather_info = get_weather(city, start_date, end_date)
        if not weather_info:
            return jsonify({'error': 'Could not retrieve weather information'}), 500
        
        # Get places to visit
        places = get_places_to_visit(city)
        
        # Get packing suggestions
        packing_suggestions = get_packing_suggestions(weather_info)
        
        return jsonify({
            'city': city,
            'weather': weather_info,
            'places': places,
            'packing': packing_suggestions
        })
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
