# 📚 API Documentation

## Base URL
`http://localhost:8000` o `http://tu-ip:8000`

---

## Endpoints

### 1. Health Check

**GET** `/health`

Verifica que el servidor esté online.

**Response (200):**
```json
{
  "status": "healthy",
  "service": "facial-recognition-api"
}
```

---

## Próximos Endpoints a Implementar

- `POST /api/detect` - Detectar rostros y objetos
- `POST /api/label-face` - Etiquetar un rostro
- `POST /api/label-object` - Etiquetar un objeto
- `GET /firebase/labeled-faces` - Obtener rostros guardados
- `GET /firebase/labeled-objects` - Obtener objetos guardados

---

## Response Format

Todas las respuestas retornan JSON con esta estructura:

```json
{
  "faces": [
    {
      "type": "face",
      "x_min": 100,
      "y_min": 150,
      "x_max": 250,
      "y_max": 350,
      "confidence": 0.95,
      "label": "Unknown Face"
    }
  ],
  "objects": [
    {
      "type": "object",
      "label": "laptop",
      "confidence": 0.87,
      "x_min": 50,
      "y_min": 100,
      "x_max": 400,
      "y_max": 350
    }
  ]
}
```

---

## Códigos de Error

| Código | Descripción |
|--------|-------------|
| 400 | Bad Request - Imagen inválida |
| 404 | Not Found - Endpoint no existe |
| 500 | Internal Server Error |
