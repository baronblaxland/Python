#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

prev_word          = "  "                #initialize previous word  to blank string
months             = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Nov','Dec']

dates_to_output    = [] #an empty list to hold dates for a given word
day_cnts_to_output = [] #an empty list of day counts for a given word
# see https://docs.python.org/2/tutorial/datastructures.html for list details

line_cnt           = 0  #count input lines

view_count = 0 # Count the number of views
running_total = 0
test_variable = 0

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list   
   
    
    #note: for simple debugging use print statements, ie:  
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item


    if(prev_word != curr_word):
        if(test_variable == 1):
            print( '%s\t%s' % (prev_word, running_total) )
            test_variable = 0
            running_total = 0

        if (value_in != "ABC"):
            view_count = int(value_in)
            running_total = int(running_total)
            running_total = view_count

    else:
        if(value_in != "ABC"):

            view_count = int(value_in) 
            running_total = int(running_total)
            running_total = running_total + view_count
        if(value_in == "ABC"):
            test_variable =1
         
        
    prev_word = curr_word