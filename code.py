Functions parameters
# Parameter are variables defined in the functions

# Identation is used to identify code blocks

def testfunction(number):
    # this code is a part of the testfunction
    print("inside the testfunction")
    sum = 0
    for i in range(number):
        # More identation because "for" has a code block
        # but still part of the function
        sum += i
        return sum
#print("this is not a part of testfuntion")

# Calling Functions
# Python uses simple syntax to invoke or call a a preexisting function

# dohomework()

# Parammeters are variables/placeholder for the actual values
# When functions are called,  the values passed by arguments

def sales(grocery_store, item_on_sale, cost):
    print(grocery_store + " selling " + item_on_sale + " for " + cost)

    sales("The farmer's Market", "toothpast", "$1")

    sales()

def hello (first_name, last_name, age):

    print(" Hello " + first_name, last_name)
    print("you are " + str(age) + " years old ")
    print(" Have a nice day")

print("this is not a part of the function")

hello("Abdimalik ", " Omar ", 36)

def cube (num):
    return num**2

print(cube(3))

result = (cube(4))
print(result)


# Exercise

def bmi_calculator (weight_kg, height_cm):
    bmi = weight_kg / height_cm**2
    return bmi

weight = float(input("Please, enter your weight in kilo meter "))
height = float(input("Please, enter your height in cm "))

resultat = bmi_calculator (weight, height)

print("Your bmi is " + str(resultat) + "\n your not over weight but not in shape neither ")


