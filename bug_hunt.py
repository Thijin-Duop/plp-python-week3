count = 1
total = 0

# BUG: The while statement was missing a colon at the end.
# Fixed by adding : after the condition.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The integer total cannot be joined directly to a string.
# Fixed by converting total to a string using str().
print("Sum of 1 to 5 is: " + str(total))