# Weather Web App
#### https://youtu.be/1AbYGAUwP6U
#### Description:
This is a web application created to fetch detailed weather reports. It allows users to enter their zip code and country code to find current weather information for the desired location. This application also allows the user to enter latitude and longitude to find the current weather information.
The application is written in Python using the Flask framework. This application is using OpenWeatherMap API to fetch the weather information. The application is using the configparser python module to read the OpenWeatherMap API key stored in the config.ini file and request the python module to make API requests.
The CSS files for all of the HTML pages are fairly similar with coordinates.html and home.html having the exact same CSS so the file used was the same.
There is also an error.html which displays when the user incorrectly enters a zip code, country code, latitude, or longitude.
The dashboard page consists of two forms, one for entering zip code and country code, and the other for entering latitude and longitude. When the user submits the form, it will make a post request to the respective results page. These pages will use the OpenWeatherMap API to fetch weather information and render it on the results page.
Config.ini was one thing that I used that we did not learn in CS50 but I found it to be important as I learned they were an easy way to store any kind of configuration.
One of the major decisions I had to make was choosing to use city names instead of zip codes. I had 2 options for choosing how I would find the weather of a place but had I not used state name as well I would not be able to find the
weather of other countries but only the United States. I wanted to be able to find the weather of all places across the world so I ultimately made the decision to use city names.
Another decision that I had to make was choosing which API for the weather I would use. This decision was mostly a choice of personal preference more than anything else and I found openweather the easiest to use while also working well.
Another not very major decision at all was choosing which parts of the weather I would display. This again was mainly personal preference and the choice was made on what I personally look for when I'm checking
the weather when I go outside. The main things that I pay attention to are min-max, feels like, temperature, and the type of weather. Looking at the wind speed and humidity is important but it's not something
that I find to be particularly useful.
get_apikey is used to get an API key from a config.ini file. It uses the configparser library to read the file and returns the API key associated with the "openweathermap" section. If an exception is thrown, it will be printed and None will be returned.
/results allow the user to enter a city name, a state code, and a country code in order to fetch the current weather data. The app first validates the input from the user, then uses the get_apikey() function to get the API key from a config.ini file. It then uses the get_weather() function to fetch the weather data from an external API. The data is then formatted and displayed in a template called weather.html.
/results_coordinates allows the user to use latitude to fetch the current weather and display the current weather for that location. The code first validates the input, then retrieves an API key from the config.ini file and uses it to fetch weather data from the OpenWeatherMap API. Once the data is retrieved, the code formats the data and passes it to the 'weather.html' template to be displayed.
get_weather is used to get a weather report from the OpenWeatherMap API. It takes three arguments as input: a city name, a state code, a country code, and an API key. The code uses the requests.Session() method to create an HTTP session, which allows for the reuse of connections, and then constructs an API URL with the input data. The code then makes a GET request to the API using the session.get() method and checks the response status code. If the response is 200 (meaning success), it will return the response data in a JSON format. If the response is not 200, it will print an error message and return None.
get_weather_coordinates is used to get the weather data from the OpenWeatherMap API based on latitude and longitude. It first creates an HTTP session to reuse connections. Then it builds the URL with the latitude, longitude, and API key, and makes a GET request to the API. If the response code is 200, it returns the JSON data. Otherwise, it will print an error message. If there is an exception, it will print an error message and return None.