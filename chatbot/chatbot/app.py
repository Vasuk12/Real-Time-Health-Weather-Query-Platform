from tkinter import *
from chat import get_response, bot_name
import string
import random
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha
import os

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_captcha()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_captcha(self):
        global entry, image_label, verify_label
        verify_label = Label(self.window)
        image_label = Label(self.window)
        entry = Entry(self.window, width=10, borderwidth=5,
                      font="Arial 15", justify="center")
        entry.grid(row=2, column=0)

        self.createImage()
        
        path = 'reload.png'  # Make sure this path is correct
        reload_img = ImageTk.PhotoImage(Image.open(path).resize((32, 32), Image.ANTIALIAS))
        reload_button = Button(image=reload_img, command=lambda: self.createImage(1))
        reload_button.image = reload_img  # Keep a reference to avoid garbage collection
        reload_button.grid(row=2, column=1, pady=10)
        
        submit_button = Button(self.window, text="Submit", font="Arial 10", command=lambda: self.check(entry.get(), random_string))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)

    def createImage(self, flag=0):
        global random_string, image_label, image_display, entry, verify_label
        if flag == 1:
            verify_label.grid_forget()
        entry.delete(0, END)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        image_captcha = ImageCaptcha(width=250, height=125)
        image_generated = image_captcha.generate(random_string)
        image_display = ImageTk.PhotoImage(Image.open(image_generated))
        image_label.grid_forget()
        image_label = Label(self.window, image=image_display)
        image_label.image = image_display  # Keep a reference to avoid garbage collection
        image_label.grid(row=1, column=0, columnspan=2, padx=10)
        
    def check(self, x, y):
        global verify_label
        verify_label.grid_forget()
        if x.lower() == y.lower():
            verify_label = Label(master=self.window,
                                text="Verified",
                                font="Arial 15",
                                bg='#ffe75c',
                                fg="#00a806"
                                )
            verify_label.grid(row=0, column=0, columnspan=2, pady=10)
            self._setup_main_window()
        else:
            verify_label = Label(master=self.window,
                                text="Incorrect!",
                                font="Arial 15",
                                bg='#ffe75c',
                                fg="#fa0800"
                                )
            verify_label.grid(row=0, column=0, columnspan=2, pady=10)
            self.createImage()

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
