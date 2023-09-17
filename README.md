# Weather Forecast App in Python

## Overview
### The Weather Forecast App is a Python application that allows users to retrieve current weather information and a 5-day forecast for a given location. It utilizes the OpenWeatherMap API to fetch real-time weather data.

## Features
- Fetch current weather conditions for a specific location.
- Display a 5-day weather forecast with daily intervals.
- Choose between Celsius and Fahrenheit units.

## Prerequisites
#### Before running the Weather Forecast App, make sure you have the following prerequisites installed:

- Python 3.x: Download Python
- Required Python packages: Install them using pip with the command: pip install -r requirements.txt


## Getting Started
1. Clone this repository to your local machine:
      - git clone https://github.com/your-username/weather-forecast-app.git

2. Navigate to the project directory:
      - cd weather-forecast-app

3. Create a virtual environment (optional but recommended):
      - python -m venv venv
   
4. Activate the virtual environment:
      - On Windows:
         - venv\Scripts\activate
      - On macOS and Linux:
         - source venv/bin/activate

5. Install project dependencies:
      - pip install -r requirements.txt

6. Set up your OpenWeatherMap API key as an environment variable:
      - Create a .env file in the project directory.
      - Add your API key to the .env file:
         - OPENWEATHERMAP_API_KEY=your_api_key_here

7. Run the Weather Forecast App:
      - python weather_app.py


## Usage
- Enter the location for which you want to fetch weather data.
- Choose the preferred units (Celsius or Fahrenheit).
- Click the "Fetch Current Weather" button to retrieve the current weather conditions.
- Click the "Fetch 5-Day Forecast" button to see the 5-day weather forecast starting from tomorrow.
  
## Contributing
#### Contributions to the Weather Forecast App are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License
#### This project is licensed under the MIT License. 
