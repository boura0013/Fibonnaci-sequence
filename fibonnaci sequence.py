#Fibbonacci number array that will be written to and read from during code with starting 2 numbers
FibonnaciNumberArray = [1,1]
#Loop with essentially infinite value(we use a loop rather than an infinite while statement because it gives us
# a convenient counter variable(i))
for i in range(100000000000000):
    #For each time the loop runs add to the end of the array the last number inputted in the array + 
    # the second last number inputted into the array
    FibonnaciNumberArray.append(FibonnaciNumberArray[i] + FibonnaciNumberArray[i+1])
    # Print the full array to your screen
    print(FibonnaciNumberArray)
    #Increase the counter variable at the end of the loop
    i = i + 1
