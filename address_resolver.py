"""
Address Resolver is a simple tool to resolve the street name and housenumber
from a given string.

How it works?
Address Resolver tries to find a certain pattern in the given address,
the recognized patterns are:
    - Address starts with a number. e.g: 200 Broadway Av
    - There is a comma used in the address. e.g: 4, rue de la revolution
    - "No." abbreviation is used before housenumber, e.g: Calle 39 No 1540
    - Address ends with a number. e.g: Musterstrasse 45B
    - If there were no matched pattern, an Exception will be raised""

It's important that the pattern matching happens in that order.
"""
import re



def resolve(address: str) -> {'street': str, 'housenumber': str}:
    """resolve takes an address as input and tries to find a known pattern
    in it to separate street name from housenumber.

    returns {'street': str, 'housenumber': str}
    """
    result = {'street': '', 'housenumber': ''}

    # patter: address starts with a number
    r = re.match(r'^(\d+) (.*)', address)
    if r:
        result['street'] = r.group(2)
        result['housenumber'] = r.group(1)
        return result

    # pattern: there is comma
    if ',' in address:
        arr = address.split(',')
        if re.match('.*?(\d+).*?, .*', address):
            housenumber = arr[0]
            street = arr[1].strip()
        else:
            street = arr[0]
            housenumber = arr[1].strip()
        result['street'] = street
        result['housenumber'] = housenumber
        return result

    # pattern: there is a "No." before housenumber
    r = re.match(r'(.*) (No)\.? (.*)', address, re.IGNORECASE)
    if r:
        result['street'] = r.group(1)
        result['housenumber'] = f'{r.group(2)} {r.group(3)}'
        return result

    # pattern: address ends with a number, or a number followed by one letter
    r = re.match(r'(.*) (\d+ ?(\w+)?)$', address)
    if r:
        result['street'] = r.group(1)
        result['housenumber'] = r.group(2)
        return result

    raise Exception(f'Couldn\'t resolve the given address: {address}')


if __name__ == '__main__':
    import sys
    print(resolve(sys.argv[1]))
