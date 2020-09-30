from tkinter import *
import json
from difflib import get_close_matches

root = Tk()
root.geometry("700x400")
root.resizable(width=False,height=False)
root.configure(bg="light sky blue")
root.title("Sahil's Dictionary")

data = json.load(open("data.json"))


def translate():
    text = word.get()
    text = text.lower()
    if text in data:
        r = data[text]
        list.delete(0, END)
        # list.insert(END, r)
        for text in r:
            list.insert(END,text)
    elif text.title() in data:
        r = data[text.title()]
        list.delete(0, END)
        for text in r:
            list.insert(END, text)
    elif text.upper() in data:
        r = data[text.upper()]
        list.delete(0, END)
        for text in r:
            list.insert(END, text)
    elif len(get_close_matches(text, data.keys())) > 0:
        print("did you mean %s instead" %
              get_close_matches(word, data.keys())[0])
       decide = input("press y for yes or n for no")
       if decide == "y":
           return data[get_close_matches(text, data.keys())[0]]
       elif decide == "n":
           return("Sorry! We can't find one ")
       else:
           return("You have entered wrong input please enter just y or n")
    else:
        list.delete(0, END)
        list.insert(END, "Sorry! We can't find one")





l1 = Label(root,text='I am a dictionary',padx=2,pady=4,font="lucida 10 bold")
l1.pack(ipady=2)

word = StringVar()
e = Entry(root,textvariable=word,width=50,font="lucida 10 bold")
e.pack(ipadx=5,ipady=8,pady=30)

b = Button(root, text='Search', font="lucida 10 bold", command=translate)
b.pack(pady=15)

scrollbar = Scrollbar(root,orient=HORIZONTAL)
scrollbar.pack(side=BOTTOM, fill=X)

list = Listbox(root, width=125, height=5, xscrollcommand=scrollbar.set)
list.pack(expand=YES,fill=BOTH)

scrollbar.config(command=list.xview)




root.mainloop()
