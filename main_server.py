from flask import render_template, Flask, request
from crawlr import Crawler
from naive_bayes import web_create_recipe
import vegetarian
import json 
import copy

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
	option_dict = {
		"vegetarian": vegetarian.make_vegetarian(original)
	}
	return option_dict[option]

if __name__ == '__main__':
	app.debug = True
	app.run()