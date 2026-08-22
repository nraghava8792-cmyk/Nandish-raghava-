Name: Nandish raghava B S
reg: KUB25EEE697

#print all the numbers which are divisible by 3,5,8 from the list(1)
'''numbers = [3, 10, 15, 54, 75, 25, 23]
for num in numbers:
    if num % 3 == 0 or num % 5 == 0 or num % 8 == 0:
        print(num)
    else:
        print("None")'''

#find the smallest and largest number in the list and swap them(2)
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]
smallest = min(numbers)
largest = max(numbers)
print("Smallest:", smallest)
print("Largest:", largest)
# Swap smallest and largest
smallest_index = numbers.index(smallest)
largest_index = numbers.index(largest)
numbers[smallest_index], numbers[largest_index] = numbers[largest_index], numbers[smallest_index]
print("After swapping:", numbers)'''


#replace -1 by 100(3)
'''numbers = [-1, 3, 34, -8, -9, 1]
numbers[numbers.index(-1)] = 100
print(numbers)'''

#find the average of two lists(4)
'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
average = (sum(list1) + sum(list2)) / (len(list1) + len(list2))
print("Average:", average)'''

#take a number from user and if it is divisible by 3 then add 5 to it and print the result otherwise print "Number is not divisible by 3"(5)
'''num = int(input("Enter a number: "))
if num % 3 == 0:
     num = num + 5
     print(num)
else:
     print("Number is not divisible by 3")'''

#print all the numbers which are divisible by 3 but not by 5(6)
'''numbers = [3, 10, 15, 54, 75, 25, 23]
for num in numbers:
    if num % 3 == 0 and num % 5 != 0:
        print(num)'''
        
#print all the numbers which are greater than 20(7)
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]
for num in numbers:
    if num > 20:
        print(num)'''

#print all the negative numbers from the list(8)
'''numbers = [-1, 3, 34, -8, -9, 1]
for num in numbers:
    if num < 0:
        print(num)'''

#find the length of the list(9)
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = len(numbers)
print(count)'''

#take the number from user and if it is divisible by 3 then multiply it by 5 and print the result otherwise print "Number is not divisible by 3"(10)
'''num = int(input("Enter a number: "))
if num % 3 == 0:
    num = num * 5
    print(num)
else:
    print("Number is not divisible by 3")'''


#take two numbers from user and print the sum of them and check whether the sum is divisible by 5 or not(11)
'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
if sum % 5 == 0:
    print("Sum is divisible by 5")
else:
    print("Sum is not divisible by 5")'''


#print all the prime numbers from the list(12)
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]
for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)'''


#perform all the operations on the list(13)
'''numbers = [-1, 3, 34, -8, -9, 1]
print("Original list:", numbers)
# Add an element
numbers.append(10)
print("After append:", numbers)
# Insert an element
numbers.insert(2, 50)
print("After insert:", numbers)
#Remove an element
numbers.remove(-8)
print("After remove:", numbers)
# Sort the list
numbers.sort()
print("After sorting:", numbers)
# Reverse the list
numbers.reverse()
print("After reverse:", numbers)
# Find length
print("Length:", len(numbers))'''

#find the average of the list(14)
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
average = sum(numbers) / len(numbers)
print("Average:", average)'''

#find the divisors of the number(15)
'''num = 157893
divisors = []
for i in range(1, 11):
    if num % i == 0:
        divisors.append(i)
print("Divisors:", divisors)'''


#take 2 number as input from user and if it divisible by 5 square the number(16)
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a % 5 == 0:
    print("Square of", a, "is", a ** 2)
else:
    print("the number is not divisible by 5")
if b % 5 == 0:
    print("Square of", b, "is", b ** 2)
else:
    print("the number is not divisible by 5")'''

    
    
#find prime numbers and even numbers and odd numbers(17)
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]
prime = []
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
print("Prime numbers:", prime)
print("Even numbers:", even)
print("Odd numbers:", odd)'''



#remove negative numbers and numbers divisible by 3(18)
'''numbers = [-1, 3, 34, -8, -9, 1]
result = []
for num in numbers:
    if num >= 0 and num % 3 != 0:
        result.append(num)
print(result)'''


#find the average, sum, count of list(19)
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = sum(numbers)
count = len(numbers)
average = total / count
print("Sum:", total)
print("Count:", count)
print("Average:", average)'''


#take the divisors from 1 to 10 and check 1578693 is divisible or not if divisible -100 from it(20)
'''number = 1578693
for i in range(1, 11):
    if number % i == 0:
        print(number, "is divisible by", i)
        number = number - 100
    else:
        print(number, "is not divisible by", i)
print("Final number:", number)'''


#"university" count vowels in it(21)
'''word = "university"
vowels = "aeiou"
count = 0
for ch in word:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)'''

#print 89 using index and 59 to the list in 9th index(22)
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]
print(numbers[12])
numbers.insert(9, 59)
print(numbers)'''


#square elements of list(23)
'''numbers = [-1, 3, 34, -8, -9, 1]
for num in numbers:
    print(num ** 2)'''
    
    
#take 2 numbers as input and 2 floor division(24)
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Floor division:", a // b)'''


#find unique values(25 )
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89, 7, 8, 54, 621, 57, 24, 3, 5, 6, 4]
unique = []
for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)
print(unique)'''
