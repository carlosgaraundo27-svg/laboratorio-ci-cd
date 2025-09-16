import unittest
from main import saludar

class TestMain(unittest.TestCase):
    def test_saludar(self):
        self.assertEqual(saludar(), "¡Hola Mundo desde Python!")

if __name__ == "__main__":
    unittest.main()
