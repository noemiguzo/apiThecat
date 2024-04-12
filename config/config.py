from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("api_key")
WEB_HOOK = os.getenv("WEB_HOOK")
URL_CATAPI = "https://api.thecatapi.com/v1"
HEADERS_TODO = {
    "x-api-key": api_key
}
IMAGE_FOLDER = "cat_api/images/"
abs_path = os.path.abspath(__file__ + "../../../")
