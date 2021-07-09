# TODO import modules
from tkinter import *
import os
import timeit

start = timeit.default_timer()
# TODO create basic gui
root = Tk()
root.title("Everything")
root.iconbitmap(r"C:\everything.ico")
root.geometry("1020x720")

# TODO indexing pdf file in a directory
all_files = [os.path.join(file) for root, directory, files in os.walk(
    r"E:") for file in files if file.endswith('.pdf')]


# TODO update the listbox
def update(data):
    listbox.delete(0, END)
    for item in data:
        listbox.insert(END, item)


# TODO update entry box
def fill_out(event):
    entry_box.delete(0, END)
    entry_box.insert(0, listbox.get(ANCHOR))


# TODO check entry
def check(event):
    typed = entry_box.get()
    if typed == "":
        data = all_files
    else:
        data = []
        for item in all_files:
            if typed.lower() in item.lower():
                data.append(item)

    update(data)


# TODO create entry box
entry_box = Entry(root, width=400)
entry_box.pack(padx=5)

end = timeit.default_timer()
duration = (end-start)


# TODO create a label showing the number of files
label = Label(root, anchor='sw', justify="left", text=f'Number of files {len(all_files)}... indexed in {round(duration, 2)}')
label.pack(fill='both')

# TODO create the listbox
listbox = Listbox(root, width=400, height=400)
listbox.pack(pady=5, padx=5)

# TODO attach a scroll bar to the list box
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcomman=scrollbar.set)
scrollbar.config(command=listbox.yview)


update(all_files)
listbox.bind('<<ListBoxSelect>>', fill_out)

entry_box.bind("<KeyRelease>", check)


# TODO run the gui
root.mainloop()

