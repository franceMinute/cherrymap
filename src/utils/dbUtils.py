
"""deprecated: switching to Obsidian output"""

import sqlite3
from sqlite3 import Error
import logging

def create_connection(db_file):
    """ Create a database connection to an CherryTree db file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to SQLite DB at {db_file}")
        logging.info(f"SQLite DB version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)

    return conn
