import tkinter as tk
from tkinter import *
from tkinter import messagebox

from pylab import plot, show, xlabel, ylabel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from collections import defaultdict
from pprint import pprint
import matplotlib.pyplot as plt

from moneymanager import MoneyManager

win = tk.Tk()

#Set window size here to '540 x 640'
win.geometry("540x640")
win.resizable(False, False)
#Set the window title to 'FedUni Money Manager'
win.title('FedUni Money Manager')
#The user number and associated variable
user_number_var = tk.StringVar()

#This is set as a default for ease of testing
user_number_var.set('123456')
user_number_entry = tk.Entry(win, textvariable=user_number_var)
user_number_entry.focus_set()

#The pin number entry and associated variables
pin_number_var = tk.StringVar()
#This is set as a default for ease of testing
pin_number_var.set('7890')

#Modify the following to display a series of * rather than the pin ie **** not 1234
user_pin_entry = tk.Entry(win, text='PIN Number', textvariable=pin_number_var)
user_pin_entry.config(show="*")
#set the user file by default to an empty string
user_file = ''

# The balance label and associated variable
balance_var = tk.StringVar()
balance_var.set('Balance: $0.00')
balance_label = tk.Label(win, textvariable=balance_var)

# The Entry widget to accept a numerical value to deposit or withdraw
#amount_var = tk.StringVar()
tkVar=StringVar(win)
amount_entry = tk.Entry(win)
entry_type=tk.Entry(win)

# The transaction text widget holds text of the transactions
transaction_text_widget = tk.Text(win, height=10, width=48)

# The money manager object we will work with
user = MoneyManager()

# ---------- Button Handlers for Login Screen ----------

def clear_pin_entry(event):
    '''Function to clear the PIN number entry when the Clear / Cancel button is clicked.'''    
    # Clear the pin number entry here
    if event == "Clear" or event == "Cancel":
        user_pin_entry.delete(0, end)

    
def handle_pin_button(event):
    '''Function to add the number of the button clicked to the PIN number entry.'''    
    # Limit to 4 chars in length

    # Set the new pin number on the pin_number_var

def log_in(event):
    '''Function to log in to the banking system using a known user number and PIN.'''
    global user
    global pin_number_var
    global user_file
    global user_num_entry

    # Create the filename from the entered account number with '.txt' on the end

    # Try to open the account file for reading
    
        # Open the account file for reading

        # First line is account number

        # Second line is PIN number, raise exceptionk if the PIN entered doesn't match account PIN read 

        # Read third and fourth lines (balance and interest rate) 
        
        # Section to read account transactions from file - start an infinite 'do-while' loop here

            # Attempt to read a line from the account file, break if we've hit the end of the file. If we
            # read a line then it's the transaction type, so read the next line which will be the transaction amount.
            # and then create a tuple from both lines and add it to the account's transaction_list            

        # Close the file now we're finished with it
        
    # Catch exception if we couldn't open the file or PIN entered did not match account PIN
    
        # Show error messagebox and & reset BankAccount object to default...

        #  ...also clear PIN entry and change focus to account number entry

    # Got here without raising an exception? Then we can log in - so remove the widgets and display the account screen

# ---------- Button Handlers for User Screen ----------

def save_and_log_out():
    '''Function  to overwrite the user file with the current state of
       the user object (i.e. including any new transactions), remove
       all widgets and display the login screen.'''
    global user

    # Save the account with any new transactions
    
    # Reset the bank acount object

    # Reset the account number and pin to blank

    # Remove all widgets and display the login screen again

def perform_deposit():
    '''Function to add a deposit for the amount in the amount entry to the
       user's transaction list.'''
    global user    
    global amount_entry
    global balance_label
    global balance_var


    # Try to increase the account balance and append the deposit to the account file
    
        # Get the cash amount to deposit. Note: We check legality inside account's deposit method

        # Deposit funds
        
        # Update the transaction widget with the new transaction by calling account.get_transaction_string()
        # Note: Configure the text widget to be state='normal' first, then delete contents, then instert new
        #       contents, and finally configure back to state='disabled' so it cannot be user edited.

        # Change the balance label to reflect the new balance

        # Clear the amount entry

        # Update the interest graph with our new balance

    # Catch and display exception as a 'showerror' messagebox with a title of 'Transaction Error' and the text of the exception

