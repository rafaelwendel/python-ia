#Ferrementa PyCharm

from flask import Flask, render_template, request as req
from dotenv import load_dotenv
from google import generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    context = 'Vamos conversar sobre clubes e jogadores de futebol'
    prompt = req.args.get('prompt')
    input_ia = f'{context} : {prompt}'
    output = model.generate_content(input_ia)
    return {'message': output.text}


app.run(debug=True)