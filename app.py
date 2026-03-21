from flask import Flask, render_template, request, jsonify
# Importamos tus funciones de los archivos que ya tienes
from services.translator import traducir_texto
from services.detect_language import detect
from services.show_language import ver_idiomas
from services.speech_to_text import  reconocimiento_de_voz
from services.text_to_speech import  texto_voz

app = Flask(__name__)

@app.route('/')
def index():
    # Obtenemos la lista de idiomas para el desplegable del HTML
    lista_idiomas = ver_idiomas()
    return render_template('index.html', idiomas=lista_idiomas)

@app.route('/procesar', methods=['POST'])
def procesar():
    texto = request.form.get('texto')
    idioma_destino = request.form.get('idioma_destino')

    if not texto:
        return "Escribe algo, anda...", 400

    # 1. Detectamos el idioma original usando tu función
    idioma_origen = detect(texto)

    # 2. Traducimos usando tu función
    resultado = traducir_texto(texto, idioma_origen, idioma_destino)

    return jsonify({
        'detectado': idioma_origen,
        'traducido': resultado
    })
    
@app.route('/speech-to-text', methods=['GET'])
def speech_to_text():
    resultado = reconocimiento_de_voz()
    return jsonify({
        'texto': resultado
    })

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    texto = request.form.get('texto')

    if not texto:
        return "No hay texto", 400

    audio_path = texto_voz(texto)

    if audio_path:
        return jsonify({
            'audio_url': audio_path
        })
    else:
        return "Error generando audio", 500

if __name__ == '__main__':
    app.run(debug=True)