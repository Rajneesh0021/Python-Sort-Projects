from tkinter import *
import os


def restart():
    os.system('shutdown /r /t 1')

def restart_time():
    os.system('shutdown /r /t 20')

def logout():
    os.system('shutdown -l')

def shutdown():
    os.system('shutdown /s /t 1')


st= Tk()
st.title("SHUTDOWN APP")
st.geometry("500x500")
st.config(bg="Green")

r_button= Button(st,text="RESTART",font=("Times New Roman",10,"bold"),relief=RAISED,cursor="Plus",command=restart)
r_button.place(x=150,y=20,height=60,width=200)

rt_button= Button(st,text="RESTART-TIME",font=("Times New Roman",10,"bold"),relief=RAISED,cursor="Plus",command=restart_time)
rt_button.place(x=150,y=100,height=60,width=200)

lg_button= Button(st,text="LOG-OUT",font=("Times New Roman",10,"bold"),relief=RAISED,cursor="Plus",command=logout)
lg_button.place(x=150,y=180,height=60,width=200)

st_button= Button(st,text="SHUT-DOWN",font=("Times New Roman",10,"bold"),relief=RAISED,cursor="Plus",command=shutdown)
st_button.place(x=150,y=260,height=60,width=200)


st.mainloop()