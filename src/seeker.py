import argparse
import logging
from utils.loggingUtils import parse_log_level
from parsers.nmapParser import parse_nmap_xml

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description='Connect to an SQLite database.')
    parser.add_argument('--vault', help='Path to Obsidian vault', required=True)
    parser.add_argument('--log-level', default='INFO', help='Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)')
    args = parser.parse_args()

    # Logging configs
    log_level = parse_log_level(args.log_level)
    logging.basicConfig(level=log_level)

    tmp = parse_nmap_xml(args.vault)

    logging.info("Done.")

if __name__ == '__main__':
    main()
