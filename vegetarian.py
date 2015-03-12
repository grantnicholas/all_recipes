import re
meat_list =    {'chicken': 'seitan',
				'veal': 'tofu',
				'beef': 'beans',
				'pork': 'tempeh',
				'lamb': 'tofu',
				'bacon': 'eggplant',
				'bison': 'portobello mushroom',
				'chorizo': 'beans',
				'dog': 'tofu',
				'duck': 'tofu',
				'foie gras': 'avocado',
				'frog': 'tofu',
				'game': 'tofu',
				'goat': 'tofu',
				'goose': 'tofu',
				'ham': 'portobello mushroom',
				'horse': 'tofu',
				'kidney': 'tofu',
				'lamb': 'tofu',
				'mutton': 'tofu',
				'meat': 'tofu',
				'ostrich': 'tofu',
				'pepperoni': 'tofu',
				'prosciutto': 'tofu',
				'quail': 'tofu',
				'rabbit': 'tofu',
				'salami': 'portobello mushroom',
				'oysters': 'tofu',
				'clams': 'tofu',
				'mussels': 'tofu',
				'tuna': 'tofu',
				'chicken broth': 'vegetable broth',
				'beef broth': 'vegetable broth',
				'cream of chicken soup': 'cream of celery soup',
				'fish sauce': 'tofu',
				'fermented fish': 'tofu',
				'sausage': 'tofu',
				'squirrel': 'tofu',
				'sweetbread': 'tofu',
				'sweetmeat': 'tofu',
				'turkey': 'tofurkey',
				'venison': 'tofu',
				'chicken bouillon': 'spiced oil',


				'Back bacon': 'tofu',
				'Boston butt': 'tofu',
				'Fatback': 'tofu',
				'Guanciale': 'tofu',
				'Ham hock': 'tofu',
				'Pancetta': 'tofu',
				"Pig's trotters": 'tofu',
				'Pork belly': 'tofu',
				'Pork chop': 'tofu',
				'Pork loin': 'tofu',
				'Pork ribs': 'tofu',
				'Pork rind': 'tofu',
				'Pork steak': 'tofu',
				'Spare ribs': 'tofu',
				'Pork tenderloin': 'tofu',


				'7-Bone': 'tofu',
				'Beef clod': 'tofu',
				'Beef shank': 'tofu',
				'Blade steak': 'tofu',
				'blade': 'tofu',
				'Brisket': 'tofu',
				'Carcass grade': 'tofu',
				'Chateaubriand': 'tofu',
				'Chuck steak': 'tofu',
				'Cube steak': 'tofu',
				'Delmonico steak': 'tofu',
				'delmonico': 'tofu',
				'Filet mignon': 'tofu',
				'Flank steak': 'tofu',
				'flank': 'portobello mushroom',
				'Flap steak': 'portobello mushroom',
				'Flat iron steak': 'tofu',
				'flat iron': 'portobello mushroom',
				'Hanger steak': 'portobello mushroom',
				'hanger': 'portobello mushroom',
				'Oxtail': 'portobello mushroom',
				'Plate steak': 'portobello mushroom',
				'Popeseye steak': 'portobello mushroom',
				'Ranch steak': 'portobello mushroom',
				'Restructured steak': 'portobello mushroom',
				'Rib eye steak': 'portobello mushroom',
				'Rib steak': 'portobello mushroom',
				'rib': 'portobello mushroom',
				'ribeye': 'portobello mushroom',
				'rib eye': 'portobello mushroom',
				'Round steak': 'portobello mushroom',
				'Rump steak': 'portobello mushroom',
				'rump roast': 'portobello mushroom',
				'Short loin': 'tofu',
				'Short ribs': 'portobello mushroom',
				'Shoulder tender': 'portobello mushroom',
				'shoulder': 'portobello mushroom',
				'Silverside': 'portobello mushroom',
				'Sirloin steak': 'portobello mushroom',
				'Sirloin': 'portobello mushroom',
				'Skirt steak': 'portobello mushroom',
				'Sobrebarriga': 'portobello mushroom',
				'Spare ribs': 'portobello mushroom',
				'Standing rib roast': 'portobello mushroom',
				'Strip steak': 'portobello mushroom',
				'steak': 'portobello mushroom',
				'T-bone steak': 'portobello mushroom',
				'T-bone': 'portobello mushroom',
				'Beef tenderloin': 'portobello mushroom',
				'tenderloin': 'portobello mushroom',
				'Top sirloin': 'portobello mushroom',
				'Tournedos': 'portobello mushroom',
				'Tri-tip': 'portobello mushroom',
				't bone': 'portobello mushroom',
				'tritip': 'portobello mushroom',
				'tri tip': 'portobello mushroom',
				'fish': 'tofu',
				'bass': 'tofu',
				'halibut': 'tofu',
				'sturgeon': 'tofu',
				'anchovies': 'tofu',
				'catfish': 'tofu',
				'cod': 'tofu',
				'salt cod': 'tofu',
				'salmon': 'tofu',
				'skate': 'tofu',
				'stockfish': 'tofu',
				'trout': 'tofu',
				'shrimp': 'tofu',
				'tuna': 'tofu'
				}
