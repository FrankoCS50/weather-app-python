import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.environ.get("OPENWEATHERMAP_API_KEY")


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Forecast App")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create and arrange GUI elements using layouts
        layout = QVBoxLayout()

        # Weather icon
        self.weather_icon = QLabel(self)
        layout.addWidget(self.weather_icon)

        # Location input
        self.label_location = QLabel("Enter location:")
        self.entry_location = QLineEdit(self)
        layout.addWidget(self.label_location)
        layout.addWidget(self.entry_location)

        # Units selection
        self.label_units = QLabel("Select units:")
        self.unit_combo = QComboBox(self)
        self.unit_combo.addItem("Celsius")
        self.unit_combo.addItem("Fahrenheit")
        layout.addWidget(self.label_units)
        layout.addWidget(self.unit_combo)

        # Fetch current weather button
        self.fetch_current_button = QPushButton("Fetch Current Weather", self)
        layout.addWidget(self.fetch_current_button)

        # Fetch 5-day forecast button
        self.fetch_5day_button = QPushButton("Fetch 5-Day Forecast", self)
        layout.addWidget(self.fetch_5day_button)

        # Result label
        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        # Set the layout to the central widget
        central_widget.setLayout(layout)

        # Connect button click events to fetch_weather methods
        self.fetch_current_button.clicked.connect(self.fetch_current_weather)
        self.fetch_5day_button.clicked.connect(self.fetch_5day_forecast)

    def get_weather(self, location, units='metric'):
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': location,
            'appid': api_key,
            'units': units,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def get_5day_forecast(self, location, units='metric'):
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        params = {
            'q': location,
            'appid': api_key,
            'units': units,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def fetch_current_weather(self):
        location = self.entry_location.text()
        units = "metric" if self.unit_combo.currentText() == "Celsius" else "imperial"

        weather_data = self.get_weather(location, units)

        if weather_data:
            # Update the weather icon
            icon_name = weather_data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_name}.png"
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(icon_url).content)
            self.weather_icon.setPixmap(pixmap)

            # Update the result label with current weather
            self.result_label.setText(
                f"Current Weather in {weather_data['name']}, {weather_data['sys']['country']}:\n"
                f"Description: {weather_data['weather'][0]['description']}\n"
                f"Temperature: {weather_data['main']['temp']}°{units[0]}\n"
                f"Humidity: {weather_data['main']['humidity']}%\n"
                f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            QMessageBox.critical(self, "Error", "Error fetching weather data. Please check your input or API key.")

    def fetch_5day_forecast(self):
        location = self.entry_location.text()
        units = "metric" if self.unit_combo.currentText() == "Celsius" else "imperial"

        forecast_data = self.get_5day_forecast(location, units)

        if forecast_data:
            # Process and display 5-day forecast data with daily intervals starting from tomorrow
            today = datetime.now().date()
            tomorrow = today + timedelta(days=1)
            forecast_text = "5-Day Forecast:\n"

            for forecast in forecast_data['list']:
                date_str = forecast['dt_txt'].split(' ')[0]
                date = datetime.strptime(date_str, "%Y-%m-%d").date()

                if date == tomorrow:
                    forecast_text += f"{date} - {forecast['weather'][0]['description']}, "
                    forecast_text += f"Temperature: {forecast['main']['temp']}°{units[0]}\n"
                    tomorrow += timedelta(days=1)

            self.result_label.setText(forecast_text)
        else:
            QMessageBox.critical(self, "Error", "Error fetching 5-day forecast data. Please check your input or API key.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))  # Replace "icon.png" with your app's icon file
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
