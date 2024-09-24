import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        x = runner.Runner('Mark')
        for i in range(10):
            x.walk()
        self.assertEqual(x.distance, 50, f'{x.name} должен пройти 50 метров, а прошел {x.distance}')

    def test_run(self):
        y = runner.Runner('Ugor')
        for i in range(10):
            y.run()
        self.assertEqual(y.distance(), 100, f'{y.name} должен пробежать 100 метров, а пробежал {y.distance()}')

    def test_challenge(self):
        x = runner.Runner('Mark')
        for i in range(10):
            x.walk()
        y = runner.Runner('Ugor')
        for i in range(10):
            y.run()
        self.assertNotEqual(x.distance(), y.distance(), "Разница значений")



if __name__ == "__main__":
    unittest.main()


#Ran 1 test in 0.017s

#Ran 3 tests in 0.001s OK

#Ran 1 test in 0.017s

#Ran 3 tests in 0.001s OK
