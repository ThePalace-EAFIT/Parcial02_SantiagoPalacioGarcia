from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

@app.route("/api/v1/factorial/<numero>", methods=["GET"])
def calcular(numero):
    if not numero.lstrip("-").isdigit():
        return jsonify(error="El parámetro debe ser un entero."), 400

    n = int(numero)
    if n < 0:
        return jsonify(error="El factorial no está definido para enteros negativos."), 400

    data = {
        "numero": n,
        "factorial": factorial(n),
        "etiqueta": "par" if (n % 2 == 0) else "impar"
    }
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
