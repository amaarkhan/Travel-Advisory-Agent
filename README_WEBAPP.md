# Travel Advisory Agent Web App

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Make sure your .env file has the API keys:**
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   WEATHER_API_KEY=your_weather_api_key_here
   ```

3. **Run the Flask app:**
   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## Features

- **Beautiful Modern UI**: Responsive design with gradient backgrounds and smooth animations
- **Real-time Weather**: Get accurate weather forecasts for your travel dates
- **Places to Visit**: Discover top attractions and landmarks in your destination
- **Smart Packing**: Get weather-appropriate packing suggestions
- **Mobile Friendly**: Works perfectly on all devices

## API Keys Required

1. **Weather API**: Get your free API key from https://www.weatherapi.com/
2. **Gemini API**: Get your API key from Google AI Studio

## Deployment

### For Local Development:
```bash
python app.py
```

### For Production (using Gunicorn):
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### For Heroku Deployment:
1. Create a `Procfile` in your project root:
   ```
   web: gunicorn app:app
   ```

2. Deploy to Heroku:
   ```bash
   heroku create your-app-name
   git add .
   git commit -m "Deploy travel advisory app"
   git push heroku main
   ```

3. Set environment variables in Heroku:
   ```bash
   heroku config:set WEATHER_API_KEY=your_weather_api_key
   heroku config:set GEMINI_API_KEY=your_gemini_api_key
   ```

## File Structure

```
Travel-Advisory-Agent/
├── app.py                 # Flask application
├── A1.py                  # Original command line version
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── templates/
│   └── index.html        # Main HTML template
├── static/               # Static assets (CSS, JS, images)
└── README.md            # This file
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **APIs**: WeatherAPI.com, OpenStreetMap Nominatim, Overpass API

## Browser Support

- Chrome (Latest)
- Firefox (Latest)
- Safari (Latest)
- Edge (Latest)
- Mobile browsers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
