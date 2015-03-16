from crawlr import Crawler
from format_autograder import web_create_recipe
import vegetarian
import nutrition
import json 
import copy
from cuisine_transformer import GLOBAL_CUISINE_TRANSFORMER

def run_interface(url):
	crawler = Crawler(url)
	crawler.crawl_ntimes(1)
	crawler.write_to_file('web_saved.json')
	web_create_recipe('web_saved.json', 'web_recipe.json')