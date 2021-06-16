def organisation():
    employee_id = input("Please enter your employee Id: ")
    current_year = int(input("please enter the current year: "))
    year_of_joining = int(input("please enter the joining year: "))
    if (current_year - year_of_joining) >= 3:
        print("The employee " + employee_id + " is working from ", year_of_joining, "so his bonus of 2500 is declared")
    else:
        print("Since the experience in the company is less than 3years bonus is not declared")


def scorecard():
    student_id = input("Please enter the student_id : ")
    science, maths, english, social, hindi = input("please enter subject score with a space:  ").split( )
    print("The student id is : " + student_id)
    print("Marks scored across subjects" + "\nscience: "+ science, "\nmaths: "+maths, "\nenglish: "+english,"\nsocial: "+social,"\nhindi: "+hindi)
    science = int(science)
    maths = int(maths)
    english = int(english)
    hindi = int(hindi)
    social = int(social)
    x = science + maths + english + hindi + social
    print("The grand total is: ", x)
    y = ((x / 500)*100)

    print("The percentage gained is: ", y)
    if social or science or maths or english or hindi < 40:
        print("Work Hard to clear the next year, you're failed")
    else:
        if y >= 60:
            print(" Well done student for the First division.")
        elif y >= 50 and y >= 59:
            print("Well done student for the second division.")
        elif y >= 40 and y >= 49:
            print("Good work for the third division")
        elif y < 40:
            print("Work Hard to clear the next year, you're failed")

def company_insur() -> object:

    # If the driver is married. // # If the driver is unmarried, male & above 30 years of age. // # If the driver is unmarried, female & above 25 years of age. // # In all other cases the driver is not insured. If the marital status, sex // and age of the driver are the inputs, write a program to determine // # whether the driver is to be insured or not.
    driver_name = input("Please enter the employee name: ")
    marital_status = input("Please enter the marital status(Married/ unmarried): ")
    age = input(input("Please enter the age: "))
    gender = input("Please enter the gender: ")

    if marital_status == 'unmarried' and gender == 'male' and age >= 30:
        print("The driver " + driver_name + " is eligible to be insured")
    elif marital_status == 'unmarried' and gender == 'female' and age >= 25:
        print("The driver " + driver_name + " is eligible to be insured")
    else:
        print("The driver "+driver_name + " is not eligible to be insured")


def odd_or_even():
    digit = int(float(input("Please enter the digit :")))
    if (digit % 2 == 0):
        print("The digit", digit, " is an even number")
    else:
        print("The digit ", digit, " is an odd number")


def leap_or_non_leap():
    year = int(input("Please enter the Year :"))
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("The year ", year, "is a leap year")
    else:
        print("The year ", year, " is not a leap year")


#organisation()
#scorecard()
#company_insur()
#odd_or_even()
leap_or_non_leap()