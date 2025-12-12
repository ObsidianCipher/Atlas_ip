"""Replace for the original my-ip.py using underscore naming so it can be imported as a module.
"""
import socket
import psutil


def get_ip_details():
    ip_details = {}
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip_details['hostname'] = hostname
    ip_details['ip_address'] = ip_address
    ip_details['network_interfaces'] = {}

    for interface, addrs in psutil.net_if_addrs().items():
        ip_details['network_interfaces'][interface] = []
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip_info = {
                    'ip_address': addr.address,
                    'netmask': addr.netmask,
                    'broadcast': addr.broadcast
                }
                ip_details['network_interfaces'][interface].append(ip_info)

    return ip_details


if __name__ == '__main__':
    # Print the collected IP details to the terminal when running directly
    details = get_ip_details()
    print(details)
