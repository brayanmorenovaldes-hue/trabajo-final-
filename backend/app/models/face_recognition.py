"""Face detection and recognition model"""
import cv2
import numpy as np
import mediapipe as mp
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class FaceRecognitionModel:
    """High-precision face detection using MediaPipe"""
    
    def __init__(self, confidence_threshold: float = 0.7):
        """Initialize face detection model"""
        self.confidence_threshold = confidence_threshold
        
        # MediaPipe Face Detection
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detector = self.mp_face_detection.FaceDetection(
            model_selection=1,  # Modelo más preciso
            min_detection_confidence=confidence_threshold
        )
        
        # MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=5,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )
    
    def detect_faces(self, image: np.ndarray) -> List[Dict]:
        """Detect faces in image"""
        try:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w = image.shape[:2]
            
            results = self.face_detector.process(image_rgb)
            faces = []
            
            if results.detections:
                for detection in results.detections:
                    bbox = detection.location_data.bounding_box
                    
                    x_min = max(0, int(bbox.xmin * w))
                    y_min = max(0, int(bbox.ymin * h))
                    width = int(bbox.width * w)
                    height = int(bbox.height * h)
                    x_max = min(w, x_min + width)
                    y_max = min(h, y_min + height)
                    
                    confidence = float(detection.score[0])
                    
                    faces.append({
                        "type": "face",
                        "x_min": x_min,
                        "y_min": y_min,
                        "x_max": x_max,
                        "y_max": y_max,
                        "width": x_max - x_min,
                        "height": y_max - y_min,
                        "confidence": confidence,
                        "label": "Unknown Face",
                        "class_id": 0
                    })
            
            logger.info(f"Detected {len(faces)} faces")
            return faces
            
        except Exception as e:
            logger.error(f"Error in face detection: {e}")
            return []
    
    def extract_face_features(self, image: np.ndarray, face_bbox: Dict) -> np.ndarray:
        """Extract facial features/landmarks"""
        try:
            x_min, y_min = face_bbox["x_min"], face_bbox["y_min"]
            x_max, y_max = face_bbox["x_max"], face_bbox["y_max"]
            face_region = image[y_min:y_max, x_min:x_max]
            
            image_rgb = cv2.cvtColor(face_region, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(image_rgb)
            
            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0]
                features = np.array([[l.x, l.y, l.z] for l in landmarks.landmark]).flatten()
                return features
            
            return np.array([])
            
        except Exception as e:
            logger.error(f"Error extracting face features: {e}")
            return np.array([])
    
    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'face_detector'):
            self.face_detector.close()
        if hasattr(self, 'face_mesh'):
            self.face_mesh.close()
