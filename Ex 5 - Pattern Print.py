# Write a script that prints the following patterns, using loops:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
i = 0
while i < 5:  # increasing * - count per row
    i += 1
    print('* ' * i, '\n')
for i in range(4, 0, -1):  # decreasing * - count per row
    print('* ' * i, '\n')
