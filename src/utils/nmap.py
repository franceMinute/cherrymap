class Scope:
    def __init__(self):
        self.hostlist = []

    def add_host(self, new_host):
        self.hostlist.append(new_host)

    def get_num_hosts(status=None, ip=None, port=None, service_name=None):
        pass

class Host:
    def __init__(self, ip, hostname, status, altip=[]):
        self.ip = ip
        self.hostname = hostname
        self.status = status
        self.altip = altip
        self.services = []

    def add_service(self, new_service):
        self.services.append(new_service)

class Service:
    def __init__(self, protocol, port, name=None, product=None, version=None, details=None):
        self.protocol = protocol
        self.port = port
        self.name = name
        self.product = product
        self.version = version
        self.details = details