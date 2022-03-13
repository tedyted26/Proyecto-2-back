
#External Imports
from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS, cross_origin

#Internal Imports
from helpers import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    
    return "Esto es el inicio de la API"

@app.route('/test', methods=["GET", "POST"])
def test_sentiment_analysis():

    #Tomado del github
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

@app.route('/app-sentiment-analysis', methods=["GET","POST"])
def sentiment_analysis():
    text_input_user = request.args.get('text')
    text = preprocessing_input_user(text_input_user)
    return text


if __name__ == '__main__':
    app.run(debug = True)