import json
import pandas as pd
import numpy as np
import sys
from model.price_pred_model import *

def input_to_df(json_input) -> pd.DataFrame:
    """
    Take the json input and return a DF same lenght as our model.
    """
    df_test = pd.DataFrame(columns=features)
    df_test = df_test.append(json_input,ignore_index=True)
    df_test = df_test.fillna(0)
    return df_test

def predict(json_input: json) -> json:
    df_to_test = input_to_df(json_input)
    X_test = df_to_test.to_numpy()
    price_pred = price_pred_poly_3deg(X_test)
    return price_pred[0][0]
