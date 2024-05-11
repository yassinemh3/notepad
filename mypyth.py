from tkinter import*
from tkinter import filedialog

root=Tk()
root.geometry('600x600')
root.title("Notepad")
root.config(bg='#000000')
root.resizable(False,False)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('textfiles','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

def delete_file():
    entry.delete(1.0,END)

def select_file():
    entry.tag_add(SEL, "1.0", END)
    entry.mark_set(INSERT, "1.0")
    entry.see(INSERT)


b1=Button(root,width='20',height='2',bg='#9FE2BF',text='save file',command=save_file).place(x=0,y=5)
b2=Button(root,width='20',height='2',bg='#9FE2BF',text='open file',command=open_file).place(x=150,y=5)
b3=Button(root,width='20',height='2',bg='#9FE2BF',text='delete file',command=delete_file).place(x=300,y=5)
b4=Button(root,width='20',height='2',bg='#9FE2BF',text='select file',command=select_file).place(x=450,y=5)
entry=Text(root,height='33',width='72',wrap=WORD,bg='#00FFFF')
entry.place(x=10,y=60)



root.mainloop()
