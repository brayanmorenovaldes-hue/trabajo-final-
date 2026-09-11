# 🎯 Sistema de Reconocimiento Facial y Detección de Objetos

## Descripción
Aplicación completa para detectar, etiquetar e identificar rostros y objetos con **alta precisión**. 

### Características
- ✅ Detección de rostros en tiempo real
- ✅ Identificación y clasificación de objetos
- ✅ **Etiquetado personalizado** (asigna nombres a lo que detecta)
- ✅ Base de datos en **Cloud (Firebase)**
- ✅ Cálculo de probabilidad/confianza
- ✅ Interfaz móvil
- ✅ **Reconocimiento futuro** - al volver a escanear, muestra la probabilidad de que sea lo mismo

## Stack Tecnológico

### Backend
- **FastAPI** - Framework web rápido
- **MediaPipe** - Detección facial (95%+ precisión)
- **YOLOv8 (Medium)** - Detección de objetos (90%+ precisión)
- **TensorFlow** - Modelos de IA
- **Firebase Admin SDK** - Cloud database

### Frontend
- **Flutter o React Native** - App móvil
- **Firebase SDK** - Autenticación

### Cloud
- **Firebase** - Almacenamiento de datos, imágenes, etiquetas

## Flujo de Funcionamiento

```
1. DETECTAR
   Escanea rostro u objeto → Backend procesa con IA

2. ETIQUETAR
   Asignas nombre personalizado → Se guarda en Firebase

3. RECONOCER
   Escaneas nuevamente → Compara con base de datos → Muestra probabilidad
```

## Estructura del Proyecto

```
trabajo-final/
├── backend/
│   ├── app/
│   │   ├── main.py           (Servidor FastAPI)
│   │   ├── config.py         (Configuración)
│   │   ├── models/           (Modelos IA)
│   │   │   ├── face_recognition.py
│   │   │   └── object_detection.py
│   │   ├── routes/           (Endpoints API)
│   │   │   ├── api.py
│   │   │   └── firebase_routes.py
│   │   └── services/         (Servicios)
│   │       ├── firebase_service.py
│   │       ├── image_processing.py
│   │       └── ml_service.py
│   ├── requirements.txt
│   ├── .env.example
│   └── firebase-key.json     (🔒 NO INCLUIR EN GIT)
├── frontend/
│   └── (Flutter o React Native)
├── docs/
│   ├── SETUP.md              (Instalación)
│   └── API.md                (Documentación de endpoints)
└── .gitignore
```

## 🚀 Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
# Configura Firebase (ver SETUP.md)
uvicorn app.main:app --reload --host 0.0.0.0
```

Accede a: `http://localhost:8000/docs`

### Frontend
```bash
cd frontend
flutter pub get
# Configura Firebase
flutter run
```

## 📱 Cómo Usar

### Escaneo 1: Etiquetar un Rostro
1. Abre la app → "Escanear Rostro"
2. Apunta a tu cara → Detecta rostro
3. Asigna nombre (ej: "Juan")
4. **Guardado en Cloud ✅**

### Escaneo 2: Reconocer el Rostro
1. Apunta a una foto tuya → Detecta rostro
2. **Compara con lo guardado**
3. **Muestra: "Juan - 92% de confianza"**

### Mismo flujo para Objetos
1. Escanea un objeto (laptop, celular, etc)
2. Asigna nombre personalizado
3. La próxima vez lo reconoce

## 📊 Modelos Utilizados

| Modelo | Uso | Precisión | Velocidad |
|--------|-----|-----------|-----------|
| **MediaPipe Face Detection** | Detectar rostros | 95%+ | 30ms |
| **MediaPipe Face Mesh** | Características faciales | 95%+ | 40ms |
| **YOLOv8 Medium** | Detectar objetos | 90%+ | 50ms |

## 🔐 Datos Guardados en Firebase

```json
{
  "labeled_items": {
    "face": {
      "Juan": {
        "name": "Juan",
        "type": "face",
        "saved_at": "2024-01-15T10:30:00",
        "features": [array de características faciales]
      }
    },
    "object": {
      "Mi Laptop": {
        "name": "Mi Laptop",
        "type": "object",
        "saved_at": "2024-01-15T11:00:00",
        "features": {características del objeto}
      }
    }
  }
}
```

## 📚 Documentación Completa

- **[SETUP.md](./docs/SETUP.md)** - Guía detallada de instalación
- **[API.md](./docs/API.md)** - Referencia de todos los endpoints

## 🎓 Requisitos Previos

- Python 3.9+
- Flutter 3.0+ (para frontend)
- Cuenta Firebase
- Conexión a internet (para cloud)

## ⚙️ Configuración Firebase

1. Crear proyecto en [Firebase Console](https://console.firebase.google.com/)
2. Descargar credenciales (JSON)
3. Guardar como `backend/firebase-key.json`
4. Copiar detalles a `.env`

**Ver [SETUP.md](./docs/SETUP.md) para pasos detallados**

---

**¿Preguntas?** Revisa la documentación en `/docs`
