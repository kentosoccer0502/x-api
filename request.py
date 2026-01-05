import os
import time
from dotenv import load_dotenv

import requests
from requests.exceptions import RequestException

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN") or os.getenv("bearer_token")
QUERY = "#アーキテクチャcon_findy"
MAX_RESULTS = 10


def fetch_tweets():
    if not BEARER_TOKEN:
        raise RuntimeError(
            "Bearer Token not found. Set env var BEARER_TOKEN=<token> before running."
        )

    url = f"https://api.x.com/2/tweets/search/recent"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    params = {
        "query": QUERY,
        "max_results": MAX_RESULTS  # 必要な件数
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        data = response.json()
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [])

        elif response.status_code == 401:
            raise RuntimeError("401 Unauthorized: Bearer Token が無効です")

        else:
            raise RuntimeError(
                f"Request failed ({response.status_code}): {response.text}"
            )

    except RequestException as e:
        raise RuntimeError(f"Network error: {e}")
    

fetch_tweets()