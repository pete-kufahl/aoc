
import hashlib

ZEROES = 6

def md5_return_hex(string):
    """Calculates the MD5 hash of a string, outputs hex string of hash."""
    # Encode the string to bytes if it's not already
    if isinstance(string, str):
        string = string.encode('utf-8')

    # Create an MD5 hash object
    hash_object = hashlib.md5(string)

    # Get the hexadecimal representation of the hash
    hex_digest = hash_object.hexdigest()

    return hex_digest

if __name__ == '__main__':
    input = "ckczppom"
    num = 0
    md5_hash = md5_return_hex(input + str(num).zfill(ZEROES))

    while not md5_hash.startswith('0' * ZEROES):
           num += 1
           md5_hash = md5_return_hex(input + str(num).zfill(ZEROES))

    print(num)