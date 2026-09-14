
#task1 find evens then create a list consisting of them.
numbers = [12,5,8,21,4,17,10]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

total_even = 0
for even in evens:
    total_even+=even

print(total_even)



# task2 - get a number from user then say it is positive, negative or zero

number = input('write a number')

if float(number) < 0:
    print('negative')
elif float(number) > 0:
    print('positive')
else:
    print('zero')


#task3
def average(numbers):
    return sum(numbers)/len(numbers)

print(average(numbers))


#task4
students = {
    "Ali": [70, 80, 90],
    "Ayşe": [90, 95, 100],
    "Mehmet": [50, 65, 70]
}


for name, exams in students.items():
    print(f'{name} gets average {(sum(exams)/len(exams)):.2f} in exams.')



# task 5 

numbers = [15, 3, 22, 8, 41, 7, 19]

lowest_number = float('inf')
highest_number = float("-inf")

for number in numbers:
    if(number < lowest_number):
        lowest_number = number
    if(number > highest_number):
        highest_number = number

print(lowest_number)
print(highest_number)



#task 6

data = [
    [18, 0],
    [22, 0],
    [25, 1],
    [30, 1],
    [35, 1],
    [20, 0]
]


ages = []
for row in data:
    if(row[1] == 1):
        ages.append(row[0])

print(f'the average of the purchased ages is: {average(ages)}')


#second part

#task 1

numbers = [4, 7, 2, 9, 7, 4, 10, 2, 7]

number_counts = {}


for number in numbers:
    
    if number in number_counts:
        number_counts[number] += 1
        

    else:
        number_counts[number] = 1
                

print(number_counts)

 


#tast 2 

temperatures = [22, 25, 19, 30, 28, 17, 31, 24]
higher_temps = []

avg_temp = average(temperatures)

for temperature in temperatures:
    if temperature > avg_temp:
        higher_temps.append(temperature)
        
print(avg_temp)        
print(f'we have {len(higher_temps)} temps bigger than average.')


 


#task 3


users = [
    ["Ali", 23, 1],
    ["Mehmet", 17, 0],
    ["Ayşe", 28, 1],
    ["Can", 31, 0],
    ["Zeynep", 19, 1]
]


names = []
ages = []
for user in users:
    if user[1] > 18 and user[2] == 1:
        names.append(user[0])
        ages.append(user[1])

avg_filtered_users = average(ages)        
print(ages)
print(names)
print(avg_filtered_users)



#final task




scores = [45, 72, 88, 91, 63, 55, 79, 100, 38]
passed_scores = []


def find_max(numbers):
    highest_number = float("-inf")
    
    for number in numbers:
        if number > highest_number:
            highest_number = number
    
    return highest_number




for score in scores:
    if(score >= 60):
        passed_scores.append(score)
        
{
    "passed_count": len(passed_scores),
    "passed_average": average(scores),
    "highest_score" : find_max(passed_scores)
}
        
        


