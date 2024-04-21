from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("api_key") or  "live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM"
WEB_HOOK = os.getenv("WEB_HOOK")
URL_CATAPI = "https://api.thecatapi.com/v1"
HEADERS_TODO = {
    "x-api-key": api_key
}
IMAGE_FOLDER = "cat_api/images/"
abs_path = "C:/Users/noemi.guzman/PycharmProjects" or os.path.abspath(__file__ + "../../../")
