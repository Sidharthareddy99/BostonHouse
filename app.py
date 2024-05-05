import pickle as pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.rout('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods = ['POST'])



