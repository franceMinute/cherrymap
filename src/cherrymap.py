import argparse
import logging
from utils.dbUtils import create_connection
from utils.loggingUtils import parse_log_level

def main():
    parser = argparse.ArgumentParser(description='Connect to an SQLite database.')
    parser.add_argument('--db', help='Path to SQLite database file', required=True)
    parser.add_argument('--log-level', default='INFO', help='Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)')

    args = parser.parse_args()
    log_level = parse_log_level(args.log_level)
    logging.basicConfig(level=log_level)

    database = args.db

    # Create a database connection
    conn = create_connection(database)

    if conn:
        conn.close()

if __name__ == '__main__':
    main()
