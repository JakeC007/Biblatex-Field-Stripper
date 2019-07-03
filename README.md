# Biblatex-Field-Stripper
This program takes out undesired fields from a biblatex file

This file strips fields from a biblatex file. The orginal code that inspired this project was written by astrobel found here: 
https://forums.zotero.org/discussion/22629/bibtex-export-request-option-to-omit-certain-fields-for-less-cluttered-bibliographies  
Though, only 6 lines from that blog post remain. 
I made the idea more robust by modifying it to run from the command line, adding automatic outputfile creation, giving options on what 
to strip, adding input validation, and (most importantly) taking in multiple fields to strip.


## How to run the program from the internet:
1. Go to https://repl.it/languages/python3
2. Copy and paste the contents of the strip.py file into the main.py text field
3. Upload your Biblatex file
4. Press the run button
5. Enter the filename of your .bib file WITHOUT the extension 
6. Enter the name of the fields you want to strip. This is case senstitive!
7. Press q to stop entering new fields
8. Download your new biblatex file(it should be on the left). The naming convention is <input filename>FIXED.bib


## How to run the program locally:
1. Run the program
2. Enter the filename of your .bib file WITHOUT the extension
3. Enter the name of the fields you want to strip. This is case senstitive!
4. Press q to stop entering new fields
5. Open your new biblatex file. The naming convention is <input filename>FIXED.bib


## Here is what the program looks like:

Below is an image of what the input looks like
![Image Of How To Use The Program](https://i.imgur.com/WTX2h92.png)


Below is an image of a biblatex entry in the input file
![Biblatex Before](https://i.imgur.com/qcRPTow.png)


Below is an image of a biblatex entry in the output file
![Biblatex After](https://i.imgur.com/WAT2nCV.png) 




