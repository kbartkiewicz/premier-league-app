import requests
from customtkinter import CTkLabel
from widgets_fonts_auth import FONT_13, FONT_13_BOLD, headers


# api request for top scorers
url = "https://api-football-beta.p.rapidapi.com/players/topscorers"
querystring = {"season": "2023", "league": "39"}
response = requests.get(url, headers=headers, params=querystring).json()["response"]


def draw_top_scorers(root):
    x_positions = [10, 150, 270, 390, 450]
    # drawing table headers
    top_scorers_headers = ["Name", "Nationality", "Team", "Goals", "Assists"]
    for i in range(len(top_scorers_headers)):
        label = CTkLabel(root, text=top_scorers_headers[i], font=FONT_13_BOLD)
        label.place(x=x_positions[i], y=40)

    # drawing players info
    k = 66
    for i in range(20):
        name_label = CTkLabel(root, text=response[i]["player"]["name"], font=FONT_13)
        name_label.place(x=x_positions[0], y=k)
        nationality_label = CTkLabel(root, text=response[i]["player"]["nationality"], font=FONT_13)
        nationality_label.place(x=x_positions[1], y=k)
        team_label = CTkLabel(root, text=response[i]["statistics"][0]["team"]["name"], font=FONT_13)
        team_label.place(x=x_positions[2], y=k)
        goals_label = CTkLabel(root, text=response[i]["statistics"][0]["goals"]["total"], font=FONT_13)
        goals_label.place(x=x_positions[3], y=k)
        if response[i]["statistics"][0]["goals"]["assists"] is not None:
            assists_label = CTkLabel(root, text=response[i]["statistics"][0]["goals"]["assists"], font=FONT_13)
        else:
            assists_label = CTkLabel(root, text="0", font=FONT_13)
        assists_label.place(x=x_positions[4], y=k)
        k += 26
