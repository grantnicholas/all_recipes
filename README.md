#requirements
Beautiful Soup: pip install beautifulsoup4
Server runs on flask: pip install Flask

#Run the GUI - main_server.py
run python main_server.py and go to http://127.0.0.1:5000/ to see the web page
enter a URL to parse a recipe and do transformations

#Run the Autograder
run python autograder.py

#crawlr.py 
Starts at an arbitrary starting place at allrecipes.com and then crawls the website for recipes; it saves the visited recipes in a dictionary with the key being the link and the value being the parsed html. This dictionary is then written to file when it is done [saved_crawlr.json].

Note: the crawlr can crawl pages and search for more recipes links on each page, which leads to an almost exponential increase in recipes. If you don't want to wait awhile do not go much above n=6

#parse_html.py 
Parses an html recipe page from allrecipes.com and extracts components of the recipe. I extracted ingredients, steps, ratings, and a few other things. 

#process_it.py
Uses the data we parsed in parse_html.py to do some processing and transform the ingredients/recipe into some new thing. 

#naive_bayes.py 
Naive bayesian classifier base. This is used in two places (one classifier for cuisines in ingredients_naive_bayes.py and one for types of food in food_cats_naive_bayes.py)

#food_cats_naive_bayes
*Look at the file for a simple API to use for prediction*
Uses a naive bayesian classifier to predict the type of food [ie: meat, dairy, vegetable, fruit, etc] from a string. 

#ingredients_naive_bayes.py
*Look at the file for a simple API to use for prediction*
Uses a naive bayesian classifier to predict the type of cuisine from a string. 
Also can predict the type of cuisine from a recipe [it uses the list of ingredients to predict]

#cuisine_transformer.py 
*Look at the file for a simple API to use for prediction*
Uses the cuisine and food type classifiers to convert a recipe from an old cuisine to a new cuisine. IE) It takes ingredients from the old recipe and converts them to ingredients of the SAME food type but of the NEW cuisine. 

ie: converting a recipe to asian

chicken => chicken
salsa   => soy sauce 
lime    => orange
rice    => noodles

#format_autograder.py 
File used to make the final_struture.json 

#files_to_learn
data used to train the naive bayesian food type classifier

data taken from:
http://www.fatsecret.com/calories-nutrition/group/salads


#tldr
    All the parsing magic happens in soup_to_Recipe which is located in 
    parse_html.py

    Converts html (in this case the html I converted to a beautifulsoup
    object for easier parsing) to a dictionary representation of a Recipe

