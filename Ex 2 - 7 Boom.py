# Print all of the numbers between 0 and 100 that are divisible by 7
# (without a remainder), or that contain the number 7, by order.
# Use only calculations, loops and 'print'

# solution with if
# for x in range(100):
#    if x % 7 == 0 or x % 10 == 7 or int(x / 10) == 7:
#        print(x)

# solution without if
x = 0
while x < 100:
    while x % 7 == 0 or x % 10 == 7 or int(x / 10) == 7:
        print(x)
        break
    x += 1
