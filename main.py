#*/3 * * * * /bin/python3.7 main.py
import os
import telebot
import time
import requests
import pymongo
from pymongo import MongoClient 

API_KEY = '<TELEGRAM_API_KEY>'
bot = telebot.TeleBot(API_KEY)

message_id = '<YOUR_TELEGRAM_CHANNEL_ID>'
whale_id='<WHALE_ADDRESS>' #obtain the address from https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html

cluster = MongoClient('mongodb+srv://<USERNAME>:<PASSWORD>@<MONGODB_HOST>/<MONGODB_DB>?retryWrites=true&w=majority')
db = cluster['<MONGODB_DB>']
collection = db['<MONGODB_COLLECTION>']

def main():

    cur_balance2 = collection.find_one({"_id": whale_id}).get('amount')
    
    new_balance2 = requests.get('https://api.blockcypher.com/v1/btc/main/addrs/'+whale_id+'/balance').json()['final_balance']
    
    if abs(cur_balance2-new_balance2) >= 100000000 :
      collection.update_one({"_id": whale_id}, {"$set" : {"amount" : new_balance2}})
      msg = 'whale movement detected: \n https://bitinfocharts.com/bitcoin/address/' + whale_id
      bot.send_message(message_id, msg)

main()
