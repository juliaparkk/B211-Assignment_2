import os
import numpy as np

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "NBA_Player_Stats.tsv")
OUTPUT_PATH = os.path.join(BASE_DIR, "Top_100_Lists.txt")

class PlayerSeasonMetrics:
    def __init__(self, data):
        self.data = data
        self.player = np.asarray(data["Player"], dtype=str)
        self.season = np.asarray(data["Season"], dtype=str)
        self.team = np.asarray(data["Team"], dtype=str)

        self.gp = np.asarray(data["GP"], dtype=float)
        self.min = np.asarray(data["MIN"], dtype=float)

        self.fgm = np.asarray(data["FGM"], dtype=float)
        self.fga = np.asarray(data["FGA"], dtype=float)

        self.pm3 = np.asarray(data["3PM"], dtype=float)
        self.pa3 = np.asarray(data["3PA"], dtype=float)

        self.ftm = np.asarray(data["FTM"], dtype=float)
        self.fta = np.asarray(data["FTA"], dtype=float)

        self.blk = np.asarray(data["BLK"], dtype=float)
        self.stl = np.asarray(data["STL"], dtype=float)

        self.pts = np.asarray(data["PTS"], dtype=float)

    @staticmethod
    def safe_divide(numerator, denominator):
        return np.divide(
            numerator,
            denominator,
            out=np.zeros_like(numerator, dtype=float),
            where=denominator > 0,
        )

    # ---- Metric Methods ----
    def fg_accuracy(self):
        return self.safe_divide(self.fgm, self.fga)

    def three_pt_accuracy(self):
        return self.safe_divide(self.pm3, self.pa3)

    def ft_accuracy(self):
        return self.safe_divide(self.ftm, self.fta)

    def points_per_minute(self):
        return self.safe_divide(self.pts, self.min)

    def points_per_game(self):
        return self.safe_divide(self.pts, self.gp)

    def overall_accuracy(self):
        made = self.fgm + self.ftm
        attempts = self.fga + self.fta
        return self.safe_divide(made, attempts)

    def blocks_per_game(self):
        return self.safe_divide(self.blk, self.gp)

    def steals_per_game(self):
        return self.safe_divide(self.stl, self.gp)

    @staticmethod
    def top_n(values, n=100):
        if values.size == 0:
            return np.array([], dtype=int)
        order = np.argsort(values)[::-1]
        return order[: min(n, values.size)]

    def format_top(self, title, values, n=100):
        idx = self.top_n(values, n)
        lines = [title]
        for i in idx:
            lines.append(f"{self.player[i]}\t{self.season[i]}\t{values[i]}")
        return "\n".join(lines)

    def print_top(self, title, values, n=100):
        print(f"\n{title}")
        idx = self.top_n(values, n)
        for i in idx:
            print(self.player[i], self.season[i], values[i])


def load_data(path):
    return np.genfromtxt(
        path,
        delimiter="\t",
        names=True,
        dtype=None,
        encoding="utf-8",
    )


def main():
    data = load_data(DATA_PATH)
    metrics = PlayerSeasonMetrics(data)

    fg = metrics.fg_accuracy()
    three_pt = metrics.three_pt_accuracy()
    ft = metrics.ft_accuracy()
    ppm = metrics.points_per_minute()
    ppg = metrics.points_per_game()
    overall = metrics.overall_accuracy()
    blk = metrics.blocks_per_game()
    stl = metrics.steals_per_game()

    lists = [
        ("Top 100 Field Goal Accuracy", fg),
        ("Top 100 Three Point Accuracy", three_pt),
        ("Top 100 Free Throw Accuracy", ft),
        ("Top 100 Points Per Minute", ppm),
        ("Top 100 Points Per Game", ppg),
        ("Top 100 Overall Shooting Accuracy", overall),
        ("Top 100 Blocks Per Game", blk),
        ("Top 100 Steals Per Game", stl),
    ]

    for title, values in lists:
        metrics.print_top(title, values)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as output_file:
        output_file.write("\n\n".join(metrics.format_top(title, values) for title, values in lists))


if __name__ == "__main__":
    main()
