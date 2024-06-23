#!/bin/sh 
python3 ./MLOPS_LAB/lab1/data_creation.py 
python3 ./MLOPS_LAB/lab1/model_preprocessing.py 
python3 ./MLOPS_LAB/lab1/model_preparation.py 
python3 ./MLOPS_LAB/lab1/model_testing.py 
 
# optional 
python3 ./mlops-demo/lab1/cleaner.py
