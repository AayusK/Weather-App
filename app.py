import configparser
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('home.html')

@app.route('/home.html')
def dashboard2():
    return render_template('home.html')


@app.route('/coordinates.html')
def coordinates():
    return render_template('coordinates.html')

@app.route('/results', methods=['POST'])
def render_result():
    # Validate input
    city_name = request.form.get('city_name')
    state_code = request.form.get('state_code')
    country_code = request.form.get('country_code')

    if not all([city_name, state_code]):
        return render_template('error.html', message='Please enter a valid city name, state code, or country code')

    # Get API key and weather data
    api_key = get_apikey()
    if not api_key:
        return render_template('error.html', message='Error reading API key from config.ini')
    data = get_weather(city_name, state_code, country_code, api_key)
    if not data:
        return render_template('error.html', message='Error fetching weather data')

    # Format and display data
    temp = "{0:.2f}".format(data["main"]["temp"])
    temp_min = "{0:.2f}".format(data["main"]["temp_min"])
    temp_max = "{0:.2f}".format(data["main"]["temp_max"])
    feels_like = data["main"]["feels_like"]
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('weather.html', location=location, temp=temp, temp_min=temp_min, temp_max=temp_max, feels_like=feels_like, weather=weather)


@app.route('/results_coordinates', methods=['POST'])
def render_result_coordinates():
    # Validate input
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    if not all([latitude, longitude]):
        return render_template('error.html', message='Please enter a valid latitude and longitude')

    # Get API key and weather data
    api_key = get_apikey()
    if not api_key:
        return render_template('error.html', message='Error reading API key from config.ini')
    data = get_weather_coordinates(latitude, longitude, api_key)
    if not data:
        return render_template('error.html', message='Error fetching weather data')

    # Format and display data
    temp = "{0:.2f}".format(data["main"]["temp"])
    temp_min = "{0:.2f}".format(data["main"]["temp_min"])
    temp_max = "{0:.2f}".format(data["main"]["temp_max"])
    feels_like = data["main"]["feels_like"]
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('weather.html', location=location, temp=temp, temp_min=temp_min, temp_max=temp_max, feels_like=feels_like, weather=weather)



if __name__ == '__main__':
    app.run()

#Gets the API Key from config.ini
def get_apikey():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['openweathermap']['api']
    except Exception as e:
        print(e)
        return None

#Gets the weather from the API
def get_weather(city_name, state_code, country_code, api_key):
    try:
        # Create HTTP session to reuse connections
        session = requests.Session()
        api_url = "https://api.openweathermap.org/data/2.5/weather?q={},{},{}&units=imperial&appid={}".format(city_name, state_code, country_code, api_key)
        response = session.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error fetching weather data: {response.status_code}')
            return None
    except Exception as e:
        print(e)
        return None

def get_weather_coordinates(latitude, longitude, api_key):
    try:
        # Create HTTP session to reuse connections
        session = requests.Session()
        api_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid={}".format(latitude, longitude, api_key)
        response = session.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error fetching weather data: {response.status_code}')
            return None
    except Exception as e:
        print(e)
        return None