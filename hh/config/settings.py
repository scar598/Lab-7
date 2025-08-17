from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = "https://api.hh.ru/vacancies"
    TEXT = "Python разработчик"
    AREA = 1 # 1 - Москва

settings = Settings()