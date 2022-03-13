
#External Imports
from flask import Flask, request, jsonify
from textblob import TextBlob

#Internal Imports
from helpers import *

app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]



@app.route('/')
def hello_world():
    #list_tweets = twitter_data_access()
    #objects = preprocessing(list_of_text=list_tweets)
    #return objects
    pass

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


@app.route('/app-sentiment-analysis', methods=["GET", "POST"])
def sentiment_analysis():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug = True)