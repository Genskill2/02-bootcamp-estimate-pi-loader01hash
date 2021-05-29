import unittest
import random
import functools
import math


def monte_carlo(i):
    circle=0
    s=0
    total=0
    for i in range(i**2):
        rx=float(random.uniform(-1,1))
        ry=float(random.uniform(-1,1))
        dist=float(math.sqrt(rx**2+ry**2))
        if dist<=1:
            circle+=1
        
        s+=1
        pi=4*(circle/s)
        #print(rx,ry,circle,s,"-",pi)
    return pi        

def wallis(n):
    pi1 = 0.0   
    for k in range(1, n):
        x = 4 * (k ** 2)
        y = x - 1
        z = float(x) / float(y)
        if (k == 1):
            pi1 = z
        else:
            pi1 *= z
    pi1 *= 2
    return pi1

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
