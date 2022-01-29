import random

#function to sort the list, random_list - it is variable of random list
def sort_list (random_list):
    # variable for sorted list
    sorted_list = []
    # while the list values exist
    while random_list:
        minimum = random_list[0]  # assign minimum to the first number in list
        for x in random_list:  # look through the every element in the list
            if x < minimum:  # check if current element is less then minimum value
                minimum = x  # if current element is less then minimum value than minimum = x
        sorted_list.append(minimum)  # add value of minimum to the sorted list
        random_list.remove(minimum)  # remove value of minimum to the sorted list
    return sorted_list

#function for errors handling

#create empty list
random_list = []
#add 100 random numbers from 0 to 1000 to the list
for i in range(0,1000): # in range from 0 to 1000
    # random int number
    n = random.randint(1,100)
    # add random number to list
    random_list.append(n)

print(random_list)

#evaluate mylist with sorted list: run the function to sort the list and print the sorted list
mylist = sort_list(random_list)
print(mylist)

#variables for summs of odd and even numbers
sum_odd, sum_even = 0, 0
#counters for odd and even numbers
i, j = 0, 0
#loop for looking through the =list
for num in mylist:
    if num % 2 == 0: #check if number is odd
        i +=1 #if number is odd -> counter i is increased by 1
        sum_odd += num #if number is odd -> add number to the summ of odd mumbers
    else: # else - if number is not odd
        j += 1 #if number is not odd (even) -> counter j is increased by 1
        sum_even += num #if number is not odd (even)  -> add number to the summ of even mumbers

print(sum_odd, i, sum_even, j)
#Trying find Averages if i or j are not zero
try:
    print("Average odd numbers = ", sum_odd / i)
    print("Average even numbers = ", sum_even / j)
except ZeroDivisionError:
        print("Division by zero")
