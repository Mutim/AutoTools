import os

import tkinter
import customtkinter
import webbrowser
from PIL import Image

import config
from AutoTools import main_menu


# Login screen -
# As this is, this will log anyone in, with any arbitrary information
# TODO: Make this authenticate to a server to verify login.


def main():
    customtkinter.set_appearance_mode(config.default_theme)
    customtkinter.set_default_color_theme(config.custom_theme)  # Themes: config.themes

    app = customtkinter.CTk()  # creating window
    app.title('Login')
    app.geometry(config.login_menu_size)
    if not os.name == 'posix':
        app.iconbitmap(config.logo_ico)

    # This assumes that the light and dark image are the same size
    bg_dimensions = Image.open(config.dark_image_pattern).size
    background_image = customtkinter.CTkImage(light_image=Image.open(config.light_image_pattern),
                                              dark_image=Image.open(config.dark_image_pattern),
                                              size=bg_dimensions)
    l1 = customtkinter.CTkLabel(master=app, image=background_image)
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Log into AutoTools", font=('Century Gothic', 20), anchor="e")
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    def login_button_function():
        app.destroy()
        menus.main_menu()

    def open_site(event=None):
        print("Opening Password Reset Link...")
        webbrowser.open_new(config.reset_password_url)

    def hover_event(event=None):
        l3.configure(text_color=["#e9d66b", "#f0e68c"])

    def unhover_event(event=None):
        l3.configure(text_color=["gray10", "#DCE4EE"])

    l3 = customtkinter.CTkLabel(master=frame, text="Forgot password?", font=('Century Gothic', 12),
                                text_color=("gray10", "#DCE4EE"))
    l3.place(x=155, y=195)
    l3.bind("<Button-1>", open_site)
    l3.bind("<Enter>", hover_event)
    l3.bind("<Leave>", unhover_event)

    # Create custom button
    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=lambda: login_button_function(),
                                      corner_radius=6)
    button1.place(x=50, y=240)

    img2 = customtkinter.CTkImage(Image.open(config.github_image).resize((20, 20), Image.Resampling.LANCZOS))
    img3 = customtkinter.CTkImage(Image.open(config.discord_image).resize((20, 20), Image.Resampling.LANCZOS))
    button2 = customtkinter.CTkButton(master=frame, image=img2, text="Github", width=100, height=20, compound="left",
                                      fg_color='white', text_color='black', hover_color='#AFAFAF')
    button2.place(x=50, y=290)

    button3 = customtkinter.CTkButton(master=frame, image=img3, text="Discord", width=100, height=20, compound="left",
                                      fg_color='white', text_color='black', hover_color='#AFAFAF')
    button3.place(x=170, y=290)

    app.mainloop()


if __name__ == '__main__':
    # main()
    main_menu.main_menu()
