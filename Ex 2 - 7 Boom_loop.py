# Print all of the numbers between 0 and 100 that are divisible by 7
# (without a remainder), or that contain the number 7, by order.
# Use only calculations, loops and 'print'

boom = 0
count = 0
signal = 1
while boom < 100:  # run until multiple of 7 is above 100
    print(boom)  # print a multiple of 7
    while boom > 10:
        while signal == 1 and int(boom/10) != 7:
            # print number with 7 in second digit
            signal = 0
            print(int(boom/10)*10+7)
        while (boom % 10) > 2 and int(boom/10) != 7 and signal == 0:
            # verify previous loop runs again when needed
            signal = 1
        while int(boom/10) == 7:  # print all numbers with 7 as first digit
            for i in range(9):
                print(int(boom/10)*10+i+1)
            boom = 0
            count = 11
        boom = 0
    count += 1
    boom = 7 * count  # calculate next multiple of 7
