import unittest
from PR4 import Lorentz_attractor
class TestLorentzAttractor(unittest.TestCase):
    def test_Lorentz_attractor(self):
        x, y, z = 1.0, 1.0, 1.0
        dt = 0.01
        x_new, y_new, z_new = Lorentz_attractor(x, y, z, dt)
        self.assertAlmostEqual(x_new, 1.0, delta=0.1)
        self.assertAlmostEqual(y_new, 1.26, delta=0.1)
        self.assertAlmostEqual(z_new, 0.99, delta=0.1)

if __name__ == '__main__':
    unittest.main()