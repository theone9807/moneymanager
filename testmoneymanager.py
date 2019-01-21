import unittest

from moneymanager import MoneyManager

class TestMoneyManager(unittest.TestCase):

    def setUp(self):
        # Create a test BankAccount object
        self.user = MoneyManager()

        # Provide it with some initial balance values        
        self.user.balance = 1000.0

    def test_legal_deposit_works(self):
        # Your code here to test that depsositing money using the account's
        # 'deposit_funds' function adds the amount to the balance.
        amount = 50.0
        expected = 1050.0
        actual = self.user.deposit_funds(self,amount)
        self.assertEqual(expected, actual, 'failed test for depost!')
    def test_illegal_deposit_raises_exception(self):
        # Your code here to test that depositing an illegal value (like 'bananas'
        # or such - something which is NOT a float) results in an exception being
        # raised.
        amount = 'bananas'
        expected = "Wrong input, Please provide correct input type!!!"
        actual = self.user.deposit_funds(amount)
        self.assertEqual(expected, actual, 'Exception R!!!')

    def test_legal_entry(self):
        # Your code here to test that adding a new entry with a a legal amount subtracts the
        # funds from the balance.
        entry = 'rent'
        amount = 50.0
        expected = 950.0
        actual = self.user.add_entry(self, amount, entry)
        self.assertEqual(expected, actual, "failed")
        

    def test_illegal_entry_amount(self):
        # Your code here to test that withdrawing an illegal amount (like 'bananas'
        # or such - something which is NOT a float) raises a suitable exception.
        amount = 'bananas'
        entry = 'rent'
        expected = "Wrong input, Please provide correct input type!!!"
        actual = MoneyManager.add_entry(self, amount, entry)
        self.assertEqual(expected, actual, "Error raised!!!")

        
    def test_illegal_entry_type(self):
        # Your code here to test that adding an illegal entry type (like 'bananas'
        # or such - something which is NOT a float) raises a suitable exception.
        amount = 50.0
        entry = 'bananas'
        expected = "Wrong input, Please provide correct input type!!!"
        actual = MoneyManager.add_entry(self, amount, entry)
        self.assertEqual(expected, actual, "Error raised!!!")

    def test_insufficient_funds_entry(self):
        # Your code here to test that you can only spend funds which are available.
        # For example, if you have a balance of 500.00 dollars then that is the maximum
        # that can be spent. If you tried to spend 600.00 then a suitable exception
        # should be raised and the withdrawal should NOT be applied to the user balance
        # or the user's transaction list.
        amount = 1100.0
        entry = 'rent'
        expected = "Wrong input, Please provide correct input type!!!"
        actual = MoneyManager.add_entry(self, amount, entry)
        self.assertEqual(expected, actual, "Insufficient Fund!!")

# Run the unit tests in the above test case
unittest.main()       
