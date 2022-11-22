
# Energy Consumption and Climate Data Analysis

With the rapid increase in global energy consumption, it is important to understand which factors impact the most. This project focuses on climate analysis and forecasting of household energy consumption with respect to various climatic conditions.
We explored big data analytics using AWS platform and its components like AWS Glue Databrew, S3, Redshift etc. 

## Overview
Climate is one of the major factors impacting household energy consumption. 
Rapid increase in global energy consumption demands analysis of different factors in order to conserve energy. 
The aim of this project is to perform big data analysis by assessing climate data and
its correlation to daily energy consumption data of household buildings in London city.

## Features

- Analysis of climate data pattern on household energy consumption
- Identifying the factor of climate data affecting energy consumption the most
- Forecast of energy consumption


## Architecture

[
![image](https://user-images.githubusercontent.com/105995798/203043934-322b45d1-d5c4-423e-8f31-25de9702c2e5.png)
](url)
## Technologies

AWS Technologies: AWS S3, AWS Lambda, AWS Glue Databrew, AWS Glue ETL, AWS Redshift, AWS Athena, AWS Forecast
Other: Tableau, Python
## Setup/Steps
1) Data Storage: Energy data from Kaggle is uploaded AWS S3 bucket using CLI and AWS Lambda is used to fetch Climate data through API call.
2) Data Pre-processing: Data from S3 is used in AWS Glue DataBrew to create recipe on sample of pre-processing and then applied on entire dataset. Output is saved in parquet format back to S3.
3) AWS Glue ETL is used to create crawler to get the schema of processed data with kms security configuration. 
4) Table is created by crawler and stored in Glue cataloge which is then connected to Redshift. Glue job to transfer data from S3 to Redshift.
5) Data in S3 and Redshift is also accessed in Amazon Athena via AWS Glue Data Catalog. 
6) Athena is connected to Tableau using AWS user access key ID and secret access key.
7) Another S3 bucket with daily data is created to use AWS Forecast to use predictor for energy data.
## Tests Performed

1) Application connection tests
2) Application security tests


## Sample Results
#### Monthly Energy Consumption wrt Temperature
[
![image](https://user-images.githubusercontent.com/105995798/203241938-15b5a0f5-a595-445a-890a-c9173c73f12c.png)
](url)
#### Hourly Energy Consumption & Temperature wrt Seasons
[
![image](https://user-images.githubusercontent.com/105995798/203241794-ab99977d-56a9-4968-bd34-aa5c236b5395.png)
](url)
#### Energy Consumption Forecast Results using AWS Forecast 
[
![image](https://user-images.githubusercontent.com/105995798/203242601-93d0fdbf-f2b5-41f0-a02e-c40d897d7768.png)
](url)
## 🔗 Contributors & Credits
Supreetha Naik https://github.com/supreetn

Sushmita Joshi https://github.com/sushmita3105

Madhura Pandit https://github.com/madhurapandit

Swetha Subramanian https://github.com/swethasubu93

## Appendix
Github Project Link: https://github.com/madhurapandit/BigData_DataDecoders


