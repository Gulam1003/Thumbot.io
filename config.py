

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    
    DALLE_API_KEY = os.getenv('DALLE_API_KEY')
                    