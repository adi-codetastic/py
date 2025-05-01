n1 = float(input("Enter No. 1: "))
n2 = float(input("Enter No. 2: "))
n3 = float(input("Enter No. 3: "))
t = n1+n2+n3
avg = t/3
print("Average: ",avg)
if(avg >= 90):
    print("Grade is A, Keep it up")
elif(avg >= 60):
    print("Grade is B, good")
elif(avg >= 40):
    print("Grade is C, you are cooked")
else:
    print("Grade is F, You are such a failiure, GAME OVER")