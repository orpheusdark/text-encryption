import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class OrphCrypt:
    def __init__(self, root):
        self.root = root
        self.root.title("OrphCrypt")
        self.root.geometry("1920x1080")
        self.root.resizable(True, True)


        # Load and resize the background image
        img = Image.open("img1.jpg")
        img = img.resize((1920, 1080))
        self.background_image = ImageTk.PhotoImage(img)

        # Create a canvas and set background image
        self.canvas = tk.Canvas(root, width=1920, height=1080)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        self.font_style = ("Happy Monkey", 14)
        
        # Title
        title_label = tk.Label(root, text="OrphCrypt", font=("Happy Monkey", 20), bd=6)
        title_label.place(relx=0.5, rely=0.1, anchor="n")

        # Message Entry
        self.message_entry = tk.Entry(root, font=("Happy Monkey", 16), bd=5)
        self.message_entry.insert(0, "Enter Message")
        self.message_entry.bind("<FocusIn>", self.on_message_entry_focus_in)
        self.message_entry.bind("<FocusOut>", self.on_message_entry_focus_out)
        self.message_entry.place(relx=0.5, rely=0.2, anchor="n")

        # Shift Entry
        self.shift_entry = tk.Entry(root, font=("Happy Monkey", 16), bd=5)
        self.shift_entry.insert(0, "Shift")
        self.shift_entry.bind("<FocusIn>", self.on_shift_entry_focus_in)
        self.shift_entry.bind("<FocusOut>", self.on_shift_entry_focus_out)
        self.shift_entry.place(relx=0.5, rely=0.3, anchor="n")


    


        # Encrypt Button
        encrypt_button = tk.Button(root, text="Encrypt", font=("Happy Monkey", 14), command=self.encrypt)
        encrypt_button.place(relx=0.5, rely=0.4, anchor="n")

        # Decrypt Button
        decrypt_button = tk.Button(root, text="Decrypt", font=("Happy Monkey", 14), command=self.decrypt)
        decrypt_button.place(relx=0.5, rely=0.5, anchor="n")

         # About Author Page
        about_page_button = tk.Button(root, text="About Author", font=("Happy Monkey", 16),command=self.show_about_page)
        about_page_button.place(relx=0.5, rely=0.8, anchor="n")


    def on_message_entry_focus_in(self, event):
        if self.message_entry.get() == "Enter Message":
            self.message_entry.delete(0, tk.END)

    def on_message_entry_focus_out(self, event):
        if not self.message_entry.get():
            self.message_entry.insert(0, "Enter Message")

    def on_shift_entry_focus_in(self, event):
        if self.shift_entry.get() == "Shift":
            self.shift_entry.delete(0, tk.END)

    def on_shift_entry_focus_out(self, event):
        if not self.shift_entry.get():
            self.shift_entry.insert(0, "Shift")

    def encrypt(self):
        message = self.message_entry.get()
        shift = int(self.shift_entry.get())
        encrypted_message = self.caesar_cipher(message, shift)
        messagebox.showinfo("Encryption Result", f"Encrypted Message: {encrypted_message}")

        # Show Important Notice Popup
        self.show_notice_popup()

    def decrypt(self):
        message = self.message_entry.get()
        shift = int(self.shift_entry.get())
        decrypted_message = self.caesar_cipher(message, -shift)
        messagebox.showinfo("Decryption Result", f"Decrypted Message: {decrypted_message}")

        # Show Important Notice Popup
        self.show_notice_popup()

    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
                result += char
        return result

    def show_notice_popup(self):
        notice_text = (
        "Disclaimer: Please Don't Copy This Code:)\n\n"
        "Instead of copying, FORK my repository."
    )
        # Display the initial message
        messagebox.showinfo("Important Notice", notice_text)

        # Create a custom dialog with a clickable link
        self.show_link_dialog()

    def show_link_dialog(self):
        link_dialog = tk.Toplevel(self.root)
        link_dialog.title("Fork a repository")

        link_label = tk.Label(
            link_dialog,
            text="For more information on forking, visit [GitHub Forking Documentation]",
            font=("Happy Monkey", 14),
            justify="center",
            padx=50,
            pady=10,
            cursor="hand2"
        )
        link_label.pack()

        # Make the label behave like a link
        link_label.bind("<Button-1>", lambda event: self.open_browser("https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#about-forks"))

    def open_browser(self, url):
        import webbrowser
        webbrowser.open_new(url)
        
    
    def show_about_page(self):
        
        about_window = tk.Toplevel(self.root)
        about_window.title("About Author")
        about_window.geometry("800x600")

        about_label = tk.Label(about_window, text="Connect And Collaborate", font=("Happy Monkey", 14), pady=10)
        about_label.pack()

        
        about_label = tk.Label(about_window, text="Nirant Chavda\n\nGreetings!\n\nContact Information:\n", font=("Happy Monkey", 14), pady=10)
        about_label.pack()

        mailme_button = tk.Button(about_window, text="Email Me", font=("Happy Monkey", 14), command=self.send_email)
        mailme_button.pack(pady=10)

        
        linkedin_img = tk.PhotoImage(file="linkedin.png")
        linkedin_button = tk.Button(about_window, image=linkedin_img, command=self.open_linkedin)
        linkedin_button.image = linkedin_img
        linkedin_button.pack(pady=5)

        github_img = tk.PhotoImage(file="github.png")
        github_button = tk.Button(about_window, image=github_img, command=self.open_github)
        github_button.image = github_img
        github_button.pack(pady=5)

    def send_email(self):
         import webbrowser
         webbrowser.open("mailto:orpheusdark@duck.com")    

    def open_linkedin(self):
        import webbrowser
        webbrowser.open("https://www.linkedin.com/in/orpheusdark")

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/orpheusdark/PRODIGY_CS_01")



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1920x1080")
    app = OrphCrypt(root)
    root.mainloop()
