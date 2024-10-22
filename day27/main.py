import tkinter

window = tkinter.Tk()
window.minsize(width = 500, height = 300)


my_label = tkinter.Label(text="My Label", font = ("Arial", 24, "italic"))
my_label.pack(side="left")



window.mainloop()