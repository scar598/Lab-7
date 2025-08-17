class ConsoleWeatherDisplayer:
    @staticmethod
    def display_weather(weather_data: dict):
        print(f"\nПогода в городе {weather_data['city']}:")
        print(f"Описание: {weather_data['description'].capitalize()}")
        print(f"Температура: {weather_data['temperature']}°C")
        print(f"Влажность: {weather_data['humidity']}%")
        print(f"Давление: {weather_data['pressure']} гПа")
        print(f"Скорость ветра: {weather_data['wind_speed']} м/с")