#!/usr/bin/env python
# coding: utf-8
# Autor: Daniel Marek <xmarek72>

# Lincense: GNU GPL v.3 
# Whole licence can be found at https://www.gnu.org/licenses/gpl-3.0.html


import math_lib as m
import unittest

## @class Math library testing - basic operations
# @param unittest.TestCase makes individual unit for testing
class test_basic_operations(unittest.TestCase):
    
    ## Test for addition 1
    # @test addition with positive whole numbers
    # @param self creates a method 
    def test_addition_positive_whole(self):
        self.assertEqual(m.addition(25,30), 55, "Expected solution: 55")
        self.assertEqual(m.addition(120, 250), 370, "Expected solution: 370") 
        self.assertEqual(m.addition(2700256, 250785121), 253485377, "Expected solution: 253 485 377")

    ## Test for addition 2
    # @test addition with negative whole numbers
    # @param self creates a method 
    def test_addition_negative_whole(self):
        self.assertEqual(m.addition(-20,-50), -70, "Expected solution: -70")
        self.assertEqual(m.addition(70,-120), -50, "Expected solution: -50")
        self.assertEqual(m.addition(-107557870,145454520), 37896650, "Expected solution: 37 896 650")

    ## Test for addition 3
    # @test addition with positive decimal numbers
    # @param self creates a method 
    def test_addition_positive_decimal(self):
        self.assertEqual(m.addition(1.5, 7.125), 8.625, "Expected solution: 8.625")
        self.assertAlmostEqual(m.addition(0.124578, 1454.15454525), 1454.27912325)
        self.assertEqual(m.addition(4545.545654564556455, 457.154564564564525), 5002.70021912912098, "Expected solution: 5 002.70021912912098")
    
    ## Test for addition 4
    # @test addition with negative decimal numbers
    # @param self creates a method 
    def test_addition_negative_decimal(self):
        self.assertEqual(m.addition(-71.5, -227.125), -298.625, "Expected solution: -298,625")
        self.assertEqual(m.addition(-45.78756456, 17.15454625), -28.63301831, "Expected solution: -28,63301831")
        self.assertAlmostEqual(m.addition(75.5456456744564, -877.15454654654655425), -801.60890087209015425)

    ## Test for substraction 1
    # @test substraction with positive whole numbers
    # @param self creates a method 
    def test_substraction_positive_whole(self):
        self.assertEqual(m.substraction(25,30),-5, "Expected solution: -5")
        self.assertEqual(m.substraction(250, 120),130 , "Expected solution: 130")
        self.assertEqual(m.substraction(2700256, 250785121), -248084865, "Expected solution:-248 084 865")

    ## Test for substraction 2
    # @test substraction with negative whole numbers
    # @param self creates a method 
    def test_substraction_negative_whole(self):
        self.assertEqual(m.substraction(-20,-50), 30, "Expected solution: 30")
        self.assertEqual(m.substraction(120,-158), 278, "Expected solution: 278")
        self.assertEqual(m.substraction(-7546467564540,-5546455450), -7540921109090, "Expected solution: -7 540 921 109 090")

    ## Test for substraction 3
    # @test substraction with positive decimal numbers
    # @param self creates a method 
    def test_substraction_positive_decimal(self):
        self.assertEqual(m.substraction(1.5, 7.125), -5.625, "Expected solution: -5,625")
        self.assertEqual(m.substraction(0.124578, 1454.15454525), -1454.02996725, "Expected solution: -1454.02996725")
        self.assertEqual(m.substraction(4545.545654564556455, 457.154564564564525), 4088.39108999999193, "Expected solution: 4 088,39108999999193")
    
    ## Test for substraction 4
    # @test substraction with negative decimal numbers
    # @param self creates a method
    def test_substraction_negative_decimal(self):
        self.assertEqual(m.substraction(-71.5, -227.125), 155.625, "Expected solution: 155,625")
        self.assertEqual(m.substraction(-45.78756456, 17.15454625), -62.94211081, "Expected solution: -62,94211081")
        self.assertEqual(m.substraction(75.5456456744564, -877.15454654654655425), 952.70019222100295425, "Expected solution: 952,70019222100295425")

    ## Test for multiplication 1
    # @test multiplication with positive whole numbers
    # @param self creates a method 
    def test_multiplication_positive_whole(self):
        self.assertEqual(m.multiplication(8,5), 40, "Expected solution: 40")
        self.assertEqual(m.multiplication(45468,0), 0, "Expected solution: 40")
        self.assertEqual(m.multiplication(85456487456,55456465456), 4739114744594761319936, "Expected solution: 4 739 114 744 594 761 319 936" )

    ## Test for multiplication 2
    # @test multiplication with negative whole numbers
    # @param self creates a method 
    def test_multiplication_negative_whole(self):
        self.assertEqual(m.multiplication(-80,-50), 4000, "Expected solution: 4 000")
        self.assertEqual(m.multiplication(-45468,956), -43467408, "Expected solution: -43 467 408")
        self.assertEqual(m.multiplication(875648953123,-231268753215645), -202510241643340984115209335, "Expected solution: -202 510 241 643 340 984 115 209 335" )

    ## Test for multiplication 3
    # @test multiplication with positive decimal numbers
    # @param self creates a method 
    def test_multiplication_positive_decimal(self):
        self.assertAlmostEqual(m.multiplication(25.86,75.885), 1962.3861)
        self.assertAlmostEqual(m.multiplication(368752.896427,0.5487865), 202366.6113950358355)
        self.assertEqual(m.multiplication(8547456.4787554211348, 5545656.35788561321564),47401256365160.577082109313779873, "Expected solution: 47 401 256 365 160.577082109313779873")

    ## Test for multiplication 4
    # @test multiplication with negative decimal numbers
    # @param self creates a method
    def test_multiplication_negative_decimal(self):
        self.assertEqual(m.multiplication(-67.215,-97.853), 6577.189395, "Expected solution: 6 577,189395‬")
        self.assertEqual(m.multiplication(-81679.246795,95546.75213489), -7804186748.08637344017755, "Expected solution: -7 804 186 748,08637344017755")
        self.assertAlmostEqual(m.multiplication(7.5452148784564,-2.74321548975465231), -20.698150328108862728653091494284)

    ## Test for division 1
    # @test division with positive whole numbers
    # @param self creates a method 
    def test_division_positive_whole(self):
        self.assertEqual(m.division(128,8),16,"Expected solution: 16")
        self.assertEqual(m.division(6385008,248),25746,"Expected solution: 25 746")
        self.assertEqual(m.division(12818713496123908905,546489789),23456455645,"Expected solution: 23 456 455 645")

    ## Test for division 2
    # @test division with negative whole numbers
    # @param self creates a method 
    def test_division_negative_whole(self):
        self.assertEqual(m.division(-2718924,7813),-348,"Expected solution: -348")
        self.assertEqual(m.division(-22333629857,-284639),78463,"Expected solution: 78463")
        self.assertEqual(m.division(41036151960494831322,-523975123),-78316985214,"Expected solution: -78 316 985 214")

    ## Test for division 3
    # @test division with zero
    # @param self creates a method
    def test_division_zero(self):
        self.assertEqual(m.division(1,0), None, "Expected solution: None -> Can't divide with zero")
        self.assertEqual(m.division(-8,0), None, "Expected solution: None -> Can't divide with zero")

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



