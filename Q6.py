import requests
import pandas as pd
import time
from datetime import datetime

def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        timestamp = data['timestamp']
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        return timestamp, latitude, longitude
    else:
        return None

def collect_iss_data(num_records=100, interval=5):
    data = []
    for _ in range(num_records):
        location = get_iss_location()
        if location:
            timestamp, latitude, longitude = location
            readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            data.append({
                'Timestamp': timestamp,
                'Readable Time': readable_time,
                'Latitude': latitude,
                'Longitude': longitude
            })
            print(f"Recorded: Time: {readable_time}, Lat: {latitude}, Long: {longitude}")
        else:
            print("Failed to fetch ISS location. Retrying...")
        time.sleep(interval)
    return data

def save_to_csv(data, filename='iss_locations.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    print("Starting ISS location tracking...")
    num_records = 100
    interval = 5  # seconds
    data = collect_iss_data(num_records, interval)
    save_to_csv(data)
    print(f"Tracking complete. Collected {len(data)} records.")

if __name__ == "__main__":
    main()