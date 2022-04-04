# Prediction Price Real Estate Belgium API (v1.0)

This is the first version of the API. All working requests are described below. 

## Install 
The API is deployed on **Heroku** and can be found here: 

==https://pp-be-immo.herokuapp.com/==

1. ## Prediction Price

This route allow your to post the data about your item and get a return prediction price. 

### GET Request 

`GET /predict/` 

### Response 

> Return the list of available post parameters. 

```
{
  "data": 
  {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
} 
``` 

---

### POST Request
` POST /predict/ `

> Enter all the **_paramters_** of your items in a **JSON** format. 
> Follow the example below. 

```
{
    "data":{
        "zip-code": 1150,
        "area": 105,
        "property-type": "APARTMENT",
        "rooms-number":2,
        "equipped-kitchen":1,
        "facades-number":2,
        "building-state": "GOOD"
    }
}
``` 

### Response

> Return the **_predicted price_** in a **JSON** format. 

```
{
    "prediction": 3321369
}
``` 

--- 


