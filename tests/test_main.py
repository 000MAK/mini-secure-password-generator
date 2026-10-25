import string,unittest
from main import generate_password
class PasswordTests(unittest.TestCase):
    def test_length_and_symbols(self):
        p=generate_password(24); self.assertEqual(len(p),24); self.assertTrue(any(c in "!@#$%^&*()-_=+[]{}?" for c in p))
    def test_no_symbols(self): self.assertTrue(set(generate_password(16,False)) <= set(string.ascii_letters+string.digits))
    def test_bounds(self):
        with self.assertRaises(ValueError): generate_password(8)
if __name__=="__main__": unittest.main()
