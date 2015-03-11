import json
from pprint import pprint
import process_it
import naive_bayes as nb

def file_to_set(filename):
    aset = set()
    with open(filename, "r") as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                aset.add(word.lower())
    # pprint(aset)
    return aset


def create_food_category_dict():
    food_dict = {}
    food_dict["drinks"] = file_to_set("./files_to_learn/drinks.txt")
    food_dict["carbs"] = file_to_set("./files_to_learn/carbs.txt")
    food_dict["dairy"] = file_to_set("./files_to_learn/dairy.txt")
    food_dict["beans"] = file_to_set("./files_to_learn/beans.txt")
    food_dict["breads"] = file_to_set("./files_to_learn/breads.txt")
    food_dict["fruits"] = file_to_set("./files_to_learn/fruits.txt")
    food_dict["meats"] = file_to_set("./files_to_learn/meats.txt")
    food_dict["sauces_spices"] = file_to_set(
        "./files_to_learn/sauces_spices.txt")
    food_dict["seafood"] = file_to_set("./files_to_learn/seafood.txt")
    food_dict["sweets"] = file_to_set("./files_to_learn/sweets.txt")
    food_dict["vegetables"] = file_to_set("./files_to_learn/vegetables.txt")

    # pprint(food_dict)
    return food_dict


def categorize_ingredient(food_dict, ingredient):
    for k in food_dict:
        if ingredient in food_dict[k]:
            return k
    return None


def categorize_cuisine_dict(food_dict, cuisine_dict):
    cat_cuisine_ingreds = {}
    ingred_dict = nb.get_dict()["ingredients"]
    for cat in cuisine_dict:
        for ingred in cuisine_dict[cat]["ingredients"]:
            print ingred
            if ingred not in cat_cuisine_ingreds:
            	cuis, prob = nb.classify_string_with_prob(ingred_dict, ingred)
                tmp = {"type" : categorize_ingredient(food_dict, ingred),
                       "cuisine" : cuis,
                       "probability" : prob}
                if tmp["type"] is not None:
                    cat_cuisine_ingreds[ingred] = tmp

    pprint(cat_cuisine_ingreds)
    return cat_cuisine_ingreds

def write_ingredient_type(cat_cuisine_dict):
    data = json.dumps(
        cat_cuisine_dict, sort_keys=False, indent=4, separators=(',', ': '))
    with open("lookup_ingred_type.json", "w") as f:
        f.write(data)

def main():
    cuisine_dict = process_it.get_cuisine_dicts()
    food_dict = create_food_category_dict()
    cat_cuisine_dict = categorize_cuisine_dict(food_dict, cuisine_dict)
    write_ingredient_type(cat_cuisine_dict)


if __name__ == '__main__':
    main()
