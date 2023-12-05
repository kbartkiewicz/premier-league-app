import requests
from customtkinter import CTkLabel
from tkinter import Label
from PIL import Image, ImageTk
from widgets_fonts_auth import ContentButton, DropdownList, FONT_12, FONT_12_BOLD, headers


# api request for teams info
url = "https://api-football-beta.p.rapidapi.com/teams"
querystring = {"season": "2023", "league": "39"}
response = requests.get(url, headers=headers, params=querystring)

content_widgets = []

# creating an ordered list of team names
teams = [response.json()["response"][i]["team"]["name"] for i in range(20)]


def draw_team_info(root):
    def show_team(root):
        # clearing currently displayed widgets
        for widget in root.winfo_children():
            if widget in content_widgets:
                widget.destroy()

        # displaying a logo
        logo_url = response.json()["response"][teams.index(teams_drop_list.get())]["team"]["logo"]
        logo_image = ImageTk.PhotoImage(Image.open(requests.get(logo_url, stream=True).raw))
        logo_label = Label(image=logo_image)
        logo_label.image = logo_image
        logo_label.place(x=14, y=100)
        content_widgets.append(logo_label)

        # displaying a stadium image
        stadium_url = response.json()["response"][teams.index(teams_drop_list.get())]["venue"]["image"]
        stadium_image = ImageTk.PhotoImage(Image.open(requests.get(stadium_url, stream=True).raw))
        stadium_label = Label(image=stadium_image)
        stadium_label.image = stadium_image
        stadium_label.place(x=14, y=330)
        content_widgets.append(stadium_label)

        # drawing headers
        info_headers = ["Name", "Code", "Founded", "City", "Stadium", "Capacity"]
        info_headers_positions = [(150, 76), (150, 110), (150, 144), (150, 178), (10, 230), (400, 230)]
        for i in range(len(info_headers)):
            label = CTkLabel(root, text=info_headers[i], font=FONT_12_BOLD)
            label.place(x=info_headers_positions[i][0], y=info_headers_positions[i][1])

        # drawing team info labels
        team_info_labels = [
            response.json()["response"][teams.index(teams_drop_list.get())]["team"]["name"],
            response.json()["response"][teams.index(teams_drop_list.get())]["team"]["code"],
            response.json()["response"][teams.index(teams_drop_list.get())]["team"]["founded"],
            response.json()["response"][teams.index(teams_drop_list.get())]["venue"]["city"],
            response.json()["response"][teams.index(teams_drop_list.get())]["venue"]["name"],
            response.json()["response"][teams.index(teams_drop_list.get())]["venue"]["capacity"]
        ]
        team_info_labels_positions = [(220, 76), (220, 110), (220, 144), (220, 178), (70, 230), (462, 230)]
        for i in range(len(team_info_labels)):
            label = CTkLabel(root, text=team_info_labels[i], font=FONT_12)
            label.place(x=team_info_labels_positions[i][0], y=team_info_labels_positions[i][1])
            content_widgets.append(label)

    # drawing dropdown list and "show" button
    teams_drop_list = DropdownList(root, values=teams, width=144)
    teams_drop_list.set("Manchester United")
    teams_drop_list.place(x=10, y=40)
    show_button = ContentButton(root, text="Show team info", command=lambda: show_team(root))
    show_button.place(x=160, y=40)
