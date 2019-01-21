import tkinter as tk
from tkinter import *
from tkinter import messagebox



from moneymanager import MoneyManager


window = Tk()
window.geometry("500x660") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("FedUni Money Manager")
window.title('FedUni Money Manager')
Label (window, text = "FedUni Money Manager", fg = "black", font= "none 28 bold") .grid(row = 0, sticky="w", padx= (40,10), pady=(15,15))
#The user number and associated variable

Label (window, text = "User Number/PIN", fg = "black", font= "none 14") .grid(row = 1, column = 0, sticky='W')
user_number_var = StringVar()
user_number_var.set('123456')
user_number_entry = Entry(window, textvariable=user_number_var, width = 27,  background = 'white') .grid(row = 1, column = 0, padx = 1, pady = 1)


#The pin number entry and associated variables
#Label (window, text = "PIN", fg = "black", font= "none 14") .grid(row = 1, column = , sticky='W')
pin_number_var = StringVar()
#This is set as a default for ease of testing
pin_number_var.set('7890')

#Modify the following to display a series of * rather than the pin ie **** not 1234
user_pin_entry = Entry(window, textvariable=pin_number_var, show="*",width = 27,  background = 'white') .grid(row = 1, column = 0, padx = 1, pady = 1, sticky='e')
#user_pin_entry.configure()


# The Entry widget to accept a numerical value to deposit or withdraw
#amount_var = tk.StringVar()
tkVar=StringVar(window)
amount_entry = tk.Entry(window)
entry_type=tk.Entry(window)
 
# The transaction text widget holds text of the transactions
transaction_text_widget = tk.Text(window, height=10, width=48)

# The money manager object we will work with
user = MoneyManager() 


################################### functions ######################################
# 'btn_click' function continuously updates the input field whenever you enters a number
def btn_click(item):
    global expression
    global expression1
    expression = expression + str(item)
    expression1 = expression1 + str(item)
   
    user_number_var.set(expression1)
    pin_number_var.set(expression)
    
# 'btn_clear' function clears the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# 'btn_equal' calculates the expression present in input field
def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval' function evalutes the string expression directly
    # you can also implement your own function to evalute the expression istead of 'eval' function
    input_text.set(result)
    expression = ""

expression = ""
expression1 = ""
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()




# creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(window, width = 500, height = 660, bg = "grey")
btns_frame.grid()




# second row
seven = Button(btns_frame, text = "7", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 23, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)


# third row
four = Button(btns_frame, text = "4", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 23, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)


# fourth row
one = Button(btns_frame, text = "1", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 23, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 24, height = 7, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)


# fourth row
cc = Button(btns_frame, text = "Cancel/Clear", fg = "black", width = 24, height = 7, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_clear()).grid(row = 4, column = 0,  padx = 1, pady = 1)
zero = Button(btns_frame, text = "0", fg = "black", width = 23, height = 7, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
equals = Button(btns_frame, text = "Log In", fg = "black", width = 24, height = 7, bd = 0, bg = "green", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 2, padx = 1, pady = 1)






window.mainloop()