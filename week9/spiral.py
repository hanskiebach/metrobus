import sys

size = 501 #I assumed I needed to change this from 5 to 501 due to the instructions in the homework, so that it is a 501 x 501 spiral

def print_square(square):
    print("-"*(2*size)) 
    for y in range(len(square)):
       for x in range(len(square[y])):
           print("{:6}".format(square[x][y]), end="")
       print()
    print("-"*(2*size)) 


square = [[f"{x}.{y}" for x in range(size)] for y in range(size)] #I know that this is the line where I need to be able to write the proper math equation in order for my program to output the answer.

print_square(square)

#I will be honest that I have been trying to figure out a way to get this program to work and I have not been close to being succesful. I am starting to get very confused and feel like I am not understanding
#or maybe even retaining the information that I should in order to get close to the answer.
#I know that I need to come up with a function that contains a complex equation that will properly sum the numbers in the diagnols, but I really don't know how to start
#I'm definitely hoping I can speak with you after class to get a better understanding of why I am blanking so badly on starting, and hopefully get closer to the answer when I pick this up again.
#I might also need to create some sort of new variable as well in order for the program to print the solution (possibly name the variable solution), but I am still unsure.

#I think the function would have to be able to take into account that with each spiral closing and starting a new, it must compensate for this by moving outwards by x number in order to locate
#the new diagnoal values for that given spiral. This I'm sure is done with some sort of equation that I unfortunately can not come up with myself. Once the program has identified all diagonal values for each
#spiral it will obviously sum the total values