import Tkinter


top = Tkinter.Tk()
top.geometry('250x150')
label = Tkinter.Label(top, text='Hello World')
quit = Tkinter.Button(top, text='quit', command=top.quit, bg='red', fg='white')
label.pack()
quit.pack(fill=Tkinter.X, expand=1)
Tkinter.mainloop()
