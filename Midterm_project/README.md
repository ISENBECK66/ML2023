# Machine Learning Zoomcamp 2023 - Midterm project 

## GOAL : Predict heart attack 

This is my first ML project and I used a dataset to train a model with the goal of predic the heart attack probability.

I find a dataset in kaggle for this pourpose :

#### Dataset description: https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data

---

#### Data :
You can follow this [link](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data) to better understand and download the data.
I uploaded the entire dataset in the repository, file: *dataset.csv*

---

#### Notebook :
The file *notebook.ipynb* contains the code for data preparation and data cleaning process, 
EDA, feature importance analysis, model parameter tuning and model selection process.

In this phase we understood that the data we chose were poorly correlated, and that our model wouldn't learn so much from them.
However I decided to continue the project with the same data.

---

#### Save final model :
the script *train.py* it is been used to train the final model that has been saved in the file *model_xgb.bin* using *pickle*.

---

#### Loading final model in web service:
The script *heart_attack_verifier.py* load our *model_xgb.bin* and can be used loading its dependencies files *Pipenv* e *Pipenv.lock* to build the environment.
It is present also the file : *Dockerfile* for running the service.

The script *heart_attack_patient_alpha.py* contains the data of one patient and can be used to test the application.
