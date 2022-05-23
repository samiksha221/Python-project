from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # ===========variables=====
        # ===========grocerry=====
        self.sugar = IntVar()
        self.oil = IntVar()
        self.rice = IntVar()
        self.daal = IntVar()
        self.coffee = IntVar()

        # ======Icecream=======
        self.Vanilla = IntVar()
        self.chocolate = IntVar()
        self.strawberry = IntVar()
        self.butterscotch = IntVar()
        self.choco_chip = IntVar()

        # ======Homeappliances====
        self.LCD = IntVar()
        self.Cooler = IntVar()
        self.mobile = IntVar()
        self.Refrigerator = IntVar()
        self.laptops = IntVar()

        # ======Total product price & Tax variable==
        self.grocerry_price = StringVar()
        self.Icecream_price = StringVar()
        self.Homeappliance_price = StringVar()

        self.grocerry_tax = StringVar()
        self.Icecream_tax = StringVar()
        self.Homeappliances_tax = StringVar()

        # =====Customer====
        self.c_name = StringVar()
        self.c_phon = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ===========Customer Detail Name
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="customer Details", font=("Times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphn_lbl = Label(F1, text="phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                            column=3,
                                                                                                            pady=5,
                                                                                                            padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="search", width=10, bd=7, font="aerial 12 bold").grid(row=0, column=6, padx=10,
                                                                                         pady=10)

        # =============Grocerry

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocerry", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        sugar_lbl = Label(F2, text="sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        sugar_txt = Entry(F2, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        oil_lbl = Label(F2, text="oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        oil_txt = Entry(F2, width=10, textvariable=self.oil, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        rice_lbl = Label(F2, text="rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        rice_txt = Entry(F2, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        daal_lbl = Label(F2, text="daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        daal_txt = Entry(F2, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        coffee_lbl = Label(F2, text="coffee", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        coffee_txt = Entry(F2, width=10, textvariable=self.coffee, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        # =============Icecreams

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Icecream", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        Vanilla_lbl = Label(F3, text="Vanilla", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Vanilla_txt = Entry(F3, width=10, textvariable=self.Vanilla, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        chocolate_lbl = Label(F3, text="chocolate", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        chocolate_txt = Entry(F3, width=10, textvariable=self.chocolate, font=("times new roman", 16, "bold"), bd=5,
                              relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        strawberry_lbl = Label(F3, text="strawberry", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        strawberry_txt = Entry(F3, width=10, textvariable=self.strawberry, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        butterscotch_lbl = Label(F3, text="butterscotch", font=("times new roman", 16, "bold"), bg=bg_color,
                                 fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        butterscotch_txt = Entry(F3, width=10, textvariable=self.butterscotch, font=("times new roman", 16, "bold"),
                                 bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        choco_chip_lbl = Label(F3, text="choco_chip", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        choco_chip_txt = Entry(F3, width=10, textvariable=self.choco_chip, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        # =============Homeappliances

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Homeappliances", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        LCD_lbl = Label(F4, text="LCD", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        LCD_txt = Entry(F4, width=10, textvariable=self.LCD, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        cooler_lbl = Label(F4, text="cooler", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        cooler_txt = Entry(F4, width=10, textvariable=self.Cooler, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        mobile_lbl = Label(F4, text="mobile", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        mobile_txt = Entry(F4, width=10, textvariable=self.mobile, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        Refrigerator_lbl = Label(F4, text="Refrigerator", font=("times new roman", 16, "bold"), bg=bg_color,
                                 fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Refrigerator_txt = Entry(F4, width=10, textvariable=self.Refrigerator, font=("times new roman", 16, "bold"),
                                 bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        laptops_lbl = Label(F4, text="laptops", font=("times new roman", 16, "bold"), bg=bg_color,
                            fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        laptops_txt = Entry(F4, width=10, textvariable=self.laptops, font=("times new roman", 16, "bold"), bd=5,
                            relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        # ============Bill Area=========
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
        bill_title = Label(F5, text="bill Area", font="Aerial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_Y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_Y.set)
        scrol_Y.pack(side=RIGHT, fill=Y)
        scrol_Y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ===== Button Frame=====
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="total grocerry price", font=("times new roman", 14, "bold")).grid(row=0, column=0,
                                                                                                   padx=20, pady=1,
                                                                                                   sticky="W")
        m1_txt = Entry(F6, width=18, textvariable=self.grocerry_price, font="arial  10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="total Icecream price", font=("times new roman", 14, "bold")).grid(row=1, column=0,
                                                                                                   padx=20, pady=1,
                                                                                                   sticky="W")
        m2_txt = Entry(F6, width=18, textvariable=self.Icecream_price, font="arial  10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="total Homeappliance  price", font=("times new roman", 14, "bold")).grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=20,
                                                                                                         pady=1,
                                                                                                         sticky="W")
        m3_txt = Entry(F6, width=18, textvariable=self.Homeappliance_price, font="arial  10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="grocerry Tax", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20,
                                                                                           pady=1, sticky="W")
        c1_txt = Entry(F6, width=18, textvariable=self.grocerry_tax, font="arial  10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text=" Icecream Tax", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20,
                                                                                            pady=1, sticky="W")
        c2_txt = Entry(F6, width=18, textvariable=self.Icecream_tax, font="arial  10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text=" Homeappliance Tax", font=("times new roman", 14, "bold")).grid(row=2, column=2,
                                                                                                 padx=20, pady=1,
                                                                                                 sticky="W")
        c3_txt = Entry(F6, width=18, textvariable=self.Homeappliances_tax, font="arial  10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text="total", bg="cadetblue", fg="white", pady=15, bd=2, width=10,
                           font="arial 12 bold").grid(row=0, column=0, padx=5, pady=5)

        Gbill_btn = Button(btn_F, text="Generate bill ", command=self.bill_area, bg="cadetblue", fg="white", pady=15,
                           bd=2, width=10, font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_F, text="clear ", bg="cadetblue", fg="white", pady=15, bd=2, width=10,
                           font="arial 12 bold").grid(row=0, column=2, padx=5, pady=5)

        Exit_btn = Button(btn_F, text="Exit ", bg="cadetblue", fg="white", pady=15, bd=2, width=10,
                          font="arial 12 bold").grid(row=0, column=3, padx=5, pady=5)
        self.Welcome_bill()

    def total(self):
        self.s = self.sugar.get() * 40
        self.o = self.oil.get() * 120
        self.r = self.rice.get() * 50
        self.d = self.daal.get() * 80
        self.c = self.coffee.get() * 20

        self.total_grocerry_price = float(
            self.s +
            self.o +
            self.r +
            self.d +
            self.c
        )

        self.grocerry_price.set("Rs. " + str(self.total_grocerry_price))
        self.g_tax = round((self.total_grocerry_price * 0.05), 2)
        self.grocerry_tax.set("Rs. " + str(self.g_tax))

        self.v = self.Vanilla.get() * 40
        self.c = self.chocolate.get() * 60
        self.s = self.strawberry.get() * 75
        self.b = self.butterscotch.get() * 80
        self.ch = self.choco_chip.get() * 100

        self.total_Icecream_price = float(
            self.v +
            self.c +
            self.s +
            self.b +
            self.ch
        )

        self.Icecream_price.set("Rs. " + str(self.total_Icecream_price))
        self.i_tax = round((self.total_Icecream_price * 0.1), 2)
        self.Icecream_tax.set("Rs. " + str(self.i_tax))

        self.l = self.LCD.get() * 20000
        self.c = self.Cooler.get() * 8000
        self.m = self.mobile.get() * 10000
        self.r = self.Refrigerator.get() * 25000
        self.lp = self.laptops.get() * 30000

        self.total_Homeappliance_price = float(
            self.l +
            self.c +
            self.m +
            self.r +
            self.lp

        )

        self.Homeappliance_price.set("Rs. " + str(self.total_Homeappliance_price))
        self.h_tax = round((self.total_Homeappliance_price * 0.05), 2)
        self.Homeappliances_tax.set("Rs. " + str(self.h_tax))

        self.total_bill = float(self.total_grocerry_price + self.total_Icecream_price +
                                self.total_Homeappliance_price + self.g_tax + self.i_tax + self.h_tax)

    def Welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to  our shop\n")
        self.txtarea.insert(END, f"\n Bill number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number :{self.c_phon.get()}")
        self.txtarea.insert(END, f"\n =================================")
        self.txtarea.insert(END, f"\n products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n =================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        else:
            self.Welcome_bill()

            # =====grocerry =====
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n sugar\t\t{self.sugar.get()}\t\t{self.s}")

            if self.oil.get() != 0:
                self.txtarea.insert(END, f"\n oil\t\t{self.oil.get()}\t\t{self.o}")

            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n rice\t\t{self.rice.get()}\t\t{self.r}")

            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n daal\t\t{self.daal.get()}\t\t{self.d}")

            if self.coffee.get() != 0:
                self.txtarea.insert(END, f"\n coffee\t\t{self.coffee.get()}\t\t{self.c}")

            # =======Icecream ======
            if self.Vanilla.get() != 0:
                self.txtarea.insert(END, f"\n Vanilla\t\t{self.Vanilla.get()}\t\t{self.v}")

            if self.chocolate.get() != 0:
                self.txtarea.insert(END, f"\n chocolate\t\t{self.chocolate.get()}\t\t{self.c}")

            if self.strawberry.get() != 0:
                self.txtarea.insert(END, f"\n strawberry\t\t{self.strawberry.get()}\t\t{self.s}")

            if self.butterscotch.get() != 0:
                self.txtarea.insert(END, f"\n butterscotch\t\t{self.butterscotch.get()}\t\t{self.b}")

            if self.choco_chip.get() != 0:
                self.txtarea.insert(END, f"\n choco_chip\t\t{self.choco_chip.get()}\t\t{self.ch}")

            # ====== Homeappliance======
            if self.LCD.get() != 0:
                self.txtarea.insert(END, f"\n LCD\t\t{self.LCD.get()}\t\t{self.l}")

            if self.Cooler.get() != 0:
                self.txtarea.insert(END, f"\n Cooler\t\t{self.Cooler.get()}\t\t{self.c}")

            if self.mobile.get() != 0:
                self.txtarea.insert(END, f"\n mobile\t\t{self.mobile.get()}\t\t{self.m}")

            if self.Refrigerator.get() != 0:
                self.txtarea.insert(END, f"\n Refrigerator\t\t{self.Refrigerator.get()}\t\t{self.r}")

            if self.laptops.get() != 0:
                self.txtarea.insert(END, f"\n laptops\t\t{self.laptops.get()}\t\t{self.lp}")

            self.txtarea.insert(END, f"\n ------------------------")
            if self.grocerry_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n grocerry tax\t\t\t{self.grocerry_tax.get()}")

            if self.Icecream_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Icecream_tax\t\t\t{self.Icecream_tax.get()}")

            if self.Homeappliances_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Homeappliances_tax\t\t\t{self.Homeappliances_tax.get()}")

            self.txtarea.insert(END, f"\n total Bill :\t\t\t Rs. {self.total_bill}")
            self.txtarea.insert(END, f"\n -------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("save bill ", "do u want to save the bill")
        if op > 0:
            bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(bill_data)

            f1.close()
        else:
            return


root = Tk()
obj = Bill_App(root)
root.mainloop()








