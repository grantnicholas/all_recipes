#crawlr.py 
Starts at an arbitrary starting place at allrecipes.com and then crawls the website for recipes; it saves the visited recipes in a dictionary with the key being the link and the value being the parsed html. This dictionary is then written to file when it is done [saved_crawlr.json].

Note: the crawlr can crawl pages and search for more recipes links on each page, which leads to an almost exponential increase in recipes. If you don't want to wait awhile do not go much above n=6

#parse_html.py 
Parses an html recipe page from allrecipes.com and extracts components of the recipe. I extracted ingredients, steps, ratings, and a few other things. 

#process_it.py
Uses the data we parsed in parse_html.py to do some processing and transform the ingredients/recipe into some new thing. I was trying to learn cuisines of recipes from ingredients but a bunch of other stuff can be done. 

#naive_bayes.py 
Uses a naive bayesian classifier to predict the type of cuisine from the list of ingredients provided for a recipe. IE) If the recipe is listed as having "tomatoes, marinara sauce, pasta, and cheese" it will probably be italian. outputs to [saved_cuisines.json]


#tldr
    All the parsing magic happens in soup_to_Recipe which is located in 
    parse_html.py

    Converts html (in this case the html I converted to a beautifulsoup
    object for easier parsing) to a dictionary representation of a Recipe

