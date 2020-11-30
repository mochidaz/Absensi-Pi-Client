import psycopg2
import tkinter  as tk 
from tkinter import * 
import time 

my_w = tk.Tk()
my_w.geometry("800x600") 
my_connect = psycopg2.connect("dbname=siswadb user=rahman")
my_conn = my_connect.cursor()
####### end of connection ####
while True:
    my_conn.execute("SELECT * FROM kehadiran ORDER BY waktu DESC")
    i=0 
    for student in my_conn: 
        for j in range(len(student)):
            e = Entry(my_w, width=20, fg='white') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    my_w.update()
    time.sleep(7)
