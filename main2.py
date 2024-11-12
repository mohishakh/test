import json
list_name=[]
list_password=[]
list_email=[]
my_dict={}
for i in range(5):
    names=input("enter name")
    password=input("enter password")
    email=input("enter email")
    if ord(password[0])<65 or ord(password[0])>97:
        print('you must enter an upper case for first letter')
        password=input("enter password again")
    list_password.append(password)
    list_email.append(email)
    list_name.append(names)
    if names not in list_name:
        list_name.append(names)
    elif names in list_name:
        new_name=(f'you can use another like {names.upper()}')
        list_name.append(new_name)
my_dict['names']=list_name
my_dict['password']=password
my_dict['email']=email
with open('main2.json','w') as File:
    json.dump(my_dict,File)
    File.close()