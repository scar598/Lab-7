from api.weather_api import WeatherAPI
from presentation.display import ConsoleWeatherDisplayer
from weather.config.settings import settings


def main():
    raw_data = WeatherAPI.get_weather(settings.DEFAULT_CITY)
    weather_data = WeatherAPI.parse_weather_data(raw_data)

    ConsoleWeatherDisplayer.display_weather(weather_data)


if __name__ == "__main__":
    main()
