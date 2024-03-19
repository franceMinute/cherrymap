from openpyxl import Workbook
import utils.nmap as nmap

def create_xls_export(scope: nmap.Scope, export_file_path: str):
    wb = Workbook()
    ws = wb.active
    ws.append(
        [
            "IP Address",
            "Port",
            "Hostname",
            "Status",
            "Protocol",
            "Service Name"
            "Service Version"
        ]
    )
    
    for current_host in scope.hostlist:
        for current_service in current_host.services:
            ws.append(
                [
                    current_host.ip,
                    current_service.port,
                    current_host.hostname,
                    current_host.status,
                    current_service.protocol,
                    current_service.name,
                    current_service.version
                ]
                )
    
    wb.save(export_file_path)