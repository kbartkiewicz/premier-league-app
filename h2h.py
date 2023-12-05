import requests
from customtkinter import CTkLabel
from tkinter import messagebox
from widgets_fonts_auth import DropdownList, ContentButton, FONT_12, FONT_12_BOLD, FONT_14_BOLD, headers


# creating a dictionary of teams and IDs
teams = {
    "Manchester United": 33,
    "Newcastle": 34,
    "Bournemouth": 35,
    "Fulham": 36,
    "Wolves": 39,
    "Liverpool": 40,
    "Arsenal": 42,
    "Burnley": 44,
    "Everton": 45,
    "Tottenham": 47,
    "West Ham": 48,
    "Chelsea": 49,
    "Manchester City": 50,
    "Brighton": 51,
    "Crystal Palace": 52,
    "Brentford": 55,
    "Sheffield Utd": 62,
    "Nottingham Forest": 65,
    "Aston Villa": 66,
    "Luton": 1359
}

# creating list of currently displayed widgets
content_widgets = []


def draw_h2h_comparison(root):
    def show_comparison(root, team_1, team_2):
        # showing message box if both teams are the same
        if team_1 == team_2:
            messagebox.showinfo("Premier League app", "Choose two different teams!")
        else:
            # api request for teams info
            url = "https://api-football-beta.p.rapidapi.com/fixtures/headtohead"
            querystring = {"h2h": f"{team_1}-{team_2}", "last": "10"}
            response = requests.get(url, headers=headers, params=querystring)

            # clearing currently displayed widgets
            for widget in root.winfo_children():
                if widget in content_widgets:
                    widget.destroy()

            team_1_wins, team_2_wins, team_1_goals, team_2_goals, team_1_clean_sheets, team_2_clean_sheets = 0, 0, 0, 0, 0, 0

            # drawing team names
            team_left_label = CTkLabel(root, text=team_left.get(), font=FONT_14_BOLD)
            team_left_label.place(x=20, y=100, anchor="w")
            content_widgets.append(team_left_label)
            team_right_label = CTkLabel(root, text=team_right.get(), font=FONT_14_BOLD)
            team_right_label.place(x=484, y=100, anchor="e")
            content_widgets.append(team_right_label)

            # setting number of displayed matches
            if response.json()["results"] > 9:
                number_of_matches = 10
            else:
                number_of_matches = response.json()["results"]

            # displaying the fixtures on screen
            k = 320
            for i in range(number_of_matches):
                home_team_name = response.json()["response"][i]["teams"]["home"]["name"]
                away_team_name = response.json()["response"][i]["teams"]["away"]["name"]
                home_team_score = response.json()["response"][i]["score"]["fulltime"]["home"]
                away_team_score = response.json()["response"][i]["score"]["fulltime"]["away"]

                teams_label = CTkLabel(root, text=f'{home_team_name}   -   {away_team_name}', font=FONT_12)
                teams_label.place(x=110, y=k)
                content_widgets.append(teams_label)
                score_label = CTkLabel(root, text=f'{home_team_score} - {away_team_score}', font=FONT_12)
                score_label.place(x=334, y=k)
                content_widgets.append(score_label)
                league_label = CTkLabel(root, text=response.json()["response"][i]["league"]["name"], font=FONT_12)
                league_label.place(x=390, y=k)
                content_widgets.append(league_label)
                date_label = CTkLabel(root, text=response.json()["response"][i]["fixture"]["date"][:10], font=FONT_12)
                date_label.place(x=10, y=k)
                content_widgets.append(date_label)
                k += 28

                # setting the wins, goals and clean sheets variables
                if home_team_name == team_left.get():
                    team_1_goals += home_team_score
                    team_2_goals += away_team_score
                    if home_team_score == 0:
                        team_2_clean_sheets += 1
                    if away_team_name == 0:
                        team_1_clean_sheets += 1
                    if home_team_score > away_team_score:
                        team_1_wins += 1
                    elif home_team_score < away_team_score:
                        team_2_wins += 1
                else:
                    team_2_goals += home_team_score
                    team_1_goals += away_team_score
                    if home_team_score == 0:
                        team_1_clean_sheets += 1
                    if away_team_score == 0:
                        team_2_clean_sheets += 1
                    if home_team_score > away_team_score:
                        team_2_wins += 1
                    elif home_team_score < away_team_score:
                        team_1_wins += 1

            # drawing h2h headers
            h2h_headers = ["Matches won", "Goals", "Clean sheets"]
            h2h_stats_positions = [(252, 160), (252, 200), (252, 240)]
            for i in range(len(h2h_headers)):
                label = CTkLabel(root, text=h2h_headers[i], font=FONT_12_BOLD)
                label.place(x=h2h_stats_positions[i][0], y=h2h_stats_positions[i][1], anchor="center")
                content_widgets.append(label)

            # displaying stats (wins, goals, clean sheets)
            t1_wins_label = CTkLabel(root, text=str(team_1_wins), font=FONT_12)
            t1_wins_label.place(x=164, y=h2h_stats_positions[0][1], anchor="e")
            content_widgets.append(t1_wins_label)
            t2_wins_label = CTkLabel(root, text=str(team_2_wins), font=FONT_12)
            t2_wins_label.place(x=340, y=h2h_stats_positions[0][1], anchor="w")
            content_widgets.append(t2_wins_label)
            t1_goals_label = CTkLabel(root, text=str(team_1_goals), font=FONT_12)
            t1_goals_label.place(x=164, y=h2h_stats_positions[1][1], anchor="e")
            content_widgets.append(t1_goals_label)
            t2_goals_label = CTkLabel(root, text=str(team_2_goals), font=FONT_12)
            t2_goals_label.place(x=340, y=h2h_stats_positions[1][1], anchor="w")
            content_widgets.append(t2_goals_label)
            t1_clean_sheets_label = CTkLabel(root, text=str(team_1_clean_sheets), font=FONT_12)
            t1_clean_sheets_label.place(x=164, y=h2h_stats_positions[2][1], anchor="e")
            content_widgets.append(t1_clean_sheets_label)
            t2_clean_sheets_label = CTkLabel(root, text=str(team_2_clean_sheets), font=FONT_12)
            t2_clean_sheets_label.place(x=340, y=h2h_stats_positions[2][1], anchor="w")
            content_widgets.append(t2_clean_sheets_label)

    # displaying two dropdown lists and "show" button
    team_left = DropdownList(root, values=list(teams.keys()), width=160)
    team_left.set(list(teams.keys())[0])
    team_left.place(x=10, y=40)
    team_right = DropdownList(root, values=list(teams.keys()), width=160)
    team_right.set(list(teams.keys())[1])
    team_right.place(x=180, y=40)
    show_button = ContentButton(root, text="Compare", command=lambda: show_comparison(
        root, teams[team_left.get()], teams[team_right.get()]))
    show_button.place(x=350, y=40)
