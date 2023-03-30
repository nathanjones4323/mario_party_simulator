import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def get_plot_directory(number_of_turns, number_of_games):
    plot_directory = f"./simulation_results/plots/{number_of_turns}_turns_{number_of_games}_games"
    return plot_directory
get_plot_directory(10, 10)

def summarize(df):
    summarized_results = df.groupby("character").agg({
    "coins": np.mean,
    "spaces": np.mean
    }).reset_index().rename(columns={"coins": "average_coins_earned", "spaces": "average_spaces_moved"})
    return summarized_results

# Plot Average Spaces Moved in desc order
def avg_spaces_plot(df, number_of_games, number_of_turns, download=True):
    desc_order = df.sort_values(by=["average_spaces_moved"], ascending=False)["character"]
    sns.barplot(data=df, y="character", x="average_spaces_moved", order=desc_order)
    plt.suptitle(f"Average Spaces Moved by Character Over {number_of_games} Games")
    plt.title(f"(Simulated games had {number_of_turns} turns each)", fontsize=9)
    plt.xlabel("Average Spaces Moved")
    plt.ylabel("Character")
    print(get_plot_directory(number_of_turns, number_of_games))
    print(f"{get_plot_directory(number_of_turns, number_of_games)}/average_spaces_moved_per_character_{number_of_turns}_turn_{number_of_games}_game_simulations.png")
    if download == True:
        plt.savefig(f"{get_plot_directory(number_of_turns, number_of_games)}/average_spaces_moved_per_character_{number_of_turns}_turn_{number_of_games}_game_simulations.png")
    else:
        plt.show()
    plt.clf()

# Plot Average Coins Earned in desc order
def avg_coins_plot(df, number_of_games, number_of_turns, download=True):
    desc_order = df[df["average_coins_earned"] != 0].sort_values(by=["average_coins_earned"], ascending=False)["character"]
    sns.barplot(data=df, y="character", x="average_coins_earned", order=desc_order)
    plt.suptitle(f"Average Coins Earned from Rolls by Character Over {number_of_games} Games")
    plt.title(f"Characters without coin blocks are removed (Simulated games had {number_of_turns} turns)", fontsize=9)
    plt.xticks(range(int(df["average_coins_earned"].min()), int(df["average_coins_earned"].max())))
    plt.xlabel("Average Coins Earned")
    plt.ylabel("Character")
    
    if download == True:
        plt.savefig(f"{get_plot_directory(number_of_turns, number_of_games)}/average_coins_earned_per_character_{number_of_turns}_turn_{number_of_games}_game_simulations.png")
    else:
        plt.show()
    plt.clf()


# Boxplots of Spaces Moved in desc order
def spaces_moved_boxplot(df, number_of_games, number_of_turns, download=True):
    desc_order = df.groupby(by=["character"])["spaces"].median().sort_values(ascending=False).index
    sns.boxplot(data=df, y="character", x="spaces", order=desc_order)
    plt.suptitle(f"Boxplots of Spaces Moved by Character Over {number_of_games} Games")
    plt.title(f"(Simulated games had {number_of_turns} turns each)", fontsize=9)
    plt.xlabel("Spaces Moved")
    plt.ylabel("Character")
    
    if download == True:
        plt.savefig(f"{get_plot_directory(number_of_turns, number_of_games)}/spaces_moved_per_character_boxplot_{number_of_turns}_turn_{number_of_games}_game_simulations.png")
    else:
        plt.show()
    plt.clf()

# Spaces Moved Distribution
def spaces_moved_histogram(df, number_of_games, number_of_turns, download=True):
    g = sns.displot(data=df, x="spaces", hue="character", col="character", kind="hist", col_wrap=4)
    g.set_axis_labels("Total Spaces Moved", "Number of Games")
    g.set_titles("Playing as {col_name}")
    
    if download == True:
        plt.savefig(f"{get_plot_directory(number_of_turns, number_of_games)}/spaces_moved_per_character_histogram_{number_of_turns}_turn_{number_of_games}_game_simulations.png")
    else:
        plt.show()
    plt.clf()