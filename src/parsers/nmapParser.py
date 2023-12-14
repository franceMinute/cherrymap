import os
from lxml import etree


def parse_nmap_xml(xml_file_path):
    """Parse nmap xml file and retrieve host services json

    REFACTOR THIS LESS BAD
    """
    with open(xml_file_path) as xml_file:    

        host_services = {}
        tree = etree.parse(xml_file)
        root = tree.getroot()

        for host in root.findall(".//host"):
            address_elem = host.find(".//address[@addrtype='ipv4']")
            if address_elem is not None:
                ip_address = address_elem.get("addr")
                tmp_services = host.findall(".//ports/port/state[@state=\"open\"]/..")
                if len(tmp_services) != 0:
                    host_services[ip_address] = []

                for service in tmp_services:
                    service_name = service.get("..//service[@name]")
                    port = service.get("portid")
                    protocol = service.get("protocol")
                    host_services[ip_address].append((service_name, protocol, port))

        return host_services

