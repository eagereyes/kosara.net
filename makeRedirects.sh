#!/usr/bin/python3

import json

REDIRECT = 'eagereyes.org/publications/'

papers = json.load(open('../eagereyes/papers.json', 'r'))

for paper in papers:
    print(paper['_key'])

    key = paper['_key'].replace(':', '-')

    with open('docs/publications/%s.html' % key, 'w') as out:
        
        out.write("""<head>
  <meta http-equiv="Refresh" content="0; URL=https://%s" />
</head>""" % (REDIRECT+key))
        out.write("""<body>
        <h1>This page has moved!</h1>

        Redirecting to <a href="https://%s">%s</a>…
    </body>""" % (REDIRECT+key, REDIRECT+key))

