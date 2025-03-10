import json

user_name = input("please input your name: ")

try:
    with open('username.json') as file_object:
        contents = json.load(file_object)
except:
    with open('username.json','w') as file_object2:
        json.dump(user_name,file_object2)
    print("Welcome " + user_name + ", we will remember your.")
else:
    print("Welcome back, " + user_name + " !")

