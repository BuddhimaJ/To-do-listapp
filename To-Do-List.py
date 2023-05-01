from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-Application',font='ariel, 25 bold', width=10,bd=5,bg='Blue',fg='white')#bd means boarder width
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',font='ariel, 18 bold', width=10,bd=5,bg='Blue',fg='white')#bd means boarder width
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',font='ariel, 18 bold', width=10,bd=5,bg='Blue',fg='white')#bd means boarder width
        self.label3.place(x=340, y=54)

        self.main_Text =Listbox(self.root, height=9, bd=5, width=23, font='ariel, 20 italic bold')
        self.main_Text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='arial, 10 bold')
        self.text.place(x=20, y=120)

        #add text
        def add():
            content = self.text.get(1.0,END)
            self.main_Text.insert(END,content)
            with open('data.txt','a')as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)

        def delete():
            delete = self.main_Text.curselection()
            look = self.main_Text.get(delete)
            with open('data.txt','r+')as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_Text.delete(delete)

        with open(r'E:\Phython\data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_Text.insert(END, ready)
            file.close()

        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',width=10, bd=5,bg='blue', fg='white',command = add)
        self.button.place(x=30, y=200)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',width=10, bd=5,bg='blue', fg='white',command = delete)
        self.button2.place(x=30, y=300)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ =="__main__":
    main()