import json
import csv
import glob
from pprint import pprint
from collections import Counter
import requests
import sys

# from your_module import your_function as student
from format_autograder import url_to_recipe_autograder as student
TEAM = 14  # enter your team number here

def check_tools(answer, stud):
    score = 0
    expans = dict([[a,a.split()] for a in answer])

    for s in stud:
        if s in answer:
            print s
            score += 1
            answer.remove(s)
            stud.remove(s)

    expans = dict([[a,{'words':a.split(), 'matches':Counter()}] for a in answer])
    expstud = dict([[a,a.split()] for a in stud])
    
    for s in expstud:
        tmpscore = -1
        for word in expans:
            complement = set(expstud[s]) ^ set(expans[word]['words'])
            intersection = set(expstud[s]) & set(expans[word]['words'])
            newscore = float(len(intersection))/(len(intersection)+len(complement))
            print "%s, %s, %d, %d, %f"%(s,word,len(intersection),len(complement),newscore)
            if newscore > tmpscore:
                tmpscore = newscore
                tmpmatch = word
        if tmpscore > 0:
            expans[tmpmatch]['matches'][s] = tmpscore
            stud.remove(s)

    for word in expans:
        match = expans[word]['matches'].most_common(1)
        if len(match) > 0:
            score += expans[word]['matches'].most_common(1)[0][1]

    return score

def check_ingredients(answer,stud):
    scores = []
    score = 0

    for x in range(min([len(answer),len(stud)])):
        for ind in ['name','measurement','quantity','descriptor','preparation','prep-description']:
            if ind in stud[x]:
                print stud[x][ind]
                print answer[x][ind]
                if stud[x][ind] in answer[x][ind]:
                    score += 1
        print "---"
        scores.append(min([score,answer[x]['max']]))
        score = 0

    return sum(scores)

def get_file(fn):
    with open(fn, 'r') as f:
        answer = json.load(f)
    return answer

def main(init=False,input_type="url",filename=None):
    """Pass 'init' as a command line variable if this is your
    first time running the program and you want it to print the
    column headers to the file. 

    Set input_type to 'html' if your program accepts HTML rather
    than a URL.

    If your program accepts copied and pasted text (as displayed),
    put it in a file, set input_type to 'text', and pass the 
    filename as another argument."""

    keys = ['ingredients','primary cooking method','cooking methods','cooking tools']

    if init:
        with open('parsegrades.csv','ab') as csvfile:
            csvwriter = csv.writer(csvfile,delimiter='\t')
            csvwriter.writerow(keys)

    scores = dict(zip(keys,[0]*len(keys)))
    
    tmpmeth = 0
    tmptool = 0
    tmping = 0

    for answer in (get_file(fn) for fn in glob.iglob('./Recipes/*.json')):
        if input_type == "url":
            stud = student(answer['url'])
        elif input_type == "html":
            stud = student(requests.get(answer['url']).text)
        elif input_type == "text" and filename:
            with open(filename, 'r') as f:
                stud = student(f.read())


        if type(stud) == str:
            stud = json.loads(stud)
        pprint(stud)
        if type(stud) == dict:            
            tmptool = min([check_tools(answer['cooking tools'],stud['cooking tools']), answer['max']['cooking tools']])/float(answer['max']['cooking tools'])
            scores['cooking tools'] += tmptool
            tmpmeths = min([check_tools(answer['cooking methods'],stud['cooking methods']), answer['max']['cooking methods']])/float(answer['max']['cooking methods'])
            scores['cooking methods'] += tmpmeths
            if stud['primary cooking method'] == answer['primary cooking method']:
                tmpmeth = 1
                scores['primary cooking method'] += 1
            stud = stud['ingredients']
            tmping = check_ingredients(answer['ingredients'],stud)/float(answer['max']['ingredients'])
            scores['ingredients'] += tmping
            print "%.3f\t%d\t%.3f\t%.3f"%(tmping,tmpmeth,tmpmeths,tmptool)
        else:
            print "student answer error"

    row = ["Team %d"%TEAM]
    row.extend([scores[k] for k in keys])

    with open('parsegrades.csv','ab') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter='\t')
        csvwriter.writerow(row)

if __name__ == '__main__':
    init = False
    input_type = False
    filename = False
    for arg in sys.argv[1:]:
        if arg == "init":
            init = True
        elif arg in ['url','html','text']:
            input_type = arg
        else:
            filename = arg
    if not input_type:
        main(init)
    elif input_type == 'text':
        if filename:
            main(init,input_type,filename)
        else:
            "Error: Filename required."
    else:
        main(init,input_type)