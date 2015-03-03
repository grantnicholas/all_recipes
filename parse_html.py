from bs4 import BeautifulSoup
import urllib2
import json


class Ingredient:

    def __init__(self, name=None, amount=None):
        self.name = name
        self.amount = amount

    def __str__(self):
        return "name: {0}, amount: {1}".format(self.name, self.amount)

    def __repr__(self):
        return "name: {0}, amount: {1}".format(self.name, self.amount)

    def to_json(self):
        return json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=True, indent=4, separators=(',', ': '))


class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return "name: {0}, ingredients: {1}".format(self.name, self.ingredients)

    def __repr__(self):
        return "name: {0}, ingredients: {1}".format(self.name, self.ingredients)

    def to_json(self):
        return json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=True, indent=4, separators=(',', ': '))


def soup_to_Recipe(soup):
    ingredients = soup_to_ingredients(soup)
    new_recipe = Recipe("Recipe name goes here", ingredients)
    return new_recipe


def ingredli_to_ingredient(ingred_li):
    name_span = ingred_li.find('span', {'class': 'ingredient-name'})
    amount_span = ingred_li.find('span', {'class': 'ingredient-amount'})

    name = name_span.text if name_span is not None else "not found"
    amount = amount_span.text if amount_span is not None else "not found"

    a_ingredient = Ingredient(name, amount)
    return a_ingredient


def url_to_soup(url):
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    return soup


def soup_to_ingredients(soup):
    zone = soup.find('div', {'id': 'zoneIngredients'})
    ingred_left = zone.find('div', {'class': 'ingred-left'})
    ingred_list = ingred_left.findAll('li', {'id': 'liIngredient'})

    ingredients = [
        ingredli_to_ingredient(ingred_li) for ingred_li in ingred_list]

    return ingredients


def url_to_ingredients(url):
    return soup_to_ingredients(
        url_to_soup(url)
    )


def main():
    testlink = "http://allrecipes.com/Recipe/Moms-Favorite-Baked-Mac-and-Cheese/?prop24=hn_slide1_Mom%27s-Favorite-Baked-Mac-and-Cheese&evt19=1"
    print url_to_ingredients(testlink)
    print soup_to_Recipe(url_to_soup(testlink))


if __name__ == '__main__':
    main()
