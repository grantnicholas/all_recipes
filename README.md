#crawlr.py 
Starts at an arbitrary starting place at allrecipes.com and then crawls the website for recipes; it saves the visited recipes in a dictionary with the key being the link and the value being html[or parsed html]. this dictionary is then written to file when it is done [saved_crawlr.json].

Note: the crawlr can crawl pages and search for more recipes links on each page, which leads to an almost exponential increase in recipes. 

#parse_html.py 
parses a recipe page from allrecipes.com and extracts components of the recipe. I extracted ingredients, steps, ratings, and a few other things. 

#tldr
    All the parsing magic happens in soup_to_Recipe which is located in 
    parse_html.py

    Converts html (in this case the html I converted to a beautifulsoup
    object for easier parsing) to a dictionary representation of a Recipe

