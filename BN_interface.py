from tkinter import *
import tkinter as tk
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MmhcEstimator
from pgmpy.estimators import HillClimbSearch, BDeuScore
from pgmpy.estimators import ExhaustiveSearch, BayesianEstimator
from pgmpy.models import BayesianModel, BayesianNetwork
from pgmpy.estimators import ParameterEstimator
import pandas as pd
import sys


# network
df = pd.read_csv('BBN_data.csv', dtype={'mood':'string'}) # impo str and not float for Variable Elimination
df = df.drop(["Unnamed: 0"], axis=1)
# model = BayesianNetwork([('Num_of_people', 'time'), ('mood', 'Num_of_people'), ('mood', 'place'), ('mood', 'time'),
#                          ('place', 'Num_of_people'), ('place', 'time'), ('what', 'Num_of_people'), ('what', 'mood'),
#                          ('what', 'place'), ('what', 'time')])
model = BayesianNetwork([('Num_of_people', 'mood'), ('Num_of_people', 'place'), ('place', 'mood'), 
                         ('time', 'Num_of_people'), ('time', 'mood'), ('time', 'place'), ('what', 'Num_of_people'), 
                         ('what', 'mood'), ('what', 'place'), ('what', 'time')])
model.fit(df, estimator=BayesianEstimator, prior_type="BDeu", equivalent_sample_size=10)


def start_gui():
    # tkinter app
    OptionListTime = [ "-",
    "Morning",
    "Afternoon",
    "Evening/Night"
    ] 

    OptionListMood = [ "-",
        "2.0",
        "3.0",
        "4.0"
    ]

    OptionListPpl = [ "-",
        '0',
        '1 - 3',
        '>= 4'
    ]

    OptionListPlace = [ "-",
        'Supermarket', 'Home', 'Outdoor', 'University', 'Shops',
        'Restaurant', 'Bar', 'Relatives Home'
    ]

    OptionListActivity = [ "-",
        'Shopping and Household', 'Breaks', 'Study/Lectures',
        'Free time/hobbies', 'Social activities', 'Physical activities',
        'Others'
    ]

    def getEvidence(variable):
        #print(ev)
        ev = variable.get()


    app = tk.Tk()

    app.title('BN interface')

    app.geometry('500x700')
    app.resizable(0, 0)
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1) # app.grid_rowconfigure(6, weight=1)

    labelText = tk.Label(text="Select evidence for time, mood, people and/or location", font=('Helvetica', 12), fg='red')
    labelText.grid(column=0, row=0, columnspan=3, ipadx=5, ipady=5, sticky="NSEW")


    # insert evidence
    # 1st drop down menu --> evidence on time
    var = tk.StringVar(app)
    var.set(OptionListTime[0])

    #lab = Label(app, text = "Time").place(x = 40, y = 300) 
    
    opt = tk.OptionMenu(app, var, *OptionListTime, command=getEvidence(var))
    opt.config(width=90, font=('Helvetica', 12))
    opt.grid(row = 1, columnspan=3, ipady = 5, pady = 5, padx = 5)


    # 2nd drop down menu --> evidence on mood
    var2 = tk.StringVar(app)
    var2.set(OptionListMood[0])

    opt2 = tk.OptionMenu(app, var2, *OptionListMood, command=getEvidence(var2))
    opt2.config(width=90, font=('Helvetica', 12))
    opt2.grid(row = 2, columnspan=3, ipady = 5, pady = 5, padx = 5)

    # 3nd drop down menu --> evidence on people
    var3 = tk.StringVar(app)
    var3.set(OptionListPpl[0])

    opt3 = tk.OptionMenu(app, var3, *OptionListPpl, command=getEvidence(var3))
    opt3.config(width=90, font=('Helvetica', 12))
    opt3.grid(row = 3, columnspan=3, ipady = 5, pady = 5, padx = 5)

    # 4th drop down menu --> evidence on location
    var4 = tk.StringVar(app)
    var4.set(OptionListPlace[0])

    opt4 = tk.OptionMenu(app, var4, *OptionListPlace, command=getEvidence(var4))
    opt4.config(width=90, font=('Helvetica', 12))
    opt4.grid(row = 4, columnspan=3, ipady = 5, pady = 5, padx = 5)



    # list with all elements to delete when resetting
    buttons = []


    def callback():
        print('Outputing probabilities...')
        # prob. given evidence
        d = {}
        infer = VariableElimination(model)
        if var.get() != '-':
            d['time'] = str(var.get())
        if var2.get() != '-':
            d['mood'] = str(var2.get())
        if var3.get() != '-':
            d['Num_of_people'] = str(var3.get())
        if var4.get() != '-':
            d['place'] = str(var4.get())
        
        # Create label
        inference = Label(app, text=str(infer.query(['what'], evidence=d)))
        inference.config(font=("Courier", 14))
        #print("Showing all the CPD's one by one")
        #for i in model.get_cpds():
        #    print(i)
        
        buttons.append(inference)
        inference.grid(columnspan=3, ipady = 5, pady = 5, padx = 5)



    '''
    def restart_program(): 
        import os
        python = sys.executable
        os.execl(python, python, * sys.argv)
    '''

    # pass evidence & hide submit botton
    def callback_and_hide(button):
        callback()
        button.grid_forget()

    # method to make widget visible
    def retrieve(widget, buttons):
        # delete previous output
        for btn in buttons:
            btn.destroy()
        # show again submit botton
        widget.grid(row = 5, column = 0, ipady = 10, pady = 10, padx = 5, sticky="NSEW")

    # submit botton
    b_sub = Button(app, text="Submit", width=10, command=lambda: callback_and_hide(b_sub))
    b_sub.grid(row = 5, column = 0, ipady = 10, pady = 10, padx = 5, sticky="NSEW")
    
    # quit app botton
    b_exit = Button(app, text='   Exit   ', command=app.quit)
    b_exit.grid(row = 5, column = 2, ipady = 10, pady = 10, padx = 5)

    # command retrieve() method is passed to delete evidence and make
    # submit botton appear again
    b3 = Button(app, text = "  Reset evidence  ", command = lambda : retrieve(b_sub, buttons))
    b3.grid(row = 5, column = 1, ipady = 10, pady = 10, padx = 5)


    app.mainloop()



if __name__ == "__main__":
    start_gui()