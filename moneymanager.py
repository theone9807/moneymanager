class MoneyManager():
    user_number = '0'
    pin_number = ''
    balance = 0.0
    entry_type = ''
    transaction_list = []


    def __init__(self):
        '''Constructor to set username to '', pin_number to an empty string,
        balance to 0.0, and transaction_list to an empty list.'''
        self.user_number = '0'
        self.pin_number = ''
        self.balance = 0.0
        self.transaction_list = []
        
    def add_entry(self, amount, entry_type):
        '''Function to add and entry an amount to the tool. Raises an
        exception if it receives a value for amount that cannot be cast to float. Raises an exception
        if the entry_type is not valid - i.e. not food, rent, bills, entertainment or other'''
        try:
            amount_to_entry_type = float(amount)
            if(amount_to_entry_type > self.balance):
                raise Exception('The entry_type is not valid')
                self.balance = float(self.balance) - amount_to_entry_type   
                transaction = ('Withdrawal',amount_to_entry_type)
                self.transaction_list.append(transaction)
                #print(self.balance)
        except Exception as error:
            print(repr(error))
      
    

    def deposit_funds(self, amount):
        '''Function to deposit an amount to the user balance. Raises an
        exception if it receives a value that cannot be cast to float. '''
        try:
            amount_to_deposit = float(amount)
            self.balance = float(self.balance) + amount_to_deposit
            transaction = ('Deposit',amount_to_deposit)
            self.transaction_list.append(transaction)
            #print(self.balance)
        except Exception as error:
            print(repr(error))

      
    def get_transaction_string(self):
        '''Function to create and return a string of the transaction list. Each transaction
        consists of two lines - either the word "Deposit" or the entry type - food etc - on
        the first line, and then the amount deposited or entry amount on the next line.'''
        #transaction = self.transaction_list[-1]
        transaction = self.transaction_list
        transaction_string = ''
        for index, t in enumerate(self.transaction_list):
            transaction_string = transaction_string + str(t[0])+'\n'+str(t[1])+'\n'
        return transaction_string

    def save_to_file(self):
        '''Function to overwrite the user text file with the current user
        details. user number, pin number, and balance (in that
        precise order) are the first four lines - there are then two lines
        per transaction as outlined in the above 'get_transaction_string'
        function.'''

        file = open(str(BankAccount.account_number) +'.txt',"w")

        file.write(BankAccount.account_number + '\n')

        file.write(BankAccount.pin_number + '\n')

        file.write(str(BankAccount.balance) + '\n')

        file.write(str(BankAccount.interest_rate) + '\n')

        for a in BankAccount.transaction_list:

            file.write(str(a[0]) + '\n')

            file.write(str(a[1]) + '\n')

        file.close()
    



