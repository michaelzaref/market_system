from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import random

class market():

    def __init__(self, root):
        self.root = root
        self.root.geometry('1547x800+1+1')
        self.root.title("school managment")
        self.root.configure(background="silver")
        title = Label(self.root,
                      text='market management system',
                      bg='#1aaecb',
                      font=('monospace', '14', 'bold'),
                      fg='white')

        title.pack(fill=X)


#-------------variables-----------------

        self.loged=StringVar()
        self.user=StringVar()
        self.password=StringVar()
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.val_var = StringVar()
        self.count_var =IntVar(root,value=1)
        self.total_var =StringVar()
        self.total_finish=StringVar()
        self.bill_id=IntVar()
        self.bill_id=random.randrange(0,4000000)
        self.current_bill=StringVar()
        self.current_bill='b'+str(self.bill_id)
        self.cliend_name=StringVar()
        self.client_phone=StringVar()



        print("crunt from top is "+self.current_bill)

#------------------frames------------------



        # ---------------main frame---------------
        main_frame = Frame(self.root, bg='white')
        main_frame.place(x='580', y='40', width='499', height='440')
        #----------------manage frama-------------
        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1085, y=40, width='440', height='740')
        # ----------------search frame--------------
        search_frame = Frame(manage_frame, bg='white')
        search_frame.place(x='1', y='80', width='440', height='330')
        #_______clint_frame_____
        clint_frame = Frame(self.root, bg='white')
        clint_frame.place(x='580', y='485', width='500', height='295')
        #_______clint_table_frame______
        clint_manage_frame = Frame(clint_frame, bg='white')
        clint_manage_frame.place(x='290', y='0', width='240', height='295')
        #_______show_clints_______
        clint_table_frame = Frame(clint_frame, bg='white')
        clint_table_frame.place(x='0', y='0', width='250', height='295')

        #-------info------------
        info_frame = Frame(self.root, bg='white')
        info_frame.place(x='1', y='40', width='570', height='740')
        title = Label(info_frame,
                      text='i',
                      bg='#1aaecb',
                      font=('monospace', '14', 'bold'),
                      fg='white')

        title.pack(fill=X)







        # --------------id------------------
        lbl_id = Label(manage_frame, text='ID', bg='white')
        lbl_id.place(x=10, y=10)
        id_entry = Entry(manage_frame, textvariable=self.id_var, bd='2', justify="center")
        id_entry.place(x=40, y=10,width=60)
        # -------------name-----------------
        lbl_name = Label(manage_frame, text='name', bg='white')
        lbl_name.place(x=100, y=10)
        name_entry = Entry(manage_frame, textvariable=self.name_var, bd='2', justify="center")
        name_entry.place(x=140, y=10)


        lbl_id = Label(manage_frame, text='total', bg='white')
        lbl_id.place(x=10, y=455)
        id_entry = Entry(manage_frame, textvariable=self.total_finish, bd='2', justify="center")
        id_entry.place(x=40, y=455)




        lbl_id = Label(manage_frame, text='count', bg='white')
        lbl_id.place(x=270, y=10)
        id_entry = Entry(manage_frame, textvariable=self.count_var, bd='2', justify="center")
        id_entry.place(x=305, y=10)

        lbl_id = Label(manage_frame, text='password', bg='white')
        lbl_id.place(x=170, y=670)
        id_entry = Entry(manage_frame, textvariable=self.password, bd='2', justify="center")
        id_entry.place(x=230, y=670)

        lbl_id = Label(manage_frame, text='user', bg='white')
        lbl_id.place(x=10, y=670)
        id_entry = Entry(manage_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=40, y=670)

        lbl_id = Label(clint_manage_frame, text='clint name', bg='white')
        lbl_id.place(x=10, y=50)

        id_entry = Entry(clint_manage_frame, textvariable=self.cliend_name, bd='2', justify="center")
        id_entry.place(x=80, y=50)

        lbl_id = Label(clint_manage_frame, text='phone', bg='white')
        lbl_id.place(x=10, y=90)

        id_entry = Entry(clint_manage_frame, textvariable=self.client_phone, bd='2', justify="center")
        id_entry.place(x=80, y=90)

        add_button = Button(clint_manage_frame, text='search clint', bg='gray',command=self.search_client)
        add_button.place(x='10', y='130', width='190', height='30')

        add_button = Button(clint_manage_frame, text='add clint', bg='gray', command=self.add_client)
        add_button.place(x='10', y='170', width='190', height='30')

        title = Label(clint_frame,
                      text='manage clients',
                      bg='#1aaecb',
                      font=('monospace', '14', 'bold'),
                      fg='white')

        title.pack(fill=X)

        add_button = Button(manage_frame, text='print', bg='gray',command=self.print)
        add_button.place(x='10', y='415', width='190', height='30')

        add_button = Button(manage_frame, text='new bill', bg='gray', command=self.new_bill)
        add_button.place(x='205', y='415', width='190', height='30')

        add_button = Button(manage_frame, text='edit bill', bg='gray', command=self.print)
        add_button.place(x='10', y='480', width='190', height='30')

        add_button = Button(manage_frame, text='delete bill', bg='gray', command=self.new_bill)
        add_button.place(x='205', y='480', width='190', height='30')

        add_button = Button(manage_frame, text='delete good', bg='gray', command=self.new_bill)
        add_button.place(x='205', y='520', width='190', height='30')


        add_button = Button(manage_frame, text='login', bg='gray', command=self.ad)
        add_button.place(x='90', y='700', width='190', height='30')


        add_button = Button(manage_frame, text='search', bg='gray' ,command=self.search_good)
        add_button.place(x='10', y='40', width='190', height='30')

        add_button = Button(manage_frame, text='add to bill', bg='gray',command=self.add_good)
        add_button.place(x='205', y='40', width='190', height='30')






        scroll_x = Scrollbar(main_frame, orient='horizontal')
        scroll_y = Scrollbar(main_frame, orient='vertical')

        self.main_table = ttk.Treeview(main_frame,

                                          columns=('id', 'name', 'val', 'count', 'total'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        self.main_table.place(x=18, y=1, width=480, height=419)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.main_table.xview)
        scroll_y.config(command=self.main_table.yview)

        self.main_table['show'] = 'headings'
        self.main_table.heading('id', text='id')
        self.main_table.heading('name', text='name')
        self.main_table.heading('val', text='count')
        self.main_table.heading('count', text='value')
        self.main_table.heading('total', text='total')

        self.main_table.column('total', width=60)
        self.main_table.column('count', width=60)
        self.main_table.column('val', width=60)
        self.main_table.column('id', width=60)
        self.main_table.column('name', width=60)



        scroll_x = Scrollbar(search_frame, orient='horizontal')
        scroll_y = Scrollbar(search_frame, orient='vertical')

        self.search_table = ttk.Treeview(search_frame,

                                          columns=('id', 'name','val'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        self.search_table.place(x=18, y=1, width=450, height=310)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.search_table.xview)
        scroll_y.config(command=self.search_table.yview)

        self.search_table['show'] = 'headings'
        self.search_table.heading('id', text='id')
        self.search_table.heading('name', text='name')
        self.search_table.heading('val', text='value')


        self.search_table.column('val', width=80)
        self.search_table.column('id', width=80)
        self.search_table.column('name', width=100)
        self.search_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_goods()

        self.search_table.bind("<ButtonRelease-1>", self.get_cursor)

        scroll_x = Scrollbar(clint_table_frame, orient='horizontal')
        scroll_y = Scrollbar(clint_table_frame, orient='vertical')

        self.client_table = ttk.Treeview(clint_table_frame,

                                         columns=('phone', 'name'),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set)

        self.client_table.place(x=18, y=29, width=250, height=249)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.client_table.xview)
        scroll_y.config(command=self.client_table.yview)

        self.client_table['show'] = 'headings'
        self.client_table.heading('phone', text='id')
        self.client_table.heading('name', text='name')



        self.client_table.column('phone', width=80)
        self.client_table.column('name', width=100)
        self.client_table.bind("<ButtonRelease-1>", self.get_cursor_client)
        self.fetch_clients()
        self.user_page()








    def fetch_goods(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()
        cur.execute('SELECT * FROM goods;')
        rows = cur.fetchall()

        if len(rows) != 0:
            self.search_table.delete(*self.search_table.get_children())
            for row in rows:

                self.search_table.insert("", END, value=row)
                con.commit()

        con.close()

    def fetch_clients(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()
        cur.execute('SELECT * FROM clients;')
        rows = cur.fetchall()

        if len(rows) != 0:
            self.client_table.delete(*self.client_table.get_children())
            for row in rows:
                self.client_table.insert("", END, value=row)
                con.commit()

        con.close()

    def get_cursor_client(self,ev):
        cursor_row=self.client_table.focus()
        content=self.client_table.item(cursor_row)
        row=content['values']
        self.client_phone.set(row[0])
        self.cliend_name.set(row[1])


        # self.id_var=int(self.id_var.get())

        print(self.total_var)
        print(self.id_var)

    def get_cursor(self,ev):
        cursor_row=self.search_table.focus()
        content=self.search_table.item(cursor_row)
        row=content['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.val_var.set(row[2])

        # self.id_var=int(self.id_var.get())

        print(self.total_var)
        print(self.id_var)

    def search_good(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()
        if(str(self.id_var.get())==''):
            cur.execute('SELECT * FROM goods')
            rows = cur.fetchall()

            if len(rows) != 0:
                self.search_table.delete(*self.search_table.get_children())

                for row in rows:
                    self.search_table.insert("", END, value=row)
                    self.id_var.set(row[0])
                    self.name_var.set(row[1])
                    self.val_var.set(row[2])
                    con.commit()
            self.id_var.set('')
            self.name_var.set('')
            self.val_var.set('')


        else:

            cur.execute('SELECT * FROM goods where id=%s',self.id_var.get())
            rows = cur.fetchall()

            if len(rows) != 0:
                self.search_table.delete(*self.search_table.get_children())

                for row in rows:

                    self.search_table.insert("", END, value=row)
                    self.id_var.set(row[0])
                    self.name_var.set(row[1])
                    self.val_var.set(row[2])
                    con.commit()

    def search_client(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()
        if (str(self.client_phone.get()) == ''):
            cur.execute('SELECT * FROM clients')
            rows = cur.fetchall()

            if len(rows) != 0:
                self.client_table.delete(*self.client_table.get_children())

                for row in rows:
                    self.client_table.insert("", END, value=row)
                    self.cliend_name.set(row[0])
                    self.client_phone.set(row[1])
                    con.commit()
            self.cliend_name.set('')
            self.client_phone.set('')



        else:

            cur.execute('SELECT * FROM clients where phone=%s', self.client_phone.get())
            rows = cur.fetchall()

            if len(rows) != 0:
                self.client_table.delete(*self.client_table.get_children())

                for row in rows:
                    self.client_table.insert("", END, value=row)
                    self.cliend_name.set(row[1])
                    self.client_phone.set(row[0])
                    con.commit()

        con.close()

    def new_bill(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
            )
        cur = con.cursor()
        self.current_bill = 'b' + str(self.bill_id)
        cur.execute("CREATE table b%s (id varchar(20),name varchar(20) ,count varchar(20),value varchar(20),total varchar(20), PRIMARY KEY(ID))", self.bill_id)

        self.current_bill = 'b' + str(self.bill_id)
        con.commit()
        self.last_bill=self.current_bill
        self.bill_id = random.randrange(0, 400000000)
        print(self.current_bill)




        con.close()
    def add_good(self):

        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()
#        print(self.total_var)
#        print(self.current_bill)
        self.total_var = int(self.count_var.get()) * int(self.val_var.get())
        ins = "INSERT INTO " + "`" + self.current_bill + "`" + "(`id`, `name`, `count`, `value`, `total`) VALUES ('"+str(self.id_var.get())+"','"+str(self.name_var.get())+"','"+str(self.count_var.get())+"','"+str(self.val_var.get())+"','"+str(self.total_var)+"')"
        #cur.execute("INSERT INTO `%s`(`id`, `name`, `count`, `value`,`total`) VALUES (%s,%s,%s,%s,%s)",(self.current_bill,self.id_var,self.name_var,self.count_var,self.val_var,str(self.total_var)))
        cur.execute(ins)
        con.commit()
        self.show_bill()
        self.total_calc()
        con.close()

    def show_bill(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()
        catch="select * from `"+self.current_bill+"`;"
        cur.execute(catch)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.main_table.delete(*self.main_table.get_children())

            for row in rows:

                self.main_table.insert("", END, value=row)
                con.commit()

        con.close()


    def total_calc(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()

        ex = "select total from " + self.current_bill
        print(ex)

        cur.execute(ex)
        rows = cur.fetchall()
        r = ''
        print(rows)

        for row in rows:
            r = r + str(row)
        print(r)
        print(type(r))

        c = ''
        for d in range(2, len(r) - 3):
            c = c + r[d]

        print(c)

        x = c.split("',)('")
        print(x)

        total = 0

        for k in range(0, len(x)):
            total += int(x[k])

        print(total)
        self.total_finish.set(str(total))

        con.commit()
        con.close()


    def print(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()

        self.total_calc()



        catch = "select * from `" + self.current_bill + "`;"
        cur.execute(catch)
        ins_total = "INSERT INTO " + "`" + self.current_bill + "`" + "(`id`, `name`, `count`, `value`, `total`) VALUES ('" + 'total' + "','" + 'total' + "','" + '' + "','" +'' + "','" + str(self.total_var.get()) + "')"
        cur.execute(ins_total)
        con.commit()

        con.close()

    def login(self):
            if(str(self.user.get())=="admin"):
                if(str(self.password.get())=="password"):
                    self.ad()

            else:
                print("no")


    def add_client(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='market'
        )
        cur = con.cursor()
        cur.execute("insert into clients values(%s,%s)", (
            self.cliend_name.get(),
            self.client_phone.get(),
        ))
        con.commit()

        self.fetch_clients()
        con.close()

    def user_page(self):
        info_frame = Frame(self.root, bg='white')
        info_frame.place(x='1', y='40', width='570', height='740')

        lbl_id = Label(info_frame, text='best seller', bg='white')
        lbl_id.place(x=300, y=40)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=390, y=40)

        lbl_id = Label(info_frame, text='SOLD VALUE', bg='white')
        lbl_id.place(x=300, y=80)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=390, y=80)

        add_button = Button(info_frame, text='edit good', bg='gray', command=self.print)
        add_button.place(x='420', y='120', width='150', height='30')

        add_button = Button(info_frame, text='delete good', bg='gray', command=self.new_bill)
        add_button.place(x='420', y='160', width='150', height='30')

        add_button = Button(info_frame, text='add good', bg='gray', command=self.print)
        add_button.place(x='420', y='200', width='150', height='30')

        lbl_id = Label(info_frame, text='id', bg='white')
        lbl_id.place(x=260, y=120)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=120)

        lbl_id = Label(info_frame, text='name', bg='white')
        lbl_id.place(x=250, y=145)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=145)
        lbl_id = Label(info_frame, text='value', bg='white')
        lbl_id.place(x=250, y=170)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=170)

        lbl_id = Label(info_frame, text='count', bg='white')
        lbl_id.place(x=250, y=195)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=196)




        good_table = Frame(info_frame, bg='white')
        good_table.place(x=0, y=40, width=250, height=249)



        title = Label(info_frame,
                      text='CASHIER NAME',
                      bg='#1affff',
                      font=('monospace', '14', 'bold'),
                      fg='white')



        title.pack(fill=X)

        scroll_x = Scrollbar(good_table, orient='horizontal')
        scroll_y = Scrollbar(good_table, orient='vertical')

        self.good_table = ttk.Treeview(good_table,

                                         columns=('phone', 'name'),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set)

        self.good_table.place(x=0, y=00, width=230, height=230)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.good_table.xview)
        scroll_y.config(command=self.good_table.yview)

        self.good_table['show'] = 'headings'
        self.good_table.heading('phone', text='id')
        self.good_table.heading('name', text='name')

        self.good_table.column('phone', width=80)
        self.good_table.column('name', width=100)

        cashier_frame = Frame(info_frame, bg='white')
        cashier_frame.place(x='1', y='300', width='570', height='230')

        lbl_id = Label(cashier_frame, text='best cashier', bg='white')
        lbl_id.place(x=0, y=0)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=70, y=0)

        lbl_id = Label(cashier_frame, text='best cashier', bg='white')
        lbl_id.place(x=0, y=0)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=70, y=0)






        lbl_id = Label(cashier_frame, text='value', bg='white')
        lbl_id.place(x=210, y=0)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=250, y=0)

        lbl_id = Label(cashier_frame, text='cashier name', bg='white')
        lbl_id.place(x=0, y=40)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=80, y=40)

        lbl_id = Label(cashier_frame, text='password', bg='white')
        lbl_id.place(x=210, y=40)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=270, y=40)

        add_button = Button(cashier_frame, text='add cashier', bg='gray', command=self.print)
        add_button.place(x='400', y='35', width='150', height='30')

        lbl_id = Label(cashier_frame, text='best user', bg='white')
        lbl_id.place(x=0, y=80)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=70, y=80)

        lbl_id = Label(cashier_frame, text='id', bg='white')
        lbl_id.place(x=210, y=80)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=250, y=80)

        lbl_id = Label(cashier_frame, text='value', bg='white')
        lbl_id.place(x=0, y=120)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=35, y=120)

        lbl_id = Label(cashier_frame, text='special discount', bg='white')
        lbl_id.place(x=160, y=120)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=255, y=120)

        add_button = Button(cashier_frame, text='add discount', bg='gray', command=self.print)
        add_button.place(x='400', y='115', width='150', height='30')

        best_frame = Frame(info_frame, bg='white')
        best_frame.place(x='0', y='470', width='570', height='270')


        scroll_x = Scrollbar(best_frame, orient='horizontal')
        scroll_y = Scrollbar(best_frame, orient='vertical')

        self.best_table = ttk.Treeview(best_frame,

                                          columns=('id', 'name', 'val', 'count', 'total'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        self.best_table.place(x=18, y=1, width=550, height=250)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.best_table.xview)
        scroll_y.config(command=self.best_table.yview)

        self.best_table['show'] = 'headings'
        self.best_table.heading('id', text='id')
        self.best_table.heading('name', text='name')
        self.best_table.heading('val', text='count')
        self.best_table.heading('count', text='value')
        self.best_table.heading('total', text='total')

        self.best_table.column('total', width=60)
        self.best_table.column('count', width=60)
        self.best_table.column('val', width=60)
        self.best_table.column('id', width=60)
        self.best_table.column('name', width=60)

    def ad(self):
        info_frame = Frame(self.root, bg='white')
        info_frame.place(x='1', y='40', width='570', height='740')

        lbl_id = Label(info_frame, text='best seller', bg='white')
        lbl_id.place(x=300, y=40)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=390, y=40)

        lbl_id = Label(info_frame, text='SOLD VALUE', bg='white')
        lbl_id.place(x=300, y=80)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=390, y=80)

        add_button = Button(info_frame, text='edit good', bg='gray', command=self.print)
        add_button.place(x='420', y='120', width='150', height='30')

        add_button = Button(info_frame, text='delete good', bg='gray', command=self.new_bill)
        add_button.place(x='420', y='160', width='150', height='30')

        add_button = Button(info_frame, text='add good', bg='gray', command=self.print)
        add_button.place(x='420', y='200', width='150', height='30')

        lbl_id = Label(info_frame, text='id', bg='white')
        lbl_id.place(x=260, y=120)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=120)

        lbl_id = Label(info_frame, text='name', bg='white')
        lbl_id.place(x=250, y=145)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=145)
        lbl_id = Label(info_frame, text='value', bg='white')
        lbl_id.place(x=250, y=170)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=170)

        lbl_id = Label(info_frame, text='count', bg='white')
        lbl_id.place(x=250, y=195)
        id_entry = Entry(info_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=290, y=196)




        good_table = Frame(info_frame, bg='white')
        good_table.place(x=0, y=40, width=250, height=249)



        title = Label(info_frame,
                      text='info',
                      bg='#1affff',
                      font=('monospace', '14', 'bold'),
                      fg='white')



        title.pack(fill=X)

        scroll_x = Scrollbar(good_table, orient='horizontal')
        scroll_y = Scrollbar(good_table, orient='vertical')

        self.good_table = ttk.Treeview(good_table,

                                         columns=('phone', 'name'),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set)

        self.good_table.place(x=0, y=00, width=230, height=230)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.good_table.xview)
        scroll_y.config(command=self.good_table.yview)

        self.good_table['show'] = 'headings'
        self.good_table.heading('phone', text='id')
        self.good_table.heading('name', text='name')

        self.good_table.column('phone', width=80)
        self.good_table.column('name', width=100)

        cashier_frame = Frame(info_frame, bg='white')
        cashier_frame.place(x='1', y='300', width='570', height='230')

        lbl_id = Label(cashier_frame, text='best cashier', bg='white')
        lbl_id.place(x=0, y=0)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=70, y=0)

        lbl_id = Label(cashier_frame, text='best cashier', bg='white')
        lbl_id.place(x=0, y=0)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=70, y=0)






        lbl_id = Label(cashier_frame, text='value', bg='white')
        lbl_id.place(x=210, y=0)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=250, y=0)

        lbl_id = Label(cashier_frame, text='cashier name', bg='white')
        lbl_id.place(x=0, y=40)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=80, y=40)

        lbl_id = Label(cashier_frame, text='password', bg='white')
        lbl_id.place(x=210, y=40)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=270, y=40)

        add_button = Button(cashier_frame, text='add cashier', bg='gray', command=self.print)
        add_button.place(x='400', y='35', width='150', height='30')

        lbl_id = Label(cashier_frame, text='best user', bg='white')
        lbl_id.place(x=0, y=80)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=70, y=80)

        lbl_id = Label(cashier_frame, text='id', bg='white')
        lbl_id.place(x=210, y=80)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=250, y=80)

        lbl_id = Label(cashier_frame, text='value', bg='white')
        lbl_id.place(x=0, y=120)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=35, y=120)

        lbl_id = Label(cashier_frame, text='special discount', bg='white')
        lbl_id.place(x=160, y=120)
        id_entry = Entry(cashier_frame, textvariable=self.user, bd='2', justify="center")
        id_entry.place(x=255, y=120)

        add_button = Button(cashier_frame, text='add discount', bg='gray', command=self.print)
        add_button.place(x='400', y='115', width='150', height='30')

        best_frame = Frame(info_frame, bg='white')
        best_frame.place(x='0', y='470', width='570', height='270')


        scroll_x = Scrollbar(best_frame, orient='horizontal')
        scroll_y = Scrollbar(best_frame, orient='vertical')

        self.best_table = ttk.Treeview(best_frame,

                                          columns=('id', 'name', 'val', 'count', 'total'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        self.best_table.place(x=18, y=1, width=550, height=250)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.best_table.xview)
        scroll_y.config(command=self.best_table.yview)

        self.best_table['show'] = 'headings'
        self.best_table.heading('id', text='id')
        self.best_table.heading('name', text='name')
        self.best_table.heading('val', text='count')
        self.best_table.heading('count', text='value')
        self.best_table.heading('total', text='total')

        self.best_table.column('total', width=60)
        self.best_table.column('count', width=60)
        self.best_table.column('val', width=60)
        self.best_table.column('id', width=60)
        self.best_table.column('name', width=60)



root = Tk()
ob = market(root)
root.mainloop()