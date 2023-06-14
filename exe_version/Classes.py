from PyQt6.QtWidgets import (QWidget, QTableWidget, QVBoxLayout)

class Task:
    NAME_LEN=25
    COM_LEN=15
    def __init__(self, name:str=None, company:str=None, dead_time: str=None, percent:int=0, desc:str='') -> None:
        '''Name[25], Company[15], Compl/All[16], DeadLine[DD.MM]'''
        self._check_all(name, company, percent, dead_time)
        self.__name=name
        self.__desc=desc
        self.__company=company
        self.__dead_time=dead_time
        self.__percent=percent

    def __str__(self) -> str:
        return '|'.join(map(str,self.values()))
    
    def values(self) -> list:
        values_lst = [self.__name, self.__company, self.__percent, self.__dead_time, self.__desc]
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
    def _check_percent(percent: int):
        try:
            int(percent)
        except:
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


class Window(QWidget):
    def __init__(self, window_name):
        super().__init__()
        self.setWindowTitle(window_name)
        self.setMinimumSize(400, 250)
        self.show()
 
    def CreateTable(self, rows, columns):
        self.table = QTableWidget(rows, columns)
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)