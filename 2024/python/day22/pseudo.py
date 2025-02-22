import argparse
from collections import defaultdict



def get_values(file_path):
    values = []
    with open(file_path, 'r') as file:
        for line in file.read().splitlines():
            values.append(int(line))
    return values

def get_secret(input):
    num = (input ^ (input * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num

def get_secret_bits(input):
    num = (input ^ (input << 6)) & 0xFFFFFF
    num = (num ^ (num >> 5)) & 0xFFFFFF
    num = (num ^ (num << 11)) & 0xFFFFFF
    return num 


def get_maximum_price_from_buyer_sequences(nums):
    """
    for each buyer (represented by an entry in nums), generate 2000 secrete numbers
    and use the last digit of each secret number as the price. Track sequences of four
    price changes (using 5 prices), with the last price in the sequence being the
    actual price offered by that buyer.
    store results in a map, return the maximum value of the map
    """
    bananas_per_sequence = defaultdict(int)

    for num in nums:
        buyer = [num % 10]      # ones digit of the secret number
        for _ in range(2000):
            num = get_secret_bits(num)
            buyer.append(num % 10)
        # iterate through slice of 5 values and get the "difference sequence"
        seen = set()
        for i in range(len(buyer) - 4):
            # monkey pays buyer[i+4] bananas after this sequence
            seq = ( buyer[i+1] - buyer[i],
                buyer[i+2] - buyer[i+1],
                buyer[i+3] - buyer[i+2],
                buyer[i+4] - buyer[i+3] )
            # only the first occurence of the sequence matters for each buyer
            if seq in seen: continue
            seen.add(seq)
            bananas_per_sequence[seq] += buyer[i+4]

    return max(bananas_per_sequence.values())


def PART_ONE(nums, debug):
    total = 0
    for num in nums:
        for _ in range(2000):
            num = get_secret_bits(num)
        total += num
    print(f'total of the 2000-th secret values is {total}')


def PART_TWO(nums, debug):
    """
    find sequence of 4 price changes, where the prices are the ones digit of each secret number,
    that gets the best price (the price after a given sequence of 4) across all of the
    buyers
    """
    ans = get_maximum_price_from_buyer_sequences(nums)
    print(f'the most bananas from the exchange will be {ans}')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="make instructions for series of keypad-typing robots")
    parser.add_argument('file_path', help="path to the text file containing the needed codes")
    args = parser.parse_args()
    nums = get_values(args.file_path)
    PART_ONE(nums, False)
    print()
    PART_TWO(nums, True)