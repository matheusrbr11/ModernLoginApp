from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Login System") 
janela.resizable(False, False)

labeltitle = customtkinter.CTkLabel(master=janela, text="Login to your account and get the platform", font=('Roboto', 18), text_color="#00B0F0").place(x=10, y=10)

frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

label = customtkinter.CTkLabel(master=frame, text='Login System', font = ('Roboto', 20, 'bold'), text_color= ('white') )
label.place(x=25, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", width=300, font=("Roboto", 14)).place(x=25, y=105)
label1 = customtkinter.CTkLabel(master=frame, text="Required ", text_color="green", font=("Roboto", 8)).place(x=25, y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", width=300, font=("Roboto", 14)).place(x=25, y=175)
label2 = customtkinter.CTkLabel(master=frame, text="Required", text_color="green", font=("Roboto", 8)).place(x=25, y=205)

Checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me").place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text="LOGIN", width=300).place(x=25, y=285)

janela.mainloop()