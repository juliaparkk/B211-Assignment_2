import csv
import os

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "NBA_Player_Stats.tsv")
OUTPUT_PATH = os.path.join(BASE_DIR, "Top_100_Lists.txt")

class PlayerSeasonStats:
    def __init__(self, row):
        self.player = row["Player"]
        self.season = row["Season"]
        self.team = row["Team"]

        self.gp = float(row["GP"])
        self.min = float(row["MIN"])

        self.fgm = float(row["FGM"])
        self.fga = float(row["FGA"])

        self.pm3 = float(row["3PM"])
        self.pa3 = float(row["3PA"])

        self.ftm = float(row["FTM"])
        self.fta = float(row["FTA"])

        self.blk = float(row["BLK"])
        self.stl = float(row["STL"])

        self.pts = float(row["PTS"])

    # ---- Metric Methods ----
    def fg_accuracy(self):
        return self.fgm / self.fga if self.fga > 0 else 0

    def three_pt_accuracy(self):
        return self.pm3 / self.pa3 if self.pa3 > 0 else 0

    def ft_accuracy(self):
        return self.ftm / self.fta if self.fta > 0 else 0

    def points_per_minute(self):
        return self.pts / self.min if self.min > 0 else 0

    def points_per_game(self):
        return self.pts / self.gp if self.gp > 0 else 0

    def overall_accuracy(self):
        made = self.fgm + self.ftm
        attempts = self.fga + self.fta
        return made / attempts if attempts > 0 else 0

    def blocks_per_game(self):
        return self.blk / self.gp if self.gp > 0 else 0

    def steals_per_game(self):
        return self.stl / self.gp if self.gp > 0 else 0

stats_list = []

with open(DATA_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        stats_list.append(PlayerSeasonStats(row))

top_fg = sorted(stats_list, key=lambda x: x.fg_accuracy(), reverse=True)[:100]
top_3pt = sorted(stats_list, key=lambda x: x.three_pt_accuracy(), reverse=True)[:100]
top_ft = sorted(stats_list, key=lambda x: x.ft_accuracy(), reverse=True)[:100]
top_ppm = sorted(stats_list, key=lambda x: x.points_per_minute(), reverse=True)[:100]
top_ppg = sorted(stats_list, key=lambda x: x.points_per_game(), reverse=True)[:100]
top_overall = sorted(stats_list, key=lambda x: x.overall_accuracy(), reverse=True)[:100]
top_blk = sorted(stats_list, key=lambda x: x.blocks_per_game(), reverse=True)[:100]
top_stl = sorted(stats_list, key=lambda x: x.steals_per_game(), reverse=True)[:100]

def format_top(title, players, value_fn):
    lines = [title]
    for player in players:
        lines.append(f"{player.player}\t{player.season}\t{value_fn(player)}")
    return "\n".join(lines)

def print_top(title, players, value_fn):
    print(f"\n{title}")
    for player in players:
        print(player.player, player.season, value_fn(player))

lists = [
    ("Top 100 Field Goal Accuracy", top_fg, lambda x: x.fg_accuracy()),
    ("Top 100 Three Point Accuracy", top_3pt, lambda x: x.three_pt_accuracy()),
    ("Top 100 Free Throw Accuracy", top_ft, lambda x: x.ft_accuracy()),
    ("Top 100 Points Per Minute", top_ppm, lambda x: x.points_per_minute()),
    ("Top 100 Points Per Game", top_ppg, lambda x: x.points_per_game()),
    ("Top 100 Overall Shooting Accuracy", top_overall, lambda x: x.overall_accuracy()),
    ("Top 100 Blocks Per Game", top_blk, lambda x: x.blocks_per_game()),
    ("Top 100 Steals Per Game", top_stl, lambda x: x.steals_per_game()),
]

for title, players, value_fn in lists:
    print_top(title, players, value_fn)

with open(OUTPUT_PATH, "w", encoding="utf-8") as output_file:
    output_file.write("\n\n".join(format_top(title, players, value_fn) for title, players, value_fn in lists))
