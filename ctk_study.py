import customtkinter as ctk

#criar a janela
janela = ctk.CTk()

#trocar a cor da janela
ctk.set_appearance_mode("Dark")

#Definir cores padrões
ctk.set_default_color_theme("blue")

#Título da janela
janela.title("DailyTrack")

#Definir dimensões
janela.geometry("700x850")


janela.mainloop()

