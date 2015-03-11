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

def is_vegetarian(recipe):
	for ingredient in recipe["ingredients"]:
		if ingredient["name"] in meat_list.keys():
			return True
	return False

def make_vegetarian(recipe):
	for ingredient in recipe["ingredients"]:
		if ingredient["name"] in meat_list.keys():
			curr_meat = ingredient["name"]
			alt_meat = meat_list[curr_meat]
			ingredient["name"] = alt_meat
	return recipe

def make_meat(recipe):
	for ingredient in recipe["ingredients"]:
		for meat, sub in meat_list.iteritems():
			if sub == ingredient["name"]:
				ingredient["name"] = sub
				break
	return recipe

def is_pescatarian(recipe):
	for ingredient in recipe["ingredients"]:
		if ingredient["name"] in meat_list.keys():
			return True
	return False

def make_pescatarian(recipe):
	for ingredient in recipe["ingredients"]:
		if ingredient["name"] in meat_list.keys() and ingredient["name"] not in fish_list.keys():
			curr_meat = ingredient["name"]
			alt_meat = meat_list[curr_meat]
			ingredient["name"] = alt_meat
	return recipe




