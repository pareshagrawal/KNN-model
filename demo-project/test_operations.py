from re import S
import unittest
import operations

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(operations.add(-1,-1),-2)
        self.assertEqual(operations.add(-1,1),0)
        self.assertEqual(operations.add(-1,-1.5),-2.5)
        self.assertEqual(operations.add(10,20),30)

    def test_subtract(self):
        self.assertEqual(operations.subtract(-1,-1),0)
        self.assertEqual(operations.subtract(-1,1),-2)
        self.assertEqual(operations.subtract(-1,-1.5),0.5)
    
if __name__ == '__main__':
    unittest.main()
