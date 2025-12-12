"""Replace for the original phno-info.py using underscore naming so it can be imported as a module.
"""
import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def get_phone_info(phone_number_str):
    phone_info = {}
    phone_number = phonenumbers.parse(phone_number_str)

    phone_info['formatted_number'] = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    phone_info['country'] = geocoder.description_for_number(phone_number, "en")
    phone_info['carrier'] = carrier.name_for_number(phone_number, "en")
    phone_info['time_zones'] = timezone.time_zones_for_number(phone_number)

    return phone_info


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python phno_info.py <phone-number>")
    else:
        info = get_phone_info(sys.argv[1])
        print(info)
