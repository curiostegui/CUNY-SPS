# Assignment 2

## Question 1

What will the following code display? Can you debug and fix the output? The code should return the entire list

>   `numbers = [1, 2, 3, 4, 5] print(numbers[1:-5] `

### **Christian's Response**

The print statement above returns an empty list. In the slice it references index -5 which doesn't exist. The correct print statement is as follows:

```
print(numbers[0:5])
```

## Question 2

Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result. '''

### **Christian's Response**

```
days = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] sales = []
for day in days: 
sale = float(input(f"Enter the sale for the {day}: $")) sales.append(sale)
totals = sum(sales) print(f"This is the sales for the week: ${totals}")
```

## Question 3

Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in alphabetical order:

-   Print your list in its original order.
-   Use the sort() function to arrange your list in order and reprint your list.
-   Use the sort(reverse=True) and reprint your list. '''

### **Christian's Response**

```
dream_travel = ['Scotland','Argentina','Canary Islands','Italy','Greece'] 
print(dream_travel) # print list in original order 
dream_travel.sort() # use sort to arrange list in order 
print(dream_travel) 
dream_travel.sort(reverse=True) # use sort reverse 
print(dream_travel)
```

## Question 4

Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. After that, the program should let the user enter a course number, then it should display the course’s room number, instructor, and meeting time. '''

### **Christian's Response**

```
rooms = {} 
instructors = {} 
class_times = {}

how_many_courses = int(input("How many courses are you taking? "))

for i in range(how_many_courses): 
course_name = input("Enter the course number: ") 
room_num = input("Enter the room number: ") 
instructor_name = input("Enter the instructors name: ") 
meeting_time = input("Enter the meeting time: ")

rooms[course_name] = room_num
instructors[course_name] = instructor_name
class_times[course_name] = meeting_time

enter_course = input("Enter a course number for more information: ")

if enter_course in rooms: 
print("Room number:", rooms[enter_course])  
print("Instructor:", instructors[enter_course]) 
print("Meeting time:",class_times[enter_course]) 
else: 
print("This course is not in your schedule")

print(room_num)
```

## Question 5

Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should then demonstrate the four options:

-   look up a person’s email address
-   add a new name and email address
-   change an existing email address,
-   delete an existing name and email address

### Christian's Response

```
contacts = {"Christian":"christian@gmail.com", "Amy":"amy@gmail.com"}
while True:
print("\nPlease select one of the following options") 
print("1. Search an email address") 
print("2. Add a new name and email address") 
print("3. Change an existing email address") 	
print("4. Delete an existing name and email address") print("5. Quit the program")

choice = input("Enter your choice: ")

if choice == '1':
    name = input("Enter the name of the person you want to look up: ")
    if name in contacts:
        print("Email address:", contacts[name])
    else:
        print("That name is not in the contacts list.")

elif choice == '2':
    name = input("Enter the name of the person you want to add: ")
    email = input("Enter their email address: ")
    contacts[name] = email
    print(name, "has been added to the contacts list with email address:", email)

elif choice == '3':
    name = input("Enter the name of the person whose email address you want to change: ")
    if name in contacts:
        email = input("Enter the new email address: ")
        contacts[name] = email
        print("Email address updated.")
    else:
        print("That name is not in the contacts list.")

elif choice == '4':
    name = input("Enter the name of the person you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(name, "has been deleted from the contacts list.")
    else:
        print("That name is not in the contacts list.")

elif choice == '5':
    print("Goodbye!")
    break

else:
    print("Invalid choice. Please enter a number between 1 and 5.")
```

