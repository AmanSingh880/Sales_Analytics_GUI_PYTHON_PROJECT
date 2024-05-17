from tkinter import *
import os
root = Tk()
root.title("Sales Analytics")
root.geometry('1200x800')
root.configure(bg='#1c1c1c')
canvas = Canvas(root, width=1200, height=800)
canvas.pack(fill='both', expand=True)

# Gradient background function
def create_gradient(canvas, color1, color2):
    for i in range(800):
        r, g, b = (
            int(color1[1:3], 16) * (800 - i) // 800 + int(color2[1:3], 16) * i // 800,
            int(color1[3:5], 16) * (800 - i) // 800 + int(color2[3:5], 16) * i // 800,
            int(color1[5:7], 16) * (800 - i) // 800 + int(color2[5:7], 16) * i // 800,
        )
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, 1200, i, fill=color)
create_gradient(canvas, "#2e2e2e", "#1c1c1c")
def nex():
    os.system("login.py")
l1 = Label(root, text=" WELCOME TO SALES ANALYTIC ", font=("Helvetica", 40, "bold"), bg='#1c1c1c', fg="#f1c40f")
l1.place(x=100, y=100)


b=Button(root,text="Start",fg="white", font=("Helvetica", 25, "bold"), relief=FLAT,bg="blue",command=nex).place(x=450,y=300,width=200,height=100)
l10 = Button(root, text="Exit", bg="blue", fg="white",font=("Helvetica", 15, "bold"), command=root.destroy)
l10.place(x=50, y=650,width=100,height=80)
root.mainloop()
