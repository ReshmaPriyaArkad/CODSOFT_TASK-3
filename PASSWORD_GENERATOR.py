import random
u_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['0','1','2','3','4','5','6','7','8','9']
sym=['#','@','*','$','!','&','#','^',')','(']
password_list=[]
u_range=int(input("Enter How many uppercase letters do you want:"))
l_range=int(input("Enter How many lowercase letters do you want:"))
n_range=int(input("Enter How many numbers do you want:"))
s_range=int(input("Enter How many symbols do you want:"))
for i in range(1,u_range+1):
    char=random.choice(u_letters)
    password_list+=char
for i in range(1,l_range+1):
    char=random.choice(l_letters)
    password_list+=char
for i in range(1,n_range+1):
    char=random.choice(num)
    password_list+=char
for i in range(1,s_range+1):
    char=random.choice(sym)
    password_list+=char
random.shuffle(password_list)
print("Generated Password:")
password=""
for char in password_list:
    password+=char
print(password)