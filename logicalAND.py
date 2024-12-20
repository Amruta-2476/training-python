p1 = int(input("Enter paper 1 marks:"))
p2 = int(input("Enter paper 2 marks:"))
p3 = int(input("Enter paper 3 marks:"))
gen = input("Enter your gender(male/female): ")

total = p1+p2+p3
percentage = total/3
print("Total =", total)
print("Percentage =", percentage)

if p1>=40 and p2>=40 and p3>=40:
    print("Student passed")
    if (gen == 'male' and percentage>= 60) or (gen=='female' and percentage>=55):
        print("Student is eligible for placement")
    else:
        print("Student is not eligible for placement")
else:
    print("Student failed")


