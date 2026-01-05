import requests

bearer_token = "YOUR_BEARER_TOKEN"
query = "#ArchitectureConference2025"

url = f"https://api.x.com/2/tweets/search/recent"
headers = {
    "Authorization": f"Bearer {bearer_token}"
}
params = {
    "query": query,
    "max_results": 50  # 必要な件数
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for tweet in data.get("data", []):
    print(tweet["id"], tweet["text"])
