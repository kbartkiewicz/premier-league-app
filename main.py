from customtkinter import *
from matches import draw_matches
from h2h import draw_h2h_comparison
from table import draw_standings
from scorers import draw_top_scorers
from teams import draw_team_info
from widgets_fonts_auth import HeaderButton

# setting properties of the app
root = CTk()
set_appearance_mode("dark")
root.title("Premier League app")
root.geometry("504x640")


# drawing home page function
def draw_home_page():
    remove_content()
    app_info = CTkLabel(root, text="Premier League app created by Kbartkieiwcz. "
                                   "\nThe trade names and marks are the exclusive property of FA Premier League.")
    app_info.place(x=252, y=60, anchor="center")


# removing currently displayed content
def remove_content():
    for widget in root.winfo_children():
        if widget not in header_buttons:
            widget.destroy()


# creating header buttons
home_button = HeaderButton(root, text="Home", command=draw_home_page)
matches_button = HeaderButton(root, text="Matches", command=lambda: [remove_content(), draw_matches(root)])
h2h_button = HeaderButton(root, text="H2H", command=lambda: [remove_content(), draw_h2h_comparison(root)])
standings_button = HeaderButton(root, text="Table", command=lambda: [remove_content(), draw_standings(root)])
top_scorers_button = HeaderButton(root, text="Scorers", command=lambda: [remove_content(), draw_top_scorers(root)])
team_stats_button = HeaderButton(root, text="Teams", command=lambda: [remove_content(), draw_team_info(root)])

# displaying header buttons on top of the screen
header_buttons = [home_button, matches_button, h2h_button, standings_button, top_scorers_button, team_stats_button]
k = 0
for button in header_buttons:
    button.place(x=k, y=0)
    k += 84

draw_home_page()
root.resizable(False, False)
root.mainloop()
