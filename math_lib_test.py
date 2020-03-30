
import math_lib as m
import unittest

class test_operacie(unittest.TestCase):
    
    def test_sucet_kladne_cele(self):
        self.assertEqual(m.sucet(25,30), 55, "Očakávaný výsledok: 55")
        self.assertEqual(m.sucet(120, 250), 370, "Očakávaný výsledok: 370") 
        self.assertEqual(m.sucet(2700256, 250785121), 253485377, "Očakávaný výsledok: 253 485 377")

    def test_sucet_zaporne_cele(self):
        self.assertEqual(m.sucet(-20,-50), -70, "Očakávaný výsledok: -70")
        self.assertEqual(m.sucet(70,-120), -50, "Očakávaný výsledok: -50")
        self.assertEqual(m.sucet(-107557870,145454520), 37896650, "Očakávaný výsledok: 37 896 650")

    def test_sucet_kladne_desatinne(self):
        self.assertEqual(m.sucet(1.5, 7.125), 8.625, "Očakávaný výsledok: 8.625")
        self.assertAlmostEqual(m.sucet(0.124578, 1454.15454525), 1454.27912325)
        self.assertEqual(m.sucet(4545.545654564556455, 457.154564564564525), 5002.70021912912098, "Očakávaný výsledok: 5 002.70021912912098")
    
    def test_sucet_zaporne_desatinne(self):
        self.assertEqual(m.sucet(-71.5, -227.125), -298.625, "Očakávaný výsledok: -298,625")
        self.assertEqual(m.sucet(-45.78756456, 17.15454625), -28.63301831, "Očakávaný výsledok: -28,63301831")
        self.assertAlmostEqual(m.sucet(75.5456456744564, -877.15454654654655425), -801.60890087209015425)

    def test_rozdiel_kladne_cele(self):
        self.assertEqual(m.rozdiel(25,30),-5, "Očakávaný výsledok: -5")
        self.assertEqual(m.rozdiel(250, 120),130 , "Očakávaný výsledok: 130")
        self.assertEqual(m.rozdiel(2700256, 250785121), -248084865, "Očakávaný výsledok:-248 084 865")

    def test_rozdiel_zaporne_cele(self):
        self.assertEqual(m.rozdiel(-20,-50), 30, "Očakávaný výsledok: 30")
        self.assertEqual(m.rozdiel(120,-158), 278, "Očakávaný výsledok: 278")
        self.assertEqual(m.rozdiel(-7546467564540,-5546455450), -7540921109090, "Očakávaný výsledok: -7 540 921 109 090")

    def test_rozdiel_kladne_desatinne(self):
        self.assertEqual(m.rozdiel(1.5, 7.125), -5.625, "Očakávaný výsledok: -5,625")
        self.assertEqual(m.rozdiel(0.124578, 1454.15454525), -1454.02996725, "Očakávaný výsledok: -1454.02996725")
        self.assertEqual(m.rozdiel(4545.545654564556455, 457.154564564564525), 4088.39108999999193, "Očakávaný výsledok: 4 088,39108999999193")
    
    def test_rozdiel_zaporne_desatinne(self):
        self.assertEqual(m.rozdiel(-71.5, -227.125), 155.625, "Očakávaný výsledok: 155,625")
        self.assertEqual(m.rozdiel(-45.78756456, 17.15454625), -62.94211081, "Očakávaný výsledok: -62,94211081")
        self.assertEqual(m.rozdiel(75.5456456744564, -877.15454654654655425), 952.70019222100295425, "Očakávaný výsledok: 952,70019222100295425")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_operacie)
    unittest.TextTestRunner(verbosity=2).run(suite)