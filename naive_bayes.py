from process_it import get_cuisine_dicts, make_string_searcher
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

    val1, cat1 = min((v, k) for k, v in prob_dict.iteritems())
    val2, cat2 = max((v, k) for k, v in cprob_dict.iteritems())

    if cat1 != cat2:
        print "disagrees"

    return cat2


def create_recipe_data_structures(ingred_dict):
    tools = ["absinthe spoon","adjustable v-rack","aluminum foil","aluminum stock pan","anodized aluminum nonstick pan","apple corer","apple cutter","auto reignition","bachelor griller","bamboo stove","bar spoon","barbecue","barbecue grill","basket rack","baster","beehive oven","berry spoon","big green egg","biscuit cutter","biscuit press","blow torch","boil over preventer","baking pan","baking sheets","baking stone","beanpot","bedrock mortar","bottle opener","bottle scraper","bowl","braiser pan","brasero","brazier pot","bread knife","bread pan","bread machine","broiler pan","browning tray","burjiko","butane torch","butcher block","butcher paper","butter churn","butter curler","caddy spoon","cake and pie server","cake pan","can opener","candy thermometer","carbon steel pan","casserole","casserole pan","cassole","cast iron skillet","cast iron dutch oven","chakla","chambers stove","cheesecloth","cheesemelter","cheese knife","cheese scoop","chef's knife","chef's pan","cherry pitter","chestnut pan","chinoise","chip pan","chocolatera","churchkey","cocktail stick","coffee filter","coffeemaker","colander","convection microwave","cookie cutter","cookie press","cookie sheet","cooking pot","cooking sheet","cooling racks","copper hand hammered brazing pot","copper sauce pan","corkscrew","crab cracker","crepe pan","cutting board","chorkor oven","clean-burning stove","clome oven","coffee percolator","coffeemaker","comal (cookware)","combi steamer","communal oven","community cooker","convection microwave","convection oven","cook stove","corn roaster","crepe maker","diffuser (heat)","double boiler","doufeu","dough blender","dough scraper","dutch oven","deep fryer","eggbeater","egg piercer","egg poacher","egg separator","egg slicer","egg timer","electric kettle","electric water boiler","embossing mat","earth oven","ecozoom","electric cooker","electric stove","energy regulator","fillet knife","fish scalar","fish slice (kitchen utensil)","flat iron grill pan","flat rack","flesh-hook","flour sifter","fondue pot","food mill","food processor","frosting spatula","frying pan","frying skillet","funnel","field kitchen","fire pot","flattop grill","food steamer","foukou","fufu machine","gas stove","garlic press","glass baking pan","gratine pan","grapefruit knife","grater","gravy strainer","greaseproof paper","griddle","grill pan","square griddle pan","hand held electric mixer","herb chopper","halogen oven","haybox","hibachi","hoang cam stove","hobo stove","horno","hot box (appliance)","hot plate","induction cooking","juicer","karahi","kettle","kitchen utensil","kitchen knife","kamado","kettle","kitchen oven","kitchen stove","kitchener range","krampouz","kujiejun","kyoto box","ladle","lame","lemon reamer","lemon squeezer","loaf pan","lobster pick","lo trau","mandoline","mated colander pot","measuring cup","measuring jug","measuring spoon","meat grinder","meat tenderizer","meat thermometer","meatloaf pan","melon baller","mezzaluna","mortar and pestle","microplane","microwave","microwave oven","milk watcher","mouli grater","mushroom cloth","masonry oven","mess kit","microwave oven","multi-fuel stove","nonadjustable v-rack","nonstick skillet","nutcracker","nutmeg grater","nomiku","omelette pan","oven","oven bag","oven glove","oxo (brand)","p-38 can opener","paella pan","palayok","parchment paper","pasta spoon","pastry bag","pastry blender","pastry brush","pastry wheel","peel (tool)","peeler","pepper mill","pie bird","pie pan","pizza cutter","plastic wrap","potato masher","potato ricer","pot boiler","pot holder","pothook","poultry shears","pressure cooker","pudding basin","pudding cloth","pyrex baking dish","popcorn maker","primus stove","ramekin","rice spoon","ricer","rice cooker","roasting jack","roasting pan","roasting pan with high cover","roasting rack","roller docker","rolling pin","rondeau","round cake pan","red cross stove","reflector oven","remoska","rice cooker","rice polisher","roasting jack","rocket mass heater","rocket stove","russian oven","salad spoon","salt and pepper shakers","saran (plastic)","saucier","saute pan","saucepan","sauteuse pan","scales","scissors","scoop","scotch hands","scraper (kitchen)","serving spoon","serving tongs","shellfish scraper","sieve","silpat","skewer","skillet","skimmer","slotted spoon","soup ladle","spatula","spider","splatter screen","springform pan","spurtle","stainless steel pan","steel saute pan","stir-fry pan","stockpot","sugar nips","sugar spoon","sugar thermometer","sugar tong","sujeo","sabbath mode","salamander broiler","samovar","sandwich toaster","self-cleaning oven","shichirin","sigri (stove)","slow cooker","solar cooker","soy milk maker","stove","susceptor","tablespoon","tajine","tamis","tava","tea infuser","teflon coated frying pan","timbale (food)","tin foil","tin opener","toaster oven","tomato knife","tongs","trivection oven","trivet","trussing needle","two burner griddle pan","tabun oven","tandoor","tangia","tea stove","thermal immersion circulator","toaster","tommy cooker","trojan room coffee pot","turkey fryer","vegetable peeler","vertical rack","vacuum fryer","wax paper","whisk","wok","wonder pot","wooden spoon","waffle iron","wet grinder","wood-burning stove","wood-fired oven","zester","stock pot", "zipper bag", "shallow dish"]
    primary_methods = ["boil", "bake", "brown", "cook", "deep-fry", "stir-fry", "simmer", "baste", "roast", "grill", "broil", "pan-fry", "poach", "steam", "braise", "stew", "scald", "sear", "blanch", "barbeque", "griddle", "sear", "fry", "melt"]
    secondary_methods = ["chop", "stir", "beat", "cream", "cure", "dice", "drizzle", "fold", "glaze", "julienne", "marinate", "mince", "sear", "shred", "sift", "slice", "peel", "puree", "reduce", "grate", "deglaze", "season", "crush", "squeeze", "shake"]
    recipe_to_cuisine = []
    total = 0
    no_primaries = 0
    no_secondaries = 0

    with open('saved_crawlr.json') as f:
        recipe_map = json.load(f)
        for link, recipe in recipe_map.iteritems():
            ingred_list = [ingred["name"] for ingred in recipe["ingredients"]]
            ingred_string = " ".join(ingred_list)
            cuisine = classify_string(ingred_dict, ingred_string)
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
                    if method in direction:
                        if method not in secondary_method:
                            secondary_method.append(method)
            if primary_method == "":
                no_primaries += 1
            if len(secondary_method) == 0:
                no_secondaries += 1
            total += 1
            recipe_to_cuisine.append({"link": link,
                                      "name": recipe["name"],
                                      "ingredients": recipe["ingredients"],
                                      "tools": tools_used,
                                      "cuisine": cuisine,
                                      "primary_method": primary_method,
                                      "secondary_methods": secondary_method})
        print "No primaries: ", no_primaries, " --- No secondaries: ", no_secondaries, " --- Total: ", total

    with open('final_structure.json', 'w') as f:
        data = json.dumps(recipe_to_cuisine, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4, separators=(',', ': '))
        f.write(data)


def main():
    summary_dict = get_dict(get_cuisine_dicts())
    ingred_dict = summary_dict["ingredients"]
    create_recipe_data_structures(ingred_dict)

if __name__ == '__main__':
    main()



