import requests

# API configuration
API_KEY = "C11JMUWIDVV9N0WB"
BASE_URL = "https://www.alphavantage.co/query"


# ---------- Function 1: Fetch data from API ----------
def get_data(symbol):
    try:
        # Parameters to send with API request
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": API_KEY
        }

        # Make API request
        response = requests.get(BASE_URL, params=params)

        # Convert response to JSON
        data = response.json()
        return data

    except:
        # Handles network or API-related errors
        print("API / Network error")
        return None


# ---------- Function 2: Extract daily time series ----------
def get_daily(data):
    try:
        # Extract daily stock data from JSON
        return data["Time Series (Daily)"]
    except:
        # Handles invalid API response or missing key
        print("Daily data not available")
        return None


# ---------- Main Program ----------
symbol = input("Enter stock symbol: ").strip().upper()

# Fetch data from API
data = get_data(symbol)
if data is None:
    exit()

# Get daily stock data
daily = get_daily(data)
if daily is None:
    exit()


# Option to JSON key mapping
mp = {
    "1": "1. open",
    "2": "2. high",
    "3": "3. low",
    "4": "4. close",
    "5": "5. volume"
}

# Option to display name mapping
name = {
    "1": "Open",
    "2": "High",
    "3": "Low",
    "4": "Close",
    "5": "Volume"
}


# ---------- User Interaction Loop ----------
while True:
    date = input("\nEnter date (YYYY-MM-DD): ").strip()

    # Check if date exists in data
    if date not in daily:
        print("Date not found")
        continue

    # User selects which values to view
    choices = input("Choose (1-5, comma separated): ").split(",")

    print("\nResult:")
    for c in choices:
        c = c.strip()
        if c in mp:
            # Print selected stock values
            print(name[c], ":", daily[date][mp[c]])
        else:
            print("Invalid option")

    # Ask user if they want to continue
    again = input("\nCheck another date? (y/n): ").lower()
    if again != "y":
        break
