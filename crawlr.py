from timer import timeit
from parse_html import soup_to_Recipe

import urllib2
from bs4 import BeautifulSoup

import re
import json


class Crawler:

    def __init__(self, start_link):
        self.start_link = start_link
        self.visited_map = {}
        self.to_visit = set()
        self.crawl_count = 0
        self.filename = None

    def is_recipe(self, link):
        if link is not None:
            return re.findall(
                "^http://allrecipes.com/[r|R]ecipe/.+/", link) != []
        else:
            return False

    def update_map(self, recipes_list):
        for recipes in recipes_list:
            self.visited_map.update(recipes)

    def crawl_init(self):
        recipe, to_visit_links = self.crawl_alink(self.start_link)
        self.visited_map.update(recipe)
        self.to_visit = set(to_visit_links)
        self.crawl_count += 1

    def format_link(self, alink):
        formatted_link = re.findall(
            "(^http://allrecipes.com/[r|R]ecipe/[^\/]+)", alink)[0]
        return formatted_link

    """
    All the parsing magic happens in soup_to_Recipe which is located in 
    parse_html.py

    Converts html (in this case the html I converted to a beautifulsoup
    object for easier parsing) to a dictionary representation of a Recipe

    """

    def crawl_alink(self, link):
        if link in self.visited_map:
            return None

        html = urllib2.urlopen(link)
        soup = BeautifulSoup(html)
        recipe = {self.format_link(link): soup_to_Recipe(soup)}
        links = [self.format_link(alink.get('href')) for alink in soup.findAll(
        'a') if self.is_recipe(alink.get('href'))]

        return recipe, links


    @timeit
    def crawl_once(self):
        links_list = []
        for link in self.to_visit:
            return_val = self.crawl_alink(link)
            if return_val is None:
                continue
            recipe, links  = return_val
            self.visited_map.update(recipe)
            links_list.extend(links)

        self.to_visit = set(links_list)
        print links_list
        self.crawl_count += 1

    def crawl_ntimes(self, ntimes):
        for i in range(ntimes):
            if self.crawl_count == 0:
                self.crawl_init()
            else:
                self.crawl_once()

    def write_to_file(self, filename=None):
        if filename is not None:
            self.filename = filename
        if self.filename is None:
            raise Exception("Supply a filename to write to")
            return

        data = json.dumps(self.visited_map, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4, separators=(',', ': '))

        with open(self.filename, "w") as f:
            f.write(data)

    def read_from_file(self, filename=None):
        if filename is not None:
            self.filename = filename
        if self.filename is None:
            raise Exception("Supply a filename to read from")
            return

        with open(self.filename, "r") as f:
            data = json.loads(f.readlines())
            self.visited_map = data


def main():
    start_link = 'http://allrecipes.com/Recipe/Easy-Chicken-Pasta-Alfredo/Detail.aspx?soid=carousel_0_rotd&prop24=rotd'
    crawlr = Crawler(start_link)
    crawlr.crawl_ntimes(8)
    for k in crawlr.visited_map:
        print k
    crawlr.write_to_file("./saved_crawlr.json")


if __name__ == '__main__':
    main()
