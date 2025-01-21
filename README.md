# iPhone 13 Price Scraper

This project tracks the price of the iPhone 13 over time using live data from Amazon and simulated historical data, however it seems amazon is a really dynamic website so i wiil change my approach and use selenium (ps help with that if you can)

## Features
- **Live Price Tracking**: Scrapes the current price of the iPhone 13 from Amazon.
- **Simulated Historical Data**: Generates realistic historical price data for testing and visualization.
- **Data Visualization**: Visualizes price trends using Seaborn and Matplotlib.

## Scripts
1. **`live_tracker.py`**: Scrapes live prices from Amazon and logs them to `live_prices.csv`.
2. **`generated_tracker.py`**: Generates simulated historical prices and logs them to `generated_prices.csv`.

## Requirements
To run this project, you need the following Python libraries:
- `requests`
- `beautifulsoup4`
- `pandas`
- `seaborn`
- `matplotlib`
- `numpy`
- `schedule`

Install the required dependencies using:
```bash
pip install -r requirements.txt