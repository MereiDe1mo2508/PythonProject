def numberascention(n):
    if n == 0:
        return
    else:
        numberascention(n-1)
        print(n)
print("Ascending number example")
numberascention(5)

def numberdescention(n):
    if n == 0:
        return
    else:
        print(n)
        numberdescention(n-1)
print("Descending number example")
numberdescention(5)

def summation(n):
    if n <= 1:
        return 1
    else:
        return n + summation(n-1)
print("Summation example: ", summation(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial example: ", factorial(5))

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)
print("Power example: ", power(5, 2))

def digitsum(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        return n % 10 + digitsum(n // 10)
print("Digit sum example: ", digitsum(572))

def counting_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + counting_digits(n//10)
print("Counting digits example: ", counting_digits(5729))

def reverse_number(n):
    if n == 0:
        return n
    else:
        print(n % 10)
        return reverse_number(n // 10)
print("Reverse number example: ", reverse_number(1234))

def fibonacci(n):
    n = abs(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci example: ", fibonacci(6))

def palindrome(word):
    if word == word[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print("Palindrome example: ", palindrome("level"))

def array_sum(arr):
    s = 0
    for i in range(len(arr)):
        s += arr[i]
    return s
print("Array sum example: ", array_sum([3, 5, 2, 7]))

def array_max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
print("Array max example: ", array_max([4, 9, 1, 7, 3]))

def target_value(arr, target):
    count = 0
    if not arr:
        return 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
        else:
            continue
    return count
print("Target value example: ", target_value([1, 2, 3, 2, 2, 5], 2))

def recursive_linear(arr, target):
    for i in range(len(arr)):
        if arr[i]  == target:
            return "Found"
    return "Not found"
print("Recursive linear example: ", recursive_linear([4, 7, 1, 9, 3], 9))

def is_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    return True
arr1 = [1, 2, 4, 7, 9]
arr2 = [1, 5, 3, 8]
print("Sorted example: ", is_sorted(arr1))
print("Not sorted example: ", is_sorted(arr2))
##Bonus one
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + (target - arr[mid])
        else:
            high = mid - (target - arr[mid])
    return "There's no value in the array"
print("Binary search example: ", binary_search([1, 2, 3, 4, 5, 6, 7], 7))