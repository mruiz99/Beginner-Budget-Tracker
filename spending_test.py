import unittest
from unittest.mock import patch
from test import Calculation, Graphs

import unittest
import matplotlib
from unittest.mock import patch
from test import Calculation, Graphs

class TestSpending(unittest.TestCase):
    """ Test the Calculation and Graph methods."""
    def setUp(self):
        """  Creates instances of Calculation and Graphs class for 
        testing purposes. 
        """
        self.calc1 = Calculation(50000.00)
        self.calc1.fixed_expenses = {'rent':650.00, 'car note':250.00, 
                                     'cellphone':90.00, 'car insurance':150.00,
                                     'health insurace':200.00, 'hulu':8.00,
                                     'netflix':8.00}
        self.calc1.var_expenses = {'gifts':150.00, 'gas bill':60.00, 'pepco':60.00,
                                   'water bill':30.00, 'nights out':300.00,
                                   'shopping':200.00, 'lunch':200.00}
        self.graph1 = Graphs()
        self.graph1.expense = {'rent':650.00, 'car note':250.00, 
                                     'cellphone':90.00, 'car insurance':150.00,
                                     'health insurace':200.00, 'hulu':8.00,
                                     'netflix':8.00, 'gifts':150.00, 
                                     'gas bill':60.00, 'pepco':60.00,
                                     'water bill':30.00, 'nights out':300.00,
                                     'shopping':200.00, 'lunch':200.00}
        self.calc2 = Calculation(25000.00)
        self.calc2.fixed_expenses = {'rent':500.00, 'school loans':200.00, 
                                     'cellphone':70.00, 'car note':300.00, 
                                     'car insurance':175.00, 
                                     'health insurance':50.00, 'amazon':8.00,
                                     'netflix':8.00, 'child support':400.00}
        self.calc2.var_expenses = {'gifts':350.00, 'gas bill':50.00, 
                                   'pepco':65.00, 'money lent for friend':200.00,
                                   'water bill':30.00, 'groceries':200.00, 
                                   'night out':150.00}
        self.graph2 = Graphs()
        self.graph2.expense = {'rent':500.00, 'school loans':200.00, 
                                     'cellphone':70.00, 'car note':300.00, 
                                     'car insurance':175.00, 
                                     'health insurance':50.00, 'amazon':8.00,
                                     'netflix':8.00, 'child support':400.00, 
                                     'gifts':350.00, 'gas bill':50.00, 
                                     'pepco':65.00, 'money lent for friend':200.00,
                                     'water bill':30.00, 'groceries':200.00, 
                                     'night out':150.00}

    def test_init(self):
        """ Test whether __init__() works as expected for both classes. 
        """
        self.assertEqual(self.calc1.total_income, 50000.00)
        self.assertEqual(self.calc1.fixed_expenses['rent'], 650.00)
        self.assertEqual(self.calc1.var_expenses['gifts'], 150.00)
        self.assertEqual(self.graph1.expense, {'rent':650.00, 'car note':250.00, 
                                     'cellphone':90.00, 'car insurance':150.00,
                                     'health insurace':200.00, 'hulu':8.00,
                                     'netflix':8.00, 'gifts':150.00, 
                                     'gas bill':60.00, 'pepco':60.00,
                                     'water bill':30.00, 'nights out':300.00,
                                     'shopping':200.00, 'lunch':200.00})
        self.assertEqual(self.calc2.total_income, 25000.00)
        self.assertEqual(self.calc2.fixed_expenses['school loans'], 200.00)
        self.assertEqual(self.calc2.var_expenses['pepco'], 65.00)
        self.assertEqual(self.graph2.expense, {'rent':500.00, 
                                     'school loans':200.00, 'cellphone':70.00, 
                                     'car note':300.00, 'car insurance':175.00, 
                                     'health insurance':50.00, 'amazon':8.00,
                                     'netflix':8.00, 'child support':400.00, 
                                     'gifts':350.00, 'gas bill':50.00, 
                                     'pepco':65.00, 'money lent for friend':200.00,
                                     'water bill':30.00, 'groceries':200.00, 
                                     'night out':150.00})

    def test_spendcheck(self):
      """ Test whether spend_check() correctly determines whether user is 
      overspending.
      """
      self.assertEqual(sum(self.calc1.fixed_expenses.values()), 1356.00)
      self.assertEqual(sum(self.calc1.var_expenses.values()), 1000.00)
      self.assertEqual(sum(self.calc2.fixed_expenses.values()), 1711.00)
      self.assertEqual(sum(self.calc2.var_expenses.values()), 1045.00)
      self.assertEqual(self.calc1.spend_check(), "Every month you are " + 
                       "spending $2356.0.  This is under your monthly " + 
                       "earnings of $4166.67")
      self.assertEqual(self.calc2.spend_check(), "Every month you are " +
                       "spending $2756.0.  This is $672.67 over your monthly " + 
                       "earnings of $2083.33")
      
    
    def test_interest(self):
        """  Test whether interest() works as expected.
        """
        calc1info = ["Bank loan", 10000.00, 1.85, 36, "SIMPLE"]
        calc2info = ["Student loan", 25000.00, 3.50, 120, "COMPOUND", "YEARLY"]
        
        R1 = calc1info[2]/100
        T1 = calc1info[3]/12
        
        R2 = calc2info[2]/100
        T2 = calc2info[3]/12
        
        simpleint = round(calc1info[1] * R1 * T1, 2)
        compoundint = round(calc2info[1] * (1 + R2/1)**(1*T2), 2)
        
        self.calc1.interest = ('Loan: ' + str(calc1info[0]) + ', ' + 
                               'Principal amount: $' + str(calc1info[1]) + 
                               ', ' + 'Rate: ' + str(calc1info[2]) + '%' + 
                               ', ' + 'Time: ' + str(calc1info[3]) + 
                               ' months' + ', ' +
                               'Simple Interest Loan' + ', ' + 
                               'Total interest paid is $' + 
                               str(round((calc1info[1] * R1 * T1), 2)))
        
        self.calc2.interest = ('Loan: ' + str(calc2info[0]) + ', ' + 
                               'Principal amount: $' + str(calc2info[1]) + 
                               ', ' + 'Rate: ' + str(calc2info[2]) + '%' + 
                               ', ' + 'Time: ' + str(calc2info[3]) + 
                               ' months' + ', ' +
                               'Compounded: Yearly' + ', ' + 
                               'Total interest paid is $' + 
                               str(round(compoundint - calc2info[1], 2)))

        self.assertIn(calc1info[0], self.calc1.interest)
        self.assertIn("Simple", self.calc1.interest)
        self.assertIn(str(calc1info[1]), self.calc1.interest)
        self.assertIn(str(calc1info[2]), self.calc1.interest)
        self.assertNotIn("Compounded", self.calc1.interest)
        self.assertNotIn("Monthly", self.calc1.interest)
        self.assertIn(calc2info[0], self.calc2.interest)
        self.assertIn(str(calc2info[1]), self.calc2.interest)
        self.assertIn(str(calc2info[2]), self.calc2.interest)
        self.assertIn("Compounded", self.calc2.interest)
        self.assertIn("Yearly", self.calc2.interest)
        self.assertNotIn("Simple", self.calc2.interest)
        self.assertAlmostEqual(simpleint, 555.00)
        self.assertAlmostEqual(compoundint - calc2info[1], 10264.97)
        
    def test_spendingallocation(self):
        """ Tests whether spending_allocation() is working as expected.
        """
        fixedcalc1 = sum(self.calc1.fixed_expenses.values())
        fixedcalc2 = sum(self.calc2.fixed_expenses.values())
        varcalc1 = sum(self.calc1.var_expenses.values())
        varcalc2 = sum(self.calc2.var_expenses.values())
        
        self.assertEqual(self.calc1.total_income, 50000.0)
        self.assertEqual(self.calc2.total_income, 25000.0)
        self.assertEqual(fixedcalc1, 1356.0)
        self.assertEqual(fixedcalc2, 1711.0)
        self.assertEqual(sum(self.calc1.fixed_expenses.values())/
                         self.calc1.total_income, 0.02712)
        self.assertEqual(sum(self.calc2.fixed_expenses.values())/
                         self.calc2.total_income, 0.06844)
        self.assertEqual(round((fixedcalc1/
                                self.calc1.total_income) * 100, 2), 2.71)
        self.assertEqual(round((fixedcalc2/
                                self.calc2.total_income) * 100, 2), 6.84)
        self.assertEqual(varcalc1, 1000.0)
        self.assertEqual(varcalc2, 1045.0)
        self.assertEqual(sum(self.calc1.var_expenses.values())/
                         self.calc1.total_income, 0.02)
        self.assertEqual(sum(self.calc2.var_expenses.values())/
                         self.calc2.total_income, 0.0418)
        self.assertEqual(round((varcalc1/self.calc1.total_income) * 100, 2), 2.0)
        self.assertEqual(round((varcalc2/self.calc2.total_income) * 100, 2), 4.18)
        
    def test_expenses(self):        
        """  Tests whether expenses() is working was expected.
        """
        self.assertEqual(self.graph1.expense['rent'], self.calc1.fixed_expenses['rent'],
                         "expenses() checks if the rent values are in the fixed dict")
        self.assertIn(self.graph1.expense['cellphone'], self.calc1.fixed_expenses.values(),
                      "expenses() checks if the cellphone value is in the fixed dict")
        self.assertIn(self.graph1.expense['water bill'], self.calc1.var_expenses.values(),
        "expenses() checks if the waterbill value is in the var dict)")
        self.assertEqual(self.graph2.expense['amazon'], self.calc2.fixed_expenses['amazon'],
                         "expenses() checks if the amazon value is in the fixed dict")
        self.assertIn(self.graph2.expense['car note'], self.calc2.fixed_expenses.values(),
                      "expenses() checks if the car note value is in the fixed dict")
        self.assertIn(self.graph2.expense['groceries'], self.calc2.var_expenses.values(),
                      "expenses() checks if the groceries value is in the var dict")
        self.assertEqual(sum(self.graph1.expense.values()), 
                         sum(self.calc1.fixed_expenses.values()) + 
                         sum(self.calc1.var_expenses.values()), "expenses() " + 
                         "checks if the sum of graph1.expenses is equal " + 
                         "to the sum of its corresponding calc1 fixed and " +
                         "var expenses")
        self.assertEqual(sum(self.graph2.expense.values()), 
                         sum(self.calc2.fixed_expenses.values()) + 
                         sum(self.calc2.var_expenses.values()), "expenses() " + 
                         "checks if the sum of graph2.expenses is equal " + 
                         "to the sum of its corresponding calc2 fixed and " +
                         "var expenses")
    
    def test_habits(self):
        
        graph1habits = self.graph1.input_habits
        graph2habits = self.graph2.input_habits
        
        graph1habits = {"uber eats": 70.00, "online shopping": 100.00, 
                                  "fast food": 50.00, "smoking": 90.00}
        graph2habits = {"smoking":50.00, "candy crush":150.00, 
                                   "alcohol":100.00, "MMORPGs":30.00}
        
        self.assertEqual(sum(graph1habits.values()), 310.00)
        self.assertEqual(sum(graph2habits.values()), 330.00)
        
        hab = []
        total = []
        lst = []
        saving = 0.0
        
        for k, v in graph2habits.items():
            hab.append(k)
            total.append(v)
            saving += v*12
            lst.append((k, v, v*12))
        
        self.assertEqual(round(graph1habits['uber eats'], 2), 70.00, "habits() " + 
                         "checks monthly spending per listed habit")
        self.assertEqual(round((graph1habits['online shopping']*12), 2), 1200.00, "habits() " + 
                         "checks yearly spending per listed habit")
        self.assertEqual(round(((graph1habits['fast food']*12)/
                         self.calc1.total_income*100), 2), 1.2, "habits() " + 
                         "checks spending percentage against total income " + 
                         "per listed habit")
        self.assertEqual(round(sum(graph1habits.values())*12, 2), 3720.00, 
                         "habits() checks how much the user is spending " + 
                         "every year on their habits.")
        self.assertEqual(round(graph2habits['smoking'], 2), 50.00, "habits() " + 
                         "checks monthly spending per listed habit")
        self.assertEqual(round(graph2habits['alcohol']*12, 2), 1200.00, "habits() " + 
                         "checks yearly spending per listed habit")
        self.assertEqual(round((graph2habits['MMORPGs']*12)/
                         self.calc2.total_income*100, 2), 1.44, "habits() " + 
                         "checks spending percentage against total income " + 
                         "per listed habit")
        self.assertEqual(round(sum(graph2habits.values())*12, 2), 3960.00, 
                         "habits() checks how much the user is spending " + 
                         "every year on their habits.")
        
if __name__ == '__main__':
    unittest.main()