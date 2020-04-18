import argparse
import random
import string
import os


parser = argparse.ArgumentParser(
    prog='keygen',
    description='Key generator')

parser.add_argument('-q', type=int)
args = parser.parse_args()


def gen_key():
    key = ''
    alphabet = string.ascii_uppercase + '0123456789'
    for block in range(5):
        for num_characters in range(5):
            key += random.choice(alphabet)
        if block != 4:
            key += "-"
    return key


def write_key(key):
    with open(f'/Users/{os.getlogin()}/Desktop/key.txt', 'a') as f:
        f.write(f'{key}\n')
        f.close()


def run(quantity):
    for _ in range(quantity):
        write_key(gen_key())


if __name__ == "__main__":
    run(args.q)
