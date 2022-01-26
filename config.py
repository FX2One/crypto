import os
from dotenv import load_dotenv
load_dotenv()

'''setup API key generated from your coinmarketcap.com and load from python-dotenv file'''
SECRET_KEY = os.getenv("CMC_PRO_API")
