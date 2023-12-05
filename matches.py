import requests
from customtkinter import CTkLabel
from widgets_fonts_auth import ContentButton, DropdownList, FONT_12_ITALIC, FONT_13, headers


# api request for displaying current round
url_current_round = "https://api-football-beta.p.rapidapi.com/fixtures/rounds"
querystring_current_round = {"league": "39", "season": "2023", "current": "true"}
current_round = requests.get(url_current_round, headers=headers, params=querystring_current_round).json()['response']

# creating list of currently displayed widgets
content_widgets = []


def draw_matches(root):
    def draw_round(root, round):
        # api request for list of matches for specific round
        url_matches = "https://api-football-beta.p.rapidapi.com/fixtures"
        querystring_matches = {"league": "39", "round": f'Regular Season - {round}', "season": "2023"}
        response = requests.get(url_matches, headers=headers, params=querystring_matches).json()["response"]

        # clearing currently displayed widgets
        for widget in root.winfo_children():
            if widget in content_widgets:
                widget.destroy()

        # displaying matches
        k = 76
        for i in range(10):
            date_label = CTkLabel(root, text=response[i]["fixture"]["date"][:10], font=FONT_13)
            date_label.place(x=10, y=k)
            content_widgets.append(date_label)
            time_label = CTkLabel(root, text=response[i]["fixture"]["date"][11:16], font=FONT_13)
            time_label.place(x=84, y=k)
            content_widgets.append(time_label)
            teams_label = CTkLabel(
                root, text=f'{response[i]["teams"]["home"]["name"]}   -   {response[i]["teams"]["away"]["name"]}',
                font=FONT_13)
            teams_label.place(x=134, y=k)
            content_widgets.append(teams_label)
            if response[i]["goals"]["home"] is None:
                result_label = CTkLabel(root, text="-", font=FONT_13)
            else:
                result_label = CTkLabel(
                    root, text=f'{response[i]["goals"]["home"]} - {response[i]["goals"]["away"]}', font=FONT_13)
            result_label.place(x=440, y=k)
            content_widgets.append(result_label)
            place_label = CTkLabel(
                root, text=f'{response[i]["fixture"]["venue"]["city"]}, {response[i]["fixture"]["venue"]["name"]}',
                font=FONT_12_ITALIC)
            place_label.place(x=10, y=20+k)
            content_widgets.append(place_label)
            k += 54

    # drawing dropdown list and "show" button
    teams_drop_list = DropdownList(root, values=[str(i) for i in range(1, 39)], width=60)
    teams_drop_list.set(["".join(c) for c in current_round[0].split() if c.isdigit()][0])
    teams_drop_list.place(x=10, y=40)
    show_button = ContentButton(root, text="Show matches", command=lambda: draw_round(root, teams_drop_list.get()))
    show_button.place(x=76, y=40)

    # drawing current game week fixtures
    draw_round(root, ["".join(c) for c in current_round[0].split() if c.isdigit()][0])
