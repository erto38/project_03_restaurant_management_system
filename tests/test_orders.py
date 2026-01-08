import unittest
from orders import calculate_bill

class TestOrders(unittest.TestCase):
    def test_total(self):
        order = {"items": [{"price": 10, "quantity": 2}]}
        bill = calculate_bill(order, 0.1, 0.1)
        self.assertEqual(bill["subtotal"], 20)

if __name__ == "__main__":
    unittest.main()
