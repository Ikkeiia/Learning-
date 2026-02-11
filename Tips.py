#Ctrl C close cmd

#Formating
#2enters between functions befor and after function
#
#

##Liberaries
#---------------------------------------------
#win32api windows movement and related stuff prety much anything
#time used for time related stuff like wait
#random used for randomising stuff
#you can use json for dumping dictionaries and reading them back great for saves
#os can chack if the file exist and do stuff with you system overall


##Functions and arguments
#---------------------------------------------
#functions are used to store recuring stuff that would be needed to be rewrote again
def mainer():    #inside functions(is a argument) 
    print("hand")
    print("hand")
    print("hand")
    return 2                    #return is for stopping the looping
mainer() #runs the function

##Conditions

if condition > Value:
    print("good")


##Dictionaries
# are used for creating lists and printing what you want from them

Dict = {'1' : "You like minecraft", '2' : "You dont like minecraft" }       #first is key second is value 
#you can make nested dictionaries like
Anime_list = {                              

    'frieren' :{'anime episodes' : 24, 'anime rating /10' : 10,},
    'yuusha-kei' :{'anime episodes' : 12,'anime rating /10' : 8,},
    'apotheacary diaries' :{'anime episodes' : 12,'anime rating /10' : 8,}
}

##Try and except Code testing


try:                   #Try will try the script and it would not close the script
    mainer()
except ValueError:     # except adds exception for the errors or stuff that might break your code
    print("there was a value error")

#---------------------------------------------
# # Pre Task 3 learning  checklist
# 1.Make sure you already understand all the previous stuff                                              ✅  eeeh kinda?                                              
# 2.Multiple and augmented assignment 🤖                                                                                                                                    ✅  
# 3.Strings, substrings, string splitting, manipulating strings (such as taking only the last letter, searching them, indexing, slicing them etc)                
# 4.Common escapes (backslash letters like \n \t), print formatting, raw strings, strings with 3x " such as """hi""" and when to use them                 
# 5.Getting a specific element, unpacking, iterating through every container in python (tuples, dictionaries, arrays, etc) 
# 6.Exception handling (try, except, else, finally, raise) 🤖
# 7.Basic iteration and counters (in loops) keep it very basic don't go off-track. 🤖
# 8.Understand the differences in imports as well as why things like 'if name == main' are relevant 🤖
#---------------------------------------------




##Multiple and augmented assignment
#---------------------------------------------
#you can do more compact definitions
#instead of this
x = 10
y = 20
z = 30

#you do this
x, y, z = 10, 20, 30
#what you can do with is is either defining stuff and using it that way or you can swap the values like
varA, varB = varB, varA

### Augmented Assignment
##common augmentations

# += (Addition)
# -= (Subtraction)
# *= (Multiplication)
# /= (Division)
# %= (Modulo/Remainder)
# **= (Exponentiation)

current_batch = "1"
#you can go from this
total_count = total_count + current_batch
# to this
total_count += current_batch
print(total_count)

# you can basicly do cool stuff like this 
x = int(input("input a number"))
while True:
    y = 10
    x += y
    print(x)



