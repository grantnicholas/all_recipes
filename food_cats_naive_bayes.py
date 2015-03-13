from pprint import pprint
import process_it
import naive_bayes as nb
from stemming.porter2 import stem


class FoodTypeClassifier:

    def __init__(self):
        self.bayes_dict = create_bayes_dict(create_food_category_dict())

    def classify_string(self, astring):
        stemmed_string = stem(astring)
        return nb.classify_string(self.bayes_dict, stemmed_string)


def file_to_dict(filename):
    stop_words = process_it.stopwords()
    adict = {}
    with open(filename, "r") as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                if word not in stop_words:
                    lower_word = stem(process_it.remove_punc(word.lower()))
                    if lower_word in adict:
                        adict[lower_word] += 1
                    else:
                        adict[lower_word] = 1
    # pprint(adict)
    return adict


def create_food_category_dict():
    food_dict = {}
    food_dict["drinks"] = file_to_dict("./files_to_learn/drinks.txt")
    food_dict["carbs"] = file_to_dict("./files_to_learn/carbs.txt")
    food_dict["dairy"] = file_to_dict("./files_to_learn/dairy.txt")
    food_dict["beans"] = file_to_dict("./files_to_learn/beans.txt")
    food_dict["breads"] = file_to_dict("./files_to_learn/breads.txt")
    food_dict["fruits"] = file_to_dict("./files_to_learn/fruits.txt")
    food_dict["meats"] = file_to_dict("./files_to_learn/meats.txt")
    food_dict["sauces_spices"] = file_to_dict(
        "./files_to_learn/sauces_spices.txt")
    food_dict["seafood"] = file_to_dict("./files_to_learn/seafood.txt")
    food_dict["sweets"] = file_to_dict("./files_to_learn/sweets.txt")
    food_dict["vegetables"] = file_to_dict("./files_to_learn/vegetables.txt")

    pprint(food_dict)
    return food_dict


def create_bayes_dict(food_dict):
    ingred_dict = {food: {"data": data, "count": 0}
                   for food, data in food_dict.iteritems()}
    for cuisine in ingred_dict:
        count = sum(times for ingred, times in ingred_dict[
                    cuisine]["data"].iteritems())
        ingred_dict[cuisine]["count"] = count
    return ingred_dict


def main():
    ClassyFood = FoodTypeClassifier()
    print ClassyFood.classify_string("purple drink")
    print ClassyFood.classify_string("cheddar cheese")
    print ClassyFood.classify_string("milk")
    print ClassyFood.classify_string("pastrami")
    print ClassyFood.classify_string("beets")
    print ClassyFood.classify_string("carrots")
    print ClassyFood.classify_string("steak")
    print ClassyFood.classify_string("chicken")
    print ClassyFood.classify_string("chocolate cake")
    print ClassyFood.classify_string("olive oil")


if __name__ == '__main__':
    main()
