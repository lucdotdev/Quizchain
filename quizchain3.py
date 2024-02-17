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

    
    total_one_word=  45970
    total_two_word = 1056597465
    total_three_word = 3238199999999




    solution_hash_start = '1d'
 
    # Sample text with words
    text = read_text_from_file('second.txt')
    bitcoinadress = '13Cv6SXUnzGDT8JHqzzJ8xMPtsSdhJA4wd'

   
    punctuation_to_remove = "!?,;.()"
    translator = str.maketrans('', '', punctuation_to_remove)



    solution_nonce = "Bitcoin Grycoin TOMI "
    solution_hash_start = '1d'
 
    # Sample text with words
    text = read_text_from_file('second.txt')
    solutions = open('v2/n/1.txt', 'a')
    hashList = []


    if text:
        words = text.split()
    
        for i in range(0, len(words)):

                wordsK = []

                try :
                    wordsK.append(words[i])
                    # wordsK.append(words[i+1])
                    # wordsK.append(words[i+2])
                    # wordsK.append(words[i+3])
                    # wordsK.append(words[i+4])
                    # wordsK.append(words[i+5])
                    # wordsK.append(words[i+6])
                    # wordsK.append(words[i+7])
                    # wordsK.append(words[i+8])
                    # wordsK.append(words[i+9])
            
                
                except IndexError : 
                    print('index error')
                    break


                solution = ' '.join(wordsK).translate(translator)

                hash_value = hashlib.md5(solution.encode('utf-8')).hexdigest()
                
                if hash_value.startswith(solution_hash_start):

                 
                    if hash_value in hashList:
                        continue

                    else: 
                        hashList.append(hash_value)

                        solutions.write(solution +  '\n')



    allow_sleep()

if __name__ == "__main__":
    main()
