import requests
import json
import csv

# api_key = 'U52BQN0803RWKKMB'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=AXP&apikey=U52BQN0803RWKKMB'

response = requests.get(url)

if response.status_code == 200:

    data = response.json()
    csv_file_path = 'daily_axp.csv'

    # Extract daily price data
    daily_data = data['Time Series (Daily)']

    # Create and open the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

        # Write the data rows
        for date, price_info in daily_data.items():
            row = [date, price_info['1. open'], price_info['2. high'], price_info['3. low'], price_info['4. close'],
                   price_info['5. volume']]
            csv_writer.writerow(row)

    print(f'Data has been saved to {csv_file_path}')
else:
    print('Error: Unable to retrieve data from the API')