#GUI, .exe
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
import pickle
import sys
from os.path import isfile
from Classes import Task, MainWindow, Window_adding
data_file='data.pickle'
columns=['Name', 'Company', 'Deadline', 'Percent %', 'Description']

def add_data(data:list)->None:
    with open(data_file, 'wb') as f:
        for task in data:
            pickle.dump(task, f)

def get_data()->list:
    data=[]
    with open(data_file, 'rb') as f:
        while True:
            try:
                data.append(pickle.load(f))
            except EOFError:
                data.sort(reverse=True, key=lambda x:int(x.values()[2]))##### percent ############ edit
                return data

def del_data():
    del_win=window.del_window
    name=del_win.input_area.text()#////////////////////////////////////////////need to finish
    print("(not)Deleted!", name)
    del_win.close()

if not isfile(data_file):
    data = []
    add_data(data)
else:
    data=get_data()

table_height=len(data)
table_width=len(columns)

app = QApplication([])
window = MainWindow()

def adding_window():
    window.add_window=Window_adding(550, 200)
    new_window=window.add_window
    new_window.create_table(1, table_width, columns)
    new_window.add_buttons(('save', 'Save'), ('cancel', 'Cancel'))
    new_window.buttons['cancel'].clicked.connect(lambda: new_window.close())
    new_window.buttons['save'].clicked.connect(save_item)
    new_window.show()


def save_item():
    new_task=[]
    for col in range(table_width):
        new_task.append(window.add_window.table.item(0,col).text())
    print(new_task)
    add_data([Task(*new_task)])
    window.add_window.close()

def del_window():
    window.del_window=Window_adding(200, 100)
    new_window=window.del_window
    new_window.add_input_area()
    new_window.add_buttons(('del', 'Delete'), ('cancel', 'Cancel'))
    new_window.buttons['cancel'].clicked.connect(lambda: new_window.close())
    new_window.buttons['del'].clicked.connect(del_data)
    new_window.show()


window.create_table(table_height, table_width, columns)
main_table=window.table
for index, task in enumerate(data):
    row=index
    for col, item in enumerate(task.values()):
        item=QTableWidgetItem(item)
        main_table.setItem(row, col, item)
window.add_buttons(('add', 'Add new task'), ('del', 'Delete task'), ('exit', 'Exit'))
window.buttons['add'].clicked.connect(adding_window)
window.buttons['del'].clicked.connect(del_window)
window.buttons['exit'].clicked.connect(lambda: window.close())
window.show()

sys.exit(app.exec())







