#name = "Marshall"
#print("hello,", name)

#print("hello\nworld")
#this is intended for making the words appear on a new line. \n means new line
#print("hello\tworld")
#this means tab.
#print("hello", end="!!!")

#name, age = eval(input("hello!\nEnter your name and age: "))
#print("good to see you", name, "you are", age, "years old!")

#hour, minute = eval(input("Enter the hour and minute: "))
#print("it is", hour, ":", minute)

#for element in [9,12,4]:
    #print(element + 4, end=" ")

#for element in range(10):
    #print(element, end=" ")

#principal_balance = eval(input("enter principal balance: ")) #principal_balance is what is called snake case.
#apr = eval(input("enter interst rate: "))
#for _ in range(10):
#    principal = principal * (1+apr)
#    print(principal)
#print("the final balance is", principal)

for i in range(5): #this is called a nested loop
    for j in range(5): # this is body for 1st loop
        print(i,j, end='-') # this is body for 2nd loop
    print()