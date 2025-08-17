from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Уфа")
    UNITS = "metric"
    LANGUAGE = "ru"

settings = Settings()