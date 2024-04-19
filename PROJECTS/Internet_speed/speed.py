from tkinter import *
import speedtest

def speed_check():
    st = speedtest.Speedtest()
    st.get_servers()
    down = str(round(st.download() / (10**6), 3)) + "Mbps"
    up = str(round(st.upload() / (10**6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("INTERNET SPEED TEST")
sp.geometry("500x350")
sp.config(bg="blue")

lab = Label(sp, text="Internet speed", font=("Time New Roman", 25, "bold"), bg="blue", fg="green")
lab.place(x=100, y=20, height=30, width=300)

lab = Label(sp, text="Download speed", font=("Time New Roman", 20, "bold"), bg="white")
lab.place(x=100, y=80, height=30, width=300)

lab_down = Label(sp, text="00", font=("Time New Roman", 20, "bold"), fg="white", bg="blue")
lab_down.place(x=100, y=130, height=30, width=300)

lab = Label(sp, text="Upload speed", font=("Time New Roman", 20, "bold"), bg="white")
lab.place(x=100, y=190, height=30, width=300)

lab_up = Label(sp, text="00", font=("Time New Roman", 20, "bold"), fg="white", bg="blue")
lab_up.place(x=100, y=240, height=30, width=300)

button = Button(sp, text="Check Speed", font=("Time New Roman", 15, "bold"), fg="white", bg="red", relief=RAISED, command=speed_check)
button.place(x=150, y=300, height=30, width=200)

sp.mainloop()
