#!/usr/bin/env python

import argparse
import glob
import os
from pathlib import Path
import re
import subprocess

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate HTML pages from Markdown wiki pages.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    return parser

def scrub_path(filepath):
    return re.sub(r'([ _?\#]+)', '_', filepath)

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    dir_wiki = str(args.wiki)
    print(dir_wiki)

# print the os.walk listing
    os_filelist=[]
    for root, dirs, files in os.walk(dir_wiki):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files = [f for f in files if not f.startswith('.')]
        readable_path = root[len(dir_wiki)+1:]
        path = scrub_path(readable_path)
#        wiki_root = "/"+Path(readable_path).relative_to(dir_wiki).as_posix()
#        print("root path: ", Path(root))
        for file in files:
            if file != 'netlify.toml':
                clean_name = scrub_path(file)
                print(Path(root) / file)
                os_filelist.append(f"{path}/{clean_name}")

    print("os.walk listing length: ", len(os_filelist))
#    print(os_filelist)

# print the glob listing
    glob_filelist = [Path(f).relative_to(dir_wiki).as_posix() \
               for f in glob.glob(f"{dir_wiki}/**/*.*", recursive=True) if f != 'netlify.toml']
    for file in glob_filelist:
        p = subprocess.run(["git", "-C", dir_wiki, "log", "-1", '--pretty="%cI\t%an\t%s"', file], capture_output=True, check=True)
#        print(file, p.stdout.decode('utf-8')[1:-2].split('\t',2))
    print("glob listing length: ", len(glob_filelist))
    print(glob_filelist)
    
if __name__ == "__main__":
    exit(main())
