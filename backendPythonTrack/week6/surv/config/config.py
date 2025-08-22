# src/config/config.py

import os
from dotenv import load_dotenv

# Load environment variables from the .env file located in the project root (src folder)
load_dotenv()

# Database file name and debug mode flag
DATABASE = os.getenv("DATABASE", "survey.db")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
