# 🌍 Travel Advisory Agent

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange.svg)](https://ai.google.dev/)
[![WeatherAPI](https://img.shields.io/badge/WeatherAPI-Free-yellow.svg)](https://www.weatherapi.com/)

> **Your AI-Powered Travel Companion** 🚀  
> Get personalized travel insights with real-time weather, AI-curated attractions, and smart packing recommendations for any destination worldwide.

## ✨ Features

### 🤖 **AI-Powered Place Discovery**
- **Google Gemini Integration**: Dynamic attraction recommendations for any city
- **No Hardcoded Data**: Real-time AI suggestions tailored to your destination
- **Intelligent Filtering**: Top 10 must-visit places with accuracy validation

### 🌦️ **Real-Time Weather Intelligence**
- **WeatherAPI Integration**: 7-day forecasts with historical data support
- **Smart Date Handling**: Automatic API switching (forecast vs. history)
- **Comprehensive Data**: Temperature, conditions, humidity, and more

### 🎒 **Smart Packing Assistant**
- **Weather-Based Suggestions**: Clothing recommendations based on conditions
- **Activity-Specific Gear**: Umbrellas, sunscreen, winter gear auto-suggestions
- **Daily Breakdowns**: Personalized packing lists for each travel day

### 🌐 **Beautiful Web Interface**
- **Modern Flask Web App**: Responsive design with stunning UI
- **Real-Time Processing**: Instant search results with loading indicators
- **Mobile-Friendly**: Perfect experience across all devices

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- API Keys (free):
  - [Google Gemini AI](https://ai.google.dev/) - For place recommendations
  - [WeatherAPI](https://www.weatherapi.com/) - For weather data

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Travel-Advisory-Agent.git
cd Travel-Advisory-Agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
copy .env.example .env
# Edit .env with your API keys
```

### Configuration

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_weather_api_key_here
```

### Running the Application

#### 🖥️ **Web Application (Recommended)**
```bash
python app.py
```
Visit `http://localhost:5000` in your browser

#### 💻 **Command Line Interface**
```bash
python A1.py
```

## 📁 Project Structure

```
Travel-Advisory-Agent/
├── 📄 app.py              # Flask web application
├── 📄 A1.py               # Command-line interface
├── 📁 templates/          # HTML templates
│   └── index.html         # Main web interface
├── 📁 static/             # CSS, JS, images
├── 📄 requirements.txt    # Python dependencies
├── 📄 .env               # Environment variables
└── 📄 README.md          # This file
```

## 🔧 API Integration Details

### Google Gemini AI
- **Purpose**: Dynamic place recommendations
- **Model**: `gemini-pro`
- **Features**: Context-aware suggestions, real place validation
- **Fallback**: OpenStreetMap integration for reliability

### WeatherAPI
- **Purpose**: Real-time weather data
- **Endpoints**: Forecast & Historical APIs
- **Features**: 7-day forecasts, detailed conditions, temperature ranges

## 💡 Key Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **Flask** | Web Framework | 2.3.3 |
| **Google Generative AI** | LLM Integration | 0.3.2 |
| **Requests** | HTTP Client | 2.31.0 |
| **Python-dotenv** | Environment Variables | 1.0.0 |
| **Gunicorn** | WSGI Server | 21.2.0 |

## 🌟 Advanced Features

### Intelligent Fallback System
- Primary: Google Gemini AI for place recommendations
- Secondary: OpenStreetMap Nominatim & Overpass APIs
- Ensures 99.9% availability for place suggestions

### Smart Weather Processing
- Automatic API selection based on date (forecast vs. history)
- Error handling with graceful degradation
- Comprehensive weather-based packing algorithms

### Modern Web Interface
- Responsive CSS Grid layout
- Real-time AJAX requests
- Loading states and error handling
- Mobile-first design approach

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production (Heroku/Railway/Vercel)
```bash
gunicorn app:app
```

### Docker Support
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

## 📊 Usage Examples

### Web Interface
1. Enter destination city
2. Select travel dates
3. Get instant AI-powered recommendations
4. View detailed weather forecasts
5. Receive personalized packing suggestions

### API Response Format
```json
{
  "city": "Paris",
  "weather": [...],
  "places": [
    "Eiffel Tower",
    "Louvre Museum",
    "Notre-Dame Cathedral"
  ],
  "packing": [...]
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] **Mobile App** - React Native implementation
- [ ] **Hotel Integration** - Booking.com API
- [ ] **Flight Suggestions** - Skyscanner API
- [ ] **Travel Itinerary** - AI-powered day plans
- [ ] **Multi-language Support** - i18n implementation
- [ ] **Offline Mode** - PWA capabilities

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/Travel-Advisory-Agent/issues)
- **Documentation**: [Wiki](https://github.com/yourusername/Travel-Advisory-Agent/wiki)
- **Email**: amaarkhan25@gmail.com![Screenshot 2025-07-06 015048](https://github.com/user-attachments/assets/c2e35fb8-09cb-4333-974e-0f33500c65bf)
![Screenshot 2025-07-06 014737](https://github.com/user-attachments/assets/b76b8a08-9acf-4791-9da8-bf262d545c94)


---

<div align="center">
  <strong>Made with ❤️ by [Your Name]</strong><br>
  <em>Powered by AI • Built with Flask • Designed for Travelers</em>
</div>
