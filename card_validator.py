# This script checks credit/debit card's checksum using Luhn algorithm
import sys


#   str to list
def card_list(card):
    full_num = []
    for x in card:
        try:
            full_num.append(int(x))
        except:
            sys.exit('Card number cannot contain characters')
    return full_num


#   multiply every second number by 2 starting from 1, except checksum digit
def mult_by2(numbers):
    mult2_num = []
    for ind, value in enumerate(numbers[:-1]):
        if ind % 2 == 0 or ind == 0:
            mult2_num.append(value * 2)
        else:
            mult2_num.append(value)
    return mult2_num


#   if number is 2 digits add them to get 1 digit value, get sum of all numbers
def sum2digits(numbers):
    sum_of_numbers = 0
    for x in numbers:
        s = 0
        while x:
            s += x % 10
            x //= 10
        sum_of_numbers += s
    return sum_of_numbers


def main():
    if len(sys.argv) > 1:
        card = sys.argv[1]

        if len(card) == 16 and (card[0] == '4' or card[0] == '5'):
            full_num = card_list(card)

            multed_by2 = mult_by2(full_num)

            digits_added = sum2digits(multed_by2)

            #   format card number with dashed between each 4 digits
            card = '-'.join([card[i:i + 4] for i in range(0, len(card), 4)])

            #   check sum of all numbers and checksum if it's even multiple of 10
            if (digits_added + full_num[-1]) % 10 == 0:
                print(f'Valid card: {card}')
            else:
                print(f'Not valid card: {card}')
        else:
            print('Not a credit card')
    else:
        print('You need to enter card number')


if __name__ == '__main__':
    main()
