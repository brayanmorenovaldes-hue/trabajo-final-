# 🚀 Guía de Configuración

## Backend Setup

### 1. Prerequisites
- Python 3.9+
- pip
- Git

### 2. Instalación

```bash
# Clonar repositorio
git clone https://github.com/brayanmorenovaldes-hue/trabajo-final-.git
cd trabajo-final-/backend

# Crear virtual environment
python -m venv venv

# Activar venv
# En Windows:
venv\\Scripts\\activate
# En Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Configurar Firebase

1. Ir a [Firebase Console](https://console.firebase.google.com/)
2. Crear nuevo proyecto
3. Ir a "Configuración del proyecto" → "Cuentas de servicio"
4. Click en "Generar nueva clave privada"
5. Guardar JSON como `firebase-key.json` en `backend/`
6. Copiar datos a `.env`:

```bash
cp .env.example .env
# Editar .env con tus datos de Firebase
```

### 4. Ejecutar servidor

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Servidor: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

---

## Frontend Setup (Flutter)

### 1. Instalar Flutter

```bash
# Descargar desde https://flutter.dev/docs/get-started/install
flutter --version
```

### 2. Crear proyecto

```bash
flutter create trabajo_final_mobile
cd trabajo_final_mobile
```

### 3. Agregar dependencias

```bash
flutter pub add firebase_core
flutter pub add firebase_database
flutter pub add camera
flutter pub add http
flutter pub add image_picker
```

### 4. Ejecutar app

```bash
flutter run
```

---

## Modelos de IA

| Modelo | Precisión | Velocidad |
|--------|-----------|-----------|
| MediaPipe Face Detection | 95%+ | 30ms |
| YOLOv8 Medium | 90%+ | 50ms |

---

## Testing

```bash
# Detectar
curl -X POST "http://localhost:8000/api/detect" \\
  -F "file=@image.jpg"
```
