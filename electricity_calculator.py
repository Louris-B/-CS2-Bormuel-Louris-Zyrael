# Electricity Bill Calculator
# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading

RATE = 12.90

while True:
    name = input("Enter customer name: ")
    
    if name.strip() != "":
        break
    else:
        print("ERROR: Name is required, please input a name.")
        
while True:
    previous = float(input("Enter previous meter reading: "))
    
    if previous >= 0:
        break
    else:
        print("ERROR: Invalid previous meter reading. Please enter  number that is equal to or greater than 0.")

while True:
    current = float(input("Enter current meter reading: "))
    
    if current >= previous:
        break
    else:
        print("ERROR: Invalid current meter reading. Please enter  number that is equal to or greater than the previous meter reading.")
    

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
