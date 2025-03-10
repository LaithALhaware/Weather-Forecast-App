from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to get weather data
def get_weather(city_name):
    try:
        # Use wttr.in or any other source to fetch weather
        url = f'https://wttr.in/{city_name}?format=%C+%t+%w+%h+%P'
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_info = response.text
            # Add emojis based on weather conditions
            if 'Sunny' in weather_info:
                weather_info += " 🌞"
            elif 'Cloudy' in weather_info:
                weather_info += " ☁️"
            elif 'Rain' in weather_info:
                weather_info += " 🌧️"
            elif 'Storm' in weather_info:
                weather_info += " ⛈️"
            elif 'Snow' in weather_info:
                weather_info += " ❄️"
            else:
                weather_info += " 🌦️"  # For other conditions
            return weather_info
        else:
            return "City not found."
    except Exception as e:
        return f"An error occurred: {e}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city_name = request.form['city']
    weather_data = get_weather(city_name)
    return render_template('index.html', weather=weather_data, city=city_name)

if __name__ == "__main__":
    app.run(debug=True)
