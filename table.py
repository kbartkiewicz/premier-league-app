import requests
from customtkinter import CTkLabel
from widgets_fonts_auth import FONT_13, FONT_13_BOLD, headers


# api request for standings
url = "https://api-football-beta.p.rapidapi.com/standings"
querystring = {"season": "2023", "league": "39"}
response = requests.get(url, headers=headers, params=querystring).json()["response"][0]["league"]["standings"][0]


def draw_standings(root):
    # drawing table headers
    table_headers_positions = [
        (10, 40), (44, 40), (168, 40), (210, 40), (242, 40), (278, 40), (316, 40), (358, 40), (400, 40), (450, 40)]
    table_headers = ["#", "Team", "M", "W", "D", "L", "GS", "GC", "GD", "P"]
    for i in range(len(table_headers)):
        label = CTkLabel(root, text=table_headers[i], font=FONT_13_BOLD)
        label.place(x=table_headers_positions[i][0], y=table_headers_positions[i][1])

    # drawing teams standings
    k = 66
    for i in range(20):
        position_label = CTkLabel(root, text=response[i]["rank"], font=FONT_13)
        position_label.place(x=table_headers_positions[0][0], y=k)
        team_label = CTkLabel(root, text=response[i]["team"]["name"], font=FONT_13)
        team_label.place(x=table_headers_positions[1][0], y=k)
        matches_label = CTkLabel(root, text=response[i]["all"]["played"], font=FONT_13)
        matches_label.place(x=table_headers_positions[2][0], y=k)
        win_label = CTkLabel(root, text=response[i]["all"]["win"], font=FONT_13)
        win_label.place(x=table_headers_positions[3][0], y=k)
        draw_label = CTkLabel(root, text=response[i]["all"]["draw"], font=FONT_13)
        draw_label.place(x=table_headers_positions[4][0], y=k)
        lose_label = CTkLabel(root, text=response[i]["all"]["lose"], font=FONT_13)
        lose_label.place(x=table_headers_positions[5][0], y=k)
        goals_scored_label = CTkLabel(root, text=response[i]["all"]["goals"]["for"], font=FONT_13)
        goals_scored_label.place(x=table_headers_positions[6][0], y=k)
        goals_conceded_label = CTkLabel(root, text=response[i]["all"]["goals"]["against"], font=FONT_13)
        goals_conceded_label.place(x=table_headers_positions[7][0], y=k)
        goals_difference_label = CTkLabel(
            root, text=response[i]["all"]["goals"]["for"] - response[i]["all"]["goals"]["against"], font=FONT_13)
        goals_difference_label.place(x=table_headers_positions[8][0], y=k)
        points_label = CTkLabel(root, text=response[i]["points"], font=FONT_13_BOLD)
        points_label.place(x=table_headers_positions[9][0], y=k)
        k += 26
