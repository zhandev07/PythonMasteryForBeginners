# Using Environment Variables in Your Python Script: Now, modify your Python script to read the API key from the .env file.

from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv()

#access the api key
api_key = os.getenv('API_KEY')

if api_key:
    print(f"{api_key} API key Loaded Sucessfully!")
else:
    print("API key not found!")