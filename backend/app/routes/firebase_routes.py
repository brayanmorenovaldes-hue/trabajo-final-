"""Firebase-related endpoints"""
from fastapi import APIRouter, HTTPException
from typing import List
import logging

from app.services.firebase_service import FirebaseService
from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()

try:
    firebase_service = FirebaseService(settings.FIREBASE_CREDENTIALS)
except Exception as e:
    logger.warning(f"Firebase not configured: {e}")
    firebase_service = None

@router.get("/labeled-faces")
def get_labeled_faces() -> List:
    """Get all labeled faces from Firebase"""
    try:
        if not firebase_service:
            raise HTTPException(status_code=503, detail="Firebase not configured")
        
        faces = firebase_service.get_labeled_items("face")
        return faces
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error getting labeled faces: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/labeled-objects")
def get_labeled_objects() -> List:
    """Get all labeled objects from Firebase"""
    try:
        if not firebase_service:
            raise HTTPException(status_code=503, detail="Firebase not configured")
        
        objects = firebase_service.get_labeled_items("object")
        return objects
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error getting labeled objects: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/save-face")
def save_face(name: str, features: List[float]):
    """Save labeled face to Firebase"""
    try:
        if not firebase_service:
            raise HTTPException(status_code=503, detail="Firebase not configured")
        
        success = firebase_service.save_labeled_item(
            item_type="face",
            custom_name=name,
            features=features
        )
        
        if success:
            return {"success": True, "message": f"Face '{name}' saved to Firebase"}
        else:
            raise HTTPException(status_code=500, detail="Failed to save face")
            
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error saving face: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/save-object")
def save_object(name: str, object_data: dict):
    """Save labeled object to Firebase"""
    try:
        if not firebase_service:
            raise HTTPException(status_code=503, detail="Firebase not configured")
        
        success = firebase_service.save_labeled_item(
            item_type="object",
            custom_name=name,
            features=object_data
        )
        
        if success:
            return {"success": True, "message": f"Object '{name}' saved to Firebase"}
        else:
            raise HTTPException(status_code=500, detail="Failed to save object")
            
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error saving object: {e}")
        raise HTTPException(status_code=500, detail=str(e))
