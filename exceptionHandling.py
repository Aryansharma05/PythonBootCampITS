print("you")
#error Handling 
# x = "aryan"
# y = int(x)
# z = 1 + y
# print(z)

# try:

#  print(z)
# except ValueError:
#     print("something went wrong")
    
def inputNumericOnly(number):
    while True:
        user_input = input(number)
        if user_input.isnumeric():
            return user_input
        else:
            print("invalid input. enter number only")
number = inputNumericOnly("enter your number: ")
print(f"hello, {number}!")