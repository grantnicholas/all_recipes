import json
from pprint import pprint
import re


def stopwords():
    stahp_words = set([
        'a', 'cannot', 'into', 'our', 'thus', 'about', 'co', 'i', 'is', 'ours', 'to', 'above',
        'could', 'it', 'ourselves', 'together', 'across', 'down', 'its', 'out', 'too',
        'after', 'during', 'itself', 'over', 'toward', 'afterwards', 'each', 'last', 'own',
        'towards', 'again', 'eg', 'latter', 'per', 'under', 'against', 'either', 'latterly',
        'perhaps', 'until', 'all', 'else', 'least', 'rather', 'up', 'almost', 'elsewhere',
        'less', 'same', 'upon', 'alone', 'enough', 'ltd', 'seem', 'us', 'along', 'etc',
        'many', 'seemed', 'very', 'already', 'even', 'may', 'seeming', 'via', 'also', 'ever',
        'me', 'seems', 'was', 'although', 'every', 'meanwhile', 'several', 'we', 'always',
        'everyone', 'might', 'she', 'well', 'among', 'everything', 'more', 'should', 'were',
        'amongst', 'everywhere', 'moreover', 'since', 'what', 'an', 'except', 'most', 'so',
        'whatever', 'and', 'few', 'mostly', 'some', 'when', 'another', 'first', 'much',
        'somehow', 'whence', 'any', 'for', 'must', 'someone', 'whenever', 'anyhow',
        'former', 'my', 'something', 'where', 'anyone', 'formerly', 'myself', 'sometime',
        'whereafter', 'anything', 'from', 'namely', 'sometimes', 'whereas', 'anywhere',
        'further', 'neither', 'somewhere', 'whereby', 'are', 'had', 'never', 'still',
        'wherein', 'around', 'has', 'nevertheless', 'such', 'whereupon', 'as', 'have',
        'next', 'than', 'wherever', 'at', 'he', 'no', 'that', 'whether', 'be', 'hence',
        'nobody', 'the', 'whither', 'became', 'her', 'none', 'their', 'which', 'because',
        'here', 'noone', 'them', 'while', 'become', 'hereafter', 'nor', 'themselves', 'who',
        'becomes', 'hereby', 'not', 'then', 'whoever', 'becoming', 'herein', 'nothing',
        'thence', 'whole', 'been', 'hereupon', 'now', 'there', 'whom', 'before', 'hers',
        'nowhere', 'thereafter', 'whose', 'beforehand', 'herself', 'of', 'thereby', 'why',
        'behind', 'him', 'off', 'therefore', 'will', 'being', 'himself', 'often', 'therein',
        'with', 'below', 'his', 'on', 'thereupon', 'within', 'beside', 'how', 'once',
        'these', 'without', 'besides', 'however', 'one', 'they', 'would', 'between', 'i',
        'only', 'this', 'yet', 'beyond', 'ie', 'onto', 'those', 'you', 'both', 'if', 'or',
        'though', 'your', 'but', 'in', 'other', 'through', 'yours', 'by', 'inc', 'others',
        'throughout', 'yourself', 'can', 'indeed', 'otherwise', 'thru', 'yourselves'
    ])

    return stahp_words


def make_string_searcher(regex):
    rx = re.compile(regex, re.IGNORECASE)

    def find_string(string):
        return re.search(rx, string)

    return find_string


def update_dict(adict, words, stopwords):
    for word in words:
        if word.lower() not in stopwords:
            if word in adict:
                adict[word] += 1
            else:
                adict[word] = 1


def get_dict_topn(thedict, n):
    return [v for k, v in enumerate(sorted(thedict.items(), key=lambda x: x[1])[::-1]) if k < n]


def pprint_dict_topn(learned_dict, n):
    pprint(get_dict_topn(learned_dict["name"], n))
    pprint(get_dict_topn(learned_dict["ingredients"], n))
    pprint(get_dict_topn(learned_dict["directions"], n))


def learn_cuisine(data, is_cuisine_string):
    learned_dict = {}
    learned_dict["name"] = {}
    learned_dict["ingredients"] = {}
    learned_dict["directions"] = {}

    for link, recipe in data.iteritems():
        if is_cuisine_string(recipe["name"]):
            words = recipe["name"].split(" ")
            update_dict(learned_dict["name"], words, stopwords())

        for ingred in recipe["ingredients"]:
            if is_cuisine_string(ingred["name"]):
                for mem_ingred in recipe["ingredients"]:
                    words = mem_ingred["name"].split(" ")
                    update_dict(learned_dict["ingredients"], words, stopwords())

        for direct in recipe["directions"]:
            if is_cuisine_string(direct):
                words = direct.split(" ")
                update_dict(learned_dict["directions"], words, stopwords())

    return learned_dict



def get_cuisine_dicts():
    cuisine_dict = {}
    with open('saved_crawlr.json') as f:
        data = json.load(f)

        is_mexican_string = make_string_searcher(
            "mexico|mexican|salsa|taco|burrito|enchilada|chile|chili")
        mexican_dict = learn_cuisine(data, is_mexican_string)
        cuisine_dict["mexican"] = mexican_dict

        is_italian_string = make_string_searcher(
            "italian|pasta|pizza|tomato")
        italian_dict = learn_cuisine(data, is_italian_string)
        cuisine_dict["italian"] = italian_dict

        is_asian_string = make_string_searcher(
            "china|chinese|asian|stir-fry|stir\sfry|fried\srice|sesame|spring\sroll|hoisin|tapioca|teryiaki|soy|tofu")
        chinese_dict = learn_cuisine(data, is_asian_string)
        cuisine_dict["asian"] = chinese_dict

        is_american_string = make_string_searcher(
            "america|american|mac\sand\scheese|hot\sdog|southern|bbq|kraft|processed|oakra|grits|burger|hamburger|fries|chicken\stender|ketchup|ranch|mayo|roast|meatloaf|spam|oscar|cream\scheese")
        american_dict = learn_cuisine(data, is_american_string)
        cuisine_dict["american"] = american_dict

        is_medit_string = make_string_searcher(
            "greek|olive|feta|mediterranean|hummus|chickpea")
        medit_dict = learn_cuisine(data, is_medit_string)
        cuisine_dict["mediterranean"] = medit_dict

    return cuisine_dict



def main():
    with open('saved_crawlr.json') as f:
        data = json.load(f)

        is_mexican_string = make_string_searcher(
            "mexico|mexican|bean|rice|sour\scream|corn")
        mexican_dict = learn_cuisine(data, is_mexican_string)
        pprint_dict_topn(mexican_dict, 10)

        is_italian_string = make_string_searcher(
            "italian|italy")
        italian_dict = learn_cuisine(data, is_italian_string)
        pprint_dict_topn(italian_dict, 10)

        is_chinese_string = make_string_searcher(
            "china|chinese")
        chinese_dict = learn_cuisine(data, is_chinese_string)
        pprint_dict_topn(chinese_dict, 10)

        is_american_string = make_string_searcher(
            "america|american|mac\sand\scheese|hot\sdog|southern|bbq")
        american_dict = learn_cuisine(data, is_american_string)
        pprint_dict_topn(american_dict, 10)

        is_indian_string = make_string_searcher(
            "india|indian|curry")
        indian_dict = learn_cuisine(data, is_indian_string)
        pprint_dict_topn(indian_dict, 10)

        # pprint(get_cuisine_dicts())

if __name__ == '__main__':
    main()
