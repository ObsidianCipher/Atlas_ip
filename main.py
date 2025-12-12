#this program acts as a main command line interface to run the ip masking functionality
#and phone number information functionality and ip details functionality
import argparse
from ip_mask import main as ip_mask_main
from my_ip import get_ip_details
from phno_info import get_phone_info
def main():
    parser = argparse.ArgumentParser(description="IP Masking and Phone Number Information Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for IP Masking
    ip_mask_parser = subparsers.add_parser('mask_ip', help='Mask the IP address of the machine')

    # Subparser for IP Details
    ip_details_parser = subparsers.add_parser('ip_details', help='Get IP details of the machine')

    # Subparser for Phone Number Information
    phno_info_parser = subparsers.add_parser('phone_info', help='Get phone number information')
    phno_info_parser.add_argument('phone_number', type=str, help='Phone number to get information for')

    args = parser.parse_args()

    if args.command == 'mask_ip':
        ip_mask_main()
    elif args.command == 'ip_details':
        details = get_ip_details()
        print(details)
    elif args.command == 'phone_info':
        info = get_phone_info(args.phone_number)
        print(info)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
