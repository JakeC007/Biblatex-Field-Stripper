#!/usr/bin/env python3
"""This file strips fields from a biblatex file. The orginal code was written by astrobel found here: 
https://forums.zotero.org/discussion/22629/bibtex-export-request-option-to-omit-certain-fields-for-less-cluttered-bibliographies  
I made the code more robust by modifying it to run from the command line, automatic outputfile creation, giving options on what to strip 
and taking in multiple fields to strip.
2019 Jake Chanenson 
"""
import sys

def main():
  if len(sys.argv) != 1:
    print("Usage: python3 prog.py ")
    sys.exit
 
  inputF = ''
  raw_inputF = input("Enter your .bib filename: ")
  inputF = raw_inputF + '.bib'
  outputF = raw_inputF + 'FIXED'+'.bib'

  lst_strip_options = getOptions(inputF)

  if lst_strip_options == "quit": #handle IOError
    sys.exit

  else: 
    print("These are your options of what you can strip:\n {}".format(lst_strip_options[0:]))

    #Get user input on what to strip
    q_flag = True
    strip = []
    while q_flag == True:
      raw_strip = input("What would you like to strip? \n (press q to when you're done): ")
      if raw_strip == "q":
        break
      if raw_strip in lst_strip_options: #validating input 
        strip.append(raw_strip)
        print("Things to strip:", end = " ")
        print(strip)
      else:
        print("Please input one of the options listed above.")

    clean(inputF, outputF, strip)

    end_pos = len(strip)-1
    print("Cleaned {} from {} and writing to {}".format(strip[0:end_pos], inputF, outputF))

def getOptions(inputF):
  strip_options = []
  try:
    with open(inputF, 'r', encoding='UTF-8') as f:
      for line in f:
        temp_word = line.split(None, 1)
        try:
          if '@' not in temp_word[0] and '}' not in temp_word[0]:
            strip_options.append(temp_word[0])
        except: #edge case for blank lines
          pass    
  except IOError: #If the input file was not found
    print("File not found. Please input the filename w/out the extension")
    return "quit"
  strip_lst = list(dict.fromkeys(strip_options)) #remove duplicates
  return strip_lst      

def clean(inputF, outputF, strip):
  filename = inputF # the input file
  filename2 = outputF # create a new file for output
  start = '' # set type for field to strip
  strip.append("cpyflg") #flag needed for complete strip
  
  tripped = False #flag to ensure that none of the desired fields have been found
  with open(filename, encoding='UTF-8') as infile, open(filename2, 'w', encoding='UTF-8') as outfile:
    for line in infile:
      tripped = False
      for word in strip:
        start = word + ' = ' #current word to strip
        if line.strip().startswith(start) == True:
          tripped = True         
        else:
          if word == "cpyflg" and tripped == False: 
            outfile.write(line)          
    
if __name__ == "__main__":
  main()
