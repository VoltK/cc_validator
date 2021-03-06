# Generate random card numbers using Luhn algorithm; You can check results with card_validator.py


import random


def master_or_visa():
    first = 0
    while first != 5 and first != 4:
        m_v = input("Enter which type you need: MasterCard('m') or Visa('v'): ")
        if m_v == 'v':
            first = 4
        elif m_v == 'm':
            first = 5

    return first


def random_number(cc, first):
    cc.append(first)
    for x in range(14):
        cc.append(random.randint(0, 9))
    return cc


def sum_all(cc, sum_nums):
    for index, x in enumerate(reversed(cc)):
        if index == 0 or index % 2 == 0:
            x *= 2
            if x >= 10:
                x -= 9
        sum_nums += x
    return sum_nums


def checksum(sum_nums, cc):
    for x in range(10):
        if (sum_nums + x) % 10 == 0:
            cc.append(x)
    return cc


def main():

    all_cards = []
    pay_s = master_or_visa()
    num_cards = int(input("How many card numbers do you want to generate: "))
    for i in range(num_cards):
        card = []
        sum_ = 0

        # generate 15 numbers
        card = random_number(card, pay_s)

        # calculate sum of odd elements and sum of multiplied by 2 even elements
        sum_ = sum_all(card, sum_)

        # calculate last digit
        card = checksum(sum_, card)

        # convert to string
        card = "".join(str(x) for x in card)

        # add to list of cards
        all_cards.append(card)

    with open('card_numbers.txt', "a") as file:
        for card in all_cards:
            file.write(f"Generated card: {card}\n")
    print(f'{num_cards} generated cards were saved to card_numbers.txt')

if __name__ == '__main__':
    main()
