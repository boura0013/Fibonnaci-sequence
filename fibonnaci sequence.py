#Import time module so that I can add a delay later in the program
import time
#Fibbonacci number array that will be written to and read from during code with starting 2 numbers
FibonnaciNumberArray = [1,1]
EndNumber = input("How many fibonnaci numbers do you want to generate")
#Loop with essentially infinite value(we use a loop rather than an infinite while statement because it gives us
# a convenient counter variable(i))
#You can change the range to decide how many numbers you want to output
for i in range(EndNumber-2):
    #For each time the loop runs add to the end of the array the last number inputted in the array + 
    # the second last number inputted into the array
    FibonnaciNumberArray.append(FibonnaciNumberArray[i] + FibonnaciNumberArray[i+1])
    # Print the full array to your screen
    print(FibonnaciNumberArray)
    #Increase the counter variable at the end of the loop
    i = i + 1
    #Add a delay so that we can see each number being outputted and for added stability
    time.sleep(0.5)