def perform_transaction():
    '''Function to add the entry the amount in the amount entry from the user balance and add an entry to the transaction list.'''
    global user    
    global amount_entry
    global balance_label
    global balance_var
    global entry_type

    # Try to decrease the account balance and append the deposit to the account file
    
        # Get the cash amount to use. Note: We check legality inside account's withdraw_funds method

        # Get the type of entry that will be added ie rent etc
        
        # Withdraw funds from the balance      

        # Update the transaction widget with the new transaction by calling user.get_transaction_string()
        # Note: Configure the text widget to be state='normal' first, then delete contents, then instert new
        #       contents, and finally configure back to state='disabled' so it cannot be user edited.

        # Change the balance label to reflect the new balance

        # Clear the amount entry

        # Update the graph

    # Catch and display any returned exception as a messagebox 'showerror'

def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''
    global win
    for widget in win.winfo_children():
        widget.grid_remove()

def read_line_from_user_file():
    '''Function to read a line from the users file but not the last newline character.
       Note: The user_file must be open to read from for this function to succeed.'''
    global user_file
    return user_file.readline()[0:-1]

def plot_spending_graph():
    '''Function to plot the user spending here.'''
    # YOUR CODE to generate the x and y lists here which will be plotted


    #Your code to display the graph on the screen here - do this last



    
# ---------- UI Drawing Functions ----------

def create_login_screen():
    '''Function to create the login screen.'''    
    

    # ----- Row 0 -----

    # 'FedUni Money Manager' label here. Font size is 28.
    


    # ----- Row 1 -----

    # Acount Number / Pin label here

    # Account number entry here

    # Account pin entry here
    
 

    # ----- Row 2 -----

    # Buttons 1, 2 and 3 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    

    # ----- Row 3 -----

    # Buttons 4, 5 and 6 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    

    # ----- Row 4 -----

    # Buttons 7, 8 and 9 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    

    # ----- Row 5 -----

    # Cancel/Clear button here. 'bg' and 'activebackground' should be 'red'. But calls 'clear_pin_entry' function.
    
    # Button 0 here

    # Login button here. 'bg' and 'activebackground' should be 'green'). Button calls 'log_in' function.


    # ----- Set column & row weights -----

    # Set column and row weights. There are 5 columns and 6 rows (0..4 and 0..5 respectively)


def create_user_screen():
    '''Function to create the user screen.'''
    global amount_text
    global amount_label
    global transaction_text_widget
    global balance_var
    
    # ----- Row 0 -----

    # FedUni Banking label here. Font size should be 24.
    

    # ----- Row 1 -----

    # Account number label here

    # Balance label here

    # Log out button here


    # ----- Row 2 -----

    # Amount label here

    # Amount entry here

    # Deposit button here

    # NOTE: Bind Deposit and Withdraw buttons via the command attribute to the relevant deposit and withdraw
    #       functions in this file. If we "BIND" these buttons then the button being pressed keeps looking as
    #       if it is still pressed if an exception is raised during the deposit or withdraw operation, which is
    #       offputting.
    
    
    # ----- Row 3 -----
    # Entry type label here

    # Entry drop list here

    # Add entry button here

    
    # ----- Row 4 -----

    # Declare scrollbar (text_scrollbar) here (BEFORE transaction text widget)
    
    # Add transaction Text widget and configure to be in 'disabled' mode so it cannot be edited.
    # Note: Set the yscrollcommand to be 'text_scrollbar.set' here so that it actually scrolls the Text widget
    # Note: When updating the transaction text widget it must be set back to 'normal mode' (i.e. state='normal') for it to be edited

    # Now add the scrollbar and set it to change with the yview of the text widget


    # ----- Row 5 - Graph -----

    # Call plot_interest_graph() here to display the graph
    

    # ----- Set column & row weights -----

    # Set column and row weights here - there are 6 rows and 5 columns (numbered 0 through 4 not 1 through 5!)




# ---------- Display Login Screen & Start Main loop ----------

create_login_screen()
win.mainloop()
