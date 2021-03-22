def fact(n):
    if n == 1:
        return 1
    result = n * fact(n - 1)
    return result


result = fact(2)
print(result)






























