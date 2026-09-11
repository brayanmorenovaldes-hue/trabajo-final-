"""Image processing utilities"""
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from typing import Tuple
import logging

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Handle image preprocessing and postprocessing"""
    
    @staticmethod
    def read_image_from_bytes(image_bytes: bytes) -> Tuple[np.ndarray, bool]:
        """Read image from bytes"""
        try:
            image = Image.open(BytesIO(image_bytes))
            image_array = np.array(image)
            
            # Convert RGB to BGR for OpenCV
            if len(image_array.shape) == 3 and image_array.shape[2] == 3:
                image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
            else:
                image_bgr = image_array
            
            return image_bgr, True
            
        except Exception as e:
            logger.error(f"Error reading image from bytes: {e}")
            return None, False
    
    @staticmethod
    def preprocess_image(image: np.ndarray, target_size: Tuple[int, int] = (640, 640)) -> np.ndarray:
        """Preprocess image for model inference"""
        try:
            h, w = image.shape[:2]
            scale = min(target_size[0] / h, target_size[1] / w)
            
            new_w = int(w * scale)
            new_h = int(h * scale)
            
            resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
            
            # Add padding
            pad_top = (target_size[0] - new_h) // 2
            pad_left = (target_size[1] - new_w) // 2
            pad_bottom = target_size[0] - new_h - pad_top
            pad_right = target_size[1] - new_w - pad_left
            
            padded = cv2.copyMakeBorder(
                resized, pad_top, pad_bottom, pad_left, pad_right,
                cv2.BORDER_CONSTANT, value=(114, 114, 114)
            )
            
            return padded
            
        except Exception as e:
            logger.error(f"Error preprocessing image: {e}")
            return image
    
    @staticmethod
    def save_image_to_bytes(image: np.ndarray, format: str = "jpg") -> bytes:
        """Convert image to bytes"""
        try:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image_pil = Image.fromarray(image_rgb)
            
            buffer = BytesIO()
            image_pil.save(buffer, format=format.upper())
            return buffer.getvalue()
            
        except Exception as e:
            logger.error(f"Error saving image to bytes: {e}")
            return b""
