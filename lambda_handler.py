#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import pandas as pd
import boto3
import csv


# In[ ]:


def lambda_handler(event, context):
    url = 'https://archive-api.open-meteo.com/v1/era5?latitude=51.5002&longitude=-0.1262&start_date=2011-01-01&end_date=2014-12-31&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,rain,snowfall,windspeed_10m,winddirection_10m,windgusts_10m&timezone=Europe%2FLondon&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch'
    # Fetch hourly weather data in London from Historical Weather API
    input_file = requests.get(url=url)
    result_json = input_file.json()
    
    # Flatten and clean hourly weather data
    time = result_json['hourly']['time']
    temp = result_json['hourly']['temperature_2m']
    hum = result_json['hourly']['relativehumidity_2m']
    app_temp = result_json['hourly']['apparent_temperature']
    rain = result_json['hourly']['rain']
    snow = result_json['hourly']['snowfall']
    wind_spd = result_json['hourly']['windspeed_10m']
    wind_dir = result_json['hourly']['winddirection_10m']
    wind_gust = result_json['hourly']['windgusts_10m']
    weather_data = pd.DataFrame({'Date-Time':time, 'Temperature(degF)':temp, 'Humidity(%)':hum, 'Rain(inch)':rain,
                                'Snowfall(cm)':snow, 'Wind_Speed(mph)':wind_spd, 'Wind_Direction(deg)':wind_dir,
                                'Wind_Gust(mph)':wind_gust})
    weather_data['Date-Time'] = pd.to_datetime(weather_data['Date-Time'])
    
    weather_data.to_csv('historical_weather_data.csv', index=False)
    
    # call your s3 bucket
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('input-data-project')

    with open('historical_weather.csv', 'w') as f:
        csv_writer = csv.writer(f, delimiter=",")
        csv_reader = csv.reader(weather_data_csv.splitlines())
        for row in csv_reader:
            csv_writer.writerow(row)
        
    #upload the data into s3
    bucket.upload_file('historical_weather.csv','climate/Historical_Weather_Data.csv')
    

