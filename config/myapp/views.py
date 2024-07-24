import pandas as pd
import pickle
from geopy.distance import geodesic
from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
import regex as re
import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.simplefilter("error", InconsistentVersionWarning)
from joblib import load



def index(request):
    return render(request, 'index.html')


def predict(request):
    

    if request.method == 'POST':
        # Extract POST data from request.POST
        var = request.POST
        Age_of_car = var.get('Age_of_car')
        age_of_policyholder = var.get('age_of_policyholder')
        policy_tenure = var.get('policy_tenure')
        area_cluster = var.get('area_cluster')
        population_density = var.get('population_density')

        target_train = pd.DataFrame({
            'age_of_car': [Age_of_car],
            'policy_tenure': [policy_tenure],
            'age_of_policyholder': [age_of_policyholder],
            'population_density': [population_density],
            'area_cluster': [area_cluster]

        })
        try:
            for i in target_train.columns:
                target_train[i] = target_train[i].astype(int)
        except Exception as e:
            return render(request, 'index.html', {'error': f'Incompatable Error: {e}'})


       
        try:
            # with open('templates/model.pkl', 'rb') as model_file:
            #     model = pickle.load(model_file)
            model = load('templates/model.joblib')
            predict_given_data = model.predict(target_train)
            print(f"Prediction: {predict_given_data}")  # Debug output
        except Exception as e:
            print(e)
            return render(request, 'index.html', {'error': f'Error loading model or making prediction: {e}'})

        if predict_given_data[0] == 0:
            text = "Your are Not Claim"
            return render(request, 'index.html', {'predict': text})

        else:
            text = "Your able to Claim"
            return render(request, 'index.html', {'predict': text})

    return render(request, 'temp.html')




