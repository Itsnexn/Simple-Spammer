from os import error
import tkinter as tk
from tkinter import Frame, filedialog, font
from PIL import Image, ImageTk
import webbrowser
import pyautogui
import time

def callback(url):
    webbrowser.open_new(url)

root = tk.Tk()
root.geometry('400x550')

# define font
myFont = font.Font(size=15, weight='bold')
myFont2 = font.Font(size=10, weight='bold')

# Root configuration
root.title('Simple Spam bot')
root.configure(bg='#141414')
root.resizable(width=0, height=0)
f = Frame(root)
f.grid(row=0,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

# logo
logo = Image.open('Logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, background='#141414')
logo_label.image = logo
logo_label.place(x=200, y=175, anchor="center")

# Instraction Label
instraction = tk.Label(root, text='Select a file for spam\n after 5sec bot automatically will\n spam each line where your cursor at ...', background='#141414', fg='#FFFFFF')
instraction['font'] = myFont2
instraction.place(x=200, y=475, anchor="center")

#credit label
link1 = tk.Label(root, text="My Github Page", fg="#BE2E28",bg='#141414', cursor="hand2")
link1.bind("<Button-1>", lambda e: callback("http://github.com/itsnexn"))
link1.place(x=200,y=525, anchor='center')
link1['font'] = myFont2


def main():
    try:
        file_path = filedialog.askopenfilename(title='Open a file for spam', filetypes=(("txt Files", "*.txt"),))
        time.sleep(5)
        with open(file_path, 'r') as file:
            for word in file :
                pyautogui.typewrite(word)
                pyautogui.press('enter')

    except:
        print('cant spam the file theres an error')
        print(e)

# Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, height=2, width=15, fg='#141414',command=lambda:main())
browse_btn['font'] = myFont
browse_text.set("Browse")
browse_btn.place(x=200, y=400, anchor='center')

# main button
status = 'Start'



root.mainloop()