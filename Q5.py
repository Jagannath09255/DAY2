import requests

def get_iss_location():
    # API endpoint URL
    url = "http://api.open-notify.org/iss-now.json"

    try:
        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract specific information
            timestamp = data['timestamp']
            latitude = data['iss_position']['latitude']
            longitude = data['iss_position']['longitude']
            
            # Print the extracted information
            print(f"Timestamp: {timestamp}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_iss_location()