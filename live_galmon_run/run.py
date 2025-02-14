
import argparse
import sys
sys.path.insert(0, '..')

from osnma.receiver.receiver import OSNMAReceiver
from osnma.receiver.input_galmon import GALMON


parser = argparse.ArgumentParser(description='Runs OSNMAlib using GALMON live data.')
args = parser.parse_args()


def live_galmon_config():
    config_dict = {
        'exec_path': '.',
        'pubk_name': 'OSNMA_PublicKey.xml',
        'merkle_name': 'OSNMA_MerkleTree.xml'
    }

    input_module = GALMON()  # Default host='86.82.68.237', port=10000 
    osnma_r = OSNMAReceiver(input_module, config_dict)

    osnma_r.start()


if __name__ == "__main__":

    print(f"Running using GALMON live data.")
    live_galmon_config()
