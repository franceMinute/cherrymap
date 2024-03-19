import os
from datetime import datetime
from lxml import etree
from utils.nmap import Service, Host, Scope


def parse_nmap_xml(xml_file_path):

    with open(xml_file_path) as xml_file:
        current_time = datetime.now().strftime("%m-%d-%y %H:%M:%S")
        new_scope = Scope(current_time)
        tree = etree.parse(xml_file)
        root = tree.getroot()

        for host in root.findall(".//host"):
            address_elem = host.find(".//address[@addrtype='ipv4']")
            if address_elem is not None:
                status_elem = host.find(".//status")
                hostnames_elem = host.find(".//hostnames")
                new_ip = address_elem.get("addr")
                new_hostname = hostnames_elem.findall(".//hostname[@name]")[0].get("name")
                new_status = status_elem.get("state")
                new_host = Host(new_ip, new_hostname, new_status)
                tmp_services = host.findall(".//ports/port/state[@state=\"open\"]/..")
                for service in tmp_services:
                    service_name = service.find(".//service").get("name")
                    port = service.get("portid")
                    protocol = service.get("protocol")
                    new_service = Service(protocol, port, service_name)
                    new_host.add_service(new_service)
                new_scope.add_host(new_host)
        return new_scope

