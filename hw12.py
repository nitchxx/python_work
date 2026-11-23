import re

user_name = input("Enter Your name : ")
user_feedback = input("Feedback : ")

try :
    if not user_name.strip():
        raise ValueError("please fill your name")

    if not user_feedback.strip():
        raise ValueError("please fill feedback area")

    print("Thanks for your valuable feedback")

except ValueError as errorside:
    print("error :",errorside)

finally:
    print("Thank you")