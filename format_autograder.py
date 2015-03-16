import json
import ingredients_naive_bayes as ib
from process_it import get_cuisine_dicts
import naive_bayes as nb
from crawlr import Crawler
from pprint import pprint


#Handles fractions 
def str_to_num(astring):
    if "/" in astring:
        try:
            num, denom = astring.split("/")
            f_num = float(num)
            f_denom = float(denom)
            return f_num / f_denom
        except:
            return float(astring)
    else:
        return float(astring)


def get_name_descriptor(name):
    print 'name:', name
    if "," in name:
        try:
            ingred, descriptor = name.split(",")
            print ingred, descriptor
            return ingred, descriptor
        except:
            return name, ""
    else:
        return name, ""


def get_quantity_measurement(quantity):
    if quantity != "not found":
        arglist = quantity.split(" ")
        if len(arglist) >= 2:
            return str_to_num(arglist[0]), arglist[1]
        elif len(arglist) >= 1:
            return str_to_num(arglist[0]), "not found"
        else:
            return "not found", "not found"
    else:
        return "not found", "not found"


def create_recipe_data_structures(ingred_dict, saved_file, final_structure_file):
    tools = ["absinthe spoon", "adjustable v-rack", "aluminum foil", "aluminum stock pan", "anodized aluminum nonstick pan", "apple corer", "apple cutter", "auto reignition", "bachelor griller", "bamboo stove", "bar spoon", "barbecue", "barbecue grill", "basket rack", "baster", "beehive oven", "berry spoon", "big green egg", "biscuit cutter", "biscuit press", "blow torch", "boil over preventer", "baking pan", "baking sheets", "baking stone", "beanpot", "bedrock mortar", "bottle opener", "bottle scraper", "bowl", "braiser pan", "brasero", "brazier pot", "bread knife", "bread pan", "bread machine", "broiler pan", "browning tray", "burjiko", "butane torch", "butcher block", "butcher paper", "butter churn", "butter curler", "caddy spoon", "cake and pie server", "cake pan", "can opener", "candy thermometer", "carbon steel pan", "casserole", "casserole pan", "cassole", "cast iron skillet", "cast iron dutch oven", "chakla", "chambers stove", "cheesecloth", "cheesemelter", "cheese knife", "cheese scoop", "chef's knife", "chef's pan", "cherry pitter", "chestnut pan", "chinoise", "chip pan", "chocolatera", "churchkey", "cocktail stick", "coffee filter", "coffeemaker", "colander", "convection microwave", "cookie cutter", "cookie press", "cookie sheet", "cooking pot", "cooking sheet", "cooling racks", "copper hand hammered brazing pot", "copper sauce pan", "corkscrew", "crab cracker", "crepe pan", "cutting board", "chorkor oven", "clean-burning stove", "clome oven", "coffee percolator", "coffeemaker",
             "comal (cookware)", "combi steamer", "communal oven", "community cooker", "convection microwave", "convection oven", "cook stove", "corn roaster", "crepe maker", "diffuser (heat)", "double boiler", "doufeu", "dough blender", "dough scraper", "dutch oven", "deep fryer", "eggbeater", "egg piercer", "egg poacher", "egg separator", "egg slicer", "egg timer", "electric kettle", "electric water boiler", "embossing mat", "earth oven", "ecozoom", "electric cooker", "electric stove", "energy regulator", "fillet knife", "fish scalar", "fish slice (kitchen utensil)", "flat iron grill pan", "flat rack", "flesh-hook", "flour sifter", "fondue pot", "food mill", "food processor", "frosting spatula", "frying pan", "frying skillet", "funnel", "field kitchen", "fire pot", "flattop grill", "food steamer", "foukou", "fufu machine", "gas stove", "garlic press", "glass baking pan", "gratine pan", "grapefruit knife", "grater", "gravy strainer", "greaseproof paper", "griddle", "grill pan", "square griddle pan", "hand held electric mixer", "herb chopper", "halogen oven", "haybox", "hibachi", "hoang cam stove", "hobo stove", "horno", "hot box (appliance)", "hot plate", "induction cooking", "juicer", "karahi", "kettle", "kitchen utensil", "kitchen knife", "kamado", "kettle", "kitchen oven", "kitchen stove", "kitchener range", "krampouz", "kujiejun", "kyoto box", "ladle", "lame", "lemon reamer", "lemon squeezer", "loaf pan", "lobster pick", "lo trau", "mandoline", "mated colander pot", "measuring cup", "measuring jug", "measuring spoon", "meat grinder", "meat tenderizer", "meat thermometer", "meatloaf pan", "melon baller", "mezzaluna", "mortar and pestle", "microplane", "microwave", "microwave oven", "milk watcher", "mouli grater", "mushroom cloth", "masonry oven", "mess kit", "microwave oven", "multi-fuel stove", "nonadjustable v-rack", "nonstick skillet", "nutcracker", "nutmeg grater", "nomiku", "omelette pan", "oven", "oven bag", "oven glove", "oxo (brand)", "p-38 can opener", "paella pan", "palayok", "parchment paper", "pasta spoon", "pastry bag", "pastry blender", "pastry brush", "pastry wheel", "peel (tool)", "peeler", "pepper mill", "pie bird", "pie pan", "pizza cutter", "plastic wrap", "potato masher", "potato ricer", "pot boiler", "pot holder", "pothook", "poultry shears", "pressure cooker", "pudding basin", "pudding cloth", "pyrex baking dish", "popcorn maker", "primus stove", "ramekin", "rice spoon", "ricer", "rice cooker", "roasting jack", "roasting pan", "roasting pan with high cover", "roasting rack", "roller docker", "rolling pin", "rondeau", "round cake pan", "red cross stove", "reflector oven", "remoska", "rice cooker", "rice polisher", "roasting jack", "rocket mass heater", "rocket stove", "russian oven", "salad spoon", "salt and pepper shakers", "saran (plastic)", "saucier", "saute pan", "saucepan", "sauteuse pan", "scales", "scissors", "scoop", "scotch hands", "scraper (kitchen)", "serving spoon", "serving tongs", "shellfish scraper", "sieve", "silpat", "skewer", "skillet", "skimmer", "slotted spoon", "soup ladle", "spatula", "spider", "splatter screen", "springform pan", "spurtle", "stainless steel pan", "steel saute pan", "stir-fry pan", "stockpot", "sugar nips", "sugar spoon", "sugar thermometer", "sugar tong", "sujeo", "sabbath mode", "salamander broiler", "samovar", "sandwich toaster", "self-cleaning oven", "shichirin", "sigri (stove)", "slow cooker", "solar cooker", "soy milk maker", "stove", "susceptor", "tablespoon", "tajine", "tamis", "tava", "tea infuser", "teflon coated frying pan", "timbale (food)", "tin foil", "tin opener", "toaster oven", "tomato knife", "tongs", "trivection oven", "trivet", "trussing needle", "two burner griddle pan", "tabun oven", "tandoor", "tangia", "tea stove", "thermal immersion circulator", "toaster", "tommy cooker", "trojan room coffee pot", "turkey fryer", "vegetable peeler", "vertical rack", "vacuum fryer", "wax paper", "whisk", "wok", "wonder pot", "wooden spoon", "waffle iron", "wet grinder", "wood-burning stove", "wood-fired oven", "zester", "stock pot", "zipper bag", "shallow dish"]
    primary_methods = ["boil", "bake", "brown", "cook", "deep-fry", "stir-fry", "simmer", "baste", "roast", "grill", "broil",
                       "pan-fry", "poach", "steam", "braise", "stew", "scald", "blanch", "barbeque", "griddle", "sear", "fry", "melt"]
    secondary_methods = ["chop", "stir", "beat", "cream", "cure", "dice", "drizzle", "fold", "glaze", "julienne", "marinate",
                         "mince", "sear", "shred", "sift", "slice", "peel", "puree", "reduce", "grate", "deglaze", "season", 
                         "crush", "squeeze", "shake", "mix", "sprinkle", "baste", "basting", "grease", "boil", "bake", "brown", 
                         "cook", "deep-fry", "stir-fry", "simmer", "baste", "roast", "grill", "broil",
                         "pan-fry", "poach", "steam", "braise", "stew", "scald", "sear", "blanch", "barbeque", "griddle", "fry", "melt",
                         "bake", "barbecuie", "baste", "blacken", "blanche", "bread", "brine", "brochette", "brown", "carmelize", "charbroil",
                         "curdle", "cure", "flambe", "fondue", "infuse", "juice", "pickle", "render", "rotisserie", "separate", "smoke", "stuff",
                         "tenderize", "preheat", "turn", "sprinkle", "coat", "arrange"]

    recipe_to_cuisine = []

    with open(saved_file) as f:
        recipe_map = json.load(f)

        for link, recipe in recipe_map.iteritems():

            # recipe_to_cuisine.append(
            #     ib.classify_recipe_by_ingredients(ingred_dict, link, recipe))

            ingred_list = [ingred["name"] for ingred in recipe["ingredients"]]
            ingred_string = " ".join(ingred_list)
            cuisine = nb.classify_string(ingred_dict, ingred_string)
            tools_used = []
            primary_method = ""
            secondary_method = []

            for direction in recipe["directions"]:
                direction = direction.lower()
                for tool in tools:
                    if tool in direction:
                        if tool not in tools_used:
                            tools_used.append(tool)
                for method in primary_methods:
                    if method in direction:
                        primary_method = method
                for method in secondary_methods:
                    # check each seconday method in another tense
                    new_tense = method + "ing"
                    if method in direction:
                        if method not in secondary_method and method not in primary_method:
                            secondary_method.append(method)
                    if new_tense in direction:
                        if new_tense not in secondary_method and new_tense not in primary_method:
                            secondary_method.append(method)

            for ingredient in recipe["ingredients"]:
                quantity, measurement = get_quantity_measurement(ingredient["quantity"])
                name, descriptor = get_name_descriptor(ingredient["name"])
                ingredient["measurement"] = measurement
                if ingredient["measurement"] == "not found":
                    ingredient["measurement"] = "units"
                ingredient["quantity"] = quantity
                ingredient["descriptor"] = descriptor
                ingredient["name"] = name
                ingredient["preparation"] = ""
                ingredient["prep-description"] = ""

            recipe_to_cuisine.append({"url": link,
                                      "name": recipe["name"],
                                      "ingredients": recipe["ingredients"],
                                      "cooking tools": tools_used,
                                      "cuisine": cuisine,
                                      "primary cooking method": primary_method,
                                      "cooking methods": secondary_method})

    with open(final_structure_file, 'w') as f:
        data = json.dumps(recipe_to_cuisine, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4, separators=(',', ': '))
        f.write(data)


def main():
    ingred_dict = ib.get_dict(get_cuisine_dicts())["ingredients"]
    create_recipe_data_structures(ingred_dict, 'saved_crawlr.json', 'final_structure.json')


def web_create_recipe(saved_file, final_structure_file):
    ingred_dict = ib.get_dict(get_cuisine_dicts())["ingredients"]
    create_recipe_data_structures(ingred_dict, saved_file, final_structure_file)


def url_to_recipe_autograder(url):
    print 'calling function'
    crawler = Crawler(url)
    crawler.crawl_ntimes(1)
    crawler.write_to_file('_auto.json')
    web_create_recipe('_auto.json', 'auto.json')
    with open('auto.json', 'r') as f:
        text = f.read()
        original_recipe_json = json.loads(text)
    return original_recipe_json[0]


if __name__ == '__main__':
    main()
