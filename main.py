import sys 
import os
import os.path
from os import path
from os import listdir
from os.path import isfile, join
import pathlib
from itertools import chain
from glob import glob
import fileinput
from collections import Counter
import pandas as pd
import numpy as np
import nltk



def writetxt(filename,text,path): 
  original_stdout = sys.stdout 
  with open(str(path)+"/"+filename, 'w') as f:
    sys.stdout =f 
    print(text)
    print('\n')


def readFile(path):
    file=open(str(path),'r')
    print(file.read())
    file.close()


def add_symbol(prefix,suffix,in_filename,out_filename):
  with open(in_filename, 'r') as src:
      with open(out_filename, 'w') as dest:
        for line in src:
            dest.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))


def lower_lines(filename):
  with open(filename , 'r') as f:
      for line in f:
          line_low=line.lower()
          # print(line_low)
          with open("new_"+filename,'a') as file:
            file.writelines(line_low+"\n")


def replace_word(filename,text_to_search,replacement_text):
  with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
      for line in file:
          print(line.replace(text_to_search, replacement_text), end='')


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles 

def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())


def modifyFile(filename):
  if filename=="test.txt":
    print('add prefix and suffix '+filename)
    add_symbol(prefix,suffix,filename,"new_"+filename)
    print('lowercase '+filename)
    lower_lines("new_"+filename)
  elif filename=="train.txt":
    print('lowercase '+filename)
    lower_lines(filename)
    for key, value in word_count("new_"+filename).items():
      if value==1:
        text_to_search=key
        replacement_text='<unk>'
        print('replacing words')
        replace_word("new_"+filename,text_to_search,replacement_text)
        add_symbol(prefix,suffix,filename,"new_"+filename)


current_path=os.getcwd()
listOfFile = os.listdir()
# print(getListOfFiles(path))

prefix="<s>"
suffix="</s>"
in_files=["test.txt","train.txt"]


# filename="train.txt"
# if "new_"+filename in listOfFile:
#   print("exist")
#   add_symbol(prefix,suffix,"new_"+filename,"new_new_train.txt")
# else:
#   lower_lines(filename)
#   print('single occurrence')
#   for key, value in word_count(filename).items():
#     if value==1:
#       text_to_search=key
#       replacement_text='<unk>'
#       replace_word("new_"+filename,text_to_search,replacement_text)
#       add_symbol(prefix,suffix,"new_"+filename,"new_new_train.txt")


    
df1=pd.read_table("test.txt", header=None, sep="/t") 

for index in df1.index:
    df1.loc[index,0]='<s>'+df1.loc[index,0]+'</s>'

df1[0] = df1[0].str.lower()
# print(small1)

print('table 2')
df2=pd.read_table("train.txt", header=None) 
print('read table 2')
df2[0] = df2[0].str.lower()
print('lowered table 2')
counter = Counter(chain.from_iterable(map(str.split, df2[0].tolist()))) 
for index in df2.index:
  df2.loc[index,0]='<s>'+df2.loc[index,0]+'</s>'
print('suffix and prefix added')
df2[0]=df2[0].str.strip()

print(df2.head(3))

prova=df2.head(3)


print('occurrences')

# print(counter)
#ha ancora la s, <s>under:1
print("lenght dictionary "+str(len(counter)))

list_single=[]
for key,value in counter.items():
  if value==1:
    list_single.append(key)

# occurrences=df2[0].str.split(expand=True).stack().value_counts()
# print(occurrences.index)
# print(occurrences.loc['the'])
#list_single=[]
# for index in occurrences.index:
#   if occurrences.loc[index]==1:
#     list_single.append(occurrences.loc[index])


print(len(list_single))

df3=df2

for word in list_single:
  df3[0].replace(word, '<unk>')

prova1=df3.head(5)
print(prova1)

numpy_array = df1.to_numpy()
np.savetxt("test_file.txt", numpy_array, fmt = "%s")
numpy_array1 = df3.to_numpy()
np.savetxt("train_file.txt", numpy_array1, fmt = "%s")
# tfile = open('train_pandas.txt', 'a')
# tfile.write(df3.to_string())
# tfile.close()


# tfile = open('test_pandas.txt', 'a')
# tfile.write(df1.to_string())
# tfile.close()