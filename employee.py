from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x7900+0+0")
        self.root.title('Employee Managenent System Of S.S.Shivam Company ')
        
        # variables
        # self.var_dep=String

        lb1_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM OF S.S.SHIVAM COMPANY',font=('times new roman',35,'bold'),fg="grey",bg="white")
        lb1_title.place(x=20,y=0,width=1530,height=50)

        # logo
        img_logo=Image.open('all images/logo.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=0,y=0,width=50,height=50)

        # frame
        img_frame=Frame (self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1 image
        img1=Image.open('all images/em1.jpeg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)


        # 2 image
        img_2=Image.open('all images/emp2.webp')
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        # 3 image
        img_3=Image.open('all images/emp3.jpg')
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)


        # main frame
        main_frame=Frame (self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=220,width=1500,height=560)

        # upper frame
        upper_frame=LabelFrame (main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',14,'bold'),fg="black")
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # labels and entery
        lbl_dep=Label(upper_frame,text="Department:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,font=('arial',12,),width=20,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=50,sticky=W)


        # NAME
        lbl_name=Label(upper_frame,text="Name:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_name.grid(row=0,column=2,padx=2,sticky=W)

        txt_name=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_name.grid(row=0,column=3,padx=50,pady=7)

         # Designition
        lbl_des=Label(upper_frame,text="Designition:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_des.grid(row=1,column=0,padx=2,sticky=W)

        txt_des=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_des.grid(row=1,column=1,padx=2,pady=7)

         # Address
        lbl_address=Label(upper_frame,text="Address:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_address.grid(row=2,column=0,padx=2,sticky=W)

        txt_address=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_address.grid(row=2,column=1,padx=50,pady=10)

         # DOB
        lbl_dob=Label(upper_frame,text="DOB:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_dob.grid(row=3,column=0,padx=2,sticky=W)

        txt_dob=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        # Adhar card
        lbl_adhar=Label(upper_frame,text="Adhar card:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_adhar.grid(row=4,column=0,padx=2,sticky=W)

        txt_adhar=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_adhar.grid(row=4,column=1,padx=2,pady=7)

        # Email
        lbl_mail=Label(upper_frame,text="Email:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_mail.grid(row=1,column=2,padx=2,sticky=W)

        txt_mail=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_mail.grid(row=1,column=3,padx=2,pady=7)

        # Phone
        lbl_phone=Label(upper_frame,text="Phone no:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_phone.grid(row=2,column=2,padx=2,sticky=W)

        txt_phone=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_phone.grid(row=2,column=3,padx=2,pady=7)

        # Country
        lbl_country=Label(upper_frame,text="Country:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_country.grid(row=3,column=2,padx=2,sticky=W)

        txt_country=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_country.grid(row=3,column=3,padx=2,pady=7)

        # DOJ
        lbl_doj=Label(upper_frame,text="DOJ:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_doj.grid(row=4,column=2,padx=2,sticky=W)

        txt_doj=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_doj.grid(row=4,column=3,padx=2,pady=7)

         # Married Status
        lbl_married=Label(upper_frame,text="Married Status:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_married.grid(row=0,column=4,padx=2,sticky=W)

        combo_married=ttk.Combobox(upper_frame,font=('arial',12,),width=20,state='readonly')
        combo_married['value']=('Select','HR','Married','Unmarried')
        combo_married.current(0)
        combo_married.grid(row=0,column=5,padx=50,sticky=W)

         # Gender
        lbl_gender=Label(upper_frame,text="Gender:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_gender.grid(row=1,column=4,padx=2,sticky=W)

        combo_gender=ttk.Combobox(upper_frame,font=('arial',12,),width=20,state='readonly')
        combo_gender['value']=('Select','Male','Female','Other')
        combo_gender.current(0)
        combo_gender.grid(row=1,column=5,padx=50,sticky=W)

        # Salary(CTC)
        lbl_salary=Label(upper_frame,text="Salary(CTC):",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_salary.grid(row=2,column=4,padx=2,sticky=W)

        txt_salary=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_salary.grid(row=2,column=5,padx=50,pady=7)

        # Blood Group
        lbl_bg=Label(upper_frame,text="Blood Group:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_bg.grid(row=3,column=4,padx=4,sticky=W)

        txt_bg=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_bg.grid(row=3,column=5,padx=50,pady=7)


        # PAN No 
        lbl_pn=Label(upper_frame,text="PAN No:",font=('arial ',12,'bold'),fg="BLACK",bg="white")
        lbl_pn.grid(row=4,column=4,padx=2,sticky=W)

        txt_pn=ttk.Entry(upper_frame,width=22,font=("arial",12,"bold"))
        txt_pn.grid(row=4,column=5,padx=50,pady=7)

        # button frame
        button_frame=Frame (upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1250,y=0,width=200,height=200)

        btn_add=Button(button_frame,text='Save',font=("arial",15,"bold"),width=15,bg="gray",fg="white")
        btn_add.grid(row=0,column=0,padx=4,pady=4)

        btn_update=Button(button_frame,text='Update',font=("arial",15,"bold"),width=15,bg="gray",fg="white")
        btn_update.grid(row=1,column=0,padx=4,pady=4)

        btn_delete=Button(button_frame,text='Delete',font=("arial",15,"bold"),width=15,bg="gray",fg="white")
        btn_delete.grid(row=2,column=0,padx=4,pady=4)

        btn_clear=Button(button_frame,text='Clear',font=("arial",15,"bold"),width=15,bg="gray",fg="white")
        btn_clear.grid(row=3,column=0,padx=4,pady=4)



        # down frame
        down_frame=LabelFrame (main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',14,'bold'),fg="black")
        down_frame.place(x=10,y=280,width=1480,height=270)


        # search frame
        search_frame=LabelFrame (down_frame,bd=2,relief=RIDGE,bg='white',text='Search Bar',font=('times new roman',14,),fg="grey")
        search_frame.place(x=4,y=0,width=1470,height=60)

        search_by=Label(search_frame,text="Search By:",font=('arial ',12,'bold'),fg="black",bg="gray")
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        # for search
        combo_txt=ttk.Combobox(search_frame,state='readonly',font=("arial",12,"bold"),width=18)
        combo_txt['value']=('Select','PHONE no','Adhar card','PAN NO','Email')
        combo_txt.current(0)
        combo_txt.grid(row=0,column=1,padx=5,sticky=W)

        txt_search=ttk.Entry(search_frame,width=22,font=("arial",12,"bold"))
        txt_search.grid(row=0,column=2,padx=5,pady=0)

        btn_search=Button(search_frame,text='Search',font=("arial",12,"bold"),width=15,bg="gray",fg="white")
        btn_search.grid(row=0,column=3,padx=5,pady=0)

        btn_showall=Button(search_frame,text='Show All',font=("arial",12,"bold"),width=15,bg="gray",fg="white")
        btn_showall.grid(row=0,column=4,padx=5,pady=0)

       
        btn_txx=Label(search_frame,text='Inner peace is the new success',font=("arial",16,"bold"),fg="black")
        btn_txx.grid(row=0,column=5,padx=160,pady=0)


        # ==========employee table==========
         
        #  table frame
        table_frame=Frame (down_frame,bd=3,relief=RIDGE,)
        table_frame.place(x=2,y=65,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","des","address","dob","adhar card","name","email","phone","country","doj","married","sallary","gender","blood group","pan no",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=BOTTOM,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('des',text='Desginition')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('phone',text='Phone no')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('adhar card',text='Adhar Card')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('sallary',text='Sallary')
        self.employee_table.heading('blood group',text='Blood Group')
        self.employee_table.heading('pan no',text='PAN No')

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("des",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("adhar card",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("sallary",width=100)
        self.employee_table.column("blood group",width=100)
        self.employee_table.column("pan no",width=100)

        


        self.employee_table.pack(fill=BOTH,expand=1)

        






        



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()