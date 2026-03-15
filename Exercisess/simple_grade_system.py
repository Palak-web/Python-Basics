marks = int(input("Enter the marks:"))
if marks >= 90:
    print(" You are passed with A grade ")
elif marks >= 75:
    print(" You are passed with B grade ")
elif marks >= 60:
    print(" You are passed with C grade ")
elif marks >= 40:
    print(" You are passed with D grade ")
else:
    print("Please do a little bit more efforts student!")


def grade(marks):
    if marks >= 90:
        return "You are passed with A grade"
    elif marks >= 75:
        return " You are passed with B grade "
    elif marks >= 60:
        return " You are passed with C grade "
    elif marks >= 40:
        return " You are passed with D grade "
    else:
        return "Please do a little bit more efforts student!"

marks = int(input("Enter marks: "))
print("Grade:",grade(marks))