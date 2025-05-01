s1 = float(input("Entes s1 marks "))
s2 = float(input("Entes s2 marks "))
s3 = float(input("Entes s3 marks "))

t = s1 + s2 + s3
avg = t / 3

print("Total is : ", t)
print("Average is : ", avg)

if (avg >= 90):
    print("Grade is- A, Excellent")

elif (avg >= 80):
    print("Grade is- B, Keep it up")

elif (avg >= 60):
    print("Grade is- C, You can do better")

else:
    print("Grade is- F, game over")
