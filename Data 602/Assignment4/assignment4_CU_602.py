'''
Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
lastname, and balance.
The default balance should be set to 0.
In addition, create ...
● A method called deposit() that allows the user to make deposits into their balance.
● A method called withdrawal() that allows the user to withdraw from their balance.
● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
in your withdrawal() method.
● Use the __str__() method in order to display the bank name, owner name, and current
balance.
● Make a series of deposits and withdrawals to test your class.
'''


class BankAccount:
    def __init__(self, bankname, firstname, lastname):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = 0    # default balance is set to 0

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        # Return a string with the bank name, owner name, and current balance
        return f"Bank Name: {self.bankname}\nOwner Name: {self.firstname} {self.lastname}\nCurrent Balance: {self.balance}"

#--- Example use ---#

account = BankAccount("RandomBank", "John", "Cena")
account.deposit(500)
account.withdrawal(50)
print(account)   
        
account = BankAccount("Bank2", "Roman", "Reigns")
account.deposit(700)
account.withdrawal(650)
print(account)   

account = BankAccount("Bank3", "Cody", "Rhodes")
account.deposit(700)
account.withdrawal(650)
print(account)   


'''
Q2: 
Create a class Box that has attributes length and width that takes values for length
and width upon construction (instantiation via the constructor).
In addition, create…
● A method called render() that prints out to the screen a box made with asterisks of
length and width dimensions
● A method called invert() that switches length and width with each other
● Methods get_area() and get_perimeter() that return appropriate geometric calculations
● A method called double() that doubles the size of the box. Hint: Pay attention to return
value here.
● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
their respective lengths and widths are identical.
● A method print_dim() that prints to screen the length and width details of the box
● A method get_dim() that returns a tuple containing the length and width of the box
● A method combine() that takes another box as an argument and increases the length
and width by the dimensions of the box passed in
● A method get_hypot() that finds the length of the diagonal that cuts through the middle

Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
box2 and box3 respectively
● Print dimension info for each using print_dim()
● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
screen accordingly
● Combine box3 into box1 (i.e. box1.combine())
● Double the size of box2
● Combine box2 into box
'''

import math

class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def render(self):
        for i in range(self.width):
            print('*' * self.length)
    
    def invert(self):
        self.length, self.width = self.width, self.length
    
    def get_area(self):
        return self.length * self.width
    
    def get_perimeter(self):
        return 2 * (self.length + self.width)
    
    def double(self):
        return Box(2*self.length, 2*self.width)
    
    def __eq__(self, other):
        return self.length == other.length and self.width == other.width
    
    def print_dim(self):
        print(f"Length: {self.length}, Width: {self.width}")
    
    def get_dim(self):
        return (self.length, self.width)
    
    def combine(self, other):
        self.length += other.length
        self.width += other.width
    
    def get_hypot(self):
        return math.sqrt(self.length**2 + self.width**2)


# create objects
box1 = Box(5,10)
box2 = Box(3,4)
box3 = Box(5,10)

#print dimensions
print("The dimensions for Box 1 is:")
box1.print_dim()
print()


print("The demensions for Box 2 is:")
box2.print_dim()
print()

print("The dimensions for Box 3 is:")
box3.print_dim()
print()

# check if box 1 equals to box2 and box3
if box1 == box2:
    print("True")
else:
    print("False")
    
if box1 == box3:
    print("True")
else:
    print("False")

# combine box3 into box1
box1.combine(box3)

# double the size of box2
box2_doubled = box2.double()

# combine box2 into box1
box1.combine(box2_doubled)

# end result 
print("The final dimensions after combining is:")
box1.print_dim()


