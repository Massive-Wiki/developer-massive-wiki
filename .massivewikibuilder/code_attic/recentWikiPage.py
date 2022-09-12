#!/usr/bin/env python
'''
recentWikiPage.py: list the most recently modified wikipage file in a Massive Wiki

Usage: ./recentWikiPage.py -w 'path to massive wiki folder'

To print a log of some steps in program execution, set the `LOGLEVEL` environment variable to `DEBUG`.

On the command line:

LOGLEVEL=DEBUG ./recentWikiPage.py -w 'path to massive wiki folder'

or:

export LOGLEVEL=DEBUG
./recentWikiPage.py -w 'path to massive wiki folder'

'''
import argparse
import os

# set up logging
import logging
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='find recently changed files in wiki.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug("args: %s", f"args: {args}")
    
    dir_wiki = args.wiki
    logging.info("wiki directory: %s", dir_wiki)

    wikifiles = []
    
    for root,dirs,files in os.walk(dir_wiki):
        dirs[:]=[d for d in dirs if not d.startswith('.')]
        files=[f for f in files if not f.startswith('.')]
        readable_path = root[len(dir_wiki):]
        logging.debug("absolute wiki directory path: %s", f"{dir_wiki}{readable_path}")
        for file in files:
            if file == 'netlify.toml' or file == 'YAML.md' or file == 'README.md':
                continue
            wikipath = f"{dir_wiki}{readable_path}/{file}"
            logging.debug("filename: %s: | wikipath: %s: | exists? %s: ",f"{file}", wikipath, str(os.path.exists(wikipath)))
            if file.lower().endswith('.md') and os.path.exists(wikipath):
                wikifiles.append(wikipath)

    print(max(wikifiles, key=os.path.getctime))
#    print(min(wikifiles, key=os.path.getctime))
    
if __name__ == "__main__":
    exit(main())
