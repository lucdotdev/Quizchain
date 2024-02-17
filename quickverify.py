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
        print('found: '+ wallet['addresses']['p2pkh'])
        return wallet
    
    else :
        raise ValueError('\rNot yet' )


def main():

    text = read_text_from_file('v2/solutions.txt')
    bitcoinadress = '13Cv6SXUnzGDT8JHqzzJ8xMPtsSdhJA4wd'

    solution_hash_start = 'f8e'

    list  = text.split( '\n')

    for i in list:
        hash_value = hashlib.md5(i.encode('utf-8')).hexdigest()

        try: 
            value = generateAndVerifyMnemonicAdress(entropy=hash_value, address=bitcoinadress)
            pass
        except ValueError as e :
            print(e, end='')
         


main()

  


