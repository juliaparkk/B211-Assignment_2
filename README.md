# B211-Assignment_2

# Purpose
This project analyzes NBA player season statistics from a TSV dataset to compute common performance metrics (shooting accuracies, points rates, and defensive rates). It produces top‑100 lists per metric and saves them to a text file for easy review.

# Data Source
Input file: NBA_Player_Stats.tsv
The dataset is a subset of a larger Kaggle repository (as provided for the assignment).
Class Design and Implementation
The program uses a single data model class, PlayerSeasonStats, to encapsulate one player’s statistics for a single season. This keeps the calculation logic close to the data and makes it easy to compute multiple metrics consistently.

# Class: PlayerSeasonStats
Represents one row of player-season statistics from the TSV file.

# Attributes
player: Player name.
season: Season identifier (e.g., 2019–2020).
team: Team abbreviation.
gp: Games played.
min: Total minutes played.
fgm: Field goals made.
fga: Field goals attempted.
pm3: Three‑pointers made.
pa3: Three‑pointers attempted.
ftm: Free throws made.
fta: Free throws attempted.
blk: Total blocks.
stl: Total steals.
pts: Total points.
All numeric attributes are stored as float to support division in metrics.

# Methods
fg_accuracy(): Field goal accuracy = fgm / fga (0 if fga is 0).
three_pt_accuracy(): Three‑point accuracy = pm3 / pa3 (0 if pa3 is 0).
ft_accuracy(): Free‑throw accuracy = ftm / fta (0 if fta is 0).
points_per_minute(): Points per minute = pts / min (0 if min is 0).
points_per_game(): Points per game = pts / gp (0 if gp is 0).
overall_accuracy(): Overall shooting accuracy = (fgm + ftm) / (fga + fta) (0 if attempts are 0).
blocks_per_game(): Blocks per game = blk / gp (0 if gp is 0).
steals_per_game(): Steals per game = stl / gp (0 if gp is 0).

# Processing Flow
Load the TSV file with csv.DictReader.
Build a list of PlayerSeasonStats objects.
Sort by each metric and extract the top 100.
Print results and write all top‑100 lists to Top_100_Lists.txt.
Output

Console output for each top‑100 list.
File output: Top_100_Lists.txt in the same folder as the script.
Limitations and Assumptions

The script expects the input file NBA_Player_Stats.tsv to exist in the same folder as Assignment 2 Numpy.py.
No data cleaning is performed beyond safe division checks. If the dataset contains unexpected text or missing columns, the script may fail.
overall_accuracy() uses total field‑goal and free‑throw attempts; three‑pointers are already included in field‑goal attempts, so they are not counted twice.
The output lists are based on raw season totals and do not include minimum‑games or minimum‑attempts filters. This can favor small‑sample seasons with unusually high percentages.
