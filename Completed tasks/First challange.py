###The first try 

# import random 

# #List for possible true answers
# List_continue = ['YES', '1', 'Y']
# #Use upper to always fit into the above list
# i = input("Do you want to start? Yes/no\n\n").upper()

# #While loop for check if the user wants to continuzes
# while i in List_continue:

#     #List with choosable object
#     #A feature could be typing no only the exact match in the list but Number and it would pull the item from the list it would need to be mooved +1 thought as array starts with 0
#     List_object = ['sphere', 'square', 'bridge', 'cylinder', 'triangle']
#     print(List_object)


#     #Random object picker from the object list
#     random_object = random.choice(List_object)

#     #Answer the damn question prompt
#     #Lower due to the fact that everything in List_object is lower
#     User_input = input(f"Where does {random_object} go?\n\n\n").lower()
    
#     if  User_input == 'square':
#         print("That is correct\n")
#     #pretty self explenatory
#     elif  User_input in List_object:
#         print("That's false as its always in the square hole\n")
#     #If someone answers random stuff let them know
#     else:
#         print("That is not part of the listed objects\n")    

#     i = input("Do you still want to continue? Yes/no\n\n").upper()
# #Quit confirmation
# else:    
#     print("OK\n\n")


###--------------------------
###The cleaner optimized code
###--------------------------
import random 


while True:
    List_object = ['sphere', 'square', 'bridge', 'cylinder', 'triangle']
    print(f"Options: {List_object}")
    random_object = random.choice(List_object)
    User_input = input(f"Where does {random_object} go?\n\n\n").lower()
    print("That's right it goes in the square hole!")