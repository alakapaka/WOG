import os

from flask import Flask, make_response
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)


@app.route("/scores")
def score_server():
    if os.path.exists(f'./{SCORES_FILE_NAME}'):
        score_file = open(f'./{SCORES_FILE_NAME}')
        SCORE = score_file.readline()
        return f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The Score Is:</h1>
                <div id="score">{SCORE}</div>
            </body>
        </html>'''
    elif not os.path.exists(f'./{SCORES_FILE_NAME}'):
        response = make_response('Score file dose not exist.')
        response.status_code = BAD_RETURN_CODE
        ERROR = f'{BAD_RETURN_CODE} Score file dose not exist'
        return  f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>ERROR:</h1>
                <div id="score" style="color:red">{ERROR}</div>
            </body>
        </html>'''