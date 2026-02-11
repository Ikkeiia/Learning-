###Notes - Chat we are cooked
###Keep cleaner code and segment better 
###
###Copy the line down
## SHIFT + ALT + Down Arrow 
# 
# 
###  Custom comment when selected
## CTRL + Q 



#int = full numbers
one = 1
#float = used for decimal numbers
onepointfive = 1.5
#Strings are used for words or characters
name = 'Andrea'
name1 = 'Adrian'

#F string = mainly better visibility i
print( f"if {name} marries {name1} then its bound to be a disaster")
print("Whad do you think?")

answer = input("tell me how you feel?")
print(answer)

My_table = ['apple', 'bannana', 'head']
table_first = My_table[0]

print(f"what do you think is on my table in first position? \n{table_first}")

#adding to the table
My_table.append('boddy')
print(f'new thing on the table {My_table}')

#extending the list by adding multiple things
My_table.extend(['boddy','barel', str(1)])
print(f'new thing on the table {My_table}')


#Wait till i make action to continue
input()

#Removing from the aray
My_table.remove('boddy')
print(My_table)

Condition = input("do you want to clear the table? Y/n\n")

if Condition == "Y":
    My_table.clear()
    print(f"you Bad boy this is how it looks now: {My_table}\n")
else:
    print(f"Good boy {My_table}")

