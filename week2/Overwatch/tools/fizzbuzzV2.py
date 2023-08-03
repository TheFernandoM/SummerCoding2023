for index in range(1,101):
    if(index % 15 == 0):
        print("FizzBuzz\n")
    if(index % 3 == 0):
        print("Fizz\n", end='')
        continue
    if(index % 5 == 0):
        print("Buzz\n", end='')
        continue
    print(index)