def main():

    def quest1 ():
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Hint: Use 'continue' statement.
        for x in range (0,7):
            if x==3 or x==6:   #skips 3 and 6
                continue
            else:
                print(x)

    def quest2 ():
#Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        evensum=0
        oddsum=0
        for x in range (1,21):
            if x%2==0:    #counts even
                evensum+=1
            else:           #counts odd
                oddsum+=1
        print("Number of even numbers: ", evensum)
        print("Number of odd numbers: ", oddsum)

    def quest3():
#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output after
# User enters a blank line to end.
        stringsentence=""
        while(True):
            sentence= input("Please input text. Enter nothing to escape. ")
            if sentence=="": # if user enters nothing, breaks out
                print(stringsentence)
                break
            else: #otherwise hold on the the variable and prints it on a new line
                stringsentence+=sentence + "\n"  # new line


    def bonus():
#Write a Python program to construct the following pattern, using a nested for loop.
        y = "*"
        z = "*"
        for x in range(1,6):
            print(y)
            y+=z
            if x == 5:
                for x in range (5,10):
                    y= y[:-1]  #uses the[:-1] to remove the final character in a string
                    if x == 5: #skips because it will print another line with 5 stars
                        continue
                    print(y)



    #quest1()
    #quest2()
    #quest3()
    bonus()


if __name__ == '__main__':
    main()
