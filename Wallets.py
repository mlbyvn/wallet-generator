from mnemonic import Mnemonic
from eth_account import Account
import os
import sys

def generate_wallet():
    Account.enable_unaudited_hdwallet_features()  # Enable HD wallet features

    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=128)  # Generate a 12-word mnemonic phrase

    # Create an account using the mnemonic phrase
    acct = Account.from_mnemonic(mnemonic_phrase)

    return acct.address, mnemonic_phrase, acct.key.hex()

def save_wallets_to_file(filename, num_wallets):
    with open(filename, "w") as file:
        for i in range(num_wallets):
            address, mnemonic, private_key = generate_wallet()
            file.write(f"Wallet {i+1}:\n")
            file.write(f"Address: {address}\n")
            file.write(f"Mnemonic: {mnemonic}\n")
            file.write(f"Private Key: {private_key}\n\n")
    print(f"Successfully saved {num_wallets} wallets to {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Wallets.py <output_file>")
        print("Example: python Wallets.py mywallets.txt")
    else:
        num_wallets = int(input("Enter the number of wallets to generate: "))
        save_wallets_to_file(sys.argv[1], num_wallets)