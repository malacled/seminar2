#the function malika takes an integer, and will print malika that number of times
def malika (int):
    print("malika " * int)
#tell user what the program does
print("This program prints malika however many times you tell it to.\n")
#times is equal to whatever number the user gives
times = input("How many times should it print malika? ")
#this line prints malika however many times the user specified in the input
malika(int(times))