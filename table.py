
from tkinter import *
from tkinter import ttk

import sqlite3

class product:
    dbase = 'database.sqlite3'

    def __init__(self, window):

        self.wind = window
        self.wind.title("Products Application")

        frame = LabelFrame(self.wind, text = "Create a new product")
        frame.grid(row=0, column=0, columnspan= 5, pady=20)

        Label(frame, text="name: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1,column=1)

        Label(frame, text='Price: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        ttk.Button(frame, text='Save').grid(row=3, columnspan=2, sticky= W+E) 
        
        self.tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2'))
        self.tree.grid(row=4, column=0, columnspan=4)

        self.tree.heading('#0', text='Product', anchor=CENTER)
        self.tree.heading('#1', text='Price', anchor=CENTER)
        self.tree.heading('#2', text='Categoria', anchor=CENTER)
        self.tree.heading('#3', text='Tipo de iva', anchor=CENTER)
        
        self.get_product(self)


    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.dbase) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_product(self, query):

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        query ='SELECT articulo, precio, categoria FROM virtualWaiter_articulos JOIN virtualWaiter_categoria ON categoria =virtualWaiter_categoria.categoria' #LEFT JOIN virtualWaiter_iva AS i ON a.iva_id=i.tipo_de_iva'
        dbrows = self.run_query(query)
        for rows in dbrows:
            self.tree.insert('',0, text=rows[0], value=(rows[1], rows[2]))
            print(rows)


if __name__ == '__main__':

    window =Tk()
    aplication =product(window) 
    window = mainloop()




