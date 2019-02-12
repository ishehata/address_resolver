from unittest import TestCase
from address_resolver import resolve

class AddressTest(TestCase):

    def simple_1number(self):
        result = {"street": "Winterallee", "housenumber": "3"}
        assert resolve('Winterallee 3') == result

    def simple_2number(self):
        result = {"street": "Musterstrasse", "housenumber": "45"}
        assert resolve('Musterstrasse 45') == {"street": "Musterstrasse", "housenumber": "45"}

    def simple_3number(self):
        result = {"street": "Blaufeldweg", "housenumber": "123B"}
        assert resolve("Blaufeldweg 123B") == result
