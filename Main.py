#frontend
from tkinter import *
import tkinter.messagebox
import Stock_Backend
class Stock:

    def __init__(self, root):
        self.root = root
        self.root.title("Stock Database Management System")
        self.root.geometry("1517x530+0+0")
        self.root.config(bg="cadet blue")

        StockID = StringVar()
        RecordDate = StringVar()
        Location = StringVar()
        Type = StringVar()
        Name = StringVar()
        BookCost = StringVar()
        Quantity = StringVar()
        TotalBookCost = StringVar()
        ExtraInfo = StringVar()

# --------------------------------------FUNCTIONS-------------------------------------------------------------------
    # yes or a no question to close the program, yes to close, no to not.
        def iExit():
            iExit = tkinter.messagebox.askyesno("Stock Database Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
    # clears data by deleting all of the input/entries on the stock information.
        def clearData():
            self.txtStock_ID.delete(0, END)
            self.txtRecordDate.delete(0, END)
            self.txtLocation.delete(0, END)
            self.txtType.delete(0, END)
            self.txtName.delete(0, END)
            self.txtItemcost.delete(0, END)
            self.txtQuantity.delete(0, END)
            self.txtTotalItemCost.delete(0, END)
            self.txtExtraInfo.delete(0, END)

# called from backend, each input needs to be received and then inserted into the stock database system.
        def addData():
            if(len(StockID.get())!=0):
                Stock_Backend.addStockRec(StockID.get(), RecordDate.get(), Location.get(), Type.get(), Name.get(), BookCost.get(), Quantity.get(), TotalBookCost.get(), ExtraInfo.get())
                stocklist.delete(0, END)
                stocklist.insert(END, (StockID.get(), RecordDate.get(), Location.get(), Type.get(), Name.get(), BookCost.get(), Quantity.get(), TotalBookCost.get(), ExtraInfo.get()))
# called from backend and is shown on the stocklist frame.
        def DisplayData():
            stocklist.delete(0, END)
            for row in Stock_Backend.viewData():
                stocklist.insert(END, row, str(""))
# it makes a event so it can record the values, when clicked on into the stock information.
        def StockRec(event):
            global sd
            searchStock = stocklist.curselection()[0]
            sd = stocklist.get(searchStock)

            self.txtStock_ID.delete(0, END)
            self.txtStock_ID.insert(END, sd[1])
            self.txtRecordDate.delete(0, END)
            self.txtRecordDate.insert(END, sd[2])
            self.txtLocation.delete(0, END)
            self.txtLocation.insert(END, sd[3])
            self.txtType.delete(0, END)
            self.txtType.insert(END, sd[4])
            self.txtName.delete(0, END)
            self.txtName.insert(END, sd[5])
            self.txtItemcost.delete(0, END)
            self.txtItemcost.insert(END, sd[6])
            self.txtQuantity.delete(0, END)
            self.txtQuantity.insert(END, sd[7])
            self.txtTotalItemCost.delete(0, END)
            self.txtTotalItemCost.insert(END, sd[8])
            self.txtExtraInfo.delete(0, END)
            self.txtExtraInfo.insert(END, sd[9])

# called from backend, uses both clear and display to update the new details, when clicked on.
        def DeleteData():
            if(len(StockID.get())!=0):
                Stock_Backend.deleteRec(sd[0])
                clearData()
                DisplayData()
# uses a for loop so it can identify the specific information, that we need to get.
        def searchDatabase():
            stocklist.delete(0, END)
            for row in Stock_Backend.searchData(StockID.get(), RecordDate.get(), Location.get(), Type.get(), Name.get(), BookCost.get(), Quantity.get(), TotalBookCost.get(), ExtraInfo.get()):
                stocklist.insert(END, row, str(""))
# update the system by deleting the previous details but replacing it with new details.
        def update():
            if (len(StockID.get()) != 0):
                Stock_Backend.deleteRec(sd[0])
            if (len(StockID.get()) != 0):
                Stock_Backend.addStockRec(StockID.get(), RecordDate.get(), Location.get(), Type.get(), Name.get(), BookCost.get(),Quantity.get(), TotalBookCost.get(), ExtraInfo.get())
                stocklist.delete(0, END)
                stocklist.insert(END, (StockID.get(), RecordDate.get(), Location.get(), Type.get(), Name.get(), BookCost.get(), Quantity.get(), TotalBookCost.get(), ExtraInfo.get()))
#--------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
 # entries, scroll bar and buttons has to have it's own frame to be able to be displayed.
        MainFrame = Frame(self.root, bg="Antique white3")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=34, pady=1, bg="Antique white3", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame, font=('times new roman', 48, 'bold'), text="     Stock Database Management System                      ",
                            bg="Antique White3")
        self.lblTit.grid()
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=3, pady=3, bg="steel blue1", relief=RIDGE)
        ButtonFrame.pack(side=LEFT)
        lblData = Label(ButtonFrame, font=('times new roman', 18, 'bold'), text="Stock Functions",
                            bg="steel blue1")
        lblData.grid(row=0, column=0)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=600, padx=0, pady=0, relief=RIDGE, bg="Antique white3")
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=0, pady=27, relief=RIDGE, bg="steel blue1",
                                   font=('times new roman', 26, 'bold'), text="Stock Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=27, relief=RIDGE,
                                    bg="ghost white", font=('times new roman', 20, 'bold'), text="Stock Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
        # --------------------------------entries-------------------------------------------------------------------------------------------------
 # all entries are held by data frame left, needs to be identified as a separate string variable.
        self.lblStock_ID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="          Stock ID:   ", padx=2, pady=0,
                                 bg="Sandy Brown")
        self.lblStock_ID.grid(row=0, column=0, sticky=W)
        self.txtStock_ID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=StockID, width=49, bg="gray80")
        self.txtStock_ID.grid(row=0, column=1)

        self.lblRecordDate = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="    Record Date:   ", padx=0,
                                   pady=0, bg="Sandy Brown")
        self.lblRecordDate.grid(row=1, column=0, sticky=W)
        self.txtRecordDate = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=RecordDate,
                                   width=49, bg="gray80")
        self.txtRecordDate.grid(row=1, column=1)

        self.lblLocation = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="          Location:   ", padx=1, pady=0,
                                 bg="Sandy Brown")
        self.lblLocation.grid(row=2, column=0, sticky=W)
        self.txtLocation = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Location, width=49, bg="gray80")
        self.txtLocation.grid(row=2, column=1)

        self.lblType = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="                 Type:   ", padx=0, pady=0,
                             bg="Sandy Brown")
        self.lblType.grid(row=3, column=0, sticky=W)
        self.txtType = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Type, width=49, bg="gray80")
        self.txtType.grid(row=3, column=1)

        self.lblName = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="                Name:  ", padx=2, pady=0,
                             bg="Sandy Brown")
        self.lblName.grid(row=4, column=0, sticky=W)
        self.txtName = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Name, width=49, bg="gray80")
        self.txtName.grid(row=4, column=1)

        self.lblItemcost = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="          Item cost:   ", padx=0, pady=0,
                                 bg="Sandy Brown")
        self.lblItemcost.grid(row=5, column=0, sticky=W)
        self.txtItemcost = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=BookCost, width=49, bg="gray80")
        self.txtItemcost.grid(row=5, column=1)

        self.lblQuantity = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="           Quantity:  ", padx=1, pady=0,
                                 bg="Sandy Brown")
        self.lblQuantity.grid(row=6, column=0, sticky=W)
        self.txtQuantity = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Quantity, width=49, bg="gray80")
        self.txtQuantity.grid(row=6, column=1)

        self.lblTotalItemCost = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Total Item Cost: ",
                                      padx=3, pady=0, bg="Sandy Brown")
        self.lblTotalItemCost.grid(row=7, column=0, sticky=W)
        self.txtTotalItemCost = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=TotalBookCost,
                                      width=49, bg="gray80")
        self.txtTotalItemCost.grid(row=7, column=1)
        self.lblExtraInfo = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="           Extra Info:", padx=0,
                                  pady=0, bg="Sandy Brown")
        self.lblExtraInfo.grid(row=8, column=0, sticky=W)
        self.txtExtraInfo = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=ExtraInfo, width=49, bg="gray80")
        self.txtExtraInfo.grid(row=8, column=1)

        # --------------------------------------scroll bar and list box----------------------------------------------------------------------------
   # where all of the details are displayed.
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        stocklist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        stocklist.bind('<<ListboxSelect>>', StockRec)
        stocklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=stocklist.yview)
        # --------------------------------------buttons-----------------------------------------------------------------------------------------------------------
    # buttons are in the buttonframe and has a separate command which activates, when clicked on(activates the functions).
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=1, width=10,
                                 bd=4, bg="coral1", command=addData)
        self.btnAddData.grid(row=1, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=1,
                                     width=10, bd=4, bg="coral1", command=DisplayData)
        self.btnDisplayData.grid(row=2, column=0)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=1, width=10,
                                   bd=4, bg="coral1", command=clearData)
        self.btnClearData.grid(row=3, column=0)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=1,
                                    width=10, bd=4, bg="coral1", command=DeleteData)
        self.btnDeleteData.grid(row=4, column=0)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=1,
                                    width=10, bd=4, bg="coral1", command=searchDatabase)
        self.btnSearchData.grid(row=5, column=0)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=1,
                                    width=10, bd=4, bg="coral1", command=update)
        self.btnUpdateData.grid(row=6, column=0)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, bg="coral1",
                              command=iExit)
        self.btnExit.grid(row=7, column=0)

if __name__ == '__main__':
    root = Tk()
    application = Stock(root)
    root.mainloop()
