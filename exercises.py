# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 07:40:14 2019

@author: Hernán
"""
import sys
help(len)
dir(sys)

help(len) #— help string for the built-in len() function; note that it's "len" not "len()", which is a call to the function, which we don't want
help(sys) #— help string for the sys module (must do an import sys first)
dir(sys) #— dir() is like help() but just gives a quick list of its defined symbols, or "attributes"
help(sys.exit) #— help string for the exit() function in the sys module
help('xyz'.split) #— help string for the split() method for string objects. You can call help() with that object itself or an example of that object, plus its attribute. For example, calling help('xyz'.split) is the same as calling help(str.split).
help(list) #— help string for list objects
dir(list) #— displays list object attributes, including its methods
help(list.append) #— help string for the append() method for list objects

# Beautifuller
# Standard of coding

raw = r'this\t\n and that'

  # this\t\n and that
print (raw)

no_raw = 'this\t\n and that'

  # this\t\n and that
print (no_raw)

multi = """It was the best of times.
  It was the worst of times."""

  # It was the best of times.
  #   It was the worst of times.
print (multi)



  if speed >= 80:
    print 'License and registration please'
    if mood == 'terrible' or speed >= 100:
      print 'You have the right to remain silent.'
    elif mood == 'bad' or speed >= 90:
      print "I'm going to have to write you a ticket."
      write_ticket()
    else:
      print "Let's try to keep it under 80 ok?"