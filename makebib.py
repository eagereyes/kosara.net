#!/usr/bin/python3

from yaml import safe_load

def paperpage(key, pub):
    filename = key.replace(':', '-')
    with open('_pages/publications/%s.md' % filename, 'w') as f:
        print("""---
layout: page
permalink: /publications/%s.html
title: "%s"
collection: hidden
---

%s

{%% bibliography -f papers -q @*[key=%s] %%}
""" % (filename, pub['title'], pub['abstract'], key), file=f)


def incfield(field, pub, o):
    if field in pub:
        print('\t%s = {%s},' % (field, pub[field]), file=o)


pubs = safe_load(open('papers.yaml'))

venues = safe_load(open('_data/venues.yml'))

with open('_bibliography/papers.bib', 'w') as o:

    for key in pubs:
        pub = pubs[key]

        # print(key)

        print('@%s{%s,' % (pub['type'], key), file=o)
        print('\ttitle = {%(title)s},' % pub, file=o)
        print('\tauthor = {%(author)s},' % pub, file=o)

        abbr = key.split(':')[1]
        if abbr == 'CGA':
            abbr = 'CG&A'
        if abbr in venues:
            print('\tabbr = {%s},' % abbr, file=o)

        year = key.split(':')[2][:4]
        print('\tyear = {%s},' % year, file=o)

        if pub['type'] == 'article':
            print('\tjournal = {%(venue)s},' % pub, file=o)
            if 'volume' in pub:
                print('\tvolume = {%(volume)s},' % pub, file=o)
            if 'number' in pub:
                print('\tnumber = {%(number)s},' % pub, file=o)
        else:
            print('\tbooktitle = {%(venue)s},' % pub, file=o)

        incfield('editor', pub, o)
        incfield('pages', pub, o)
        incfield('doi', pub, o)
        incfield('data', pub, o)
        incfield('website', pub, o)
        incfield('talk', pub, o)

        filename = key.replace(':', '-')
        if not 'pdf' in pub: # means there's a 'pdf: no' key
            print('\tpdf = {https://kosara.net/papers/%s/%s.pdf},' % (year, filename), file = o)

        print('\tfilename = {%s},' % filename, file=o)

        if 'abstract' in pub:
            print('\tabstract = {{%(abstract)s}},' % pub, file=o)

        print('}\n', file=o)

        if not 'pdf' in pub: # means there's a 'pdf: no' key
            paperpage(key, pub)
