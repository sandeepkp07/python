import unittest


class Testum(unittest.TestCase):
    def test_num(self):
        self.assertEqual((3*4),12)

if __name__=='__main__':
    unittest.main()