## @class Math library testing - advanced operations
# @param unittest.TestCase makes individual unit for testing
class test_advanced_operations(unittest.TestCase):

    ## Test for factorial 1
    # @test factorial with correct numbers
    # @param self creates a method
    def test_factorial_correct(self):
        self.assertEqual(m.factorial(5),120 , "Expected solution: 120")
        self.assertEqual(m.factorial(12),479001600, "Expected solution: 479 001 600" )
        self.assertEqual(m.factorial(20), 2432902008176640000, "Expected solution: 2 432 902 008 176 640 000" )
        self.assertEqual(m.factorial(0), 1, "Expected solution: 1")
        self.assertEqual(m.factorial(29), 8841761993739701954543616000000, "Expected solution: 8 841 761 993 739 701 954 543 616 000 000‬")

    ## Test for factorial 2
    # @test factorial with incorrect numbers (negative and decimal numbers)
    # @param self creates a method
    def test_factorial_incorrect(self):
        self.assertEqual(m.factorial(-1), None, "Expected solution: None -> Can't do factorial with negative number")
        self.assertEqual(m.factorial(1.5), None, "Expected solution: None -> Can't do factorial with decimal number")
        self.assertEqual(m.factorial(-10), None, "Expected solution: None -> Can't do factorial with negative number")

    ## Test for exponencial 1
    # @test exponencial with incorrect exponent (negative and decimal exponent + 0^0)
    # @param self creates a method
    def test_exponencial_incorrect(self):
        self.assertEqual(m.exponencial(12,0.5), None, "Expected solution: None -> Function works only with natural exponents")
        self.assertEqual(m.exponencial(0,0), None, "Expected solution: None -> It is undefined")
        self.assertEqual(m.exponencial(2,-2), None, "Expected solution: None -> Function works only with natural exponents")

    ## Test for exponencial 2
    # @test exponencial with correct exponent and positive whole numbers
    # @param self creates a method
    def test_exponencial_correct_positive_whole(self):
        self.assertEqual(m.exponencial(12,5), 248832, "Expected solution: 248 832")
        self.assertEqual(m.exponencial(1,2000), 1, "Expected solution: 1")
        self.assertEqual(m.exponencial(12456879875646546545123,0), 1, "Expected solution: 1")

    ## Test for exponencial 3
    # @test exponencial with with correct exponent and negative whole numbers
    # @param self creates a method
    def test_exponencial_correct_negative_whole(self):
        self.assertEqual(m.exponencial(-5, 4), 625,  "Expected solution: 625")
        self.assertEqual(m.exponencial(-127, 5), -33038369407,  "Expected solution: -33 038 369 407")
        self.assertEqual(m.exponencial(-79135546879875646, 0), 1,  "Expected solution: 1")

    ## Test for exponencial 4
    # @test exponencial with with correct exponent and positive decimal numbers
    # @param self creates a method
    def test_exponencial_correct_positive_decimal(self):
        self.assertAlmostEqual(m.exponencial(45.78512, 4), 4394378.155480441923306127)
        self.assertAlmostEqual(m.exponencial(5.7854545612, 7), 216951.37601471197541142619333761)
        self.assertAlmostEqual(m.exponencial(1.54878465465465, 12), 190.498887598528009755207019)

    ## Test for exponencial 5
    # @test exponencial with correct exponent and negative decimal numbers
    # @param self creates a method
    def test_exponencial_correct_negative_decimal(self):
        self.assertAlmostEqual(m.exponencial(-18.4896,6), 39954444.3220161036302421023)
        self.assertAlmostEqual(m.exponencial(-8.1236,5), -35378.7638681105623096)
        self.assertAlmostEqual(m.exponencial(1.57896325,60), 798585317979.60359157739249626795)


    ## Test for root 1
    # @test root with incorrect options (positive root of negative number, 0 root of number, negative root of 0)
    # @param self creates a method
    def test_root_incorect(self):
        self.assertEqual(m.root(-5, 2), None, "Expected solution: None -> Can't do even root of a negative number" )
        self.assertEqual(m.root(17, 0), None, "Expected solution: None -> Can't do zero root of a number" )
        self.assertEqual(m.root(0, -8), None, "Expected solution: None -> Can't do root of a zero" )
        self.assertEqual(m.root(-53, -8), None, "Expected solution: None -> Can't do even negative root of a negative number" )
        self.assertEqual(m.root(-127, 5.52), None, "Expected solution: None -> Can't do decimal even root of a negative number" )

    ## Test for root 2
    # @test root with positive whole numbers
    # @param self creates a method
    def test_root_correct_positive_whole(self):
        self.assertEqual(m.root(601692057,5), 57, "Expected solution: 57")
        self.assertEqual(m.root(16777216,8), 8, "Expected solution: 8")
        self.assertEqual(m.root(2090278243656, 3), 12786, "Expected solution: 102 786")

    ## Test for root 3
    # @test root with with negative whole numbers
    # @param self creates a method
    def test_root_correct_negative_whole(self):
        self.assertEqual(m.root(-10460353203,7), -27, "Expected solution: -27")
        self.assertEqual(m.root(-46411484401953,9), -33, "Expected solution: -33")
        self.assertEqual(m.root(-94143178827 ,23), -3, "Expected solution: -3")

    ## Test for root 4
    # @test root with positive decimal numbers
    # @param self creates a method
    def test_root_correct_positive_decimal(self):
        self.assertAlmostEqual(m.root(2,2), 1.41421356237309504880168872420 )
        self.assertAlmostEqual(m.root(428.56489,12), 1,657046576)
        self.assertAlmostEqual(m.root(2090278243656, 5.58564), 160.5803766)

    ## Test for root 5
    # @test root with negative decimal numbers
    # @param self creates a method
    def test_root_correct_negative_decimal(self):
        self.assertAlmostEqual(m.root(-22,-5), -0.5389090339 )
        self.assertAlmostEqual(m.root(428.56489,-12), 0.6034833386)
        self.assertAlmostEqual(m.root(-2090278243656.45878, 5.51), 172.17564)

    ## Test for modulo 1
    # @test modulo with positive numbers
    # @param self creates a method
    def test_modulo_positive(self):
        self.assertEqual(m.modulo(128,79),49, "Expected solution: 49")
        self.assertEqual(m.modulo(54615628,78989),34229, "Expected solution: 34 229")
        self.assertEqual(m.modulo(879754665432184789,545645132),350789181, "Expected solution: 350 789 181")

    ## Test for modulo 2
    # @test modulo with negative numbers
    # @param self creates a method
    def test_modulo_negative(self):
        self.assertEqual(m.modulo(-259,-28),-7, "Expected solution: -7")
        self.assertEqual(m.modulo(-54615628,78989),-34229, "Expected solution: -34 229")
        self.assertEqual(m.modulo(45623125432184789,-4541221132),1637930181 ,"Expected solution: 1 637 930 181‬")

    ## Test for neg 
    # @test neg with multiple different numbers
    # @param self creates a method
    def test_neg(self):
        self.assertEqual(m.neg(-2590), 2590, "Expected solution: 2590")
        self.assertEqual(m.neg(698798.987564), -698798.987564, "Expected solution: 698 798,987564")
        self.assertEqual(m.neg(0), 0, "Expected solution: 2590")

    ## Test for inverse 
    # @test inverse with multiple different numbers
    # @param self creates a method
    def test_inverse(self):
        self.assertEqual(m.inverse(0), None, "Expected solution: None -> Can't divide with 0" )
        self.assertEqual(m.inverse(1), 1, "Expected solution: 1" )
        self.assertAlmostEqual(m.inverse(-269), -0.00371747211895910780669)
        self.assertAlmostEqual(m.inverse(0.4564548987), 2.190796950252995499290059)
        self.assertAlmostEqual(m.inverse(-98.546454213), -0.0101474985374773892068944)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_basic_operations)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite2 = unittest.TestLoader().loadTestsFromTestCase(test_advanced_operations)
    unittest.TextTestRunner(verbosity=2).run(suite2)
