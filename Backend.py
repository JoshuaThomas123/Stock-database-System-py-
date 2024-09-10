import sqlite3


# backend
# backend is being called from the frontend for each function

# stockData has to create a table if there's none because it has to record the data within the database.
def stockData():
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS stock(id INTEGER PRIMARY KEY,StockID text, RecordDate text, Location text, Type text,Name text, BookCost text,Quantity text,TotalBookCost text, ExtraInfo text)")
    con.commit()
    con.close()

# calls every value as a ? because there should be no values already inputted for new data
def addStockRec(StockID, RecordDate, Location, Type, Name, BookCost, Quantity, TotalBookCost, ExtraInfo):
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("INSERT INTO stock VALUES (NULL,?,?,?,?,?,?,?,?,?) ",
                (StockID, RecordDate, Location, Type, Name, BookCost, Quantity, TotalBookCost, ExtraInfo))
    con.commit()
    con.close()

# all data is selected from the stock database system to be shown
def viewData():
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM stock")
    rows = cur.fetchall()
    con.close()
    return rows

# deleting is identified by a id number shown on the front of each value within the stock details so it can have a separate identity to delete.
def deleteRec(id):
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("DELETE FROM stock WHERE id=?", (id,))
    con.commit()
    con.close()

# data is being searched by introducing them as inputs and then as unknown so the code could find the closest value to our code.
def searchData(StockID="", RecordDate="", Location="", Type="", Name="", BookCost="", Quantity="", TotalBookCost="", ExtraInfo=""):
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM stock WHERE StockID=? OR RecordDate=? OR Location=? OR Type=? OR Name=? OR BookCost=? OR Quantity=? OR TotalBookCost=? OR ExtraInfo=?",
        (StockID, RecordDate, Location, Type, Name, BookCost, Quantity, TotalBookCost, ExtraInfo))
    rows = cur.fetchall()
    con.close()
    return rows

# data is being updated similar to search data but it is called UPDATE within the code.
def dataUpdate(id, StockID="", RecordDate="", Location="", Type="", Name="", BookCost="", Quantity="", TotalBookCost="", ExtraInfo=""):
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("UPDATE stock SET StockID=?, RecordDate=?, Location=?, Type=?,Name=?,BookCost=?,Quantity=?,TotalBookCost=?,ExtraInfo=?,WHERE id=?",
                (StockID, RecordDate, Location, Type, Name, BookCost, Quantity, TotalBookCost, ExtraInfo, id))
    con.commit()
    con.close()


stockData()
