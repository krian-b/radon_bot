import argparse
from data_engine.data_extract import data_extract


parser = argparse.ArgumentParser(
    description="RadonBot"
)
parser.add_argument(
    "-b", "--broker", 
    default="yf",
    type=str, 
    help="Specify the broker. Example: 'yf' for Yahoo Finance \n ao for Angel One"
)
parser.add_argument(
    "-s", "--symbol", 
    type=str, 
    help="Specify the stock symbol. Example: 'SBIN' for State Bank of India"
)
parser.add_argument(
    "-i", "--index", 
    type=str, 
    default="nifty",
    help="Specify the stock index. Example: 'nifty50' for NIFTY 50 Index"
)
parser.add_argument(
    "-p", "--period", 
    type=str, 
    default="1y",
    help="Specify the data period (e.g., '1d' for 1 day, '5d' for 5 days, '1mo' for 1 month, '3mo' for 3 months, '6mo' for 6 months, '1y' for 1 year, '2y' for 2 years, '5y' for 5 years, '10y' for 10 years, 'ytd' for year-to-date, 'max' for maximum)"
)
parser.add_argument(
    "-v", "--interval", 
    default="1d",
    type=str, 
    help="Specify the data interval (e.g., '1m' for 1 minute, '5m' for 5 minutes, '15m' for 15 minutes,'1h' for 1 hour, '1d' for 1 day)"
)

args = parser.parse_args()

data = data_extract(args)
print(data)