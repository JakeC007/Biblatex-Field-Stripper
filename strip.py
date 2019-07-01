#!/usr/bin/env python3
"""This file strips fields from a biblatex file. The orginal code was written by astrobel found here: https://forums.zotero.org/discussion/22629/bibtex-export-request-option-to-omit-certain-fields-for-less-cluttered-bibliographies  
I made the code more robust by modifying it to run from the command line, automatic outputfile creation, and taking in multiple fields to strip.
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

  #Get user input on what to strip
  q_flag = True
  strip = []
  while q_flag == True:
     raw_strip = input("What would you like to strip? \n (press q to when you're done): ")
     if raw_strip == "q":
       break
     strip.append(raw_strip)
     print("Things to strip", end = " ")
     print(strip)

  print("Striping {} from {} and writing to {}".format(strip[0:], inputF, outputF))

  clean(inputF, outputF, strip)

def clean(inputF, outputF, strip):
  filename = inputF # the input file
  filename2 = outputF # create a new file for output
  start = '' # set type for field to strip
  end = '},'
  strip.append("cpyflg") #flag needed for complete strip

  
  flag = 0 
  tripped = False #flag to ensure that none of the desired fields have been found
  with open(filename) as infile, open(filename2, 'w+') as outfile:
    for line in infile:
      tripped = False
      for word in strip:
        start = word + ' = ' #current word to strip
        if line.strip().startswith(start) == True:
          flag = 1
          tripped = True

        elif flag == 1:
            if line.strip().endswith(end) == True:
              flag = 0
                      
        else:
          if word == "cpyflg" and tripped == False: 
            outfile.write(line)
            
    
if __name__ == "__main__":
  main()
