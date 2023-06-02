import streamlit as st
import numpy as np
import pandas as pd
import requests
import datetime as dt

st.markdown("""# Taxi Fare Prediction""")

#user input
pickup_date = st.date_input('pickup_date', value= dt.date(2012,10,6))
pickup_time = st.time_input('pickup_time', value = dt.time(10,0))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('pickup_longitude', value = 40.76)
pickup_latitude = st.number_input('pickup_latitude', value =-73.98)
dropoff_longitude = st.number_input('dropoff_longitude', value = 40.64)
dropoff_latitude = st.number_input('dropoff_latitude', value = -73.78)
passenger_count = st.number_input('passenger_count', value =1)



if st.button('Predict'):
    url = "https://taxifare.lewagon.ai/predict"

    querystring = {"pickup_datetime":pickup_datetime,
                   "pickup_longitude":pickup_longitude,
                   "pickup_latitude":pickup_latitude,
                   "dropoff_longitude":dropoff_longitude,
                   "dropoff_latitude":dropoff_latitude,
                   "passenger_count":passenger_count}

    #https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
    #response = requests.get(url, params = querystring)
    #st.write(response.json()["fare"])
    #st.write(querystring)
    
    value_to_predict=[nb_past_orders, avg_basket, total_purchase_cost, avg_quantity, total_quantity, avg_nb_unique_products, total_nb_codes]


if st.button('Predict'):
    calculator = joblib.load('model.joblib')
    value_to_predict=calculator.transform([value_to_predict])
    print(value_to_predict)
    filename = 'model.joblib'
    model = joblib.load(filename)
    pred=model.predict(value_to_predict)[0]
    st.write(pred)
