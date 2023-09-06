import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

#tasks=[]
def add_task():
    task_string=task_field.get()
    if len(task_string)==0:
        messagebox.showinfo('Error','Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        list_update()
        task_field.delete(0,'end')
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end',task)
def delete_task():
    try:
        value=task_listbox.get(task_listbox.curselection())
        if value in tasks:
            tasks.remove(value)
            list_update()
            the_cursor.execute('delete from tasks where title=?',(value,))
    except:
        messagebox.showinfo('Error','No task is selected, cannot delete')
def delete_all_tasks():
    message_box=messagebox.askyesno('Delete all','Are you sure?')
    if message_box==True:
        while(len(tasks)!=0):
            tasks.pop()
            the_cursor.execute('delete from tasks')
            list_update()
def clear_list():
    task_listbox.delete(0,'end')
def close():
    print(tasks)
    guiWindow.destroy()
def retrieve_database():
    while(len(tasks)!=0):
        tasks.pop()
    for row in the_cursor.execute('Select title from tasks'):
        tasks.append(row[0])

#main function
if __name__=="__main__":
    guiWindow=tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0,0)
    guiWindow.configure(bg="white")
    the_connection=sql.connect("listOfTasks.db")
    the_cursor=the_connection.cursor()
    the_cursor.execute('Create table if not exists tasks(title text)')
    tasks=[]
    header_frame=tk.Frame(guiWindow,bg="white")
    functions_frame=tk.Frame(guiWindow,bg="#87CEEB")
    listbox_frame=tk.Frame(guiWindow,bg="#87CEEB")
    header_frame.pack(fill="both")
    functions_frame.pack(side="left",expand=True,fill="both")
    listbox_frame.pack(side="right",expand=True,fill="both")
    header_label=ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Bold","30"),
        background="white",
        foreground="#87CEEB"
    )

    header_label.pack(padx=20,pady=20)
    task_label=ttk.Label(
        functions_frame,
        
        text="Enter the task",
        font=("Consolas","11","bold"),
          background = "#87CEEB",  
            foreground = "white"  
    )
    task_label.place(x=30,y=40)
    task_field = ttk.Entry(  
    functions_frame,  
    font = ("Consolas", "12"),  
    width = 18,  
    background = "white",  
    foreground = "#87CEEB"  
    )  
    task_field.place(x=30,y=80)
    add_button = ttk.Button(  
    functions_frame,  
    text = "Add Task",
    width = 24,  
    command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task", 
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)   
    task_listbox = tk.Listbox(  
    listbox_frame,  
    width = 27,  
    height = 17,  
    selectmode = 'SINGLE',  
    background = "white",  
    foreground = "white",  
    selectbackground = "white",  
    selectforeground = "white"  
    )
    task_listbox.place(x=10,y=20)  
    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()