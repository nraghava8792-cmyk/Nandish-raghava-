'''age= int(input("enter your age: "))
if(age>=18):
    print("Eligible to vote")
    if(age>=22):
        print("Eligible to marry")
    else:
        print("not eligible to Marry")
else:
    print("not eligible to vote")'''

#print the number divisible by 2
'''l=[10, 3,5,6,7,8,9,24,3,5,6,7,89]
even = []
for i in l:
    if i% 2 ==0:
        even.append(i)
print(even)'''
#print the number not divisible by 3
'''l=[3,10,12,54,75,89,25,23]
even = []
for i in l:
    if i % 3!= 0:
        even.append(i)
print(even)'''

#consider a string 'university' and count the characterstics
'''t= "university"
print(len(t))'''

#find the second smallest number
'''l = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

l.sort()

for i in range(1, len(l)):
    if l[i] != l[0]:
        print(l[i])
        break'''

'''l = [3, 10, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for i in l:
    if i % 3 == 0 and i % 5 == 0:
        print(i)'''

'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)'''



'''s = "university"
rev = ""

for char in s:
    rev = char + rev

print(rev)'''







'''numbers = [10, 3, 34, -8, -9, 1]

smallest = min(numbers)

print(smallest)'''







'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num in list3:
        common.append(num)

print(common)'''







'''numbers = [3, 10, 12, 54, 75, 89, 25, 23]

for num in numbers:
    if num % 3 != 0:
        print(num)'''
        
        
        
        
        
'''s = "university"

count = 0

for char in s:
    count += 1

print(count)'''







'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Smallest:", smallest)
print("Second smallest:", second_smallest)'''








'''numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)'''





'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for num in list1:
    if num in list2:
        print(num)'''
        
        
        
        
        

'''numbers = [3, 10, 15, 54, 75, 89, 25, 23]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(num)'''
        
        
        
        
        
        
        
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest = min(numbers)
largest = max(numbers)

print("Smallest:", smallest)
print("Largest:", largest)'''









numbers = [-1, 3, 34, -8, -9, 1]

numbers[0], numbers[2] = numbers[2], numbers[0]

print(numbers)








'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = list(set(list1) ^ set(list2))

print(result)'''









'''




num = int(input("Enter a number: "))

if num % 3 == 0:
    print("Square:", num ** 2)
else:
    print("Number is not divisible by 3")'''