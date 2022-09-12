#!/usr/bin/env python

import argparse
import os
import re

from pathlib import Path

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    dir_wiki = Path(args.wiki).resolve().as_posix()
    print(dir_wiki)

    wikifiles = {}
    
    for root,dirs,files in os.walk(dir_wiki):
        dirs[:]=[d for d in dirs if not d.startswith('.')]
        files=[f for f in files if not f.startswith('.')]
        readable_path = root[len(dir_wiki):]
        path = re.sub(r'([ _]+_)', '_', readable_path)
        for file in files:
            if file == 'netlify.toml':
                continue
            clean_name = re.sub(r'([ _]+_)', '_', file)
#            print( {'filename':f"/{file}", 'wikipath':f"{path}/{clean_name}"})
            wikifiles[file] = f"{path}/{clean_name}"
#            if file.lower().endswith('.md'):
#                    print( {'title':f"{readable_path}/{file[:-3]}", 'path':f"{path}/{clean_name[:-3]}.html"})

    print(wikifiles)
    
if __name__ == "__main__":
    exit(main())
