import logging
from neo4j import GraphDatabase, RoutingControl
from neo4j.exceptions import DriverError, Neo4jError
from constants import NEO4J_USER, NEO4J_PASS, NEO4J_URI


class Neo4JConnection:

    def __init__(self, database=None):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
        self.database = database

    def close(self):
        self.driver.close()

    def create_scan(self, name, data=None):
        query = (
            "CREATE (s:Scan {name: $name})"
        )

        try:
            self.driver.execute_query(
                query,
                name=name,
                database_=self.database
            )
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise

    def create_host(self, ip, hostname, status):
        query = (
            """CREATE (h:Host {
                ip: $ip,
                hostname: $hostname,
                status: $status
            })"""
        )

        try:
            self.driver.execute_query(
                query,
                ip=ip,
                hostname=hostname,
                status=status,
                database_=self.database
            )
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise
