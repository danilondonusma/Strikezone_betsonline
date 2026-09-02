

# seeder/config.py
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'apuestas_d'),
    'charset': 'utf8mb4',
    'autocommit': False
}

def get_conn():
    """Returns a MySQL connection using the .env configuration."""
    return mysql.connector.connect(**DB_CONFIG)