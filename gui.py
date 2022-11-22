from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter.ttk import Entry


class Pharmacymanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1300x800+0+0")
        self.root.iconbitmap("New folder\IMAGES\ICON.ico")

#----------------------------------------CREATING THE VARIABLES FOR FUNCTION-------------------------------
        # variables for RHS table
        self.refno_var=StringVar()
        self.MedName_var=StringVar()

        #variables for major table
        self.ref_var=StringVar()
        self.CompName_var=StringVar()
        self.MedType_var=StringVar()
        self.TabletName_var=StringVar()
        self.LotNo_var=StringVar()
        self.IssueDate_var=StringVar()
        self.ExpDate_var=StringVar()
        self.uses_var=StringVar()
        self.sideeffect_var=StringVar()
        self.precNwar_var=StringVar()
        self.dosage_var=StringVar()
        self.Price_var=StringVar()
        self.ProductQT_var=StringVar()

#----------------------------------------------MAKING THE GUI---------------------------------------------

# ADDING THE LABEL
        lbl=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bg="black",fg="white",bd=5,relief=RAISED,font=("helvetica",40,"bold"),padx=4,pady=4)
        lbl.pack(side=TOP,fill=X)

# ADDING THE LOGO
        logo=Image.open("New folder\IMAGES\logo.jpg")
        logo=logo.resize((50,50),Image.ANTIALIAS)
        self.photologo=ImageTk.PhotoImage(logo)
        logobtn=Button(self.root,image=self.photologo,borderwidth=0)
        logobtn.place(x=80,y=15)

#CREATING THE MAIN DATA-FRAME
        maindf=Frame(self.root,bd=10,relief=RIDGE,padx=20,bg="#731d1d")
        maindf.place(x=0,y=80,width=1280,height=400)

