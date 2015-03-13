import re
low_fat_ingredient_sub = { 
    'bacon':'canadian bacon',
    'sausage':'lean ham',
    'chicken':'skinless chicken',
    'turkey':'skinless turkey',
    'duck':'skinless turkey',
    'goose':'skinless turkey',
    'rib':'beef loin',
    'brisket':'beef loin',
    'spareribs':'pork tenderloin',
    'sausage':'turkey sausage',
    'milk':'skim milk',
    'cream':'evaporated skim milk',
    'iceberg lettuce':'arugula',
    'butter':'cooking spray',
    'margarine':'olive oil',
    'oil':'olive oil',
    'shortening':'fat-free margarine',
    'soy sauce':'low-sodium soy sauce',
    'alfredo':'marinara',
    'pasta':'whole wheat pasta',
    'sour cream':'Greek yogurt',
    'bread':'pita',
    'flour tortilla':'corn tortilla',
    'bread':'whole wheat bread',
    'mayonnaise':'Greek yogurt',
    'eggs':'egg whites',
    'cream cheese':'fat-free ricotta cheese',
    'rice':'brown rice'
}
high_fat_ingredient_sub ={
    'turkey':'ground beef',
    'canadian bacon':'bacon',
    'ham':'sausage',
    'sausage':'chorizo sausage',
    'milk':'whole milk',
    'arugula':'iceberg lettuce',
    'oil':'margarine',
    'margarine':'shortening',
    'tortilla':'flour tortilla',
    'bread':'white bread',
    'whites':'eggs',
    'rice':'white rice'
}
low_fat_method_sub = {
    'fry':'bake',
    'boil':'steam',
    'deep-fry':'bake',
    'fry':'bake'
}
high_fat_method_sub = {
    'bake':'fry',
    'steam':'boil',
}

salt_list = {
"soy sauce",
"oyster sauce",
"teriyaki",
"marinara sauce",
"salsa",
"salt",
"beef broth",
"chicken broth",
"vegetable broth",
"gravy",
"hoisin sauce",
"fish sauce",
"satay sauce",
"tentsuyu",
"doubanjiang",
"pla ra",
"lobster sauce",
"shacha sauce",
"budu",
"garum",
"nam chim",
"salt",
"cooking wine",
"chick stock",
"sauce espagnole",
"sauce veloute",
"sauce hollandaise",
"allemande sauce",
"au jus",
"sauce bourguignonne",
"breton sauce",
"beurre noir",
"beurre noisette",
"sauce charcutiere",
"chasseur",
"nantua sauce",
"rouennaise",
"sauce gribiche",
"fish stock",
"bechamel sauce",
"bigoli in salsa",
"sugo alla puttanesca",
}

testrecipe = {
        "ratings": {
            "1": "4 cooks couldn't eat it",
            "3": "25 cooks thought it was OK",
            "2": "11 cooks didn't like it",
            "5": "311 cooks loved it!",
            "4": "82 cooks liked it!"
        },
        "name": "Smoky Grilled Pork Chops",
        "nutrition": [
            {
                "units": "254 kcal",
                "percentages": "13%",
                "categories": "Calories"
            },
            {
                "units": "5.4 g",
                "percentages": "2%",
                "categories": "Carbohydrates"
            },
            {
                "units": "66 mg",
                "percentages": "22%",
                "categories": "Cholesterol"
            },
            {
                "units": "14.3 g",
                "percentages": "22%",
                "categories": "Fat"
            },
            {
                "units": "1.2 g",
                "percentages": "5%",
                "categories": "Fiber"
            },
            {
                "units": "25 g",
                "percentages": "50%",
                "categories": "Protein"
            },
            {
                "units": "773 mg",
                "percentages": "31%",
                "categories": "Sodium"
            }
        ],
        "ingredients": [
            {
                "amount": "1 tablespoon",
                "name": "seasoned salt (such as LAWRY'S\u00ae)"
            },
            {
                "amount": "1 pound",
                "name": "bacon"
            },
            {
                "amount": "9 2/3 tablespoon",
                "name": "garlic powder"
            },
            {
                "amount": "1 tablespoon",
                "name": "onion powder"
            },
            {
                "amount": "1 tablespoon",
                "name": "ground paprika"
            },
            {
                "amount": "2 teaspoons",
                "name": "Worcestershire sauce"
            },
            {
                "amount": "1 teaspoon",
                "name": "liquid smoke flavoring"
            },
            {
                "amount": "4",
                "name": "bone-in pork chops (1/2 to 3/4 inch thick)"
            }
        ],
        "primary cooking method": "bake",
        "directions": [
            "Preheat an outdoor grill for medium heat, and lightly oil the grate.",
            "In a bowl, mix together the seasoned salt, black pepper, garlic powder, onion powder, paprika, Worcestershire sauce, and smoke flavoring until thoroughly combined. Rinse pork chops, and sprinkle the wet chops on both sides with the spice mixture. With your hands, massage the spice rub into the meat; allow to stand for 10 minutes.",
            "Grill the chops over indirect heat until no longer pink inside, about 12 minutes per side. An instant-read thermometer should read at least 145 degrees F (63 degrees C). Allow chops to stand for 10 more minutes before serving."
        ],
        "footnotes": []
    }

#takes the main dictionary section of the recipe (the value corresponding to the URL key) and lowers the fat in the ingredients
def increase_fat(recipe):
    for ingredient in recipe["ingredients"]:
        if ingredient["name"] in high_fat_ingredient_sub.keys():
            curr_ingredient = ingredient["name"]
            alt_ingredient = high_fat_ingredient_sub[curr_ingredient]
            ingredient["name"] = alt_ingredient
    curr_method = recipe["primary cooking method"]
    if curr_method in high_fat_method_sub.keys():
        recipe["primary cooking method"] = high_fat_method_sub[curr_method]
    return recipe

#takes the main dictionary section of the recipe (the value corresponding to the URL key) and lowers the fat in the ingredients
def decrease_fat(recipe):
    for ingredient in recipe["ingredients"]:
        if ingredient["name"] in low_fat_ingredient_sub.keys():
            curr_ingredient = ingredient["name"]
            alt_ingredient = low_fat_ingredient_sub[curr_ingredient]
            ingredient["name"] = alt_ingredient
    curr_method = recipe["primary cooking method"]
    if curr_method in low_fat_method_sub.keys():
        recipe["primary cooking method"] = low_fat_method_sub[curr_method]
    return recipe

# def decrease_salt(recipe):
#     for ingredient in recipe["ingredients"]:
#         for line in ingredient["amount"]:
#             numbers = re.findall('\d+\.*\/*\d*', line)
#             if numbers:
#                 print numbers





def main():
    test = decrease_salt(testrecipe)
    print test

if __name__ == '__main__':
    main()