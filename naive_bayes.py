from math import log


def prob_one(ingred_dict, category, word):
    if word in ingred_dict[category]["data"]:
        prob = log(
            (.01 + ingred_dict[category]["data"][word]) / (.01 + ingred_dict[category]["count"]))
    else:
        prob = log(.01 / (.01 + ingred_dict[category]["count"]))

    return -1 * prob


def cprob_one(ingred_dict, category, word):
    cprob = 0
    for cat in ingred_dict:
        if cat != category:
            if word in ingred_dict[cat]["data"]:
                cprob += log(
                    (.01 + ingred_dict[cat]["data"][word]) / (.01 + ingred_dict[cat]["count"]))
            else:
                cprob += log(.01 / (.01 + ingred_dict[cat]["count"]))

    return -1 * cprob


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

    total_count = sum(ingred_dict[cat]["count"] for cat in ingred_dict)
    for cat in prob_of_cuisine:
        prior = -1 * log(ingred_dict[cat]["count"] * 1.0 / total_count)
        prob_of_cuisine[cat] += prior

    return prob_of_cuisine


def cprob_string(ingred_dict, string):
    cprob_of_cuisine = {cuisine: 0 for cuisine in ingred_dict}
    for word in string.split(" "):
        cprob_dict = cprob_word(ingred_dict, word)
        for cuisine in cprob_dict:
            cprob_of_cuisine[cuisine] += cprob_dict[cuisine]

    total_count = sum(ingred_dict[cat]["count"] for cat in ingred_dict)
    for cat in cprob_of_cuisine:
        prior = -1 * log(ingred_dict[cat]["count"] * 1.0 / total_count)
        cprob_of_cuisine[cat] += prior

    return cprob_of_cuisine


def classify_string(ingred_dict, astring):
    prob_dict = prob_string(ingred_dict, astring)
    cprob_dict = cprob_string(ingred_dict, astring)

    # pprint(prob_dict)
    # pprint(cprob_dict)

    val1, cat1 = min((v, k) for k, v in prob_dict.iteritems())
    val2, cat2 = max((v, k) for k, v in cprob_dict.iteritems())

    # if cat1 != cat2:
    #     print "disagrees"

    return cat2


def classify_string_with_prob(ingred_dict, astring):
    prob_dict = prob_string(ingred_dict, astring)
    cprob_dict = cprob_string(ingred_dict, astring)
    # pprint(prob_dict)
    # pprint(cprob_dict)

    val1, cat1 = min((v, k) for k, v in prob_dict.iteritems())
    val2, cat2 = max((v, k) for k, v in cprob_dict.iteritems())

    # if cat1 != cat2:
    #     print "disagrees"

    return cat2, val2


def main():
    print "no main function"

if __name__ == '__main__':
    main()
