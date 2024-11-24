'''
    CS5001
    Spring 2023
    HW1

    Brendan Sheehan
'''

'''
    This program calculates the fewest number of bills for an ATM to dispense a specified amount of money
'''

'''Test case #1:
Input: $174
Output: 3 fifties, 1 twenties, 0 tens, 0 fives, 4 ones

Test case #2:
Input: $673
Output:  13 fifties, 1 twenties, 0 tens, 0 fives, 3 ones

Test case #3:
Input: $1432
Output:  28 fifties, 1 twenties,1 tens, 0 fives, 2 ones
'''

def main ():

    amount_to_withdraw = int (input("Welcome to PDQ Bank! Amount to withdraw? $"))  #input amount to withdraw.
    
    fifties = amount_to_withdraw // 50                                                   #calculate number of fifties needed and twenties needed
    twenties = (amount_to_withdraw % 50) // 20
    
    leftover_from_twenties = (amount_to_withdraw % 50) % 20        #variable money left to be distributed after twenties for use in calculations
    
    tens = leftover_from_twenties // 10                                                 #calculate number of tens, fives, and ones needed
    fives = (leftover_from_twenties % 10) // 5                                     
    ones = (leftover_from_twenties % 10) % 5                              
    
    print (f"Cha-ching! You asked for ${amount_to_withdraw:.0f}")  #print total amount customer is withdrawing in 50's, 20's, 10's, 5's, 1's
    print ("That breaks down to:")  
    
    print(f"{fifties:.0f} fifties")  
    print(f"{twenties:.0f} twenties")
    print(f"{tens:.0f} tens")
    print(f"{fives:.0f} fives")
    print(f"{ones:.0f} ones")
    
if __name__ == "__main__" :
    main () 

