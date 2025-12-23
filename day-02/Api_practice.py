import requests
import json

# ---------- CONFIG ----------
api_key = "C11JMUWIDVV9N0WB"
base_url = "https://www.alphavantage.co/query"
output_file = "output.json"

# ---------- INPUT ----------
symbol = input("Enter stock symbol: ").strip().upper()

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol,
    "apikey": api_key
}

# ---------- API CALL ----------
response = requests.get(base_url, params=params)
data = response.json()

# ---------- ERROR HANDLING ----------
if "Error Message" in data:
    print("❌ Invalid stock symbol")
    exit()

if "Note" in data:
    print("❌ API limit reached. Try later.")
    exit()

# ---------- DAILY DATA ----------
daily = data["Time Series (Daily)"]

# ---------- FIELD OPTIONS ----------
field_map = {
    "1": ("Open", "1. open"),
    "2": ("High", "2. high"),
    "3": ("Low", "3. low"),
    "4": ("Close", "4. close"),
    "5": ("Volume", "5. volume")
}

# ---------- LOAD OLD RESULTS (if exists) ----------
try:
    with open(output_file, "r") as f:
        results = json.load(f)
except FileNotFoundError:
    results = []

# ---------- USER LOOP ----------
while True:
    date = input("\nEnter date (YYYY-MM-DD): ").strip()

    if date not in daily:
        print("❌ No data for this date")
        continue

    print("\nChoose data to check:")
    for k, v in field_map.items():
        print(f"{k}. {v[0]}")

    choices = input("Enter numbers (comma separated): ").split(",")

    entry = {
        "symbol": symbol,
        "date": date
    }

    print(f"\n📊 Stock: {symbol} | Date: {date}")
    for c in choices:
        c = c.strip()
        if c in field_map:
            label, key = field_map[c]
            value = daily[date][key]
            print(f"{label}: {value}")
            entry[label.lower()] = value
        else:
            print("Invalid option:", c)

    # ---------- SAVE AFTER EACH QUERY ----------
    results.append(entry)

    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print("✅ Saved to output.json")

    again = input("\nCheck another date? (y/n): ").strip().lower()
    if again != "y":
        break

print("\n👋 Program finished safely")
#importsnt file