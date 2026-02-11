import json
import os

#Default list
anime_list = {}


save_file = "anime_list.json" 

def save_data(data):
    with open (save_file, "w" ) as sf:                      #with ensures that the resource is closed automatically the moment the code inside the block finishes. AS = alias 
        json.dump(data, sf, )
    print("Current list saved successfully\n")


def load_data():
    if os.path.exists(save_file):                           #asks checks if the file exists
        with open(save_file, "r") as sf:
            return json.load(sf)
    return anime_list                                       #Fallback to default list if no file found meaining it creates it


def get_rating(anime_name):
    while True:
        try:
            rating = int(input(f"What is your rating for {anime_name} (1-10)? \n"))
            if 1 <= rating <= 10:
                return rating
            print("Rating must be between 1 and 10.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def mainer():
     while True:
        current_list = load_data()
        user_input = input("Choose an option from the list:\n1. Show anime list\n2. Add to the anime list\n3. Remove from the animelist\n\n")


        if  user_input == '1':
            print(current_list)
            
        elif user_input == '2':
            name = input("Enter the name of the anime: \n").lower()
            current_list[name] = {
            'Anime episodes': int(input(f"How many episodes does {name} have? \n")),
            'Anime rating /10': get_rating(name)
            }
            save_data(current_list)
            print("Entry added to the list \n")
            
        elif user_input == '3':
            name = input("Enter the name of the anime: \n").lower()
            if name in current_list:
                del current_list[name]
                print(f"Deleted {name}\n")
                save_data(current_list)
            else:
                print("Not found\n")

        else:
            print("Wrong option\n")

    
mainer()