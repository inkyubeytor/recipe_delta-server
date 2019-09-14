import requests
#import db_interface
import os
import json
from typing import List

def search(ingredients: List[str]) -> List[int]:
    tot = ',+'.join(ingredients)
    response = requests.get(f"https://api.nutritionix.com/v1_1/search/{tot}?results=0:10&fields=item_name,brand_name,item_id,brand_id&appId={os.environ['NUTRITIONIX_ID']}&appKey={os.environ['NUTRITIONIX_KEY']}")
    recipe_dict = json.loads(response.text)
    recipe_url_list = [recipe['fields']['item_id'] for recipe in recipe_dict['hits']]
    print(recipe_url_list)
    #return db_interface.add(recipe_url_list)

