##Basic help
#---------------------------------------------
#Ctrl C close cmd
#you can use midle mouse button to select text verticaly instead of selecting all to the point you can select the whole column and leave the rest untuched
#---------------------------------------------




##Formating
#---------------------------------------------
#2enters between functions befor and after function
#---------------------------------------------


##Arrays
#---------------------------------------------
#An array is a collection of values
#arrey uses indexing meanig every position is depicitet as an number
#values are whats inside and array
#tiference from Dictionaries is that the array is ordered
#most of the time arrays will have same datatype meaning it will aither be string int or float

dealership = ['toyota', 'subaru', 'ford']


#---------------------------------------------
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


#---------------------------------------------
##Conditions
#---------------------------------------------
if condition > Value:
    print("good")


#---------------------------------------------
##Dictionaries
#---------------------------------------------
# are used for creating lists and printing what you want from them
#the diference from arays is that its chaotic meaning order doesnt matter
#dictionaries map relationships between keys and values. 

Dict = {'1' : "You like minecraft", '2' : "You dont like minecraft" }       #first is key second is value 
#you can make nested dictionaries like
Anime_list = {                              

    'frieren' :{'anime episodes' : 24, 'anime rating /10' : 10,},
    'yuusha-kei' :{'anime episodes' : 12,'anime rating /10' : 8,},
    'apotheacary diaries' :{'anime episodes' : 12,'anime rating /10' : 8,}
}
#---------------------------------------------
##Try and except Code testing
#---------------------------------------------
#Try will try the script and it would not close the script
# except adds exception for the errors or stuff that might break your code

try:                   
    mainer()
except ValueError:     
    print("there was a value error")


#---------------------------------------------
# # Pre Task 3 learning  checklist
#---------------------------------------------
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
#you can do more compact definitions (fancier)

#instead of this
x = 10
y = 20
z = 30

#you do this
x, y, z = 10, 20, 30

#what you can do with it is either defining stuff and using it that way or you can swap the values like
varA, varB = varB, varA


#---------------------------------------------
### Augmented Assignment
#---------------------------------------------
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
def test():
    x = int(input("input a number"))
    while True:
        x += 10
        print(x)
test()
    
    
#---------------------------------------------
##Strings, substrings, string splitting, manipulating strings (such as taking only the last letter, searching them, indexing, slicing them etc)
#---------------------------------------------
#every letter in string is indexed means you can print the invidual letters you can also start from the back via negative -1

text = "Script"
print(text[0])
print(text[3]) #prints i as its the 3rd index
print(text[-1]) # (The last letter)


##String slicing
#there is specific patern to string[start:stop:step]
#[] is an index aka position in the string
#p[0] == *p         
#p[1] == *(p+1)

path = "C:/Users/Documents/report.pdf"

# 1. Taking the last 3 letters (The extension)
extension = path[-3:]  # 'pdf'

# 2. Taking only the first 3 letters (The drive)
drive = path[:3]       # 'C:/'

# 3. Reversing a string (A classic interview trick)
# We leave start and stop empty and use a step of -1
reversed_path = path[::-1]    #prints --> fdp.troper/stnemucoD/sresU/:C


##String finding
#for string finding we use .find() function Returns the index of the first occurrence

email = "contact.user@provider.com"

# Find the position of the '@' symbol
at_position = email.find("@") # Returns 12

    # Use that index to slice out the domain!
domain = email[at_position + 1:] # We start one AFTER the @ and go to the end
print(domain) # Output: provider.com
    

##Advanced Splitting & Joining
#
raw_data = "  apple, banana , cherry  "

# 1. Strip the outer whitespace
clean_data = raw_data.strip() # "apple, banana , cherry"

# 2. Split by the comma
fruits_list = clean_data.split(",") # ["apple", " banana ", " cherry"]

# 3. Fix the spaces inside the list (List comprehension - a cool script tool)
final_list = [f.strip() for f in fruits_list] # ["apple", "banana", "cherry"]

# 4. Join them back with a dash for a URL slug
url_slug = "-".join(final_list) # "apple-banana-cherry"