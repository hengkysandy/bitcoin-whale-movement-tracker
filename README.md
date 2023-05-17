
# Bitcoin Whale Movement Tracker

Following the signal of buy and sell execution from big whale on Bitcoin asset.

## How to Use

1. Clone the repository.
2. Install the dependencies: `pip3 install -r requirements.txt`
3. Create your own telegram channel and Telegram API Key
4. Create your own mongodb atlas account and create collection name with format, _id for whale address, amount for number of BTC holding
```
{"_id":"1LQoWist8KkaUXSPKZHNvEyfrEkPHzSsCd","amount":{"$numberLong":"1"}}
```
5. Run the project in cronjob that will run every 5 minutes, by using the following command: 
```0 5 * * * /bin/python3.7 /path/to/main.py```
