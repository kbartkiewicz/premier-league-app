from customtkinter import *

# api request authentication
headers = {
    "X-RapidAPI-Key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
}

FONT_12 = ("Arial", 12)
FONT_12_BOLD = ("Arial", 12, "bold")
FONT_12_ITALIC = ("Arial", 12, "italic")
FONT_13 = ("Arial", 13)
FONT_13_BOLD = ("Arial", 13, "bold")
FONT_14 = ("Arial", 14)
FONT_14_BOLD = ("Arial", 14, "bold")


class HeaderButton(CTkButton):
    def __init__(self, root, *args, **kwargs):
        CTkButton.__init__(self, root, width=84, fg_color="#37DA7C", bg_color="transparent",
                           text_color="#440948", hover_color="#27a15b", font=FONT_14, *args, **kwargs)


class ContentButton(CTkButton):
    def __init__(self, root, *args, **kwargs):
        CTkButton.__init__(self, root, fg_color="#4E0A53", font=FONT_13, hover_color="#5F0C64", *args, **kwargs)


class DropdownList(CTkComboBox):
    def __init__(self, root, *args, **kwargs):
        CTkComboBox.__init__(self, root, state="readonly", fg_color="#5F0C64", font=FONT_13, button_color="#4E0A53",
                             border_color="#4E0A53", *args, **kwargs)
