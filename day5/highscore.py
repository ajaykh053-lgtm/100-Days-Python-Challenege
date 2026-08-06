studentscore = [178, 142, 195, 87, 160, 123, 200, 134, 99, 185]

# sum operator in python

totalsumofstudentscore = sum(studentscore)
print(totalsumofstudentscore)
totalsum = 0
for score in studentscore:
    totalsum += score
print(totalsum)


# max in list

max_score = max(studentscore)
print(max_score)

max_scoer = 0
for score in studentscore:
    if score > max_score:
        max_score = score
print(max_score)


# Range Funtion with For Loop

for number in range(1, 10):
    print(number)

for number in range(1, 100, 10):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
