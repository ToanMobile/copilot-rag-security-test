"""Simple web application."""
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
API_KEY = os.getenv("API_KEY", "")

def get_status():
    return {"status": "ok", "version": "1.0.0"}
