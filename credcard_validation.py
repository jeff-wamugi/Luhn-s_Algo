#!/usr/bin/env python3

def val_card(a):
    """
    Steps in validation:
     - Doubling the value of every second digit from the right (starting 
       from second-to-last)
     - If a doubled value is greater than 9, sum its digits.
     - Sum all the digits in the card
     - Finally check if the last digit in the sum is 0 (Multiple of ten)

    """
    card_list = [int(num) for num in str(a)]
    num = len(str(a)) 
    for val in range(num - 2, -1, -2):
        card_list[val] = card_list[val] * 2 # double value of every second digit
        if card_list[val] > 9:
            # Convert to string, map digits to int, and sum them
            card_list[val] = sum(map(int, str(card_list[val])))
            pass
    
    # Now add the digits in the card number
    sum_digits = sum(card_list)
    print(f"Your Card Number after Luhn's Transformation: {card_list}")
    print(f"The sum of the digits in your Card's Number: {sum_digits}")

    # Check if the last digit is a 0
    if sum_digits%10 == 0:
        print(f"Card ({a}) is a valid Card Number")
    else:
        print(f"Card ({a}) is NOT a valid Card Number!")


def main():
    while True:
        card_no = input("Enter Card Number or press Enter to exit: ")  # Take input 
        if card_no == "":
            break  # Exit the loop
        """
         -> Check the length of the card number to verify
            its valid. Cards vary in length from 13-19 
            depending on the card type, this program checks
            for 16 (for demonstration purpose/Standard length).
         -> Also checks input type is integer
        """
        if not card_no.isdigit() or len(card_no) != 16:
            print("Card Number should be 16 characters long and all digits(0-9)")
        else:
            card_no = int(card_no)  # Convert to integer only after validation
            val_card(card_no)

if __name__ == "__main__":
    main()