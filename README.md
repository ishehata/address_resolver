
# Address Resolver

Address Resolver is a simple tool to resolve the street name and housenumber
from a given string.

## How it works?

Address Resolver tries to find a certain pattern in the given address,

The recognized patterns are:

    - Address starts with a number. e.g: 200 Broadway Av
    - There is a comma used in the address. e.g: 4, rue de la revolution
    - "No." abbreviation is used before housenumber, e.g: Calle 39 No 1540
    - Address ends with a number. e.g: Musterstrasse 45B
    - If there were no matched pattern, an Exception will be raised""

It's important that the pattern matching happens in that order.


## Usage

1. From command line:

It's possible to run the tool from CLI and pass address to it as first argument, example:

```
python address_resolver.py "31 Boyenstrasse"
```


2. From Python

You can import the library in your project and use the `resolve` function to resolve and address.

```python
import address_resolver

info = address_resolver.resolve("31 Boyenstrasse")

print(info) # => {'street': 'Boyenstrasse', 'housenumber': '31'}
```


## Testing

Current tests are implement it `unittest` test cases, you can run them from the command line using:

```
python -m unittest -vv address_test.py
```
