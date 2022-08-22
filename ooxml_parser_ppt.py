import sys
import os

def ppt_read(path_file):
    c = ''
    word = ''
    print("\n==ppt start==")
    for filename in os.listdir(path_file+"\\ppt\\slides"):
        if '.xml' not in filename:
            continue
        with open(os.path.join(path_file+"\\ppt\\slides", filename), 'r', encoding="UTF-8") as f:
            while 1: 
                c = f.read(1)
                if c == ' ':
                    word = ''
                elif c == '"':
                    word = ''
                elif c == '>':
                    word = word + c
                    if word == '<a:t>':
                        word = ''
                        while 1:
                            c = f.read(1)
                            if c == '<':
                                print(word)
                                break
                            word = word + c
                    word = ''
                elif c == '':
                    print("==ppt finish==\n")
                    break
                else:
                    word = word + c
                
path_file = sys.argv[1]
for all_file in os.listdir(path_file):
    ppt_read(path_file)
    exit()
    