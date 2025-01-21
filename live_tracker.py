import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

# Function to scrape the price of iPhone 13
def scrape_iphone_price():
    url = "https://www.amazon.com/iPhone-13-128GB-Midnight-Unlocked/dp/B0BGQKY8S9"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Updated price extraction logic
        price = soup.select_one("span.a-offscreen")  # More general price selector
        
        if price:
            price_text = price.get_text().strip().replace("$", "").replace(",", "")
            try:
                price_value = float(price_text)
                return price_value
            except ValueError:
                print("Could not convert price to float.")
                return None
        else:
            print("Price element not found on the page.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

# Function to log the price and timestamp
def price_logger(price):
    if price:
        timestamp = pd.Timestamp.now()
        data = {"Timestamp": timestamp, "Price": price}
        df = pd.DataFrame([data])
        df.to_csv("live_prices.csv", mode="a", header=not pd.io.common.file_exists("live_prices.csv"), index=False)
        print(f"Scraped Price: ${price} at {timestamp}")
    else:
        print("Price not found.")

# Function to visualize the data
def visualize_data():
    try:
        df = pd.read_csv("live_prices.csv")
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
        sns.lineplot(x="Timestamp", y="Price", data=df)
        plt.title("iPhone 13 Price Over Time (Live Data)")
        plt.xlabel("Timestamp")
        plt.ylabel("Price ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No data to visualize yet.")

# Run the scraper periodically
if __name__ == "__main__":
    while True:
        price = scrape_iphone_price()
        price_logger(price)
        visualize_data()
        time.sleep(3600)  # Wait for 1 hour (3600 seconds) before running again
