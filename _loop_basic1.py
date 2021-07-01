#Create a Python file called for_loop_basic1.py that performs the following tasks.

#Basic - Print all integers from 0 to 150.
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

for i in range(1, 151):
    print(i)




for i in range(1,101):
    if i%5==0 and i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    elif i%10==0:
        print("Coding Dojo")
    else:
        print(i)

sum = 0
for x in range(0, 10):
    if x % 2 != 0:
        sum += x
print(sum)

for x in range(2018, 0, -4):
    if x > 0:
        print(x)

lowNum = 2
highNum = 9
multi = 3

for x in range(lowNum, highNum+1):
    if x % multi == 0:
        print(x)


