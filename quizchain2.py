import ctypes
import os
import csv
import hashlib
import itertools
import time
from bitcoinlib.mnemonic import Mnemonic
from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC as SYMBOL


# Define constants for Windows power settings
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
AWAYMODE = 0x00000040

def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | AWAYMODE)

def allow_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)


def calculate_remaining_time(start_time, current_index, total_combinations):
    current_time = time.time()
    elapsed_time = current_time - start_time
    combinations_processed = current_index + 1
    time_per_combination = elapsed_time / combinations_processed
    remaining_combinations = total_combinations - combinations_processed
    remaining_time = remaining_combinations * time_per_combination
    return remaining_time

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    
def save_data_to_text(data, filename):
    with open(filename, mode='w', newline='\r\n') as file:
        for item in data:
            file.write(str(item) + '\n')


def generateAndVerifyMnemonicAdress(entropy, address):
    # Initialize Bitcoin mainnet HDWallet
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=True)
    # Get Bitcoin HDWallet from entropy
    hdwallet.from_entropy(
        entropy=entropy, language='english'
    )

    wallet = hdwallet.dumps()

    if(wallet['addresses']['p2pkh']==address): 
        save_data_to_text(wallet, 'v2/wallet.txt')
        print('found: '+ wallet['addresses']['p2pkh'])
        return wallet
    
    else :
        raise ValueError('Not yet: adress: ' + wallet['addresses']['p2pkh'] + 'not valid' )
    

  





def main():
    prevent_sleep()

    bitcoinadress = '13Cv6SXUnzGDT8JHqzzJ8xMPtsSdhJA4wd'

    hashList = []

    punctuation_to_remove = "!?,;.()"
    translator = str.maketrans('', '', punctuation_to_remove)

    solutions = open('v2/solutionsanGRY.txt', 'a')

    solution_nonce = 'people anGRY TOMI '
    #"Bitcoin Grycoin TOMI "

    solution_hash_start = 'f8e'
 
    # Sample text with words
    text = read_text_from_file('second.txt')
    if text:
        words = text.split()
        max_words = min(len(words), 3)
        start_time = time.time()

        for i in range(1, max_words + 1):
            print(f"Generating combinations of {i} word(s):")
            combinations = itertools.combinations(words, i)
    

            for j, combination in enumerate(combinations):
                solution = (solution_nonce + ' '.join(combination)).translate(translator)
                hash_value = hashlib.md5(solution.encode('utf-8')).hexdigest()
                if hash_value.startswith(solution_hash_start):
                    if hash_value in hashList:
                        continue
                    else : 
                        solutions.write(solution + '\n')
                        hashList.append(hash_value)
                        try: 
                            value = generateAndVerifyMnemonicAdress(entropy=hash_value, address=bitcoinadress)
                            print(value)
                            pass
                        except ValueError as e :
                            continue

        solutions.close()
        total_time = time.time() - start_time
        print(f"Total time taken: {total_time:.2f} seconds")

    allow_sleep()


if __name__ == "__main__":
    main()
