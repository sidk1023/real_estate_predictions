from flask import Flask, render_template, request
import pandas as pd 
import numpy as np
import joblib
import os

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home_page():
	request_str = request.method
	if request_str == 'GET':
		API_KEY = os.environ["API_KEY"]
		return render_template('index.html',**locals())

@app.route('/prediction/', methods = ['GET','POST']) 
def prediction_page():
	request_str = request.method
	if request_str == 'GET':
		API_KEY = os.environ["API_KEY"]
		cluster = joblib.load('clusterer.sav')
		pipeline = joblib.load('pipeline.sav')
		predictor = joblib.load('predictor.sav')			
		address = request.args['address']
		property_type = request.args['property']
		seller_type = request.args['seller']
		num_beds = int(request.args['bedrooms'])
		prop_size = int(request.args['size']) 
		latitude = float(request.args['lat'])
		longitude = float(request.args['lng'])
		df = pd.DataFrame(data = [latitude,longitude,num_beds,prop_size,seller_type,property_type]).transpose()
		df.columns=['latitude','longitude','bedrooms','area','seller','property_type']
		coords= list(zip(df['latitude'],df['longitude']))
		df['cluster_center'] = cluster.predict(coords)
		df = pipeline.transform(df)
		rent_price = predictor.predict(df)       
		rent_val = int(rent_price[0] ) 
		rent_val = rent_val-rent_val%1000  
		return render_template('prediction.html',**locals())





if __name__ == '__main__':
	app.run()