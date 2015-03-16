from flask import render_template, Flask, request
from crawlr import Crawler
from format_autograder import web_create_recipe
import vegetarian
import nutrition
import json 
import copy
from cuisine_transformer import GLOBAL_CUISINE_TRANSFORMER

app = Flask(__name__)
original_recipe_json = {}

# initial page 
@app.route('/')
def main():
	return render_template('main.html')

# after user entered url, creates recipe
@app.route('/urlForm', methods=['POST','GET'])
def urlForm():	
	global original_recipe_json
	url = request.args.get('url','')
	crawler = Crawler(url)
	crawler.crawl_ntimes(1)
	# write to file to keep other file consistent
	crawler.write_to_file('web_saved.json')
	web_create_recipe('web_saved.json', 'web_recipe.json')
	with open('web_recipe.json', 'r') as f:
		text = f.read()
		original_recipe_json = json.loads(text)
	return render_template('main.html', recipe = original_recipe_json[0])

# transform to different recipe 
@app.route('/button/', methods=['POST', 'GET'])
@app.route('/button/<option>', methods=['POST', 'GET'])
def button_option(option):
	# transform object returns new json
	original = copy.deepcopy(original_recipe_json[0])
	new_recipe = option_dict(option, original)
	return render_template('main.html', recipe = original_recipe_json[0], new_recipe = new_recipe)

def option_dict(option, original):
	if option == "vegetarian":
		return vegetarian.make_vegetarian(original)
	elif option == "pescatarian":
		return vegetarian.make_pescatarian(original)
	elif option == "low_fat":
		return nutrition.decrease_fat(original)
	elif option in set(["italian", "mexican", "asian", "american", "mediterranean", "french"]):
		return cuisine_change(option, original)
	else:
		return original

def cuisine_change(option, original):
	original["cuisine"] = option
	#Don't rebuild the cuisine transformer for every request as that is expensive
	#use some module level immutable global state
	return GLOBAL_CUISINE_TRANSFORMER.transform_recipe(original, option) 

if __name__ == '__main__':
	app.debug = True
	app.run()