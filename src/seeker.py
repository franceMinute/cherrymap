import argparse
import logging
from utils.loggingUtils import parse_log_level
from utils.excel import create_xls_export
from utils.neo4j import Neo4JConnection
from parsers.nmapParser import parse_nmap_into_db, parse_nmap_xml

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Parser for nmap output to Obsidan vaults")
    parser.add_argument("-iX", "--input-xml", help="Path to input XML nmap file", required=True)
    parser.add_argument("-v", "--vault", help="Path to Obsidian vault")
    parser.add_argument("-oE", "--output-excel", help="Path to Excel output file")
    parser.add_argument("-db", help="Output results to local Neo4J database.", action="store_true")
    parser.add_argument("--log-level", default="INFO", help="Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    args = parser.parse_args()

    # Logging configs
    log_level = parse_log_level(args.log_level)
    logging.basicConfig(level=log_level)

    logging.info("Parsing inputs")
    nmap_data = parse_nmap_xml(args.input_xml)

    if args.output_excel:
        logging.info("Generating Excel export...")
        create_xls_export(nmap_data, args.output_excel)

    if args.db:
        db = Neo4JConnection()
        try:
            parse_nmap_into_db(args.input_xml, db)
        finally:
            db.close()




    # Export to obsidian

    logging.info("Done.")

if __name__ == '__main__':
    main()
