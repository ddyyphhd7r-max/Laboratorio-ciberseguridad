from flask import Flask, request
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def inicio():
    return {
        "estado": "activo",
        "servidor": "Laboratorio de ciberseguridad",
        "fecha": datetime.now(timezone.utc).isoformat()
    }

@app.route("/mensaje", methods=["POST"])
def recibir():
    datos = request.get_json(silent=True) or {}
    mensaje = datos.get("mensaje", "")

    if not isinstance(mensaje, str) or len(mensaje) > 200:
        return {"error": "Mensaje no válido"}, 400

    return {
        "estado": "recibido",
        "mensaje": mensaje
    }

if __name__ == "__main__":
    app.run()