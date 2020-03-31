#!/usr/bin/env python
# coding: utf-8
# Autor: Daniel Marek <xmarek72>

# Lincense: GNU GPL v.3 
# Whole licence can be found at https://www.gnu.org/licenses/gpl-3.0.html


import math_lib as m
import unittest

## @class Math library testing
# @param unittest.TestCase makes individual unit for testing
class test_operations(unittest.TestCase):
    
    ## Test for addition 1
    # @test addition with positive whole numbers
    # @param self creates a method 
    def test_addition_positive_whole(self):
        self.assertEqual(m.addition(25,30), 55, "Očakávaný výsledok: 55")
        self.assertEqual(m.addition(120, 250), 370, "Očakávaný výsledok: 370") 
        self.assertEqual(m.addition(2700256, 250785121), 253485377, "Očakávaný výsledok: 253 485 377")

    ## Test for addition 2
    # @test addition with negative whole numbers
    # @param self creates a method 
    def test_addition_negative_whole(self):
        self.assertEqual(m.addition(-20,-50), -70, "Očakávaný výsledok: -70")
        self.assertEqual(m.addition(70,-120), -50, "Očakávaný výsledok: -50")
        self.assertEqual(m.addition(-107557870,145454520), 37896650, "Očakávaný výsledok: 37 896 650")

    ## Test for addition 3
    # @test addition with positive decimal numbers
    # @param self creates a method 
    def test_addition_positive_decimal(self):
        self.assertEqual(m.addition(1.5, 7.125), 8.625, "Očakávaný výsledok: 8.625")
        self.assertAlmostEqual(m.addition(0.124578, 1454.15454525), 1454.27912325)
        self.assertEqual(m.addition(4545.545654564556455, 457.154564564564525), 5002.70021912912098, "Očakávaný výsledok: 5 002.70021912912098")
    
    ## Test for addition 4
    # @test addition with negative decimal numbers
    # @param self creates a method 
    def test_addition_negative_decimal(self):
        self.assertEqual(m.addition(-71.5, -227.125), -298.625, "Očakávaný výsledok: -298,625")
        self.assertEqual(m.addition(-45.78756456, 17.15454625), -28.63301831, "Očakávaný výsledok: -28,63301831")
        self.assertAlmostEqual(m.addition(75.5456456744564, -877.15454654654655425), -801.60890087209015425)

    ## Test for substraction 1
    # @test substraction with positive whole numbers
    # @param self creates a method 
    def test_substraction_positive_whole(self):
        self.assertEqual(m.substraction(25,30),-5, "Očakávaný výsledok: -5")
        self.assertEqual(m.substraction(250, 120),130 , "Očakávaný výsledok: 130")
        self.assertEqual(m.substraction(2700256, 250785121), -248084865, "Očakávaný výsledok:-248 084 865")

    ## Test for substraction 2
    # @test substraction with negative whole numbers
    # @param self creates a method 
    def test_substraction_negative_whole(self):
        self.assertEqual(m.substraction(-20,-50), 30, "Očakávaný výsledok: 30")
        self.assertEqual(m.substraction(120,-158), 278, "Očakávaný výsledok: 278")
        self.assertEqual(m.substraction(-7546467564540,-5546455450), -7540921109090, "Očakávaný výsledok: -7 540 921 109 090")

    ## Test for substraction 3
    # @test substraction with positive decimal numbers
    # @param self creates a method 
    def test_substraction_positive_decimal(self):
        self.assertEqual(m.substraction(1.5, 7.125), -5.625, "Očakávaný výsledok: -5,625")
        self.assertEqual(m.substraction(0.124578, 1454.15454525), -1454.02996725, "Očakávaný výsledok: -1454.02996725")
        self.assertEqual(m.substraction(4545.545654564556455, 457.154564564564525), 4088.39108999999193, "Očakávaný výsledok: 4 088,39108999999193")
    
    ## Test for substraction 4
    # @test substraction with negative decimal numbers
    # @param self creates a method
    def test_substraction_negative_decimal(self):
        self.assertEqual(m.substraction(-71.5, -227.125), 155.625, "Očakávaný výsledok: 155,625")
        self.assertEqual(m.substraction(-45.78756456, 17.15454625), -62.94211081, "Očakávaný výsledok: -62,94211081")
        self.assertEqual(m.substraction(75.5456456744564, -877.15454654654655425), 952.70019222100295425, "Očakávaný výsledok: 952,70019222100295425")

    ## Test for multiplication 1
    # @test multiplication with positive whole numbers
    # @param self creates a method 
    def test_multiplication_positive_whole(self):
        self.assertEqual(m.multiplication(8,5), 40, "Očakávaný výsledok: 40")
        self.assertEqual(m.multiplication(45468,0), 0, "Očakávaný výsledok: 40")
        self.assertEqual(m.multiplication(85456487456,55456465456), 4739114744594761319936, "Očakávaný výsledok: 4 739 114 744 594 761 319 936" )

    ## Test for multiplication 2
    # @test multiplication with negative whole numbers
    # @param self creates a method 
    def test_multiplication_negative_whole(self):
        self.assertEqual(m.multiplication(-80,-50), 4000, "Očakávaný výsledok: 4 000")
        self.assertEqual(m.multiplication(-45468,956), -43467408, "Očakávaný výsledok: -43 467 408")
        self.assertEqual(m.multiplication(875648953123,-231268753215645), -202510241643340984115209335, "Očakávaný výsledok: -202 510 241 643 340 984 115 209 335" )

    ## Test for multiplication 3
    # @test multiplication with positive decimal numbers
    # @param self creates a method 
    def test_multiplication_positive_decimal(self):
        self.assertAlmostEqual(m.multiplication(25.86,75.885), 1962.3861)
        self.assertAlmostEqual(m.multiplication(368752.896427,0.5487865), 202366.6113950358355)
        self.assertEqual(m.multiplication(8547456.4787554211348, 5545656.35788561321564),47401256365160.577082109313779873, "Očakávaný výsledok: 47 401 256 365 160.577082109313779873")

    ## Test for multiplication 4
    # @test multiplication with negative decimal numbers
    # @param self creates a method
    def test_multiplication_negative_decimal(self):
        self.assertEqual(m.multiplication(-67.215,-97.853), 6577.189395, "Očakávaný výsledok: 6 577,189395‬")
        self.assertEqual(m.multiplication(-81679.246795,95546.75213489), -7804186748.08637344017755, "Očakávaný výsledok: -7 804 186 748,08637344017755")
        self.assertAlmostEqual(m.multiplication(7.5452148784564,-2.74321548975465231), -20.698150328108862728653091494284)

    ## Test for division 1
    # @test division with positive whole numbers
    # @param self creates a method 
    def test_division_positive_whole(self):
        self.assertEqual(m.division(128,8),16,"Očakávaný výsledok: 16")
        self.assertEqual(m.division(6385008,248),25746,"Očakávaný výsledok: 25 746")
        self.assertEqual(m.division(12818713496123908905,546489789),23456455645,"Očakávaný výsledok: 23 456 455 645")

    ## Test for division 2
    # @test division with negative whole numbers
    # @param self creates a method 
    def test_division_negative_whole(self):
        self.assertEqual(m.division(-2718924,7813),-348,"Očakávaný výsledok: -348")
        self.assertEqual(m.division(-22333629857,-284639),78463,"Očakávaný výsledok: 78463")
        self.assertEqual(m.division(41036151960494831322,-523975123),-78316985214,"Očakávaný výsledok: -78 316 985 214")

    ## Test for division 3
    # @test division with zero
    # @param self creates a method
    def test_division_zero(self):
        self.assertEqual(m.division(1,0), None)

    ## Test for division 4
    # @test division with positive decimal numbers
    # @param self creates a method 
    def test_division_positive_decimal(self):
        self.assertAlmostEqual(m.division(8,128),0.0625)
        self.assertAlmostEqual(m.division(248.548794, 7008.24556448),0.0354651947785225618424561771414)
        self.assertAlmostEqual(m.division(12818713496123908905.5484564,546489789.31564),23456455631.452087845024528706421)

    ## Test for division 5
    # @test division with negative decimal numbers
    # @param self creates a method
    def test_division_negative_decimal(self):
        self.assertAlmostEqual(m.division(7813, -2718924) , -0.0028735632183908045977011494)
        self.assertAlmostEqual(m.division(-22329857.546546,-284639.65213),78.449567301844355300013)
        self.assertAlmostEqual(m.division(41.54584512318978795,-5.5648956321),-7.465700683322935297354)



        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_operations)
    unittest.TextTestRunner(verbosity=2).run(suite)