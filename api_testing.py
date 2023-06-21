import requests

# Step 1: Register a weather station
api_key = "77e323da18455d8860d5d56a52148542"  # Replace with your OpenWeatherMap API key
base_url = "https://api.openweathermap.org/data/3.0/stations"

register_payload = {
    "external_id": "YOUR_STATION_ID",
    "name": "Your Station Name",
    "latitude": 40.7128,
    "longitude": -74.0060,
    "altitude": 10
}

headers = {
    "Content-Type": "application/json",
    "Authorization": api_key
}

response = requests.post(base_url, json=register_payload, headers=headers)
response.raise_for_status()  # Check for any API errors
station_id = response.json()["ID"]

# Step 2: Get the newly registered weather station info
get_url = f"{base_url}/{station_id}"

response = requests.get(get_url, headers=headers)
response.raise_for_status()
station_info = response.json()

# Step 3: Update the station info
update_payload = {
    "name": "Updated Station Name",
    "altitude": 20
}

response = requests.put(get_url, json=update_payload, headers=headers)
response.raise_for_status()

# Step 4: Delete the weather station and confirm it has been deleted
response = requests.delete(get_url, headers=headers)
response.raise_for_status()

# Verify deletion by getting the station info again
response = requests.get(get_url, headers=headers)
assert response.status_code == 404  # Confirm that the station is not found

print("Weather station automation scenario executed successfully!")
