age=int(input("what is your age: "))
level=int(input("what level are you: "))
premium=str(input("do you have premium(yes or no): "))
if age>=13 and level>=10 and premium=="yes":
    print("full access granted")
elif age>=13 and premium=="no":
    print("limited access granted")
elif age<13 and premium=="yes":
    print("guest access granted")
else:
    print("access denied")