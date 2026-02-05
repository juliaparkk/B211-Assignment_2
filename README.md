# B211-Assignment_2

## Purpose
This project analyzes NBA player season statistics using NumPy to compute shooting accuracy and per‑game/per‑minute performance metrics. It then outputs top‑100 lists for each metric to a text file for easy review.

## Data
Input file: NBA_Player_Stats.tsv (tab‑separated values)

Each row represents one player season and includes fields such as games played, minutes, field goals, three‑pointers, free throws, points, blocks, and steals.

## Design Overview
The solution is centered around one NumPy‑driven class plus small helper functions:

### Class: PlayerSeasonMetrics
**Purpose:**
Stores the full dataset in NumPy arrays and provides vectorized methods to compute all required metrics.

**Attributes:**
- player: NumPy array of player names (string)
- season: NumPy array of seasons (string)
- team: NumPy array of team abbreviations (string)
- gp: games played (float)
- min: minutes played (float)
- fgm, fga: field goals made/attempted (float)
- pm3, pa3: three‑pointers made/attempted (float)
- ftm, fta: free throws made/attempted (float)
- blk: blocks (float)
- stl: steals (float)
- pts: points (float)

**Methods:**
- safe_divide(numerator, denominator)
  - Vectorized divide that returns 0 where the denominator is 0.
- fg_accuracy()
  - Field goal accuracy: FGM / FGA.
- three_pt_accuracy()
  - Three‑point accuracy: 3PM / 3PA.
- ft_accuracy()
  - Free throw accuracy: FTM / FTA.
- points_per_minute()
  - Average points per minute: PTS / MIN.
- points_per_game()
  - Average points per game: PTS / GP.
- overall_accuracy()
  - Overall shooting accuracy: (FGM + FTM) / (FGA + FTA).
- blocks_per_game()
  - Average blocks per game: BLK / GP.
- steals_per_game()
  - Average steals per game: STL / GP.
- top_n(values, n=100)
  - Returns the indices of the top N values.
- format_top(title, values, n=100)
  - Formats the top N list for file output.
- print_top(title, values, n=100)
  - Prints the top N list to the console.

### Helper Functions
- load_data(path)
  - Uses NumPy’s genfromtxt to load the TSV into a structured array.
- main()
  - Orchestrates loading data, computing metrics, printing results, and writing the top‑100 lists to Top_100_Lists.txt.

## Output
Top‑100 lists are printed to the console and written to:
- Top_100_Lists.txt

Metrics included:
- Field goal accuracy
- Three‑point accuracy
- Free throw accuracy
- Points per minute
- Points per game
- Overall shooting accuracy
- Blocks per game
- Steals per game

## Limitations
- Rows with zero attempts/minutes/games return 0 for that metric (to avoid division errors).
- The input file must match the expected column names.
- Ties are kept in NumPy’s default sort order (stable ordering is not enforced).

