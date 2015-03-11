
low_fat_ingredient_sub = {
    'ground beef':'lean ground turkey',
    'bacon':'canadian bacon',
    'sausage':'lean ham',
    'chicken':'skinless chicken',
    'turkey':'skinless turkey',
    'duck':'skinless turkey',
    'goose':'skinless turkey',
    'beef chuck':'beef loin',
    'beef rib':'beef loin',
    'beef brisket':'beef loin',
    'pork spareribs':'pork tenderloin',
    'chorizo sausage':'turkey sausage',
    'milk':'skim milk',
    'cream':'evaporated skim milk',
    'iceberg lettuce':'arugula',
    'butter':'cooking spray',
    'margarine':'olive oil',
    'vegetable oil':'olive oil',
    'shortening':'fat-free margarine',
    'soy sauce':'low-sodium soy sauce',
    'alfredo':'marinara',
    'pasta':'whole wheat pasta',
    'sour cream':'Greek yogurt',
    'bread':'pita',
    'flour tortilla':'corn tortilla',
    'white bread':'whole wheat bread',
    'mayonnaise':'Greek yogurt',
    'eggs':'egg whites',
    'cream cheese':'fat-free ricotta cheese',
    'white rice':'brown rice'
}
high_fat_ingredient_sub ={
    'lean ground turkey':'ground beef',
    'canadian bacon':'bacon',
    'lean ham':'sausage',
    'skinless chicken':'chicken',
    'skinless turkey':'turkey',
    'turkey sausage':'chorizo sausage',
    'skim milk':'whole milk',
    'evaporated skim milk':'cream',
    'arugula':'iceberg lettuce',
    'cooking spray':'butter',
    'olive oil':'margarine',
    'olive oil':'vegetable oil',
    'fat-free margarine':'shortening',
    'low-sodium soy sauce':'soy sauce',
    'whole wheat pasta':'pasta',
    'corn tortilla':'flour tortilla',
    'whole wheat bread':'white bread',
    'egg whites':'eggs',
    'brown rice':'white rice'
}
low_fat_method_sub = {
    'fry':'bake',
    'boil':'steam',
    'deep-fry':'bake',
    'pan fry':'bake'
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

def increase_fat(recipe):
    for ingredient in recipe["ingredients"]:
        if ingredient["name"] in high_fat_ingredient_sub.keys():
            curr_ingredient = ingredient["name"]
            alt_ingredient = high_fat_ingredient_sub[curr_ingredient]
            ingredient["name"] = alt_ingredient
    # TODO Replace methods using high_fat_method_sub
    return recipe

def decrease_fat(recipe):
    for ingredient in recipe["ingredients"]:
        if ingredient["name"] in low_fat_ingredient_sub.keys():
            curr_ingredient = ingredient["name"]
            alt_ingredient = low_fat_ingredient_sub[curr_ingredient]
            ingredient["name"] = alt_ingredient
    # TODO Replace methods using low_fat_method_sub
    return recipe

def decrease_salt(recipe):
    for ingredient in recipe["ingredients"]:
        if ingredient["name"] in salt_list.keys():
            # TODO decrease ingredient aount somehow
