'''
    CS5001
    Spring 2023
    HW1

    Brendan Sheehan

    This program calculates the fewest number of bills needed for an ATM to
    dispense a specified amount of money
'''

'''
    Test case #1:
    Input: $174
    Output: 3 fifties, 1 twenties, 0 tens, 0 fives, 4 ones

    Test case #2:
    Input: $673
    Output:  13 fifties, 1 twenties, 0 tens, 0 fives, 3 ones

    Test case #3:
    Input: $1432
    Output:  28 fifties, 1 twenties,1 tens, 0 fives, 2 ones
'''

def main():

    # input amount to withdraw.
    withdrawal = int(input("Welcome to PDQ Bank! Amount to withdraw? $"))

    # calculate number of fifties needed and twenties needed
    fifties = withdrawal // 50   
    twenties = (withdrawal % 50) // 20

    # variable for calculations: money left to be distributed after twenties
    leftover_from_twenties = (withdrawal % 50) % 20        

    # calculate number of tens, fives, and ones needed
    tens = leftover_from_twenties // 10                                                 
    fives = (leftover_from_twenties % 10) // 5                                     
    ones = (leftover_from_twenties % 10) % 5                              

    # print total amount customer is withdrawing in 50's, 20's, 10's, 5's, 1's
    print(f"Cha-ching! You asked for ${withdrawal:.0f}")    
    print("That breaks down to:")  
    
    print(f"{fifties:.0f} fifties")  
    print(f"{twenties:.0f} twenties")
    print(f"{tens:.0f} tens")
    print(f"{fives:.0f} fives")
    print(f"{ones:.0f} ones")
    
if __name__ == "__main__":
    main() 
