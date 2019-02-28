import unittest
from address_resolver import resolve


class AddressTest(unittest.TestCase):

    def test_simplist_case(self):
        result = {'street': 'Winterallee', 'housenumber': '3'}
        self.assertEqual(resolve('Winterallee 3'), result)

    def test_double_number(self):
        result = {'street': 'Musterstrasse', 'housenumber': '45'}
        self.assertEqual(resolve('Musterstrasse 45'), result)

    def test_alphabetic_house_number(self):
        result = {'street': 'Blaufeldweg', 'housenumber': '123B'}
        self.assertEqual(resolve('Blaufeldweg 123B'), result)

    def test_medium_complexity(self):
        result = {'street': 'Am Bächle', 'housenumber': '23'}
        self.assertEqual(resolve('Am Bächle 23'), result)

    def test_separate_words_street(self):
        result = {'street': 'Auf der Vogelwiese', 'housenumber': '23 b'}
        self.assertEqual(resolve('Auf der Vogelwiese 23 b'), result)

    def test_house_number_before_comma(self):
        result = {'street': 'rue de la revolution', 'housenumber': '4'}
        self.assertEqual(resolve('4, rue de la revolution'), result)

    def test_house_number_first(self):
        result = {'street': 'Broadway Av', 'housenumber': '200'}
        self.assertEqual(resolve('200 Broadway Av'), result)

    def test_comma_separator(self):
        result = {'street': 'Calle Aduana', 'housenumber': '29'}
        self.assertEqual(resolve('Calle Aduana, 29'), result)

    def test_no_separate(self):
        result = {'street': 'Calle 39', 'housenumber': 'No 1540'}
        self.assertEqual(resolve('Calle 39 No 1540'), result)

    def test_no_separate_2(self):
        result = {'street': 'Calle 39', 'housenumber': 'No 1540 b'}
        self.assertEqual(resolve('Calle 39 No 1540 b'), result)

    def test_address_with_two_separators(self):
        result = {'street': 'Chausserstrasse', 'housenumber': 'No. 5123'}
        self.assertEqual(resolve('No. 5123, Chausserstrasse'), result)

    def test_exception_raised(self):
        # self.assertRaises(ValueError, callable=resolve('Streetname'))
        try:
            resolve('Streetname')
        except Exception:
            assert True
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
