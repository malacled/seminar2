print("This program calculates your grade for the CSF module.\n")
cw = input("What was your coursework grade? ")
ex = input("What was your exam grade? ")
p1 = int(cw) * 40/100
p2 = int(ex) * 60/100

print(f"Your coursework, weighted is equal to {p1}. Your exam grade, weighted, is equal to {p2}. This means your final grade is equal to {p1+p2}")