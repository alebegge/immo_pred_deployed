import json
import pandas as pd
import numpy as np
import model.price_pred_model as ppm

def input_to_df(json_input: json) -> pd.DataFrame:
    """
    Take the json input and return a DF same lenght as our model.
    """
    df_test = pd.DataFrame(columns=ppm.features)
    df_test = df_test.append(json_input,ignore_index=True)
    df_test = df_test.fillna(0)
    return df_test

def predict(json_input: json) -> json:
    """
    Take the json input, and return the predicted price in our model (ppm).
    """
    df_to_test = input_to_df(json_input)
    X_test = df_to_test.to_numpy()
    price_pred = ppm.price_pred_poly_3deg(X_test)
    return price_pred[0][0]
