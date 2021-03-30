import unittest


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_consumer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, 'org xyz')
        self.assertEqual(customer.adress, '')


class TestComplexData(unittest.TestCase):
    def setUp(self):
        self.app = App(database='fixtures/test_complex.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)

    def test_existence_of_consumer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, 'org xyz')
        self.assertEqual(customer.adress, '')


if __name__ == '__main__':
    unittest.main()
