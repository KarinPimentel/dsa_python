__author__ = 'Karin Melissa Rodrigues Pimentel'
__version__ = 1.0
__manteiner__ = 'Karin Melissa Rodrigues Pimentel'
__email__ = 'karin_melissa@hotmail.com'
__status__ = 'Development'
__last_atualization__ =  '24/10/2021'

# Defining the functions
def add(x, y):
    return(sum(x, y))

def sub(x, y):
    return(x - y)

def mult(x, y):
    return(x * y)

def div(x, y):
    return(x/y)

# presenting to the user the operations available
print("************************************* Python Calculator *************************************\n"
      "Choose the number related to the operation wanted:\n"
      "\n"
      "1 - SUM\n"
      "2 - SUBTRACTION\n"
      "3 - MULTIPLICATION\n"
      "4 - DIVISION\n")

# requesting the first input, choosing what kind of operation wanted
operation = int(input("Enter your choice (1/2/3/4): "))

# requesting the numbers to create the operation

n1 = float(input("Enter the first number: "))

n2 = float(input("Enter the second number: "))

# Operations and conditionals
if operation == 1:
      print(n1,'+',n2,'=', add(n1, n2))
elif operation == 2:
      print( n1, '-', n2, '=', sub(n1, n2))
elif operation == 3:
      print( n1, '*', n2, '=', mult(n1, n2))
elif operation == 4:
      print( n1, '/', n2, '=', div(n1, n2))
else:
      print('This operation is not yet available.')