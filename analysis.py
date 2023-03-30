import pandas as pd
import os
from utils import *

for file in os.listdir("./simulation_results/data"):
    data = pd.read_csv(f"./simulation_results/data/{file}")
    turns = file.split('_')[0]
    games = file.split('_')[2]
    subdirectory = f"{turns}_turns_{games}_games"
    # Create directory if one does not exist
    if not os.path.exists(f"./simulation_results/plots/{subdirectory}"):
        os.makedirs(f"./simulation_results/plots/{subdirectory}")
    # Average Spaces Moved and Coins Earned
    summarized_results = summarize(data)

    # Plot Average Spaces Moved in desc order
    avg_spaces_plot(summarized_results, number_of_games=games, number_of_turns=turns, download=True)

    # Plot Average Coins Earned in desc order
    avg_coins_plot(summarized_results, number_of_games=games, number_of_turns=turns, download=True)

    # Boxplots of Spaces Moved in desc order
    spaces_moved_boxplot(data, number_of_games=games, number_of_turns=turns, download=True)

    # Spaces Moved Distribution
    spaces_moved_histogram(data, number_of_games=games, number_of_turns=turns, download=True)