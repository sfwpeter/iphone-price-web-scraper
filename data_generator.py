import pandas as pd
import numpy as np

# Define the date range
start_date = "2023-09-01"  # Start date for historical data
end_date = pd.Timestamp.now()  # End date (today)

# Generate a date range with daily frequency
dates = pd.date_range(start=start_date, end=end_date, freq="D")

# Generate a gradual downward trend
np.random.seed(42)  # For reproducibility
base_price = 499  # Starting price
trend = np.linspace(0, -100, len(dates))  # Gradual decrease of $100 over the period
prices = base_price + trend + np.random.normal(0, 10, len(dates))  # Add some noise

# Add occasional outliers (e.g., price spikes or drops)
outlier_indices = np.random.choice(len(dates), size=5, replace=False)  # 5 random outliers
prices[outlier_indices] += np.random.uniform(-50, 50, size=5)  # Add random outliers

# Ensure prices stay within a realistic range (e.g., $290 to $500)
prices = np.clip(prices, 290, 499)

# Create a DataFrame
df = pd.DataFrame({"Timestamp": dates, "Price": prices})

# Save to CSV
df.to_csv("iphone_prices.csv", index=False)
print("Simulated historical data saved to 'iphone_prices.csv'")