import os
import logging

def generate_vault(vault_path):
    try:
        os.makedirs(vault_path)
    except FileExistsError:
        logging.info("File {} already exists. ".format(vault_path))
        

