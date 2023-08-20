#!/usr/bin/python3

import json

REDIRECT = 'eagereyes.org/publications/'

papers = json.load(open('../eagereyes/papers.json', 'r'))

def makeRedirect(key):

    with open('docs/publications/%s.html' % key, 'w') as out:

        if key == 'index':
            key = ''
        
        out.write("""<html>
    <head>
        <meta http-equiv="Refresh" content="0; URL=https://%s" />
    </head>\n""" % (REDIRECT+key))
        out.write("""   <body>
        <h1>This page has moved!</h1>

        Redirecting to <a href="https://%s">%s</a>...
    </body>\n</html>\n""" % (REDIRECT+key, REDIRECT+key))


for paper in papers:
    print(paper['_key'])

    key = paper['_key'].replace(':', '-')

    makeRedirect(key)

makeRedirect('index')
