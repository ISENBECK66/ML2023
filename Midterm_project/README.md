# Machine Learning Zoomcamp 2023 - Midterm project 

## GOAL : Predict heart attack 

This is my first ML project and I used a dataset to train a model with the goal of predic the heart attack probability.

I find a dataset in kaggle for this pourpose :

#### Dataset description: https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data

#### Data :
You can follow this [link](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data) to better understand and download the data.
I uploaded *dataset.csv* in the project's repository.

#### Notebook :
In the file *notebook.ipynb* there are is the data preparation and data cleaning process, 
EDA, feature importance analysis, model selection process and parameter tuning

In this phase we understood that the data we chose were poorly correlated, and that our model wouldn't learn so much from them.
I decided to keep them and continue the project.

#### Save final model :
the script *train.py* it is been used to train the final model, and using *pickle* it has been saved in the file *model_xgb.bin*.

#### Loading final model in web service:
Script *heart_attack_verifier.py* load *model_xgb.bin* and have its associated dependencies files *Pipenv* e *Pipenv.lock* to build the environment.
It is present also *Dockerfile* for running the service.
