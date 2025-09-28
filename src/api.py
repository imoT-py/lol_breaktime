import os
from dotenv import load_dotenv

load_dotenv()

# read api key
api_key = os.getenv("API_KEY")
headers = {"X-Riot-Token": api_key}