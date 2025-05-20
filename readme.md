# 🎯 API Comprobador de Lotería – Navidad y El Niño (España)

Una API sencilla y rápida desarrollada con **FastAPI** que permite comprobar si un número de boleto de lotería ha sido premiado en los sorteos de **Navidad** o **El Niño** en España.
Lo he utilizado como prueba para levantar un servidor y recibir peticiones externas a mi red y alguna prueba de stress.

La idea es usar un scrapper del documento oficial de loteria que actualiza el archivo JSON correspondiente. (El scrapper no esta incluido en este proyecto)

Este proyecto tiene una ramificacion en la que se probó el uso de APIKey para la securización. En este caso, esta funcionalidad pretende ser publica y sin restricciones(puede que un middleware para evitar un exceso de llamadas fuese buena idea.)

---

## 🚀 Características

- Consulta de número premiado por sorteo (Navidad o El Niño)
- Respuesta con detalle del premio (si corresponde)
- Rápido y ligero (asíncrono, basado en FastAPI)
- Ideal para integraciones con frontend o bots

---

## 📦 Instalación

```bash
git clone https://github.com/izurza/LotoAPI.git
cd LotoAPI
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Por defecto levanta un servidor en el puerto 8000

## 🔌 Endpoints

GET /Navidad/{numero}
Descripción: Verifica si un número está premiado en el sorteo de Navidad.
GET /Navidad/{numero}/{apuesta}
Descripción: Verifica si un número está premiado en el sorteo de Navidad y recalcula dependiendo de los euros apostados. Util para participaciones.

GET /Niño/{numero}
Descripción: Verifica si un número está premiado en el sorteo de el Niño.
GET /Niño/estado
Descripción: Devuelve el estado del sorteo.

### 📥 Parámetros

numero int Número del boleto (ej: 12345) ✅ Sí \
apuesta float Cantidad apostada (Por defecto es 20) ✅ Sí

### 📤 Ejemplo de request

```bash
GET /Navidad/{numero}
```

### ✅ Ejemplo de respuesta (200 OK)

```json
{
  "numero": "11111",
  "estado": "Premiado",
  "premio": 100,
  "apuesta": 20
}
```

### ❌ Ejemplo si no está premiado

```json
{
  "numero": "99221",
  "estado": "No Premiado",
  "premio": 0,
  "apuesta": 20
}
```

🧪 Pruebas
Puedes probar la API localmente accediendo a:

Documentación automática (Swagger UI):
http://127.0.0.1:8000/docs

Documentación alternativa (ReDoc):
http://127.0.0.1:8000/redoc

### 👤 Autor

Iñigo Izurza

GitHub: @izurza

Contacto: izurza1994@gmail.com

### 📄 Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Libre para uso personal o comercial.
