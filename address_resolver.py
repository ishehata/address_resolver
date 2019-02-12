def resolve(address: str):
    # Determine Delimiter
    delimiter = ',' if ',' in address else ' '


    result = {'street': None, 'housenumber': None}

    arr = address.split(delimiter)
    for item in arr:
        if item.isdigit():
            result['housenumber'] = item
        else:
            result['street'] = item

    return result