#SUB-FRAME TO THE LEFT OF THE MAIN FRAME
        leftSF=LabelFrame(maindf,bd=10,relief=SUNKEN,padx=20,text="MEDICINE INFORMATION",fg="darkgreen",font=("helvetica",12,"bold"))
        leftSF.place(x=0,y=5,width=800,height=350)

        #-------------ADDING THE LABELS & ENTRY-BOX--------------------------
        #reference tag
        refnolbl=Label(leftSF,text="Reference no. :",padx=20,font=('helvetica',12,'bold'))
        refnolbl.grid(row=0,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharmacy")
        row=my_cursor.fetchall()
        #reference-combobox
        ref_combobox = ttk.Combobox(leftSF,textvariable=self.ref_var,width=15,font=('helvetica',12,'bold'), state='readonly')
        ref_combobox["values"]=row
        ref_combobox.current()
        ref_combobox.grid(row=0, column=1)

        #company-name tag
        compnamelbl= Label(leftSF,text='Company Name:',padx=20,font=('helvetica',12,'bold'))
        compnamelbl.grid(row=1, column=0, sticky=W)  
        #company-name entrybox    
        comp_entrybox=Entry(leftSF,textvariable=self.CompName_var,bd=2,relief=RIDGE, width=15,font=('helvetica',12,'bold'))
        comp_entrybox.grid(row=1,column=1)

        #type of medicine
        typmedlbl = Label(leftSF, text='Type of medicine',padx=20 ,font=('helvetica',12,'bold'))
        typmedlbl.grid(row=2, column=0, sticky=W)
        #combobox- medicine label
        typmedlbl_combo = ttk.Combobox(leftSF,textvariable=self.MedType_var, width=15,font=('helvetica',12,'bold'), state='readonly')
        typmedlbl_combo['values']=('Tablet', 'Liquid','Capsules','Topical Medicine','Drops','Inhales')
        typmedlbl_combo.grid(row=2, column=1)
        typmedlbl_combo.current(0)

        #medicine-name tag
        mednamelbl= Label(leftSF,text='Medicine Name:',padx=20,font=('helvetica',12,'bold'))
        mednamelbl.grid(row=3, column=0, sticky=W)  
        #adding the connection to mysql pharamacy table from database pms
        conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharmacy")
        med=my_cursor.fetchall()
        #medicine-name entrybox    
        medname_entrybox= ttk.Combobox(leftSF,textvariable=self.TabletName_var,bd=2, relief = RIDGE, width=15,font=('helvetica',12,'bold'),state="readonly")
        medname_entrybox["value"]=med 
        medname_entrybox.current(0)
        medname_entrybox.grid(row=3,column=1)

        #lot-no tag
        lotno_lbl= Label(leftSF,text='Lot No.:',padx=20,font=('helvetica',12,'bold'))
        lotno_lbl.grid(row=4, column=0, sticky=W)  
        #company-name entrybox    
        lotno_entrybox= Entry(leftSF,textvariable=self.LotNo_var,bd=2, relief = RIDGE, width=15,font=('helvetica',12,'bold'))
        lotno_entrybox.grid(row=4,column=1)

        #Issue-date label
        issuedate_lbl= Label(leftSF,text='Issue Date.:',padx=20,font=('helvetica',12,'bold'))
        issuedate_lbl.grid(row=5, column=0, sticky=W)  
        #issuedate entrybox    
        issuedate_entrybox= Entry(leftSF,textvariable=self.IssueDate_var,bd=2, relief = RIDGE, width=15,font=('helvetica',12,'bold'))
        issuedate_entrybox.grid(row=5,column=1)

        #expiry-date tag
        expirydate_lbl= Label(leftSF,text='Expiry-date:',padx=20,font=('helvetica',12,'bold'))
        expirydate_lbl.grid(row=6, column=0, sticky=W)  
        #expiry-date entrybox    
        expirydate_entrybox= Entry(leftSF,textvariable=self.ExpDate_var,bd=2, relief = RIDGE, width=15,font=('helvetica',12,'bold'))
        expirydate_entrybox.grid(row=6,column=1)

        #uses tag
        uses_lbl= Label(leftSF,text='Uses:',padx=20,font=('helvetica',12,'bold'))
        uses_lbl.grid(row=7, column=0, sticky=W)  
        #uses entrybox    
        uses_entrybox= Entry(leftSF,textvariable=self.uses_var,bd=2, relief = RIDGE, width=15,font=('helvetica',12,'bold'))
        uses_entrybox.grid(row=7,column=1)

        #side-effect tag
        sideeffect_lbl= Label(leftSF,text='Side-Effect:',padx=20,font=('helvetica',12,'bold'))
        sideeffect_lbl.grid(row=8, column=0, sticky=W)  
        #company-name entrybox    
        sideeffect_entrybox= Entry(leftSF,textvariable=self.sideeffect_var,bd=2, relief = RIDGE, width=15,font=('helvetica',12,'bold'))
        sideeffect_entrybox.grid(row=8,column=1)

        #prescription & Warning
        PW_lbl= Label(leftSF,text='Prec&Warning:',padx=20 ,pady=6,font=('helvetica',12,'bold'))
        PW_lbl.grid(row=0, column=2, sticky=W)
        #prescription & warning entrybox   
        PW_lbl= Entry(leftSF,textvariable=self.precNwar_var,font=('helvetica',12,'bold'),bg='white',bd=2,relief= RIDGE,width=15)
        PW_lbl.grid(row=0, column=3)

        #Dosage
        dosage_lbl= Label(leftSF,text='Dosage:',padx=20 ,pady=6,font=('helvetica',12,'bold'))
        dosage_lbl.grid(row=1,column=2, sticky=W)
        #dosage  entrybox   
        dosage= Entry(leftSF,textvariable=self.dosage_var,font=('helvetica',12,'bold'),bg='white',bd=2,relief= RIDGE,width=15)
        dosage.grid(row=1,column=3)

        #tablet price
        TbltPrice_lbl= Label(leftSF,text="Tablet Price: ",padx=20 ,pady=6,font=('helvetica',12,'bold'))
        TbltPrice_lbl.grid(row=2, column=2, sticky=W)
        #tablet price entrybox   
        TbltPrice_lbl= Entry(leftSF,textvariable=self.Price_var,font=('helvetica',12,'bold'),bg='white',bd=2,relief= RIDGE,width=15)
        TbltPrice_lbl.grid(row=2,column=3)

        #Product-QT 
        ProductQT_lbl= Label(leftSF,text="Product QT: ",padx=20 ,pady=6,font=('helvetica',12,'bold'))
        ProductQT_lbl.grid(row=3, column=2, sticky=W)
        #Product-QT entrybox   
        ProductQT_lbl= Entry(leftSF,textvariable=self.ProductQT_var,font=('helvetica',12,'bold'),bg='white',bd=2,relief= RIDGE,width=15)
        ProductQT_lbl.grid(row=3,column=3)

        #adding the images
                        #tagline
        tagline= Label(leftSF,text='EAT HEALTHY - STAY HEALTHY',padx=2,pady=6,font=('helvetica',12,'bold'),bg="black",fg="white",width=30)
        tagline.place(x=410,y=145)

                        #img-1
        img1=Image.open("New folder\IMAGES\img-1.jpg")
        img1=img1.resize((130,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=420,y=300)
                        #img-2
        img2=Image.open("New folder\IMAGES\img-2.png")
        img2=img2.resize((130,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=550,y=300)
                    #img-3
        img3=Image.open("New folder\IMAGES\img-3.jpg")
        img3=img3.resize((130,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=690,y=300)



#SUB-FRAME TO THE RIGHT OF THE MAIN FRAME
        rightSF=LabelFrame(maindf,bd=10,relief=RIDGE,padx=20,text="UPDATE MEDICINE",fg="darkgreen",font=("helvetica",12,"bold"))
        rightSF.place(x=830,y=5,width=400,height=350)

        #Adding the images
                #img-4
        img4=Image.open("New folder\IMAGES\img-4.jpg")
        img4=img4.resize((255,75),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=875,y=115)
                #img-5
        img5=Image.open("New folder\IMAGES\img-5.jpg")
        img5=img5.resize((115,140),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=1135,y=115)

        # Adding the labels
            #reference number
        refno_lbl= Label(rightSF,text='Reference No:',pady=6,font=('helvetica',12,'bold'))
        refno_lbl.place(x=0,y=80)
            #entry-box
        refno_box= Entry(rightSF,textvariable=self.refno_var,font=('helvetica',15,'bold'),bg='white',bd=2,relief= RIDGE,width=8)
        refno_box.place(x=135,y=80)

            #medicine name
        med_lbl= Label(rightSF, text='Medicine Name:',pady=6,font=('helvetica',12,'bold'))
        med_lbl.place(x=0,y=110)
            #entry-box
        med_entry= Entry(rightSF,textvariable=self.MedName_var,font=('helvetica',12,'bold'), bg='white',bd=2,relief= RIDGE,width=10)
        med_entry.place(x=135,y=115)

        # Adding the entry-table
                #creating the frame
        table_frame= Frame(rightSF, bd=4, relief=RIDGE)
        table_frame.place(x=0,y=150, width=240,height=160)
        
        sc_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(table_frame,column=("ref","med-name"), xscrollcommand= sc_x.set,yscrollcommand= sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading('ref',text="Reference")
        self.medicine_table.heading('med-name',text="Medicine-Name")
        
        self.medicine_table["show"]="headings"   
        self.medicine_table.pack(fill=BOTH, expand=1)
        
        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("med-name", width=100)  

        #binding the function of cursor to the ref and med rows to accept the data on while using cursor 
        self.medicine_table.bind("<ButtonRelease-1",self.Medget_cursor)

        #ADDING THE BUTTONS
                # creating the frame to set the buttons

        frame=Frame(rightSF,bd=4, relief=RIDGE, bg='#F4C2C2')
        frame.place(x=250, y=150, width=108,height=140)

                #adding the buttons
        add_btn= Button(frame,text='ADD',command=self.addbtn,bg='#FFD700',width=9,fg='black',font=('helvetica',12,'bold'))
        add_btn.grid(row=0,column=0)

        update_btn= Button(frame,command=self.updateMed,text='UPDATE',bg='#FFD700',width=9,fg='black',font=('helvetica',12,'bold'))
        update_btn.grid(row=1,column=0)

        delete_btn= Button(frame,command=self.DeleteMed,text='DELETE',bg='red',width=9,fg='black',font=('helvetica',12,'bold'))
        delete_btn.grid(row=2,column=0)

        clear_btn= Button(frame,command=self.clear_btn, text='CLEAR',bg='#FFD700',width=9,fg='black', font=('helvetica',12,'bold'))
        clear_btn.grid(row=3,column=0)
        
        

#ADDING BUTTONS FRAME TO THE BOTTOM
        btnframe=Frame(self.root,bd=15,relief=GROOVE,padx=20)
        btnframe.place(x=0,y=485,width=1280,height=65)
        
        #------------------ADDING THE BUTTONS------------------------
        #add-button
        addbtn=Button(btnframe,command=self.AddMed_btn,text="ADD-MEDICINE",font=("helvetica",12,"bold"),bg="#FFD700",fg="black")
        addbtn.grid(row=0,column=0)
        #update-button
        updatebtn=Button(btnframe,command=self.updateMed,text="UPDATE",font=("helvetica",12,"bold"),bg="#FFD700",fg="black")
        updatebtn.grid(row=0,column=1)
        #delete-button
        deletebtn=Button(btnframe,command=self.DeleteMed,text="DELETE",font=("helvetica",12,"bold"),bg="RED",fg="black")
        deletebtn.grid(row=0,column=2)
        #reset-button
        resetbtn=Button(btnframe,text="RESET",font=("helvetica",12,"bold"),bg="#FFD700",fg="black")
        resetbtn.grid(row=0,column=3)
        #exit-button
        exitbtn=Button(btnframe,text="EXIT",font=("helvetica",12,"bold"),bg="#FFD700",fg="black")
        exitbtn.grid(row=0,column=4)
        #search-button
        searchlbl=Label(btnframe,font=("helvetica",17,"bold"),text="SEARCH BY",padx=2,relief=SUNKEN,bg="black",fg="white")
        searchlbl.grid(row=0,column=5,sticky=NW)

        #reference combo-box

        #making the variable for search by button
        self.search_var=StringVar()
        ref_combobox=ttk.Combobox(btnframe,textframe=self.search_var,width=12,font=("helvetica",17,"bold"),state="readonly")
        ref_combobox["values"]=("Ref","medname","Lot")
        ref_combobox.current(0)
        ref_combobox.grid(row=0,column=6)
        #searchbox

        #variable for the box
        self.searchbox_var=StringVar()
        searchbox=Entry(btnframe,textvariable=self.searchbox_var,bd=3,relief=RIDGE,width=12,font=("helvetica",17,"bold"))
        searchbox.grid(row=0,column=7)
        #search-button
        searchbtn=Button(btnframe,command=self.search,text="SEARCH",font=("helvetica",13,"bold"),width=14,bg="#FFD700",fg="black")
        searchbtn.grid(row=0,column=8)
        #show-all-button
        showallbtn=Button(btnframe,command=self.fetch_data,text="SHOW ALL",font=("helvetica",13,"bold"),width=14,bg="#FFD700",fg="black")
        showallbtn.grid(row=0,column=9)

# DATABASE SECTION

#ADDING THE DATABASE FRAME
        database_frame=Frame(self.root, bd=15, relief=RIDGE)
        database_frame.place(x=0,y=550, width=1500,height=140)

#MAIN TABLE AND SCROLLBAR
        table_frame=Frame(database_frame,bd=0, relief=FLAT)
        table_frame.place(x=0,y=0,width=1250,height=100)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.pharmacy_table=ttk.Treeview(table_frame, column=("ref","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideeffect","warning","dosage","price",
                                                              "productqt"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                                        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=BOTTOM, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table['show']="headings"
        
        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Med Type")
        self.pharmacy_table.heading("tabletname",text="Medicine Name")
        self.pharmacy_table.heading("lotno",text="Lot No.")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry-Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side-Effect")
        self.pharmacy_table.heading("warning",text="Prec & Wrning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product QTs")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_datamed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

#----------------------------------------------CREATING THE FUNCTIONS NEEDED-------------------------------
                        #functions for RHS buttons
        def addbtn(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO  pharmacy (Ref,MedName) VALUES(%s,%s)",(
                                                                self.refno_var.get(),
                                                                self.MedName_var.get()
                                                        ))
                conn.commit()
                self.fetch_datamed()
                self.Medget_cursor()
                conn.close()
                messagebox.showinfo("success","Medicine added")

                        #to fetch the data and present it in the table on rhs

        def fetch_datamed(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM pms")
                rows=my_cursor.fetchall()

                if len(rows)!=0:
                        self.medicine_table.delete(*self.medicine_table.get_children())
                        self.medicine_table.insert("",END,values=i)
                        conn.connect()
                conn.close()        

                        #to get the cursor function in table 
        def Medget_cursor(self,event=""):
                cursor_row=self.medicine_table.focus()
                content=self.medicine_table.item(cursor_row)
                row=content["values"]
                self.refno_var.set(row[0])
                self.MedName_var.set(row[1])

                        #update function 
        def updateMed(self):
                if self.refno_var.get()=="" or self.MedName_var=="":
                        messagebox.showerror("Error","all fields are required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                        my_cursor.cursor()
                        my_cursor.execute("update Pharmacy set MedName=%s where Ref=%s",(
                                                                self.MedName_var.get(),
                                                                self.refno_var.get()
                        
                        ))
                conn.commit()
                conn.fetch_datamed()
                conn.close()
                messagebox.showinfo("success","medicine Updated")

                        #function to delete the data
        def DeleteMed(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                my_cursor.cursor()
                sql="delete from pharmacy where Ref=%s"
                val=(self.refno_var.get(),)
                my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_datamed()
        conn.close()

                        # function for clear button
        def clear_btn(self):
                self.refno_var.set("")
                self.MedName_var.set("")

#----------------------------------------------FUNCTIONS FOR MAJOR TABLE-------------------------------
        #function for add button

        def AddMed_btn(self):
                if self.ref_var.get()=="" or self.LotNo_var.get()=="":
                        messagebox.showerror("error","all fields are required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                        my_cursor=conn.cursor()
                        my_cursor.execute("INSERT INTO  majortable  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.ref_var.get(),
                                                                                        self.CompName_var.get(),
                                                                                        self.MedType_var.get(),
                                                                                self.TabletName_var.get(),
                                                                                        self.LotNo_var.get(),
                                                                                self.IssueDate_var.get(),
                                                                                        self.ExpDate_var.get(),
                                                                                        self.uses_var.get(),
                                                                                self.sideeffect_var.get(),
                                                                                        self.precNwar_var.get(),
                                                                                        self.dosage_var.get(),
                                                                                        self.Price_var.get(),
                                                                                        self.ProductQT_var.get()
                                                                ))

                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("success","Medicine added")

        #function to fetch the data so that it can be displayed on the screen

        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM majortable")
                row=my_cursor.fetchall()

                if len(row)!=0:
                        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                        for i in row:
                                self.pharmacy_table.insert("",END,values=i)
                        conn.commit()
                conn.close()  

                #function to connect via cursor between the table and the netry fields (same as that on the rhs using bind function)

        def get_cursor(self,ev=""):
                cursor_row=self.medicine_table.focus()
                content=self.medicine_table.item(cursor_row)
                row=content["values"]

                self.ref_var.set(row[0]),
                self.CompName_var.set(row[1]),
                self.MedType_var.set(row[2]),
                self.TabletName_var.set(row[3]),
                self.LotNo_var.set(row[4]),
                self.IssueDate_var.set(row[5]),
                self.ExpDate_var.set(row[6]),
                self.uses_var.set(row[7]),
                self.sideeffect_var.set(row[8]),
                self.precNwar_var.set(row[9]),
                self.dosage_var.set(row[10]),
                self.Price_var.set(row[11]),
                self.ProductQT_var.set(row[12]),

                #function for update button
                #same as that of above
        def updateMed(self):
                if self.ref_var.get()=="" or self.LotNo_var=="":
                        messagebox.showerror("Error","all fields are required")
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                        my_cursor.cursor()
                        my_cursor.execute("update Pharmacy set compName=%s,MedType=%s,TabletName=%s,LotNo.%s,IssueDate=%s,ExpDate=%s,sideEffect=%s,Prec&Warn=%s,Dosage=%s,Price=%s,Product QT=&s where refNo=%s",(
                                                                                        
                                                                                        self.CompName_var.get(),
                                                                                        self.MedType_var.get(),
                                                                                self.TabletName_var.get(),
                                                                                        self.LotNo_var.get(),
                                                                                self.IssueDate_var.get(),
                                                                                        self.ExpDate_var.get(),
                                                                                        self.uses_var.get(),
                                                                                self.sideeffect_var.get(),
                                                                                        self.precNwar_var.get(),
                                                                                        self.dosage_var.get(),
                                                                                        self.Price_var.get(),
                                                                                self.ProductQT_var.get(),
                                                                                        self.ref_var.get()
                        
                        ))
                conn.commit()
                conn.fetch_data()
                conn.close()
                messagebox.showinfo("ipdate","medicine has been updated successfully")

        #delete button function
        def DeleteMed(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                my_cursor.cursor()
                sql="delete from majortable where refno=%s"
                val=(self.ref_var.get(),)
                my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Delete","Info deleted successfully")

        #reset button  function 
        def reset(self):
                #self.ref_var.set(""),
                self.CompName_var.set(""),
                #self.MedType_var.set(""),
                #self.TabletName_var.set(""),
                self.LotNo_var.set(""),
                self.IssueDate_var.set(""),
                self.ExpDate_var.set(""),
                self.uses_var.set(""),
                self.sideeffect_var.set(""),
                self.precNwar_var.set(""),
                self.dosage_var.set(""),
                self.Price_var.set(""),
                self.ProductQT_var.set("")

        def search(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Sharma9077@@",database="pms")
                my_cursor.cursor()
                my_cursor.execute("select * from pharmacy where"+str(self.search_var.get())+"LIKE"+str(self.searchbox_var.get())+"%")

                rwos=my_cursor.fetchall()
                if len(rows)!=0:
                        self.pharmacy_table.delete(*self.pharamcy_table.get_children())
                        for i in rows:
                                self.pharamcy_table.insert("",END,values=i)
                        conn.commit()
                conn.close()
#closing the window
if __name__=="__main__":
    root=Tk()
    obj=Pharmacymanagementsystem(root)
    root.mainloop()