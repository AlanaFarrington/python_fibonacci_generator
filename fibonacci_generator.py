def fibonacci_generator(row_request):
    row = 3
    fib_prev = 1
    fib_pre_prev = 0
    while row <= int(row_request):
        fib_num = fib_pre_prev + fib_prev
        fib_pre_prev = fib_prev
        fib_prev = fib_num
        row += 1
    return fib_num

row_request = input("What fibonacci row number would you like? ")

result = fibonacci_generator(row_request)

print("Row {}s fibonacci number is {}".format(row_request, result))