fish_list = {
				'fish': 'tofu',
				'bass': 'tofu',
				'halibut': 'tofu',
				'sturgeon': 'tofu',
				'anchovies': 'tofu',
				'catfish': 'tofu',
				'cod': 'tofu',
				'salt cod': 'tofu',
				'salmon': 'tofu',
				'skate': 'tofu',
				'stockfish': 'tofu',
				'trout': 'tofu',
				'shrimp': 'tofu',
				'tuna': 'tofu'}
testrecipe = {
     "ratings": {
            "1": "not found",
            "3": "1 cook thought it was OK",
            "2": "not found",
            "5": "47 cooks loved it!",
            "4": "7 cooks liked it!"
        },
        "name": "Ham and Hash Brown Quiche",
        "nutrition": [
            {
                "units": "286 kcal",
                "percentages": "14%",
                "categories": "Calories"
            },
            {
                "units": "16.2 g",
                "percentages": "5%",
                "categories": "Carbohydrates"
            },
            {
                "units": "153 mg",
                "percentages": "51%",
                "categories": "Cholesterol"
            },
            {
                "units": "23.2 g",
                "percentages": "36%",
                "categories": "Fat"
            },
            {
                "units": "1.4 g",
                "percentages": "6%",
                "categories": "Fiber"
            },
            {
                "units": "13.8 g",
                "percentages": "28%",
                "categories": "Protein"
            },
            {
                "units": "663 mg",
                "percentages": "27%",
                "categories": "Sodium"
            }
        ],
        "ingredients": [
            {
                "amount": "3 cups",
                "name": "salmon"
            },
            {
                "amount": "3 tablespoons",
                "name": "butter, melted"
            },
            {
                "amount": "1 cup",
                "name": "cooked ham, chopped"
            },
            {
                "amount": "1 cup",
                "name": "shredded Cheddar cheese"
            },
            {
                "amount": "1/4 cup",
                "name": "chopped onion"
            },
            {
                "amount": "1/4 cup",
                "name": "chopped green bell pepper"
            },
            {
                "amount": "3",
                "name": "large eggs"
            },
            {
                "amount": "1/2 cup",
                "name": "milk"
            },
            {
                "amount": "1/2 teaspoon",
                "name": "salt"
            },
            {
                "amount": "1/4 teaspoon",
                "name": "ground black pepper"
            }
        ],
        "directions": [
            "Preheat oven to 425 degrees F (220 degrees C).",
            "Press hash brown potatoes between paper towels to remove excess moisture. Transfer potatoes to an 8-inch pie dish and press into the bottom and up the sides of the dish to form a crust. Drizzle with melted butter.",
            "Bake in preheated oven until golden, about 25 minutes. Remove from oven and reduce heat to 350 degrees F (175 degrees C).",
            "Combine ham, Cheddar cheese, onion, and bell pepper in a bowl; spread mixture over potato crust. Beat eggs, milk, salt, and black pepper in the same bowl; pour over ham mixture.",
            "Bake in oven until eggs are set, 25 to 30 minutes."
        ],
        "footnotes": []
    }

def is_vegetarian(recipe):
	for ingredient in recipe["ingredients"]:
		for split_ing in ingredient["name"].split():
			split_ing = re.sub('[;,.]', '', split_ing)
			if split_ing in meat_list.keys():
				return True
	return False

def make_vegetarian(recipe):
	for ingredient in recipe["ingredients"]:
		for split_ing in ingredient["name"].split():
			split_ing = re.sub('[;,.]', '', split_ing)
			if split_ing in meat_list.keys():
				curr_meat = ingredient["name"]
				alt_meat = meat_list[split_ing]
				ingredient["name"] = alt_meat
	return recipe

def make_meat(recipe):
	for ingredient in recipe["ingredients"]:
		for split_ing in ingredient["name"].split():
			split_ing = re.sub('[;,.]', '', split_ing)
			for meat, sub in meat_list.iteritems():
				if sub == split_ing:
					ingredient["name"] = meat
					break
	return recipe

def is_pescatarian(recipe):
	for ingredient in recipe["ingredients"]:
		for split_ing in ingredient["name"].split():
			split_ing = re.sub('[;,.]', '', split_ing)
			if split_ing in meat_list.keys() and split_ing not in fish_list.keys():
				return True
	return False

def make_pescatarian(recipe):
	for ingredient in recipe["ingredients"]:
		for split_ing in ingredient["name"].split():
			split_ing = re.sub('[;,.]', '', split_ing)
			if split_ing in meat_list.keys() and split_ing not in fish_list.keys():
				curr_meat = ingredient["name"]
				alt_meat = meat_list[split_ing]
				ingredient["name"] = alt_meat
	return recipe


def main():
    test = make_meat(make_vegetarian(testrecipe))
    print test

if __name__ == '__main__':
    main()

