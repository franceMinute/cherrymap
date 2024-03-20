import logging
from uuid import uuid4
from neo4j import GraphDatabase, RoutingControl
from neo4j.exceptions import DriverError, Neo4jError
from constants import NEO4J_USER, NEO4J_PASS, NEO4J_URI


class Neo4JConnection:

    def __init__(self, database=None):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
        self.database = database

    def close(self):
        self.driver.close()

    def create_scan(self, data=None):
        id = str(uuid4())
        query = (
            "CREATE (s:Scan {id: $id})"
        )

        try:
            self.driver.execute_query(
                query,
                id=id,
                database_=self.database
            )
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise

        return id

    def _create_host_node(self,scan_id, ip, hostname, status):
        query = (
            """MATCH (sc:Scan {id: $scan_id})
            CREATE (sc)-[:SCANNED]->(h:Host {
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
                scan_id=scan_id,
                database_=self.database
            )
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise

    def add_host(self,scan_id, ip, hostname, status):
        query = (
            """MATCH (h:Host {ip: $ip})
            RETURN (n)"""
        )

        try:
            result = self.driver.execute_query(query, ip=ip, database_=self.database)
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise
        
        if result:
            # Add services to existing node
            pass
        else:
            self._create_service_node(scan_id, ip, hostname, status)


    def _create_service_node(self,
                       scan_id,
                       host_ip,
                       port,
                       proto,
                       name="",
                       product=None,
                       version="",
                       details=""
                       ):
        query = (
            "MATCH (:Scan {id: $scan_id})-[:SCANNED]->(h:Host{ip: $host_ip}) "
            "CREATE (h)-[:RUNS]->(sv:Service { port: $port, proto: $proto, name: $name, product: $product, version: $version, details: $details}) "
        )

        try:
            self.driver.execute_query(
                query,
                port=port,
                proto=proto,
                name=name,
                product=product,
                version=version,
                details=details,
                scan_id=scan_id,
                host_ip=host_ip,
                database_=self.database
            )
        except (DriverError, Neo4jError) as exception:
            logging.error("%s raised an error: \n%s", query, exception)
            raise

    def add_service(self, scan_id, host_ip, port,
                    proto, name="", product=None,
                    version="", details=""):
        # IF Doesnt exist
        self._create_service_node(scan_id=scan_id, host_ip=host_ip, port=port,
                                  proto=proto, name=name, product=product,
                                  version=version, details=details)