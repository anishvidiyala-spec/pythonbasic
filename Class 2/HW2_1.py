subject1_one = int(input("What is your grade in subject one?"))
subject1_two = int(input("What is your grade in subject two?"))
subject1_three = int(input("What is your grade in subject three?"))

total = subject1_one+subject1_two+subject1_three

average = total/3

print("Total Marks: ", total)
print("Average: ", average)

if average > 90:
    print("Excellent")
else:
    print("Try harder next time")