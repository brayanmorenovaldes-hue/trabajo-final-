"""Object detection model using YOLOv8"""
import cv2
import numpy as np
from ultralytics import YOLO
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class ObjectDetectionModel:
    """High-precision object detection using YOLOv8"""
    
    def __init__(self, model_size: str = "m", confidence_threshold: float = 0.7):
        """Initialize object detection model
        
        Args:
            model_size: 'n' (nano) for speed, 'm' (medium) for precision
            confidence_threshold: Minimum confidence threshold
        """
        self.confidence_threshold = confidence_threshold
        self.model_size = model_size
        
        try:
            self.model = YOLO(f"yolov8{model_size}.pt")
            logger.info(f"YOLOv8{model_size} model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading YOLOv8 model: {e}")
            raise
    
    def detect_objects(self, image: np.ndarray) -> List[Dict]:
        """Detect objects in image"""
        try:
            results = self.model(image, conf=self.confidence_threshold)
            
            objects = []
            
            for result in results:
                names = result.names
                
                for box in result.boxes:
                    x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
                    confidence = float(box.conf[0])
                    class_id = int(box.cls[0])
                    class_name = names[class_id]
                    
                    objects.append({
                        "type": "object",
                        "x_min": int(x_min),
                        "y_min": int(y_min),
                        "x_max": int(x_max),
                        "y_max": int(y_max),
                        "width": int(x_max - x_min),
                        "height": int(y_max - y_min),
                        "confidence": confidence,
                        "label": class_name,
                        "class_id": class_id,
                        "default_name": class_name
                    })
            
            logger.info(f"Detected {len(objects)} objects")
            return objects
            
        except Exception as e:
            logger.error(f"Error in object detection: {e}")
            return []
