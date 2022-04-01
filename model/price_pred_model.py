import pandas as pd
import numpy as np 
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

path_csv = os.path.join("model", 'db_model.csv')

df_model = pd.read_csv(path_csv)
df_model = df_model.drop(columns=["Unnamed: 0"])

#Creating the shaped DF 
features = [
    "Livable surface",
    "Type property",
    "Brussels",
    "Walloon Brabant",
    "Flemish Brabant",
    "Antwerp",
    "Limburg",
    "Liege",
    "Namur",
    "Luxembourg",
    "Hainaut",
    "West Flanders",
    "East Flanders",
    "Kitchen equipment",
    "State of the property",
    "Furnished",
    "Number of facades",
    "Surface terrace",
    "Surface garden",
]
shaped_df = df_model[features]

#creating model reg 3degree
X = shaped_df.to_numpy()
y = df_model["Price"].to_numpy()
y = y.reshape(-1,1)
degree = 3
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
polyreg=make_pipeline(PolynomialFeatures(degree),LinearRegression(),)
polyreg.fit(X,y)
y_pred = polyreg.predict(X_test)
# polyreg.score(X_test, y_test)

def price_pred_poly_3deg(X_test):
    price_pred = polyreg.predict(X_test)
    return price_pred