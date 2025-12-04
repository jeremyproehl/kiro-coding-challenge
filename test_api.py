import requests
import json

API_URL = "https://2gw8nqdwla.execute-api.us-west-2.amazonaws.com/prod"

print("Testing API endpoints...")
print()

print("1. Testing root endpoint:")
try:
    response = requests.get(f"{API_URL}/")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
print()

print("2. Testing health endpoint:")
try:
    response = requests.get(f"{API_URL}/health")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
print()

print("3. Testing events endpoint:")
try:
    response = requests.get(f"{API_URL}/events")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
