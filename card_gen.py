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
    for x in range(1, 10):
        if (sum_nums + x) % 10 == 0:
            cc.append(x)
    return cc


def main():
    pay_s = master_or_visa()

    card = []
    sum_ = 0
    while sum_ == 0:

        # generate 15 numbers
        card = random_number(card, pay_s)

        # calculate sum of odd elements and sum of multiplied by 2 even elements
        sum_ = sum_all(card, sum_)

        # if we don't have any remainder we need to get another card number, because we won't be able to calculate checksum
        if sum_ % 10 == 0:
            sum_ = 0
            card.clear()

    card = checksum(sum_, card)

    card = "".join(str(x) for x in card)
    print(f"Generated card: {card}")


if __name__ == '__main__':
    main()

