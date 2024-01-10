# Assignment 3

## Question 1

Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”

The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

### Christian’s Response

```
meal_choice = input("What would you like to eat? (breakfast, lunch, or dinner):")

if meal_choice == "breakfast":
    print("Can I interest you in huevos rancheros?")
elif meal_choice == "lunch":
    print("How about chilaquiles rojos?")
elif meal_choice == "dinner":
    print("I recommend carna asada")
else:
    print("Sorry, we only offer breakfast, lunch and dinner")
```

## Question 2

The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20.

You should take in the user’s input for the number of hours worked, and their rate of pay.

### Christian’s Response

```
def gross_pay_calculator(hours_worked, hourly_rate):
    overtime_limit = 20
    overtime_rate = 1.5
    
    if hours_worked <= overtime_limit:
        gross_pay = hours_worked * hourly_rate
    else:
        regular_pay = overtime_limit * hourly_rate
        overtime_pay = (hours_worked - overtime_limit) * overtime_rate * hourly_rate
        gross_pay = regular_pay + overtime_pay
    
    return gross_pay

hours_week = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly rate of your pay: "))

gross_pay = gross_pay_calculator(hours_week, rate)
print(f"Gross pay: ${gross_pay:.2f}")
```

## Question 3

Write a function named times ten. The function should accept an argument and display the product of its argument multiplied times 10.

### Christian’s Response

```
def times_ten(num):
    product = num * 10
    print(product)

times_ten(10)
```

## Question 4

Find the errors, debug the program, and then execute to show the output.

```
def main()
    Calories1 = input( "How many calories are in the first food?"
    Calories2 = input( "How many calories are in the first food?")
    showCalories(calories1, calories2)
    def showCalories()   
    print(“The total calories you ate today”, format(calories1 + calories2,.2f))
```
------------------------------------------------------------------------------------

### Christian’s Response

```
def main(): # missing colon
      Calories1 = float(input( "How many calories are in the first food?")) # added float
      Calories2 = float(input( "How many calories are in the second food?")) # changed text to 'second' food
      showCalories(Calories1, Calories2) # capitalized objects in the argument

def showCalories(Calories1, Calories2): # added colon
    totalCalories = Calories1 + Calories2 # added total calories object
    print("The total calories you ate today:", format(totalCalories, ".2f")) # fixed format

main()
```

## Question 5

Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:

>   1/30 + 2/29 + 3/28 ............. + 30/1

### Christian’s Response

```
total = 0
for i in range(1,31):
    total += i/(31-i)
print(total)
```

## Question 6

Write a function that computes the area of a triangle given its base and height.

The formula for an area of a triangle is:

>   `AREA = 1/2 * BASE * HEIGHT`

For example, if the base was 5 and the height was 4, the area would be 10.

>   triangle_area(5, 4) \# should print 10

### Christian’s Response

```
def area_calc(base,height):
    area = base * height
    print(area)

area_calc(5,3)
```
