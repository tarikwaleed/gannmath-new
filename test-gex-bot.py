import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv()
load_dotenv(find_dotenv(), override=True)

GEX_BOT_API_KEY = os.environ.get("GEX_BOT_API_KEY")
BASE_URL = "https://api.gexbot.com/spx"


def test_gex_bot_uri_full_all():
    url = f"{BASE_URL}/all/gex?key={GEX_BOT_API_KEY}"
    response = requests.get(url)
    return response.json()


def test_gex_bot_uri_full_zero():
    url = f"{BASE_URL}/zero/gex?key={GEX_BOT_API_KEY}"
    response = requests.get(url)
    return response.json()


def test_gex_bot_uri_major_all():
    url = f"{BASE_URL}/all/majors?key={GEX_BOT_API_KEY}"
    response = requests.get(url)
    return response.json()


def test_gex_bot_uri_major_zero():
    url = f"{BASE_URL}/zero/majors?key={GEX_BOT_API_KEY}"
    response = requests.get(url)
    return response.json()


def test_gex_bot_uri_max_all():
    url = f"{BASE_URL}/all/maxchange?key={GEX_BOT_API_KEY}"
    response = requests.get(url)
    return response.json()


def test_gex_bot_uri_max_zero():
    url = f"{BASE_URL}/zero/maxchange?key={GEX_BOT_API_KEY}"
    response = requests.get(url)
    return response.json()


response = test_gex_bot_uri_full_all()
print(response.keys())
