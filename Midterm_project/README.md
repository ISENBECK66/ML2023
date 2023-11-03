# Machine Learning Zoomcamp 2023 - Midterm project 

## GOAL : Predict heart attack 

This is my first ML project and I used a dataset to train a model with the goal of predic the heart attack probability.
\nI find a dataset in kaggle for this pourpose :

#### Dataset description: https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data

#####Data :
You can follow the link<https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data> to better understand and download the data.
I uploaded *dataset.csv* in the project's repository.

#####Notebook :
In the file *notebook.ipynb* there are is the data preparation and data cleaning process, 
EDA, feature importance analysis, model selection process and parameter tuning

In this phase we understood that the data we chose were poorly correlated, and that our model wouldn't learn so much from them.
I decided to keep them and continue the project.

####Final model :
the script *train.py* it is been used to train the final model thru *pickle* in *model_xgb.bin*



Script predict.py (suggested name)
Loading the model
Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)
Files with dependencies
Pipenv and Pipenv.lock if you use Pipenv
or equivalents: conda environment file, requirements.txt or pyproject.toml
Dockerfile for running the service
