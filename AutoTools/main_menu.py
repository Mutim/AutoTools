import os
import tkinter
import customtkinter
from tktooltip import ToolTip
import keyboard
from PIL import Image

import config
from tools import AutoTyper
from widgets import scrollable_frame


class MainMenu(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        if not os.name == 'posix':
            self.iconbitmap(config.logo_ico)
        self.title("AutoTools - Automation Toolbox")
        self.geometry(config.menu_size)

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(3, weight=0)
        self.grid_rowconfigure(2, weight=1)

        # load images with light and dark mode image
        self.logo_image = customtkinter.CTkImage(Image.open(config.logo_png),
                                                 size=(56, 56))
        self.typer_image = customtkinter.CTkImage(
            light_image=Image.open(config.light_image_typer),
            dark_image=Image.open(config.dark_image_typer),
            size=(36, 36))
        self.clicker_image = customtkinter.CTkImage(
            light_image=Image.open(config.light_image_clicker),
            dark_image=Image.open(config.dark_image_clicker),
            size=(36, 36))
        self.settings_image = customtkinter.CTkImage(
            light_image=Image.open(config.light_image_settings),
            dark_image=Image.open(config.dark_image_settings),
            size=(36, 36))
        self.converter_image = customtkinter.CTkImage(
            light_image=Image.open(config.light_image_convert),
            dark_image=Image.open(config.dark_image_convert),
            size=(36, 36))

        # create sidebar frame with sections to tools
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, rowspan=3, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(3, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Auto Tools Main Menu",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.auto_typer_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40,
                                                         border_spacing=10,
                                                         text="Typer",
                                                         fg_color="transparent",
                                                         text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         image=self.typer_image,
                                                         anchor="w",
                                                         command=self.auto_typer_button_event)
        self.auto_typer_button.grid(row=1, column=0, sticky="ew")

        self.clicker_frame_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40,
                                                            border_spacing=10, text="Auto Clicker",
                                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                                            hover_color=("gray70", "gray30"),
                                                            image=self.clicker_image, anchor="w",
                                                            command=self.clicker_frame_button_event)
        self.clicker_frame_button.grid(row=2, column=0, sticky="ew")

        self.options_frame_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=5, height=40,
                                                            border_spacing=10, text="Settings",
                                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                                            hover_color=("gray70", "gray30"),
                                                            image=self.settings_image, anchor="w",
                                                            command=self.options_frame_button_event)
        self.options_frame_button.grid(row=3, column=0, sticky="ew")

        # # # create typer frame
        self.typer_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.typer_frame.grid(row=0, rowspan=5, column=0, columnspan=4, sticky="nsew")
        self.typer_frame.grid_columnconfigure(3, weight=1)
        self.typer_frame.grid_rowconfigure(3, weight=1)

        self.type_textbox = customtkinter.CTkTextbox(master=self.typer_frame, width=400)
        self.type_textbox.grid(row=0, rowspan=3, column=1, columnspan=3, padx=(15, 15), pady=(20, 15), sticky="nesw")
        self.type_textbox.insert("0.0", config.default_textbox_text)
        self.type_textbox.configure(font=("Comic Sans MS", 16, "bold", "italic"))

        # typer tabview
        self.typer_tabview = customtkinter.CTkTabview(self.typer_frame, width=250)
        self.typer_tabview.grid(row=0, column=4, rowspan=2, padx=(15, 15), pady=(20, 15), sticky="nsew")
        self.typer_tabview.add("Typer Options")
        self.typer_tabview.tab("Typer Options").grid_columnconfigure(0, weight=1)

        self.amount_label = customtkinter.CTkLabel(master=self.typer_tabview.tab("Typer Options"),
                                                   text="Times to Repeat: 50", anchor="center")
        self.amount_label.grid(row=0, column=0)

        def set_times_repeated(amount):
            amount = int(amount)
            self.amount_label.configure(text=f"Times to Repeat: {amount}")

        self.repeat_amount_slider = customtkinter.CTkSlider(master=self.typer_tabview.tab("Typer Options"), from_=1,
                                                            to=100,
                                                            command=set_times_repeated,
                                                            number_of_steps=99)

        self.repeat_amount_slider.set(50)
        self.repeat_amount_slider.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.initial_sleep_label = customtkinter.CTkLabel(master=self.typer_tabview.tab("Typer Options"),
                                                          text="5 seconds sleep before starting", anchor="center")
        self.initial_sleep_label.grid(row=2, column=0)

        def initial_sleep_time(amount):
            amount = int(amount) / 10
            self.initial_sleep_label.configure(text=f"{amount} seconds sleep before starting")

        self.initial_sleep_amount_slider = customtkinter.CTkSlider(master=self.typer_tabview.tab("Typer Options"),
                                                                   from_=1,
                                                                   to=100,
                                                                   command=initial_sleep_time,
                                                                   number_of_steps=99)

        self.initial_sleep_amount_slider.set(50)
        self.initial_sleep_amount_slider.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.sleep_label = customtkinter.CTkLabel(master=self.typer_tabview.tab("Typer Options"),
                                                  text="0.50 seconds sleep between messages", anchor="center")
        self.sleep_label.grid(row=4, column=0)

        def sleep_time(amount):
            amount = int(amount) / 100
            self.sleep_label.configure(text=f"{amount} seconds sleep between messages")

        self.sleep_amount_slider = customtkinter.CTkSlider(master=self.typer_tabview.tab("Typer Options"), from_=1,
                                                           to=1000,
                                                           command=sleep_time,
                                                           number_of_steps=999)

        self.sleep_amount_slider.set(50)
        self.sleep_amount_slider.grid(row=5, column=0, padx=20, pady=(10, 10))

        def random_checkbox_event():
            if self.checkbox_random.get():
                print("Random Times has been selected")
                self.checkbox_random.configure(text="Random Wait Times [ON]")
                self.random_min_slider.configure(state="normal", button_color=self.original_button_color)
                self.random_max_slider.configure(state="normal", button_color=self.original_button_color)
            else:
                print("Random Times has been de-selected")
                self.checkbox_random.configure(text="Random Wait Times [OFF]")
                self.random_min_slider.configure(state="disabled", button_color="gray45")
                self.random_max_slider.configure(state="disabled", button_color="gray45")

        self.checkbox_random = customtkinter.CTkCheckBox(master=self.typer_tabview.tab("Typer Options"),
                                                         text="Random Wait Times [OFF]", command=random_checkbox_event)
        ToolTip(self.checkbox_random, msg='Random amount of time added to "Sleep Time"', delay=0, refresh=0.1)

        self.checkbox_random.grid(row=6, column=0, pady=20, padx=20, sticky="n")

        self.min_amount = 0
        self.max_amount = 10
        self.random_values = customtkinter.CTkLabel(master=self.typer_tabview.tab("Typer Options"),
                                                    text=f"Random Wait Time\nMIN - MAX", anchor="center")
        self.random_values.grid(row=7, column=0)

        def reset_colors(button_object, *attrs: str):
            button_object.configure(
                button_color=self.original_button_color,
                button_hover_color=self.original_button_hover_color)

        def button_error_color(button_object):
            button_object.configure(button_color="#B52838", button_hover_color="#9D2235")

        def random_wait_time_min(amount):
            self.min_amount = int(amount) / 100
            self.random_values.configure(text=f"Random Wait Time\nMIN ({self.min_amount}) - MAX ({self.max_amount})")
            if self.min_amount > self.max_amount:
                self.random_values.configure(text="MIN cannot be greater than MAX")
                button_error_color(self.random_min_slider)
                button_error_color(self.random_max_slider)
            else:
                reset_colors(self.random_min_slider)
                reset_colors(self.random_max_slider)

        def random_wait_time_max(amount):
            self.max_amount = int(amount) / 100
            self.random_values.configure(text=f"Random Wait Time\nMIN ({self.min_amount}) - MAX ({self.max_amount})")
            if self.max_amount < self.min_amount:
                self.random_values.configure(text="MAX cannot be lesser than MIN")
                button_error_color(self.random_min_slider)
                button_error_color(self.random_max_slider)
            else:
                reset_colors(self.random_min_slider)
                reset_colors(self.random_max_slider)

        self.random_min_slider = customtkinter.CTkSlider(master=self.typer_tabview.tab("Typer Options"), from_=1,
                                                         to=1000,
                                                         command=random_wait_time_min,
                                                         number_of_steps=999)
        self.original_button_color = self.random_min_slider.cget("button_color")
        self.original_button_hover_color = self.random_min_slider.cget("button_hover_color")
        self.random_min_slider.configure(state="disabled", button_color="gray45")

        self.random_min_slider.set(0)
        self.random_min_slider.grid(row=8, column=0, padx=(25, 25), pady=(1, 10))
        self.random_max_slider = customtkinter.CTkSlider(master=self.typer_tabview.tab("Typer Options"), from_=1,
                                                         to=1000,
                                                         command=random_wait_time_max,
                                                         number_of_steps=999)
        self.original_button_color = self.random_max_slider.cget("button_color")
        self.random_max_slider.configure(state="disabled", button_color="gray45")

        self.random_max_slider.set(1000)
        self.random_max_slider.grid(row=9, column=0, padx=(25, 25), pady=(10, 10))

        def send_enter_checkbox_event():
            if self.checkbox_send_enter.get():
                print("Sending Enter has been selected")
                self.checkbox_send_enter.configure(text="Sending Enter Keystroke [True]")
            else:
                print("Sending Enter has been de-selected")
                self.checkbox_send_enter.configure(text="Sending Enter Keystroke [False]")

        self.checkbox_send_enter = customtkinter.CTkCheckBox(master=self.typer_tabview.tab("Typer Options"),
                                                             text="Sending Enter Keystroke [False]",
                                                             command=send_enter_checkbox_event)
        ToolTip(self.checkbox_send_enter, msg='Should the "Enter" key be pressed after sending the message?', delay=0,
                refresh=0.1)

        self.checkbox_send_enter.grid(row=10, column=0, pady=20, padx=20, sticky="n")

        # hotkeys tabview
        # TODO: Set keybind menu for setting a keybind to start and stop the typing.
        # def key_pressed(event):
        #     w = Label(root, text="Key Pressed:" + event.char)
        #
        #     w.place(x=70, y=90)
        #
        # customtkinter.CTk.bind("<Key>", key_pressed)

        # self.hotkey_tabview = customtkinter.CTkTabview(self.typer_frame, width=250)
        # self.hotkey_tabview.grid(row=3, column=0, columnspan=4, padx=(15, 0), pady=(10, 10), sticky="new")
        # self.hotkey_tabview.add("Hotkeys")
        # self.hotkey_tabview.tab("Hotkeys").grid_columnconfigure(0, weight=1)

        # self.start_stop_hotkey_button = customtkinter.CTkButton(self.hotkey_tabview.tab("Hotkeys"), text="test", width=65, height=50)
        # self.start_stop_hotkey_button.grid(row=1, column=0, padx=(5, 5), pady=(15, 15))

        # # Buttons
        self.typer_button = customtkinter.CTkButton(self.typer_frame, command=self.run_tool_typer, text="Execute Type!",
                                                    corner_radius=50)
        self.typer_button.grid(row=3, column=1, columnspan=1, padx=(15, 5), pady=(5, 15), sticky="w")

        self.clear_button = customtkinter.CTkButton(self.typer_frame, command=self.delete_textbox_text,
                                                    text="Clear Texbox", corner_radius=50)
        self.clear_button.grid(row=3, column=2, columnspan=1, padx=(15, 5), pady=(5, 15), sticky="w")

        self.hotkeys_button = customtkinter.CTkButton(self.typer_frame, command=self.open_hotkeys_window,
                                                      text="Edit Hotkeys", corner_radius=50)
        self.hotkeys_button.grid(row=3, column=3, columnspan=1, padx=(15, 5), pady=(5, 15), sticky="w")

        # # # create clicker frame
        self.clicker_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.clicker_frame.grid_columnconfigure(2, weight=1)
        self.clicker_frame.grid_rowconfigure(2, weight=1)

        # # create main entry and button
        # self.entry = customtkinter.CTkEntry(self.clicker_frame, placeholder_text="Game File Query")
        # self.entry.grid(row=3, column=1, columnspan=3, padx=(5, 5), pady=(20, 20), sticky="nsew")
        #
        #
        # self.main_button_1 = customtkinter.CTkButton(master=self.clicker_frame, text='Search', fg_color="transparent",
        #                                              border_width=2,
        #                                              text_color=("gray10", "#DCE4EE"),
        #                                              command=lambda: self.query_result())
        # self.main_button_1.grid(row=3, column=4, padx=(10, 10), pady=(20, 20), sticky="nsew")

        # # create textbox
        # self.textbox = customtkinter.CTkTextbox(self.clicker_frame, width=300, font=('DejaVu Sans Mono', 12, 'normal'))
        # self.textbox.grid(row=0, rowspan=3, column=1, columnspan=3, padx=(10, 0), pady=(10, 0), sticky="nsew")

        # # # Create options frame
        self.options_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.options_frame.grid_columnconfigure(2, weight=1)
        self.options_frame.grid_rowconfigure(2, weight=1)

        # Create options frame tabs
        self.options_tabview = customtkinter.CTkTabview(self.options_frame, width=0)
        self.options_tabview.grid(row=0, rowspan=1, column=4, padx=(10, 10), pady=(0, 0), sticky="w")
        self.options_tabview.add("Configure")
        self.options_tabview.tab("Configure").grid_columnconfigure(0, weight=1)

        # # Configuration Menu
        self.scripts_menu = customtkinter.CTkLabel(self.options_tabview.tab("Configure"), text="Configuration")
        self.scripts_menu.grid(row=0, column=0, padx=5, pady=(0, 0))

        # Set Appearance Mode
        self.appearance_mode_label = customtkinter.CTkLabel(self.options_tabview.tab("Configure"),
                                                            text="Appearance Mode:",
                                                            anchor="center")
        self.appearance_mode_label.grid(row=0, column=0, padx=5, pady=(0, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.options_tabview.tab("Configure"),
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=5, pady=(0, 10))

        # # Set path to Extracted Game Files
        # self.config_label_path_label = customtkinter.CTkLabel(self.options_tabview.tab("Configure"),
        #                                                       text="Set Path")
        # self.config_label_path_label.grid(row=3)
        # self.config_label_path_button = customtkinter.CTkButton(self.options_tabview.tab("Configure"),
        #                                                         text="Extracted Files")

        # Set Scaling Percentage
        self.scaling_label = customtkinter.CTkLabel(self.options_tabview.tab("Configure"), text="UI Scaling:",
                                                    anchor="w")
        self.scaling_label.grid(row=5, column=0, padx=5, pady=(0, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.options_tabview.tab("Configure"),
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=6, column=0, padx=5, pady=(0, 10))

        # self.config_label_path_button.grid(row=4, column=0, padx=5, pady=(0, 10))

        # # set default values
        self.appearance_mode_optionemenu.set(config.default_theme)
        self.scaling_optionemenu.set("100%")
        self.select_frame_by_name("auto_typer_frame")  # select default frame

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type here:", title="Search Commands")
        print("Test Dialog Box:", dialog.get_input())

    def sidebar_button_event(self, button):

        global mapped_list
        self.textbox.delete("0.0", customtkinter.END)

        post_filter_entries = mapped_list[button.lower()]
        print(f'{button} Sidebar button pressed')
        for e in post_filter_entries:
            # Insert the hyperlink
            self.textbox.insert("0.0", f"{e}\n")
        self.textbox.insert("0.0", f"Showing {len(post_filter_entries)} entries for {button.title()}\n\n")

    # # # Run Tools
    def run_tool_typer(self):
        type_options = {
            "text": str(self.type_textbox.get('1.0', "end")),
            "initial_sleep": int(self.initial_sleep_amount_slider.get()),
            "amount_repeat": int(self.repeat_amount_slider.get()),
            "time_sleep": self.sleep_amount_slider.get(),
            "random_wait": self.checkbox_random.get(),
            "random_time_min": self.random_min_slider.get(),
            "random_time_max": self.random_max_slider.get(),
            "send_enter": self.checkbox_send_enter.get()
        }
        auto_type = AutoTyper(type_options)
        auto_type.log_write()
        auto_type.typer()

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def delete_textbox_text(self):
        self.type_textbox.delete("1.0", "end")

    def open_hotkeys_window(self):
        hotkey_window = customtkinter.CTkToplevel()
        hotkey_window.title('Editing Hotkeys')
        hotkey_window.geometry("400x400")
        if not os.name == 'posix':
            hotkey_window.after(210, lambda: hotkey_window.iconbitmap(config.logo_ico))  # Bug in CTk source that will stop TopLevel from changing Ico
        hotkey_window.maxsize(400, 600)
        hotkey_window.after(20, hotkey_window.lift)  # Bug in CTk Code that spawns the TopLevel window behind MainLoop

        # # Create button frame
        scrollable_label_button_frame = scrollable_frame.ScrollableLabelButtonFrame(master=hotkey_window, width=400,
                                                                                    height=400,
                                                                                    command=self.label_button_frame_event,
                                                                                    corner_radius=0)
        scrollable_label_button_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        hotkeys = {'Start': 'F6', 'Stop': 'F7', 'Pause': 'F8', 'Clear': 'F4'}
        for h in hotkeys:
            button = customtkinter.CTkButton(scrollable_label_button_frame,
                                             text=h, width=100, height=24,
                                             corner_radius=10)
            scrollable_label_button_frame.add_item(f"Edit Hotkey: {h}", button=button, image=customtkinter.CTkImage(
                light_image=Image.open(config.light_image_settings),
                dark_image=Image.open(config.dark_image_settings),
                size=(36, 36)))

    def label_button_frame_event(self, item):
        print(f"Modifying Hotkey for Command: {item.split(':')[1].replace(' ', '')}")

    def select_frame_by_name(self, name):
        # set button color for selected button
        # TODO: Change so that this will set fg_color to be the current theme's options.

        self.auto_typer_button.configure(fg_color=("gray75", "gray25") if name == "auto_typer_frame" else "transparent")
        self.clicker_frame_button.configure(fg_color=("gray75", "gray25") if name == "clicker_frame" else "transparent")
        self.options_frame_button.configure(fg_color=("gray75", "gray25") if name == "options_frame" else "transparent")
        # self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "auto_typer_frame":
            self.typer_frame.grid(row=0, rowspan=5, column=1, columnspan=4, sticky="nsew")
        else:
            self.typer_frame.grid_forget()
        if name == "clicker_frame":
            self.clicker_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.clicker_frame.grid_forget()
        if name == "options_frame":
            self.options_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.options_frame.grid_forget()
        # if name == "frame_3":
        #     self.converter_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.converter_frame.grid_forget()

    def auto_typer_button_event(self):
        self.select_frame_by_name("auto_typer_frame")

    def clicker_frame_button_event(self):
        self.select_frame_by_name("clicker_frame")

    def options_frame_button_event(self):
        self.select_frame_by_name("options_frame")

    # def frame_3_button_event(self):
    #     self.select_frame_by_name("frame_3")

    # current_theme = customtkinter.ThemeManager.theme
    # current_appearance_mode = customtkinter.get_appearance_mode()
    # print(f"Current Theme: {current_theme}")
    # print(f"Current Appearance Mode: {current_appearance_mode}")


def main_menu():
    app = MainMenu()
    app.mainloop()
