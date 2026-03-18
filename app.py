from flask import Flask, render_template, request, jsonify
# Importamos todas tus funciones


app = Flask(__name__)

#el approute es para ejecutar o redirigir
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)