# config/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

# ====================
# ENVIRONMENT SETTINGS
# ====================
APP_NAME = "DatasetForge"
APP_VERSION = "0.1.0"
ENV = os.getenv("ENV", "development")  # development, staging, production

# ===========
# BASE PATHS
# ===========
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SCRAPED_DATA_DIR = DATA_DIR / "scraped"
CONVERTED_DATA_DIR = DATA_DIR / "converted"
MODEL_DIR = BASE_DIR / "models"
LOG_DIR = BASE_DIR / "logs"

# Create folders if they don’t exist
for path in [DATA_DIR, SCRAPED_DATA_DIR, CONVERTED_DATA_DIR, MODEL_DIR, LOG_DIR]:
    os.makedirs(path, exist_ok=True)

# =================
# DATABASE SETTINGS
# =================
DATABASE = {
    "ENGINE": "postgresql",
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", "5432"),
    "NAME": os.getenv("DB_NAME", "dataset_forge"),
    "USER": os.getenv("DB_USER", "postgres"),
    "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
}

# =====================
# GUI APPLICATION CONFIG
# =====================
WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
THEME = "dark"  # or 'light'

# ==============
# SCRAPER CONFIG
# ==============
SCRAPER_HEADERS = {
    "User-Agent": os.getenv("SCRAPER_UA", "Mozilla/5.0 (compatible; DatasetForgeBot/0.1)"),
}
SCRAPER_TIMEOUT = 10  # seconds

# ===================
# FILE EXTENSIONS
# ===================
SUPPORTED_INPUT_FORMATS = [".csv", ".json", ".xlsx"]
SUPPORTED_EXPORT_FORMATS = [".csv", ".json", ".xlsx"]
