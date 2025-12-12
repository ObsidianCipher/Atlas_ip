"""Replace for the original ip-mask.py using underscore naming so it can be imported as a module.
This module exposes `main()` and is safe to import from `main.py`.
"""
import socket
import random


def mask_ip(ip_address):
    # Split the IP address into its components
    ip_parts = ip_address.split('.')
    
    # Generate random values for each part to create a masked IP
    masked_parts = [str(random.randint(1, 254)) for _ in ip_parts]
    
    # Join the masked parts to form the masked IP address
    masked_ip = '.'.join(masked_parts)
    
    return masked_ip

def get_actual_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def main():
    actual_ip = get_actual_ip()
    masked_ip = mask_ip(actual_ip)
    print(f"Actual IP Address: {actual_ip}")
    print(f"Masked IP Address: {masked_ip}")


if __name__ == '__main__':
    main()
