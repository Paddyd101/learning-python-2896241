import json

import pandas_market_calendars as mcal
import os
from datetime import datetime

cwd = os.getcwd()

if not os.path.exists(f"{cwd}/outputs"):
	os.mkdir(f"{cwd}/outputs")

nyse = mcal.get_calendar('NYSE')
market_days = nyse.valid_days(start_date='2022-12-01', end_date=datetime.now())

trading_days={}

trading_days["margins"] ={}
trading_days["canada"] = {}
trading_days["trade_processing"] ={}
current_process_date = datetime.now() if datetime.now() in market_days else market_days[-1]
current_process_date = current_process_date.strftime("%Y-%m-%d")

previous_process_dates = [day.strftime("%Y-%m-%d") for day in market_days]

trading_days["margins"]["current_process_date"] = current_process_date
trading_days["margins"]["prev_process_dates"] = previous_process_dates
trading_days["canada"]["current_process_date"] = current_process_date
trading_days["canada"]["prev_process_dates"] = previous_process_dates
trading_days["trade_processing"]["current_process_date"] = current_process_date
trading_days["trade_processing"]["prev_process_dates"] = previous_process_dates

list(trading_days)[0]

for key, value in trading_days.items():
	with open(f"outputs/{key}.json","w+") as outfile:
		outfile.write("{}\n".format(value))



