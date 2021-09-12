import mysql.connector
from mysql.connector import errorcode
import csv
import tkinter as tk
from tkinter import *
import webbrowser
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox  
import os
from tkinter import Button, Tk, HORIZONTAL
from tkinter import *
import urllib.request
from PIL import ImageTk, Image
from datetime import datetime

from tkinter.ttk import Progressbar
import time
import threading
import difflib
# Python Program to Get IP Address
import socket   
    

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        urllib.request.urlretrieve(
        'http://anvesak.marketing/images/logo.png',
        "logo.png")

        img = Image.open("logo.png")
        img = img.resize((150, 80), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.pack(side=TOP, anchor=N)

        border = tk.LabelFrame(self, text='LOGIN', bg='snow', bd = 10, height=50, font=("Arial Bold", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=100)

        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='snow')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width = 30, bd = 5)
        T1.place(x=180, y=20)
        
        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='snow')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width = 30, show='*', bd = 5)
        T2.place(x=180, y=80)
        Label(self, text="Powered by DITHOK TECHNOLOGIES LLP", foreground='grey1', font=("Arial", 10)).pack(side=BOTTOM,anchor=SE)
        
        
        
        def submitact():
            global user
            user = T1.get()
            passw = T2.get()
        
            print(f"The name entered by you is {user} {passw}")
        
            logintodb(user, passw)


        
        def logintodb(user, passw):
            
            try:
                if passw:
                    db = mysql.connector.connect(host ="localhost",
                                                user = user,
                                                password = passw,
                                                db ="mycommerce")
                    cursor = db.cursor()
                    controller.show_frame(SecondPage)
                    
                # If no password is enetered by the
                # user
                else:
                    db = mysql.connector.connect(host ="localhost",
                                                user = user,
                                                db ="mycommerce")
                    cursor = db.cursor()
            
            except:
                print("Error occured") 
                messagebox.showwarning("warning","Enter Correct Login Credentials")


        B1 = tk.Button(border, text="Submit", font=("Arial", 10), command=submitact)
        B1.place(x=320, y=115)   
        
        
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
  
        def UploadAction():
            global filename
            filename = filedialog.askopenfilename()
            print('Selected:', filename) 
            ent1.insert(END,filename)

        def Csv():
                try:
                    db = mysql.connector.connect(host ="localhost",
                                                    user = "root",
                                                    password = "root",
                                                    db ="mycommerce")
                    cursor = db.cursor()
                    table_name = 'company_data'

                    
                    file = open(filename, 'r', encoding='utf-8-sig')
                    csv_data = csv.reader(file)
                    my_reader = csv.DictReader(file)
                    insert_sql = 'insert into ' + table_name  + ' (' + ','.join(my_reader.fieldnames) + ') VALUES (' + ','.join(['%s'] * len(my_reader.fieldnames))+ ')'

                    values1 = []
                    for row in my_reader:
                        row_values = []
                        for field in my_reader.fieldnames:
                            row_values.append(row[field])
                        values1.append(row_values)
                        
                    cursor.executemany(insert_sql,values1)
                    print(cursor.rowcount, 'Data Succesfully Inserted')
                    DCount=cursor.rowcount
                    db.commit()
                    if DCount >= 1:
                        Label(self, text= str(DCount) + ' New Data Inserted Successfully!', foreground='green').pack()
                        global now
                        now = datetime.now()
                        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                        global hostname
                        global IPAddr
                        hostname = socket.gethostname()   
                        IPAddr = socket.gethostbyname(hostname)
                        details = 'Inserted {} New Data from {} from {} {}'.format(DCount, filename, hostname, IPAddr)
                        sql = "INSERT INTO audit_log (details, timestamp, user_name) VALUES (%s,%s,%s)"
                        val = (details, formatted_date , user)
                        cursor.execute(sql, val)
                        db.commit()


                except:
                    table_name = 'demo'

                    
                    file = open(filename, 'r', encoding='utf-8-sig')
                    csv_data = csv.reader(file)
                    my_reader = csv.DictReader(file)

                    insert_sql = 'insert into ' + table_name  + ' (' + ','.join(my_reader.fieldnames) + ') VALUES (' + ','.join(['%s'] * len(my_reader.fieldnames))+ ');'
                    
                    values2 = []
                    for row in my_reader:
                        row_values = []
                        for field in my_reader.fieldnames:
                            row_values.append(row[field])
                        values2.append(row_values)
                        
                    cursor.executemany(insert_sql,values2)
                    print(cursor.rowcount, 'Data Succesfully Inserted')
                    db.commit()
                    controller.show_frame(ThirdPage)

        def success():
            Label(self, text='Data Inserted Successfully!', foreground='green').pack()

        img = Image.open("logo.png")
        img = img.resize((150, 80), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self, image=img)
        panel.image = img
        panel.pack(side=TOP, anchor=NW)

        Label(self, text="WELCOME ADMIN", font=("Arial Bold", 15)).pack(pady=20)

        Label(self, text="Please Choose Your CSV File", font=("Arial Bold", 15)).pack(pady=20)

        ent1 = tk.Entry(self, width = 50, bd = 5)
        ent1.place(x=180, y=220)

            
        Button = tk.Button(self, text="Choose file", font=("Arial", 10), command=UploadAction)
        Button.place(x=500, y=220)
        
        Button = tk.Button(self, text="     Sync    ", font=("Arial", 10), command=Csv)
        Button.place(x=500, y=300)

        # progress = Progressbar(self, orient = HORIZONTAL,length = 100, mode = 'determinate')
        # # progress.place(x=250, y=300 )

        Label(self, text="Powered by DITHOK TECHNOLOGIES LLP", foreground='grey1', font=("Arial", 10)).pack(side=BOTTOM,anchor=SE)

        # def bar():
        #     import time
        #     progress['value'] = 20
        #     self.update_idletasks()
        #     time.sleep(1)
        
        #     progress['value'] = 40
        #     self.update_idletasks()
        #     time.sleep(1)
        
        #     progress['value'] = 50
        #     self.update_idletasks()
        #     time.sleep(1)
        
        #     progress['value'] = 60
        #     self.update_idletasks()
        #     time.sleep(1)
        
        #     progress['value'] = 80
        #     self.update_idletasks()
        #     time.sleep(1)
        #     progress['value'] = 100
        #     success()
        #     # Label(self, text='Data Inserted Successfully!', foreground='green').pack()
        
        # progress.pack(pady = 10)
        
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        
        def check():
            db = mysql.connector.connect(host ="localhost",
                                                        user = "root",
                                                        password = "root",
                                                        db ="mycommerce")
            cursor = db.cursor()
            global my_listbox 
            my_frame = Frame(self)
            my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
            scrollbarx = Scrollbar(my_frame, orient=HORIZONTAL)

            my_listbox = Listbox(my_frame, width=50, height=10, yscrollcommand=my_scrollbar.set, xscrollcommand=scrollbarx.set, bg='lavender', selectmode=MULTIPLE)
            my_scrollbar.config(command=my_listbox.yview)
            my_scrollbar.pack(side=RIGHT,fill=Y)
            scrollbarx.config(command=my_listbox.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            my_frame.pack(padx=5, pady=15, side=tk.LEFT)
            my_listbox.pack(pady=15)

            
            cursor.execute('SELECT DISTINCT SrNo FROM demo INNER JOIN company_data USING(SrNo)')
            results = cursor.fetchall()

            newfile = open("Csv-data.txt","a+", encoding='utf-8')
            for row in results:
                lst = row[0]
                cursor.execute('select * from demo where SrNo = %s',(lst,))
                resultsdemo = cursor.fetchall()
                my_listbox.insert("end",resultsdemo)
                

                for index in resultsdemo:
                    ltr=[]
                    for i in range(len(index)):
                        ltr.append(index[i])
                    lenltr=len(ltr)
                    for i in range(lenltr):
                        newfile.write('{}'.format(ltr[i]))
                        newfile.write("\t\t")
                    newfile.write("\n\n")
                    newfile.write("##########################################################################")
                    newfile.write("\n\n")
                    

            newfile.close()

            my_frame2 = Frame(self)
            my_scrollbar2 = Scrollbar(my_frame2, orient=VERTICAL)
            scrollbarx2 = Scrollbar(my_frame2, orient=HORIZONTAL)

            my_listbox2 = Listbox(my_frame2, width=50, height=10,bg='gainsboro', yscrollcommand=my_scrollbar2.set, xscrollcommand=scrollbarx2.set)
            my_scrollbar2.config(command=my_listbox2.yview)
            my_scrollbar2.pack(side=RIGHT,fill=Y)
            scrollbarx2.config(command=my_listbox2.xview)
            scrollbarx2.pack(side=BOTTOM, fill=X)
            my_frame2.pack(padx=5, pady=15, side=tk.RIGHT)
            my_listbox2.pack(pady=15)

            newfile2 = open("db-data.txt","a+", encoding='utf-8')
            for row in results:
                lst = row[0]
                cursor.execute('select * from company_data where SrNo = %s',(lst,))
                resultsdemo2 = cursor.fetchall()
                my_listbox2.insert("end",resultsdemo2)
                

                for index in resultsdemo2:
                    ltr=[]
                    for i in range(len(index)):
                        ltr.append(index[i])
                    lenltr=len(ltr)
                    for i in range(lenltr):
                        newfile2.write('{}'.format(ltr[i]))
                        newfile2.write("\t\t")
                    newfile2.write("\n\n")
                    newfile2.write("##########################################################################")
                    newfile2.write("\n\n")
            newfile2.close()
                


            with open("Csv-data.txt") as f, open("db-data.txt") as g:
                flines = f.readlines()
                glines = g.readlines()

                d = difflib.Differ()
                diff = d.compare(flines, glines)

            from difflib import HtmlDiff

            delta_html = HtmlDiff(wrapcolumn=75).make_file(flines,glines)
            with open('diff.html','w') as f:
                f.write(delta_html)




        def OverWrite():
            db = mysql.connector.connect(host ="localhost",
                                                        user = "root",
                                                        password = "root",
                                                        db ="mycommerce")
            cursor = db.cursor()
            table_name = 'company_data'

                    
            file = open(filename, 'r', encoding='utf-8-sig')
            csv_data = csv.reader(file)
            my_reader = csv.DictReader(file)

            insert_sql = 'insert into ' + table_name  + ' (' + ','.join(my_reader.fieldnames) + ') VALUES (' + ','.join(['%s'] * len(my_reader.fieldnames))+ ')'
            query = ''
            for i in range(len(my_reader.fieldnames)):
                if(i == len(my_reader.fieldnames)-1):
                    query += my_reader.fieldnames[i] + '=VALUES(' + my_reader.fieldnames[i] + ')'
                else:
                    query += my_reader.fieldnames[i] + '=VALUES(' + my_reader.fieldnames[i] + '),'
            UpdateQuery = insert_sql + 'ON DUPLICATE KEY UPDATE ' + query
            values3 = []
            for row in my_reader:
                row_values = []
                for field in my_reader.fieldnames:
                    row_values.append(row[field])
                values3.append(row_values)
                
            cursor.executemany(UpdateQuery,values3)
            print(cursor.rowcount, 'Data Succesfully Inserted')
            db.commit()
            DCount=cursor.rowcount
            success()
            global hostname
            global IPAddr
            hostname = socket.gethostname()   
            IPAddr = socket.gethostbyname(hostname)
            global now
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            global fileentry
            fileentry = os.path.basename(filename)
            details = 'Overwrited {} Data from {} from {} {}'.format(DCount, filename, hostname, IPAddr)
            sql = "INSERT INTO audit_log (details, timestamp, user_name) VALUES (%s,%s,%s)"
            val = (details, formatted_date , user)
            if DCount >= 1:
                cursor.execute(sql, val)
                db.commit()
                
        def Skip():
            db = mysql.connector.connect(host ="localhost",
                                                        user = "root",
                                                        password = "root",
                                                        db ="mycommerce")
            cursor = db.cursor()
            table_name = 'company_data'

                    
            file = open(filename, 'r', encoding='utf-8-sig')
            csv_data = csv.reader(file)
            my_reader = csv.DictReader(file)

            insert_sql = 'insert into ' + table_name  + ' (' + ','.join(my_reader.fieldnames) + ') VALUES (' + ','.join(['%s'] * len(my_reader.fieldnames))+ ')'
            intsqlskip = insert_sql + 'ON DUPLICATE KEY UPDATE SrNo=VALUES(SrNo)'
            values4 = []
            for row in my_reader:
                row_values = []
                for field in my_reader.fieldnames:
                    row_values.append(row[field])
                values4.append(row_values)
                
            cursor.executemany(intsqlskip,values4)
            print(cursor.rowcount, 'Data Succesfully Inserted')
            db.commit()
            global DCountskip
            DCountskip=cursor.rowcount
            db.commit()
            if DCountskip >= 1:
                Label(self, text= str(DCountskip) + ' New Data Inserted Successfully!', foreground='green').pack()
                global hostname
                global IPAddr
                hostname = socket.gethostname()   
                IPAddr = socket.gethostbyname(hostname)
                global now
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                global fileentry
                fileentry = os.path.basename(filename)
                details = 'Inserted {} New Data from {} and all Duplicate data Skipped from {} {}'.format(DCountskip, filename, hostname, IPAddr)
                sql = "INSERT INTO audit_log (details, timestamp, user_name) VALUES (%s,%s,%s)"
                val = (details, formatted_date , user)
                cursor.execute(sql, val)
                db.commit()

        def success():
            Label(self, text='Data Inserted Successfully!', foreground='green').pack()
        
        def greater():
            MsgBox = tk.messagebox.askquestion("ARE YOU SURE YOU WANT TO PROCEED?","CLICKING ON THE YES BUTTON WILL UPDATE THE SELECTED DUPLICATE DATA AND INSERT THE NEW DATA")
            if MsgBox == 'yes':
                db = mysql.connector.connect(host ="localhost",
                                                        user = "root",
                                                        password = "root",
                                                        db ="mycommerce")
                cursor = db.cursor()
                table_name = 'company_data'
   
                file = open(filename, 'r', encoding='utf-8-sig')
                csv_data = csv.reader(file)
                my_reader = csv.DictReader(file)
                insert_sql = 'insert into ' + table_name  + ' (' + ','.join(my_reader.fieldnames) + ') VALUES (' + ','.join(['%s'] * len(my_reader.fieldnames))+ ')'
                query = ''
                for i in range (1 , len(my_reader.fieldnames)):
                    if(i == len(my_reader.fieldnames)-1):
                        query += my_reader.fieldnames[i] + '=VALUES(' + my_reader.fieldnames[i] + ')'
                    else:
                        query += my_reader.fieldnames[i] + '=VALUES(' + my_reader.fieldnames[i] + '),'
                UpdateQuery = insert_sql + 'ON DUPLICATE KEY UPDATE ' + query

                items = ()
                for item in my_listbox.curselection():
                    items = items + my_listbox.get(item)
                    for row in items:
                        List = list(row)
                        cursor.execute(UpdateQuery,row)
                    db.commit()
                var = str(len(items))
                Label(self, text= var+ ' Data Updated Successfully!', foreground='green').pack()
                Skip()
                global hostname
                global IPAddr
                hostname = socket.gethostname()   
                IPAddr = socket.gethostbyname(hostname)
                global now
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                global fileentry
                fileentry = os.path.basename(filename)
                var2 = int(var)
                details = '{} Data Updated Successfully from {} from {} {}'.format(var2, filename, hostname, IPAddr)
                sql = "INSERT INTO audit_log (details, timestamp, user_name) VALUES (%s,%s,%s)"
                val = (details, formatted_date , user)
                cursor.execute(sql, val)
                db.commit()

   
        new = 1
        url = "diff.html"

        def openweb():
            webbrowser.open(url,new=new)
            db = mysql.connector.connect(host ="localhost",
                                                        user = "root",
                                                        password = "root",
                                                        db ="mycommerce")
            cursor = db.cursor()
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            global fileentry
            fileentry = os.path.basename(filename)
            details = '{} User Viewed Highlighted Difference'.format(user)
            sql = "INSERT INTO audit_log (details, timestamp, user_name) VALUES (%s,%s,%s)"
            val = (details, formatted_date , user)
            cursor.execute(sql, val)
            db.commit()

                   

        Label(self, text="DUPLICATES FOUND", font=("Arial Bold", 15)).pack(pady=20)

        Label(self, text="CSV DATA                                                                             DB DATA", font=("Arial Bold", 15)).pack(padx=5, pady=15)

        Button = tk.Button(self, text="SHOW DETAILS", font=("Arial", 10), command=check)
        Button.place(x=650, y=20)


        Button = tk.Button(self, text="Overwrite Database", font=("Arial", 10), command=OverWrite)
        Button.place(x=150, y=420)

        Button = tk.Button(self, text=">>", font=("Arial", 10), command=greater)
        Button.place(x=385, y=300)

        Button = tk.Button(self, text="Show Difference", font=("Arial", 10), command=openweb)
        Button.place(x=350, y=250)
        
        Button = tk.Button(self, text="    Skip Duplicate Data    ", font=("Arial", 10), command=Skip)
        Button.place(x=500, y=420)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("DATA SYNC TERMINAL")

def shutdown():
    db = mysql.connector.connect(host ="localhost",
                                                        user = "root",
                                                        password = "root",
                                                        db ="mycommerce")
    cursor = db.cursor()
    MsgBox = tk.messagebox.askquestion("QUIT?","ARE YOU SURE YOU WANT TO PROCEED")
    if MsgBox == 'yes':
        cursor.execute('DELETE FROM demo')
        db.commit()
        if os.path.exists("Csv-data.txt"):
            os.remove("Csv-data.txt")
        if os.path.exists("db-data.txt"):
            os.remove("db-data.txt")
        if os.path.exists("diff.html"):
            os.remove("diff.html")
        app.destroy()


    


app = Application()
app.maxsize(800,500)
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()