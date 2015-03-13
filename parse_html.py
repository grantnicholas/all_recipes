from bs4 import BeautifulSoup
import urllib2
from timer import timeit


def url_to_soup(url):
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    return soup


def url_to_ingredients(url):
    return soup_to_ingredients(
        url_to_soup(url)
    )


def soup_to_Recipe(soup):
    title       = soup_to_title(soup)
    ingredients = soup_to_ingredients(soup)
    directions  = soup_to_directions(soup)
    ratings     = soup_to_ratings(soup)
    footnotes   = soup_to_footnotes(soup)
    nutrition   = soup_to_nutrition(soup)
    new_recipe = {"name": title,
                  "ratings": ratings,
                  "ingredients": ingredients,
                  "directions": directions,
                  "nutrition": nutrition,
                  "footnotes": footnotes}
    return new_recipe


def ingredli_to_ingredient(ingred_li):
    name_span = ingred_li.find('span', {'class': 'ingredient-name'})
    amount_span = ingred_li.find('span', {'class': 'ingredient-amount'})
    name = name_span.text if name_span is not None else "not found"
    amount = amount_span.text if amount_span is not None else "not found"
    a_ingredient = {"name": name,
                    "quantity": amount}
    return a_ingredient


def directli_to_direction(direct_li):
    direct_span = direct_li.find('span')
    text = direct_span.text if direct_span is not None else "not found"
    a_direction = text
    return a_direction


def ratingli_to_rating(rating_li):
    if rating_li is not None and rating_li.has_attr('title'):
        num_stars = rating_li['title']
    else:
        num_stars = "not found"
    rating = num_stars
    return rating


def noteli_to_note(note_li):
    if note_li is not None and note_li is not []:
        note = note_li.text
    else:
        note = "not found"
    return note


def nutritionul_to_nutrition(nutrition_ul):
    nut_list = nutrition_ul.findAll('li')
    forbidden_cats = [
        "nutrition-rating-img", "nutrition-rating-grad", "nutrition-rating"]
    nutrition = {nut_li["class"][0]: nut_li.text for nut_li in nut_list if nut_li["class"][
        0] not in forbidden_cats}
    return nutrition


def soup_to_title(soup):
    title_h1 = soup.find('h1', {'id' : 'itemTitle'})
    title = title_h1.text if title_h1 is not None else "Title not found"
    return title

def soup_to_ingredients(soup):
    zone = soup.find('div', {'id': 'zoneIngredients'})
    ingred_left = zone.find('div', {'class': 'ingred-left'})
    ingred_list = ingred_left.findAll('li', {'id': 'liIngredient'})
    ingredients = [ingredli_to_ingredient(ingred_li) 
                    for ingred_li in ingred_list]
    return ingredients


def soup_to_directions(soup):
    zone = soup.find('div', {'class': 'directions'})
    direct_left = zone.find('div', {'class': 'directLeft'})
    directions_list = direct_left.findAll('li')
    directions = [directli_to_direction(direct_li)
                  for direct_li in directions_list]
    return directions


def soup_to_ratings(soup):
    graph_ul = soup.find('ul', {'id': 'ulGraph'})
    rating_list = graph_ul.findAll('li')
    ratings = {str(k): ratingli_to_rating(v)
               for k, v in zip(range(1, 6)[::-1], rating_list)}
    return ratings


def soup_to_footnotes(soup):
    footnote_div = soup.find('div', {'class': 'footnotes'})
    note_list = soup.findAll('div', {'id': 'noteContainer'})
    footnotes = [noteli_to_note(note_li) for note_li in note_list]
    return footnotes


def soup_to_nutrition(soup):
    nut_zone = soup.find('div', {'id': 'zoneNutrition'})
    nut_uls = nut_zone.findAll('ul', {'id': 'ulNutrient'}) if nut_zone is not None else []
    nutrition = [nutritionul_to_nutrition(nut_ul) 
                    for nut_ul in nut_uls]
    return nutrition



def main():
    # testlink = "http://allrecipes.com/Recipe/Moms-Favorite-Baked-Mac-and-Cheese/?prop24=hn_slide1_Mom%27s-Favorite-Baked-Mac-and-Cheese&evt19=1"
    # print soup_to_Recipe(url_to_soup(testlink))

    # notherlink = "http://allrecipes.com/recipe/chicago-dip"
    # print soup_to_footnotes(url_to_soup(notherlink))
    # print soup_to_Recipe(url_to_soup(notherlink))

    testlink3 = "http://allrecipes.com/recipe/chocolate-yummies-3"
    print soup_to_nutrition(url_to_soup(testlink3))
    print soup_to_Recipe(url_to_soup(testlink3))


if __name__ == '__main__':
    main()
