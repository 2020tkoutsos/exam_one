## If the class average is an A, every student gets a donut
## If the class average is a B, every student gets a half donut. Make sure not to round half donuts up. Return the float.
## If the class average is a C, every student gets 1/3 of a donut. Make sure not to round up, but to return the float
## If the class average is a D, every student will give Mr. James a half donut.

print("enter your 10 grades")
student_score1=int(input())
student_score2=int(input())
student_score3=int(input())
student_score4=int(input())
student_score5=int(input())
student_score6=int(input())
student_score7=int(input())
student_score8=int(input())
student_score9=int(input())
student_score10=int(input())

arr = [student_score1,student_score2,student_score3,student_score4,student_score5,student_score6,student_score7,student_score8,student_score9,student_score10]
# the array above groups all the users 10 grades
def avg(student_scores):
    num = 0
    for i in arr:
        num = num + 0
        average = num/10
# above we told the code to take all the numbers and add them up so we can divide by 10 to find the average
    if avg >= 90:
        print("You got a A, Every student gets a donut")
    if avg >= 80 and avg <= 90:
        print("You got a B, Every student gets half a donut")
    if avg >= 70 and avg <= 80:
        print("You got a C, 1/3 of a donut is given to each student")
    if avg >= 65 and avg <= 70:
        print("You got a D, Every student must give a half donut to Mr. James")
avg(arr)
# using if statemnts the user input numbers will be averaged and the computer will give the amount of donuts you will earn or give
