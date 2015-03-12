from process_it import get_cuisine_dicts
import naive_bayes as nb


class FoodCuisineClassifier:

    def __init__(self):
        self.ingred_dict = get_dict(get_cuisine_dicts())["ingredients"]

    def classify_string(self, astring):
        return nb.classify_string(self.ingred_dict, astring)

    def classify_recipe(self, recipe):
        return _classify_recipe_by_ingredients(self.ingred_dict, recipe)


def get_dict(cuisine_dict=None):
    if cuisine_dict is None:
        cuisine_dict = get_cuisine_dicts()
    summary_dict = {}
    summary_dict["ingredients"] = get_ingredient_dict(
        cuisine_dict, "ingredients")
    summary_dict["directions"] = get_ingredient_dict(
        cuisine_dict, "directions")
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


def _classify_recipe_by_ingredients(ingred_dict, recipe):
    ingred_list = [ingred["name"] for ingred in recipe["ingredients"]]
    ingred_string = " ".join(ingred_list)
    cuisine = nb.classify_string(ingred_dict, ingred_string)
    return cuisine


def classify_recipe_by_ingredients(ingred_dict, link, recipe):
    cuisine = _classify_recipe_by_ingredients(ingred_dict, recipe)
    classified_recipe = {"link": link,
                         "name": recipe["name"],
                         "ingredients": recipe["ingredients"],
                         "cuisine": cuisine}
    return classified_recipe


def main():
    CuisineClassifier = FoodCuisineClassifier()
    print CuisineClassifier.classify_string("lime and salsa")


if __name__ == '__main__':
    main()
