class Task:
    NAME_LEN=25
    COM_LEN=15
    def __init__(self, name:str, company:str, dead_time: str, completed:int=0, all_: int=100, desc:str='') -> None:
        '''Name[25], Company[15], Compl/All[16], DeadLine[DD.MM]'''
        self._check_all(name, company, completed, all_, dead_time)
        self.__name=name
        self.__desc=desc
        self.__company=company
        self.__dead_time=dead_time
        self.__completed=completed
        self.__all_=all_

    def __str__(self) -> str:
        attrs=[self.__name+(self.NAME_LEN-len(self.__name))*'_',\
               self.__company+(self.COM_LEN-len(self.__company))*'_',\
                f"{self.__completed}/{self.__all_}",\
                self.__dead_time, self.__desc]
        return '|'.join(attrs)
        
    @classmethod
    def _check_all(cls, name, company, percent1, percent2, deadtime) -> None:
        cls._check_name(name)
        cls._check_company(company)
        cls._check_percent(percent1)
        cls._check_percent(percent2)
        cls._check_time(deadtime)
    @classmethod
    def _check_name(cls, name):
        if not(isinstance(name, str) and len(name) <= cls.NAME_LEN):
            raise Exception("Invalid task name")
    @classmethod
    def _check_company(cls, company):
        if not (isinstance(company, str) and len(company) <= cls.COM_LEN):
            raise Exception("Invalid company name")
    @staticmethod
    def _check_percent(percent: int):
        if not percent.isnumeric():
            raise Exception("invalid percent")
    @staticmethod
    def _check_time(date: str):
        date=date.split('.')
        flags=[date[0].isnumeric() and 0<int(date[0])<=31, date[1].isnumeric() and 0<int(date[1])<13]
        if not all(flags):
            raise Exception("Invalid deadline")
