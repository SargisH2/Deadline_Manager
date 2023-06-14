#with txt files
from classes import Task

# line_len=65
add_tasks_file="AddTask.txt"
old_tasks_file="DeadLines.txt"

default_txt_add='''Name[25]_________________|Company[15]____|Compl/All[C/C16]|DeadLine[DD.MM]|Description(optional)
Example Name|My Company|65/100|16.08|My example's description
_____________________________________________________________[65]'''
with open(add_tasks_file, 'r') as file:
    all_lines=file.read().split('\n')
    lines=all_lines[3:]

def lines_to_tasks(txt: list)->list:
    '''from list of lines to list of Tasks'''
    lst=[]
    for make in txt:
        make=make.split('|')
        name = make[0]
        company = make[1]
        dead_time = make[3]
        completed = make[2].split('/')[0]
        all_ = make[2].split('/')[1]
        desc = make[4].strip('\n')
        lst.append(Task(name, company, dead_time, completed, all_, desc))
    return lst

new_tasks_list=lines_to_tasks(lines)

with open(old_tasks_file, 'a') as file:
    write_list=map(lambda x:str(x)+'\n', new_tasks_list)
    file.writelines(write_list)
with open(add_tasks_file, 'w') as file:
    file.write(default_txt_add)
