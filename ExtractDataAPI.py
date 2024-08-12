import requests
import pandas as pd
from datetime import datetime

# Function to fetch exchange rates data from an API
def get_exchange_rates(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
        return None

# URL for the exchange rates API
api_url = "https://api.exchangerate-api.com/v4/latest/USD"  # Replace with actual API endpoint

# Fetch the exchange rates data
exchange_data = get_exchange_rates(api_url)

# Convert the data to a DataFrame and save it as CSV
if exchange_data:
    exchange_rates_df = pd.DataFrame(exchange_data)
    exchange_rates_df.to_csv("exchange_rates.csv", index=False)
    print("Exchange rates data has been saved to exchange_rates.csv")
else:
    print("No data to save.")

# Log function to record the process
def log(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write(f"{timestamp}: {message}\n")

# Log messages
log("API Data Extract Job Started")
log("Data fetched and saved to CSV")
log("API Data Extract Job Ended")
