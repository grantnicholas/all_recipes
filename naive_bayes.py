from process_it import get_cuisine_dicts
from pprint import pprint
from math import log
import json


def get_dict(cuisine_dict):
    summary_dict = {}
    summary_dict["ingredients"] = get_ingredient_dict(cuisine_dict, "ingredients")
    summary_dict["directions"] = get_ingredient_dict(cuisine_dict, "directions")
    summary_dict["name"] = get_ingredient_dict(cuisine_dict, "name")
    return summary_dict


def get_ingredient_dict(cuisine_dict, atype):
    ingred_dict = {cuisine: {"data": adict[atype], "count": 0}
                   for cuisine, adict in cuisine_dict.iteritems()}
    for cuisine in ingred_dict:
        count = sum(times for ingred, times in ingred_dict[
                    cuisine]["data"].iteritems())
        ingred_dict[cuisine]["count"] = count
    return ingred_dict


def prob_one(ingred_dict, category, word):
    if word in ingred_dict[category]["data"]:
        prob = log(
            (.01 + ingred_dict[category]["data"][word]) / (.01 + ingred_dict[category]["count"]))
    else:
        prob = log(.01 / (.01 + ingred_dict[category]["count"]))

    return -1*prob


def cprob_one(ingred_dict, category, word):
    cprob = 0
    for cat in ingred_dict:
        if cat != category:
            if word in ingred_dict[cat]["data"]:
                cprob += log(
                    (.01 + ingred_dict[cat]["data"][word]) / (.01 + ingred_dict[cat]["count"]))
            else:
                cprob += log(.01 / (.01 + ingred_dict[cat]["count"]))

    return -1*cprob


def prob_word(ingredient_dict, word):
    prob_dict = {category: prob_one(ingredient_dict, category, word)
                 for category in ingredient_dict}
    return prob_dict


def cprob_word(ingredient_dict, word):
    cprob_dict = {category: cprob_one(ingredient_dict, category, word)
                  for category in ingredient_dict}
    return cprob_dict


def prob_string(ingred_dict, string):
    prob_of_cuisine = {cuisine: 0 for cuisine in ingred_dict}
    for word in string.split(" "):
        prob_dict = prob_word(ingred_dict, word)
        for cuisine in prob_dict:
            prob_of_cuisine[cuisine] += prob_dict[cuisine]

    return prob_of_cuisine


def cprob_string(ingred_dict, string):
    cprob_of_cuisine = {cuisine: 0 for cuisine in ingred_dict}
    for word in string.split(" "):
        cprob_dict = cprob_word(ingred_dict, word)
        for cuisine in cprob_dict:
            cprob_of_cuisine[cuisine] += cprob_dict[cuisine]

    return cprob_of_cuisine

def classify_string(ingred_dict, string):
    prob_dict = prob_string(ingred_dict, string)
    cprob_dict = cprob_string(ingred_dict, string)
    pprint(prob_dict)
    pprint(cprob_dict)

    val1, cat1 = min((v, k) for k, v in prob_dict.iteritems())
    val2, cat2 = max((v, k) for k, v in cprob_dict.iteritems())

    if cat1 != cat2:
        print "disagrees"

    return cat2


def classify_recipes_by_ingredients(ingred_dict):

    recipe_to_cuisine = []
    with open('saved_crawlr.json') as f:
        recipe_map = json.load(f)

        for link, recipe in recipe_map.iteritems():
            ingred_list = [ingred["name"] for ingred in recipe["ingredients"]]
            ingred_string = " ".join(ingred_list)
            cuisine = classify_string(ingred_dict, ingred_string)
            recipe_to_cuisine.append({"link": link,
                                      "name": recipe["name"],
                                      "ingredients": recipe["ingredients"],
                                      "cuisine": cuisine})

    with open('saved_cuisines.json', 'w') as f:
        data = json.dumps(recipe_to_cuisine, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4, separators=(',', ': '))
        f.write(data)


def main():
    summary_dict = get_dict(get_cuisine_dicts())

    ingred_dict = summary_dict["ingredients"]
    pprint(ingred_dict)
    for cuisine in ingred_dict:
        print cuisine, ingred_dict[cuisine]["count"]

    # print "------------bean and cheese taco------------"
    # print classify_string(ingred_dict, "bean cheese taco")

    # print "------------sausage pizza bread----------------"
    # print classify_string(ingred_dict, "sausage pizza bread")

    # print "------------processed cheese burger with velveeta----"
    # print classify_string(ingred_dict, "processed cheese burger velveeta")

    # print "------------waffle fries ketchup---------------------"
    # print classify_string(ingred_dict, "waffle fries ketchup")

    # print "------------ginger garlic sesame oil fried rice------"
    # print(classify_string(ingred_dict, "ginger garlic sesame oil fried rice"))

    # print "------------hot dogs mac and cheese------------------"
    # print(classify_string(ingred_dict, "hot dogs mac and cheese"))

    # print "------------southern fried chicken-------------------"
    # print(classify_string(ingred_dict, "southern fried chicken"))

    # print "------------poop poop poop poop----------------------"
    # print(classify_string(ingred_dict, "poop poop poop poop"))

    # print "------------tomato basil pasta-----------------------"
    # print(classify_string(ingred_dict, "tomato basil pasta"))

    # print "------------mozarella olive pizza--------"
    # print classify_string(ingred_dict, "mozarella olive pizza")

    # print "------------greek salad------------------"
    # print classify_string(ingred_dict, "greek salad feta")

    # print "------------baked potato with cheese and sour cream------------------"
    # print classify_string(ingred_dict, "baked potato cheese sour cream")

    # print "------------steamed spicy dumplings------------------"
    # print classify_string(ingred_dict, "steamed spicy dumplings")

    # pprint(ingred_dict["american"])
    classify_recipes_by_ingredients(ingred_dict)

if __name__ == '__main__':
    main()
