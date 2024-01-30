import PySimpleGUI as sg
import sqlite3
import os

class Not_Cookie_clicker():

    def __init__(self):
        if os.path.exists('dbase.db'):
            file = 'dbase.db'
            self.connection = sqlite3.connect(file)
            self.cursor = self.connection.cursor()
            query = "select * from upgrades where id=1"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            print(result)
            x = result[0]
            x = list(x)
            print(x)
            self.p_money_per_click = x[1]
            self.p_currency = x[2]
            self.p_clicker = x[3]
            self.p_grandma = x[4]
            self.p_farm = x[5]
            self.p_upgradelist = {'clicker': self.p_clicker,'grandma': self.p_grandma,'farm': self.p_farm}
            self.more_than_one_run()
        else:
            file = 'dbase.db'
            self.connection = sqlite3.connect(file)
            self.cursor = self.connection.cursor()
            query = """
            create table if not exists upgrades (
                id integer primary key autoincrement,
                money_per_click int,
                currency int,
                clicker int,
                grandma int,
                farm int);
            """
            self.cursor.execute(query)
            self.money_per_click = 1
            self.currency = 0
            self.upgradelist = {"clicker": 0,"grandma": 0,"farm": 0}
            query = f"insert into upgrades (money_per_click,currency,clicker,grandma,farm) values ('{self.money_per_click}','{self.currency}','{self.upgradelist['clicker']}','{self.upgradelist['grandma']}','{self.upgradelist['farm']}')"
            self.cursor.execute(query)
            self.main()
        #sajaslfjaslkfasfssa
        
        

    def main(self):
        sg.theme('DarkAmber')
        
        col_layoutright = [ 
            [sg.Text('Clicker'),sg.Button('add 1 for $10',key = 'purchase_a'),sg.Button('add 10 for $100',key = 'purchase_b'),sg.Button('add 100 for $1000',key = 'purchase_c')],
            [sg.Text('Grandma'),sg.Button('add 1 for $20',key = 'purchase_d'),sg.Button('add 10 for $200',key = 'purchase_e'),sg.Button('add 100 for $2000',key = 'purchase_f')],
            [sg.Text('Farm'),sg.Button('add 1 for $30',key = 'purchase_g'),sg.Button('add 10 for $300',key = 'purchase_h'),sg.Button('add 100 for $3000',key = 'purchase_i')]
        ]
        #dictname[keyname] = value
        col_layoutleft = [
            [sg.Button('go',size = (30,3), visible= True,key = 'clicked')]
        ]
        combo_layout = [
            [sg.Column(col_layoutleft,element_justification='left')],
            [sg.Column(col_layoutright,element_justification='right')]
        ]
        progress_layout = [
            [sg.Text('buy the first clicker upgrade to start the file')],
            [sg.Text(f'{self.upgradelist}',key='upgrades')],
            [sg.Text('money per click')],[sg.Text(self.money_per_click,key = 'incvalue')],
            [sg.Text('currency')],[sg.Text(self.currency,key = 'money_gained')]
        ]
        main_layout = [
            [sg.Text('welcome to not Cookie clicker')],
            [sg.Column(progress_layout,element_justification='right')],
            [sg.Column(combo_layout,element_justification='left')]
        ]
        win  = sg.Window('not cookie clicker',main_layout,element_justification='center')

        while True:
            e,v = win.read()
            if e == sg.WIN_CLOSED:
                break
            elif e == 'clicked':
                
                self.currency+= self.money_per_click
                win['money_gained'].update(self.currency)
                query = f"update upgrades set (currency) = ('{self.currency}') where id=1"
                self.cursor.execute(query)
                #dictname[keyname] = value
            elif e == 'purchase_a':
                if self.currency >= 10:
                    self.currency -= 10
                    self.money_per_click += 1
                    self.upgradelist['clicker'] += 1
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    query = f"update upgrades set (clicker,money_per_click,currency) = ({self.upgradelist['clicker']},{self.money_per_click},{self.currency}) where id=1"
                    #this is the good code -- query = f"update upgrades set (clicker,money_per_click,currency) = ({self.upgradelist['clicker']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_b':
                if self.currency >= 100:
                    self.currency -= 100
                    self.money_per_click += 10
                    self.upgradelist['clicker'] += 10
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    #query = f"update upgrades set clicker = {self.upgradelist['clicker']}, money_per_click = {self.money_per_click}, currency = {self.currency} where id=1"
                    query = f"update upgrades set (clicker,money_per_click,currency) = ({self.upgradelist['clicker']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_c':
                if self.currency >= 1000:
                    self.currency -= 1000
                    self.money_per_click += 100
                    self.upgradelist['clicker'] += 100
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    query = f"update upgrades set (clicker,money_per_click,currency) = ({self.upgradelist['clicker']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_d':
                if self.currency >= 20:
                    self.currency -= 20
                    self.money_per_click += 2
                    self.upgradelist['grandma'] += 1
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    query = f"update upgrades set (grandma,money_per_click,currency) = ({self.upgradelist['grandma']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_e':
                if self.currency >= 200:
                    self.currency -= 200
                    self.money_per_click += 20
                    self.upgradelist['grandma'] += 10
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    query = f"update upgrades set (grandma,money_per_click,currency) = ({self.upgradelist['grandma']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_f':
                if self.currency >= 2000:
                    self.currency -= 2000
                    self.money_per_click += 200
                    self.upgradelist['grandma'] += 100
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    query = f"update upgrades set (grandma,money_per_click,currency) = ({self.upgradelist['grandma']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_g':
                if self.currency >= 30:
                    self.currency -= 30
                    self.money_per_click += 3
                    self.upgradelist['farm'] += 1
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    query = f"update upgrades set (farm,money_per_click,currency) = ({self.upgradelist['farm']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_h':
                if self.currency >= 300:
                    self.currency -= 300
                    self.money_per_click += 30
                    self.upgradelist['farm'] += 10
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)
                    query = f"update upgrades set (farm,money_per_click,currency) = ({self.upgradelist['farm']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_i':
                if self.currency >= 3000:
                    self.currency -= 3000
                    self.money_per_click += 300
                    self.upgradelist['farm'] += 100
                    win['upgrades'].update(self.upgradelist)
                    win['money_gained'].update(self.currency)
                    win['incvalue'].update(self.money_per_click)        
                    query = f"update upgrades set (farm,money_per_click,currency) = ({self.upgradelist['farm']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)      
            self.connection.commit()      
        win.close()
        #this is how to retrieve the values from the table in the database
        query = "select * from upgrades"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result) #this is a tuple in a list #a list of things in a list
        x = result[0] #retrieving from the first tuple
        print(x)  #retrieving the second value from the tuple

    def more_than_one_run(self):
        sg.theme('DarkAmber')
        
        col_layoutright = [ 
            [sg.Text('Clicker'),sg.Button('add 1 for $10',key = 'purchase_a'),sg.Button('add 10 for $100',key = 'purchase_b'),sg.Button('add 100 for $1000',key = 'purchase_c')],
            [sg.Text('Grandma'),sg.Button('add 1 for $20',key = 'purchase_d'),sg.Button('add 10 for $200',key = 'purchase_e'),sg.Button('add 100 for $2000',key = 'purchase_f')],
            [sg.Text('Farm'),sg.Button('add 1 for $30',key = 'purchase_g'),sg.Button('add 10 for $300',key = 'purchase_h'),sg.Button('add 100 for $3000',key = 'purchase_i')]
        ]
        #dictname[keyname] = value
        col_layoutleft = [
            [sg.Button('go',size = (30,3), visible= True,key = 'clicked')]
        ]
        combo_layout = [
            [sg.Column(col_layoutleft,element_justification='left')],
            [sg.Column(col_layoutright,element_justification='right')]
        ]
        progress_layout = [
            [sg.Text('buy the first clicker upgrade to start the file')],
            [sg.Text(f'{self.p_upgradelist}',key='upgrades')],
            [sg.Text('money per click')],[sg.Text(self.p_money_per_click,key = 'incvalue')],
            [sg.Text('currency')],[sg.Text(self.p_currency,key = 'money_gained')]
        ]
        main_layout = [
            [sg.Text('welcome to not Cookie clicker')],
            [sg.Column(progress_layout,element_justification='right')],
            [sg.Column(combo_layout,element_justification='left')]
        ]
        win  = sg.Window('not cookie clicker',main_layout,element_justification='center')

        while True:
            e,v = win.read()
            if e == sg.WIN_CLOSED:
                break
            elif e == 'clicked':
                
                self.p_currency+= self.p_money_per_click
                win['money_gained'].update(self.p_currency)
                query = f"update upgrades set (currency) = ('{self.p_currency}') where id=1"
                self.cursor.execute(query)
                #dictname[keyname] = value
            elif e == 'purchase_a':
                if self.p_currency >= 10:
                    self.p_currency -= 10
                    self.p_money_per_click += 1
                    self.p_upgradelist['clicker'] += 1
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (clicker,money_per_click,currency) = ({self.p_upgradelist['clicker']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    #this is the good code -- query = f"update upgrades set (clicker,money_per_click,currency) = ({self.upgradelist['clicker']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_b':
                if self.p_currency >= 100:
                    self.p_currency -= 100
                    self.p_money_per_click += 10
                    self.p_upgradelist['clicker'] += 10
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (clicker,money_per_click,currency) = ({self.p_upgradelist['clicker']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    #this is the good code -- query = f"update upgrades set (clicker,money_per_click,currency) = ({self.upgradelist['clicker']},{self.money_per_click},{self.currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_c':
                if self.p_currency >= 1000:
                    self.p_currency -= 1000
                    self.p_money_per_click += 100
                    self.p_upgradelist['clicker'] += 100
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (clicker,money_per_click,currency) = ({self.p_upgradelist['clicker']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_d':
                if self.p_currency >= 20:
                    self.p_currency -= 20
                    self.p_money_per_click += 2
                    self.p_upgradelist['grandma'] += 1
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (grandma,money_per_click,currency) = ({self.p_upgradelist['grandma']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_e':
                if self.p_currency >= 200:
                    self.p_currency -= 200
                    self.p_money_per_click += 20
                    self.p_upgradelist['grandma'] += 10
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (grandma,money_per_click,currency) = ({self.p_upgradelist['grandma']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_f':
                if self.p_currency >= 2000:
                    self.p_currency -= 2000
                    self.p_money_per_click += 200
                    self.p_upgradelist['grandma'] += 100
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (grandma,money_per_click,currency) = ({self.p_upgradelist['grandma']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_g':
                if self.p_currency >= 30:
                    self.p_currency -= 30
                    self.p_money_per_click += 3
                    self.p_upgradelist['farm'] += 1
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (farm,money_per_click,currency) = ({self.p_upgradelist['farm']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_h':
                if self.p_currency >= 300:
                    self.p_currency -= 300
                    self.p_money_per_click += 30
                    self.p_upgradelist['farm'] += 10
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (farm,money_per_click,currency) = ({self.p_upgradelist['farm']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    self.cursor.execute(query)
            elif e == 'purchase_i':
                if self.p_currency >= 3000:
                    self.p_currency -= 3000
                    self.p_money_per_click += 300
                    self.p_upgradelist['farm'] += 100
                    win['upgrades'].update(self.p_upgradelist)
                    win['money_gained'].update(self.p_currency)
                    win['incvalue'].update(self.p_money_per_click)
                    query = f"update upgrades set (farm,money_per_click,currency) = ({self.p_upgradelist['farm']},{self.p_money_per_click},{self.p_currency}) where id=1"
                    self.cursor.execute(query)
            self.connection.commit() 
        win.close()
        query = "select * from upgrades"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result) #this is a tuple in a list #a list of things in a list
        x = result[0] #retrieving from the first tuple
        print(x)  #retrieving the second value from the tuple
Not_Cookie_clicker()