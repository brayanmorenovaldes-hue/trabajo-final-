"""Configuration settings"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # App
    APP_NAME = "Facial Recognition & Object Detection API"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False") == "True"
    
    # Firebase
    FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase-key.json")
    FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL")
    FIREBASE_STORAGE_BUCKET = os.getenv("FIREBASE_STORAGE_BUCKET")
    
    # ML Models
    FACE_DETECTION_MODEL = "mediapipe"
    OBJECT_DETECTION_MODEL = "yolov8m"  # 'm' para mejor precisión
    CONFIDENCE_THRESHOLD = 0.7  # 70% mínimo
    
    # Security
    ALLOWED_ORIGINS = ["*"]
    API_KEY = os.getenv("API_KEY", "tu-api-key-aqui")
    
    # Paths
    MODELS_PATH = os.path.join(os.path.dirname(__file__), "models")
    UPLOADS_PATH = "/tmp/uploads"
    
settings = Settings()
