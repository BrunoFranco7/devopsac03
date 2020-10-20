import os
from flask import Flask
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    
    limite = 100

    c = 1
    p = 1
    numero = 3

    primmos = "2,"

    while p < limite:
        ehprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ","
            p = p + 1
        numero += 1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

