import os
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv('API_KEY')
EMAIL = os.getenv('EMAIL') # nueva

print(EMAIL)