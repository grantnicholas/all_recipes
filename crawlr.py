from timer import timeit
from parse_html import url_to_ingredients, Recipe, soup_to_Recipe

import urllib2
from bs4 import BeautifulSoup

import re
from pprint import pprint
import json 




class Crawler:

    def __init__(self, start_link):
        self.start_link  = start_link
        self.visited_map = {}
        self.crawl_count = 0
        self.filename = None

    def is_recipe(self, link):
        if link is not None:
            return re.findall("^http://allrecipes.com/[r|R]ecipe/.+/", link) != []
        else:
            return False

    def update_map(self, recipes_list):
        for recipes in recipes_list:
            self.visited_map.update(recipes)    

    def crawl_init(self):
        recipes_dict = self.crawl_alink(self.start_link)
        self.visited_map.update(recipes_dict)
        self.crawl_count+=1

    def format_link(self, alink):
        formatted_link = re.findall("(^http://allrecipes.com/[r|R]ecipe/[^\/]+)", alink)[0]
        return formatted_link

    def crawl_alink(self, link):
        html = urllib2.urlopen(link)
        soup = BeautifulSoup(html)
        links = {alink.get('href'):soup for alink in soup.findAll('a')}
        recipes = {self.format_link(k): soup_to_Recipe(soup) for k,v in links.iteritems() if self.is_recipe(k) }
        return recipes

    @timeit
    def crawl_once(self):
        recipes_list = [self.crawl_alink(link) for link in self.visited_map]
        self.update_map(recipes_list)
        self.crawl_count+=1

    def crawl_ntimes(self, ntimes):
        for i in range(ntimes):
            if self.crawl_count == 0:
                self.crawl_init()
            else:
                self.crawl_once()

    def write_to_file(self, filename=None):
        if filename is not None:
            self.filename = filename
        if self.filename == None:
            raise Exception("Supply a filename to write to")
            return

        data=json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, separators=(',', ': '))

        with open(self.filename, "w") as f:
            f.write(data)

    def read_from_file(self, filename=None):
        if filename is not None:
            self.filename = filename
        if self.filename == None:
            raise Exception("Supply a filename to read from")
            return

        with open(self.filename, "r") as f:
            data = json.loads(f.readlines())
            self.visited_map = data






def main():
    crawlr = Crawler('http://allrecipes.com/Recipe/Easy-Chicken-Pasta-Alfredo/Detail.aspx?soid=carousel_0_rotd&prop24=rotd')
    crawlr.crawl_ntimes(3)
    for k in crawlr.visited_map:
        print k
    crawlr.write_to_file("./saved_crawlr.json")


if __name__ == '__main__':
    main()
