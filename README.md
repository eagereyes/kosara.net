
# README

## To Create/Update Site

Basic update workflow:

```
git pull origin
pipenv run python3 makebib.py
bundle exec jekyll build
```

Run `pipenv run python3 makebib.py` to create `_bibliography/papers.bib` and the individual pages under `_pages/publications`.

The directory `_pages/publications` might need to be created, it's not checked in.

Then run `bundle exec jekyll serve` locally or `bundle exec jekyll build` on the server.

## License

Based on https://github.com/otiliastr/otiliastr.github.io

License: MIT
