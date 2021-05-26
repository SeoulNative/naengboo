from utils import dotenv
dotenv.load_file(".env")

# For getting MONGO_URI properly, init config after loading .env
from app import create_app
import os
app = create_app(os.getenv("FLASK_CONFIG") or "default")
