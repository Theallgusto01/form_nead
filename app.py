from flask import Flask

app = Flask(__name__)

try:
    from views import *
except ImportError:
    print("O módulo 'views' não foi encontrado. Certifique-se de que ele existe.")

if __name__ == "__main__":
    app.run(debug=True)
