import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv("DATABASE", "information.db")
DEBUG = os.getenv("DEBUG", "TRUE").lower() == "true"