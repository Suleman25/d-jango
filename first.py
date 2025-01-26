#status = int(input("enter code :"))
#match status:
    #case 200 | 201:
        #print ('success')
    #case 400:
        #print ('not  found')
    #case 500 | 501:
       # print ('server error')
   # case _:
        #print ('unknown')

# for i in range(10):
#     print('looping...' , i)
# fav = ['cream cake' , 'apple pie' , 'churros' , 'dry cake']
# # for desserts in fav:
# #     print(desserts)
# count = 0
# while count < len(fav):
#     print(fav[count] )
#     count +=1
# for x in range (3):
#     print (x)
#     for y in range(3):
#         print (y)
# tax = float(input('enter your tax :'))
# bill = float(input('enter your bill :'))
# def calculate(bill ,tax):
#     return (bill*tax)/100 
# print ('total tax:', calculate(bill,tax))

# print("hello world")
# x=5
# print(x)
# y=7
# x="sam"
# y=3.4
# print(y)
# print(x)
# name= input("enter your name :")
# print("my name is ",name)
# x=int(input("enter any number :"))
# if(x%2==0):
#     print(f"{x} is even")
# else:
#     print(f"{x} is odd") 
# for i in range (100,0,-2):
#     print(i)
# i=100
# while(i>0):
#     print(i
#     i=i-1


# global_v = 10

# def fn1():
#     enclosed= 8
#     def fn2():
#         local_v = 5
#         print ('access to globL ', global_v)
#         print ('access to enclosed ', enclosed)
#     print (enclosed)    
#         print (local_v)  
   
# text = "sdfghjkl asdfghjkl asdfghjkl qwertyuio"
# print (text[-1])
# print (text[6])
# def got_word(sentence, n):
#     if n>0:
#         words=sentence.split()
#         if n<=len(words):
#             return(words[n-1])
#     return("")
# print(got_word("this is a lesson about the list" ,4)) 
# print(got_word("this is a lesson about the list" ,-4))
# print(got_word("now we are cooking" ,1))
# print(got_word("now we are cooking" ,5))  
# name=input("enter your name ")
# num=len(name) *3
# print(f'hello {name} , your lucky number is {num}')
# fruits = ["pineapple","banana","apple","melon"]
# # fruits.append("kiwi")
# # print(fruits)
# # fruits.insert(0,'orange')
# # print(fruits)
# # fruits.remove('banana')
# # print(fruits)
# fruits.pop()
# print(fruits)
# def convert_sec(seconds):
#     hours=seconds // 3600
#     min = (seconds - hours * 3600)// 60
#     remaining_seconds = seconds - hours * 3600 - min * 60
#     return hours , min , remaining_seconds
# result = convert_sec(5000)
# print (result)
# print (type (result))

# def convert_sec(seconds):
#     hours=seconds // 3600
#     min = (seconds - hours * 3600)// 60
#     remaining_seconds = seconds - hours * 3600 - min * 60
#     return hours , min , remaining_seconds
# hours, min , seconds = convert_sec(5000)
# print (hours, min ,seconds)
# print (type (hours))
# file_count = {"jpg":10,"txt":14,"csv":2,"py":23}
# for extension in file_count:
#     print(extension)

# for ext, amount in file_count.items():
#     print ("There are {} files with the .{} extensions".format(amount,ext))    
# cool_beasts = {"octopuses" : "tentacles" , "dolphins" : "fins" , "rhino" : "horns"}
# for animals , qualities in cool_beasts.items():
#     print(f"{animals} have {qualities}")
# a= int(input("enter first number "))
# b = int ( input("enter second number "))
# c = a/b
# print(c)

# def div(a,b):
#     return  a/b
# try:
#     ans = div(50,0)
#     print (ans)
# except Exception as e:
#     print("something went wrong --->" , e)   
#     print (e.__class__)

# items = [1,2,3,4,5]
# item = items[0]
# print(item)     

# menu = ['espresso' , 'mocha' , 'latte' , 'cappuccino' , 'cortado' , 'americano']

# def coffee(cof):
#     if cof[0] == 'l':
#         return cof
    
# map_coffee = map(coffee , menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)  




# menu = ['espresso' , 'mocha' , 'latte' , 'cappuccino' , 'cortado' , 'americano']
# def coffee(cof):
#     if cof[0] == 'l':
#         return cof
    
# filter_coffee = filter(coffee , menu)
# print(filter_coffee)
# for x in filter_coffee:
#     print(x)    
# users = {}

# def sign_up():
#     while True:
#         username = input("Username: ")
#         if username in users:
#             print("Username taken. Try again.")
#             continue
        
#         password = input("Password (8 chars): ")
#         if len(password) != 8:
#             print("Password must be 8 characters.")
#             continue
        
#         users[username] = password
#         print("Account created!")
#         break

# def sign_in():
#     username = input("Username: ")
#     password = input("Password: ")
    
#     if username in users and users[username] == password:
#         print(f"Welcome, {username}!")
#         return True
#     print("Invalid credentials.")
#     return False

# while True:
#     print("\n1.Sign Up\n2.Sign In\n3.Exit")
#     choice = input("Choose: ")
    
#     if choice == '1':
#         sign_up()
#     elif choice == '2':
#         sign_in()
#     elif choice == '3':
#         break
users = {}

def sign_up():
    username = input("Username: ")
    if username in users:
        print("Username taken.")
        return
    
    password = input("Password (8 chars): ")
    if len(password) != 8:
        print("Password must be 8 characters.")
        return
    
    users[username] = password
    print("Account created!")

def sign_in():
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return True
    print("Invalid credentials.")
    return False

sign_up()
sign_in()