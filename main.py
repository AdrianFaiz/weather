from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Get the city parameter from the query string
    api_key = 'a5567bf3896017f9e342258ddaa5434c'  # Replace with your actual API key from OpenWeatherMap

    # Make a request to the OpenWeatherMap API
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return 'Error retrieving weather data', 500

if __name__ == '__main__':
    app.run()
