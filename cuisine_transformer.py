import json
from pprint import pprint
from ingredients_naive_bayes import _classify_recipe_by_ingredients, FoodCuisineClassifier
import food_cats_naive_bayes as fc
import copy
import random
import naive_bayes as nb


class CuisineTransformer:

    def __init__(self):
        self.food_classifier = FoodCuisineClassifier()
        self.ingred_dict = FoodCuisineClassifier().ingred_dict
        self.forbidden_ingredients = set(["small", "large", "leaf", "1inch", "prepared", "unsalted", "divided", "lean", "fat", "american", "sweetened", "roasted", "extract", "freshly", "undrained", "melted", "blue", "split", "removed", "degrees", "inch", "12inch", "thinly", "thin", "flakes", "crumbs", "cubes", "canned", "cored", "cubed", "kidney", "stewed", "extra", "beaten", "baby", "sauce", "diced", "crumbled", "black", "halves", "crushed", "vegetable", "fruit", "dairy", "minced", "boneless", "sliced", "chopped", "skinless", "grated", "finely", "taste", "ground",
                                          "seeded", "peeled", "drained", "red", "green", "yellow", "bell", "white", "seasoning", "fresh", "cut", "boil", "bake", "brown", "cook", "deep-fry", "stir-fry", "simmer", "baste", "roast", "grill", "broil", "pan-fry", "poach", "steam", "braise", "stew", "scald", "sear", "blanch", "barbeque", "griddle", "sear", "fry", "melt", "chop", "stir", "beat", "cream", "cure", "dice", "drizzle", "fold", "glaze", "julienne", "marinate", "mince", "sear", "shred", "sift", "slice", "peel", "puree", "reduce", "grate", "deglaze", "season", "crush", "squeeze", "shake", "", " "])

    def transform_recipe(self, recipe, newcuisine):
        return convert_recipe_to_cuisine(self.ingred_dict, recipe, self.food_classifier, newcuisine, self.forbidden_ingredients)


def get_dict_topn(thedict, n):
    return [v for k, v in enumerate(sorted(thedict.items(), key=lambda x: x[1])[::-1]) if k < n]


def convert_recipes_to_cuisine(ingred_dict, newcuisine):
    new_recipes = []

    FoodClassifier = fc.FoodTypeClassifier()
    forbidden_ingredients = set(["small", "large", "leaf", "1inch", "prepared", "unsalted", "divided", "lean", "fat", "american", "sweetened", "roasted", "extract", "freshly", "undrained", "melted", "blue", "split", "removed", "degrees", "inch", "12inch", "thinly", "thin", "flakes", "crumbs", "cubes", "canned", "cored", "cubed", "kidney", "stewed", "extra", "beaten", "baby", "sauce", "diced", "crumbled", "black", "halves", "crushed", "vegetable", "fruit", "dairy", "minced", "boneless", "sliced", "chopped", "skinless", "grated", "finely", "taste", "ground",
                                 "seeded", "peeled", "drained", "red", "green", "yellow", "bell", "white", "seasoning", "fresh", "cut", "boil", "bake", "brown", "cook", "deep-fry", "stir-fry", "simmer", "baste", "roast", "grill", "broil", "pan-fry", "poach", "steam", "braise", "stew", "scald", "sear", "blanch", "barbeque", "griddle", "sear", "fry", "melt", "chop", "stir", "beat", "cream", "cure", "dice", "drizzle", "fold", "glaze", "julienne", "marinate", "mince", "sear", "shred", "sift", "slice", "peel", "puree", "reduce", "grate", "deglaze", "season", "crush", "squeeze", "shake", "", " "])
    [forbidden_ingredients.add(str(num)) for num in range(100)]

    with open("saved_crawlr.json", "r") as f:
        recipes = json.load(f)
        for recipe_link, recipe in recipes.iteritems():
            new_recipes.append(
                convert_recipe_to_cuisine(ingred_dict, recipe, FoodClassifier,
                                          newcuisine, forbidden_ingredients))

    return new_recipes


def convert_recipe_to_cuisine(ingred_dict, recipe, FoodClassifier, newcuisine, forbidden_ingredients):
    cuisine = _classify_recipe_by_ingredients(ingred_dict, recipe)
    if cuisine == newcuisine:
        print "must transform recipe to a NEW cuisine"
        return

    change_ingredients = []
    for pos, ingred in enumerate(recipe["ingredients"]):
        cuisine_name, prob = nb.classify_string_with_prob(
            ingred_dict, ingred["name"])
        # ie KEEP the ingredients that give the original cuisine feel
        if cuisine_name != cuisine:
            change_ingredients.append(
                (prob, ingred["name"], cuisine_name, pos, FoodClassifier.classify_string(ingred["name"])))

    sorted_ingreds = sorted(change_ingredients)

    replacement_ingreds = {ingred[4]: [] for ingred in sorted_ingreds}

    # Forbidden ingredients are words learned by the naive bayesian classifier that are distinctly *NOT* ingredients
    # Often these words have to do with ingredient preparation or describing food
    # It is ALWAYS ok to ignore these words; even though we are hardcoding them the approach will generalize
    # as "thinly" or "split" or "black" or "chopped" are not ingredients

    best_cuisine_replacements = filter(lambda x: x not in forbidden_ingredients, map(
        lambda x: x[0], get_dict_topn(ingred_dict[newcuisine]["data"], 200)))

    for replacement in best_cuisine_replacements:
        typeof_food = FoodClassifier.classify_string(replacement)
        if typeof_food in replacement_ingreds:
            replacement_ingreds[typeof_food].append(replacement)

    # pprint(sorted_ingreds)
    # pprint(replacement_ingreds)
    new_recipe = copy.deepcopy(recipe)
    for ingred in sorted_ingreds:
        if replacement_ingreds[ingred[4]] != []:
            new_ingred = random.choice(replacement_ingreds[ingred[4]])
            new_recipe["ingredients"][ingred[3]] = {"amount": "new ingred",
                                                    "name": new_ingred}

    print "--------------OLDRECIPE-----------"
    pprint(recipe["ingredients"])
    print "--------------NEWRECIPE-----------"
    pprint(new_recipe["ingredients"])
    return new_recipe


def main():
    FoodClassifier = FoodCuisineClassifier()
    convert_recipes_to_cuisine(FoodClassifier.ingred_dict, "italian")


if __name__ == '__main__':
    main()
