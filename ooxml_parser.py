import sys
import os

def word_read(path_file):
    c = ''
    word = ''
    print("\n==word.xml start==")
    for filename in os.listdir(path_file+"\\word"):
        with open(os.path.join(path_file+"\\word", filename), 'r', encoding="UTF-8") as f:
            while 1: 
                c = f.read(1)
                if c == ' ':
                    word = ''
                elif c == '"':
                    word = word + c
                    if word == 'descr="':
                        word = ''   
                        while 1:
                            c = f.read(1)
                            if c == '"':
                                print(word)
                                break
                            word = word + c    
                    word = ''
                elif c == '>':
                    word = word + c
                    if word == '<w:t>':
                        word = ''
                        while 1:
                            c = f.read(1)
                            if c == '<':
                                print(word)
                                break
                            word = word + c
                    word = ''
                elif c == '':
                    print("==word finish==\n")
                    exit()
                else:
                    word = word + c

def core_read(path_file):
    c = ''
    word = ''
    print("\n==core.xml start==")
    with open(os.path.join(path_file, "docProps\\core.xml"), 'r', encoding="UTF-8") as f:
        while 1: 
            c = f.read(1)
            if c == ' ':
                word = ''
            elif c == '\"':
                word = ''
            elif c == '>':
                word = word + c
                if word == '<dc:creator>':
                    word = ''
                    while 1:
                        c = f.read(1)
                        if c == '<':
                            print(word)
                            break
                        word = word + c
                if word == '<cp:lastModifiedBy>':
                    word = ''
                    while 1:
                        c = f.read(1)
                        if c == '<':
                            print(word)
                            break
                        word = word + c
                word = ''
            elif c == '':
                print("==core.xml finish==\n")
                break
            else:
                word = word + c

def word__rels_read(path_file):
    c = ''
    word = ''
    print("\n==document.xml.rels start==")
    with open(os.path.join(path_file, "word\\_rels\\document.xml.rels"), 'r', encoding="UTF-8") as f:
        while 1: 
            c = f.read(1)
            if c == '>':
                word = ''
            elif c == '"':
                word = word + c
                if word == ' Target="':
                    word = ''
                    while 1:
                        c = f.read(1)
                        if c == '"':
                            if word[-1] == '/':
                                print(word[1:])
                                break
                            word = ''
                        word = word + c
                        if c == '':
                            break
                word = ''
            elif c == '':
                print("==document.xml.rels finish==\n")
                break
            else:
                word = word + c
                
path_file = sys.argv[1]
for all_file in os.listdir(path_file):
    core_read(path_file)
    word__rels_read(path_file)
    word_read(path_file)
    