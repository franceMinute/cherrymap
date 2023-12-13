import argparse
import logging
from utils.dbUtils import create_connection
from utils.loggingUtils import parse_log_level

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description='Connect to an SQLite database.')
    parser.add_argument('--db', help='Path to SQLite database file', required=True)
    parser.add_argument('--log-level', default='INFO', help='Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)')
    args = parser.parse_args()

    # Logging configs
    log_level = parse_log_level(args.log_level)
    logging.basicConfig(level=log_level)

    # Create a database connection
    database = args.db
    conn = create_connection(database)

    # Close db connection
    if conn:
        conn.close()

if __name__ == '__main__':
    main()
