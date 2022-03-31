import json
from preprocessing.cleaning_fct import *


def preprocess(input_json) -> json:
    """
    This function will be able to take all the input from the user as Json file and clean it. 
    erreur custom -> class from inerhit (flask ?)
    """

    predict_dict = {}

    # non-optional Livable surface
    if "area" in input_json:
        predict_dict["Livable surface"] = cleaning_livable_surface(input_json["area"])
    else: 
        raise ValueError("You must enter a value for area.")
    
    #non-optional Type of property
    if "property-type" in input_json:
        predict_dict["Type property"] = cleaning_proprety_type(input_json["property-type"])
    else: 
        raise ValueError("You must enter a type of property")
    
    #non-optional zip-code
    if "zip-code" in input_json:
        zip_code = cleaning_zip_code(input_json["zip-code"])
        if 1000 <= zip_code <= 1299:
            predict_dict["Brussels"] = 1
        if 1300 <= zip_code <= 1499:
            predict_dict["Walloon Brabant"] = 1
        if 1500 <= zip_code <= 1999:
            predict_dict["Flemish Brabant"] = 1
        if 2000 <= zip_code <= 2999:
            predict_dict["Antwerp"] = 1
        if 3000 <= zip_code <= 3499:
            predict_dict["Flemish Brabant"] = 1
        if 3500 <= zip_code <= 3999:
            predict_dict["Limburg"] = 1
        if 4000 <= zip_code <= 4999:
            predict_dict["Liege"] = 1
        if 5000 <= zip_code <= 5999:
            predict_dict["Namur"] = 1
        if 6000 <= zip_code <= 6599:
            predict_dict["Namur"] = 1
        if 6600 <= zip_code <= 6999:
            predict_dict["Luxembourg"] = 1
        if 7000 <= zip_code <= 7999:
            predict_dict["Hainaut"] = 1
        if 8000 <= zip_code <= 8999:
            predict_dict["West Flanders"] = 1
        if 9000 <= zip_code <= 9999:
            predict_dict["East Flanders"] = 1

    else:
        raise ValueError("You must enter a valib zip code.")

    #optional kitchen equipement
    if "equipped-kitchen" in input_json:
        predict_dict["Kitchen equipment"] = cleaning_equipped_kitchen(input_json["equipped-kitchen"])
    else:
        predict_dict["Kitchen equipment"] = 0

    #optional building state
    if "building-state" in input_json:
        predict_dict["State of the property"] = cleaning_building_state(input_json["building-state"])
    else:
        predict_dict["State of the property"] = 1

    #optional furnished
    if "furnished" in input_json:
        predict_dict["Furnished"] = cleaning_furnished(input_json["furnished"])
    else:
        predict_dict["Furnished"] = 0
    
    # #optional number of facades
    if "facades-number" in input_json:
        predict_dict["Number of facades"] = cleaning_facades_number(input_json["facades-number"])
    else:
        predict_dict["Number of facades"] = 2
    
    #surface terrace 
    if "terrace-area" in input_json:
        predict_dict["Surface terrace"] = cleaning_surface_terrace(input_json["terrace-area"])
    else:
        predict_dict["Surface terrace"] = 0

    #garden area
    if "garden-area" in input_json:
        predict_dict["Surface garden"] = cleaning_garden_surface(input_json["garden-area"])
    else:
        predict_dict["Surface garden"] = 0

    return predict_dict