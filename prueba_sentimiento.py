from flask import Flask, jsonify, request, abort, make_response
from textblob import TextBlob

prueba_sentimiento = Flask(__name__)

@prueba_sentimiento.route('/sentimiento', methods = ['POST'])
def create_actividad():
    if not 'texto' in request.json:
        return 'ERROR'
    analisis = TextBlob(request.json['texto'])
    trad = TextBlob(str(analisis.translate(to = 'en')))
    json_trad = float(trad.sentiment.polarity)
    
    return jsonify(
        {
            'frase': str(trad),
            'polaridad' : json_trad
        }
    )

if __name__ == '__main__':
    prueba_sentimiento.run(debug = True)
