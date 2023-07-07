from PyQt6.QtWidgets import (QMainWindow, QTableWidget, QVBoxLayout, QWidget, QPushButton, QLineEdit)

class Task:
    NAME_LEN=25
    COM_LEN=15
    def __init__(self, name:str=None, company:str=None, dead_time: str=None, percent:str='0', desc:str='') -> None:
        self._check_all(name, company, percent, dead_time)
        self.__name=name
        self.__desc=desc
        self.__company=company
        self.__dead_time=dead_time
        self.__percent=int(percent)

    def __str__(self) -> str:
        return '|'.join(map(str,self.values()))
    
    def values(self) -> list:
        values_lst = [self.__name, self.__company, str(self.__percent), self.__dead_time, self.__desc]
        return values_lst
    
    @classmethod
    def _check_all(cls, name, company, percent, deadtime) -> None:
        cls._check_name(name)
        cls._check_company(company)
        cls._check_percent(percent)
        cls._check_time(deadtime)
    @classmethod
    def _check_name(cls, name):
        if not(isinstance(name, str) and len(name) <= cls.NAME_LEN) and name!=None:
                raise Exception("Invalid task name")
    @classmethod
    def _check_company(cls, company):
        if not (isinstance(company, str) and len(company) <= cls.COM_LEN) and company!=None:
            raise Exception("Invalid company name")
    @staticmethod
    def _check_percent(percent: str):
        try:
            int(percent)
        except:
            print(percent)
            raise Exception("invalid percent")
    @staticmethod
    def _check_time(date: str):
        if date != None:
            try:
                date=date.split('.')
                flags=[date[0].isnumeric() and 0<int(date[0])<=31, date[1].isnumeric() and 0<int(date[1])<13]
            except:
                raise Exception("Invalid deadline")
            if not all(flags):
                raise Exception("Invalid deadline")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Tasks")
        self.setMinimumSize(550, 250)
        self.main_layout=QVBoxLayout()
        self.buttons=dict()
        
    def create_table(self, h:int, w:int, head:list):
        self._head=head
        table=QTableWidget()
        table.setRowCount(h)
        table.setColumnCount(w)
        table.setHorizontalHeaderLabels(head)
        self.table=table
        self.update(table)
    
    def add_buttons(self, *buttons):
        '''(key, button_text) tuples to buttons'''
        for key, text in buttons:
            button=QPushButton(text)
            self.update(button)
            self.buttons[key]=button

    def update(self, obj):
        self.main_layout.addWidget(obj)
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)


class Window_adding(QWidget):
    def __init__(self, len, height):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.buttons=dict()
        self.setFixedSize(len, height)

    def create_table(self, h:int, w:int, head:list):
        self._head=head
        table=QTableWidget()
        table.setRowCount(h)
        table.setColumnCount(w)
        table.setHorizontalHeaderLabels(head)
        self.table=table

        self.main_layout.addWidget(table)
        self.setLayout(self.main_layout)
        
    def add_buttons(self, *buttons):
        '''(key, button_text) tuples to buttons'''
        for key, text in buttons:
            button=QPushButton(text)

            self.main_layout.addWidget(button)
            self.setLayout(self.main_layout)
            self.buttons[key]=button

    def add_input_area(self):
        input=QLineEdit(self)
        self.input_area=input

        self.main_layout.addWidget(input)
        self.setLayout(self.main_layout)
        