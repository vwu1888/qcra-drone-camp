"""
    Two bugs:
        ---Unterminated string literal
        ---Incorrect indents
"""

greeting = input("What is the password: )
if greeting in "12345drones":
	print("Access Granted!")
else:
print("Incorrect!!")

"""
    Two bugs:
        ---List indexing
        ---Input is not cast to correct type
"""

months = [
    'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
    'nov', 'dec'
]

def getMonth(monthNumber: int) -> str:
    return months[monthNumber]

month = input("What is this month's number: ")
print(getMonth(month))


"""
    One bug:
        ---For loop range is short
"""
numOfElements = int(input("Number of Elements to take average of: "))
elements = []
for _ in range(1, numOfElements):
    element = int(input("Enter the element: "))
    elements.append(element)
average = sum(elements) / numOfElements
print("Average of the elements in list", round(average, 2))
