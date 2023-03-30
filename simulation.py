import pandas as pd
import time
import numpy as np
import os

# Time the code execution
start_time = time.time()

# Rolls per Game * Number of Games = Total Rolls

# Read in data
dice_data = pd.read_csv("super_mario_party_characters_and_dice.csv")
dice_data = dice_data.astype(str)

# Initialize empty df to store the results
results = pd.DataFrame()

# Run the Simulation
turns = [10, 15, 20, 25]
games = [1, 10, 100, 1000, 10000]
# Get unique combinations of turns and games
pairs = [(x, y) for x in turns for y in games]
for i in range(0, len(pairs)):
    number_of_turns = pairs[i][0]
    number_of_games = pairs[i][1]
    for i in range(0, number_of_games):
        # Initalize lists to store results of X rolls for each character
        coin_list = []
        space_list = []
        for character in dice_data["character"]:
            # Initialize coins and spaces counters
            coins = 0
            spaces = 0
            for j in range(0, number_of_turns):
                roll = dice_data[dice_data["character"] == character].drop(columns=["character"]).sample(axis="columns").iloc[0].item()
                # Parse coin amounts
                if 'c' in roll:
                    roll = roll.replace('c', '')
                    roll = int(roll)
                    coins = coins + roll
                else:
                    roll = int(roll)
                    spaces = spaces + roll
            # Add total coins and spaces to lists
            coin_list.append(coins)
            space_list.append(spaces)

        # Dataframe to store the results of the simulation
        result = pd.DataFrame({
            "game_id": i+1,
            "character": dice_data["character"],
            "coins": coin_list,
            "spaces": space_list,
        })
        results = pd.concat([results, result])
    if not os.path.exists(f"./simulation_results/data"):
        os.makedirs(f"./simulation_results/data")
    results.to_csv(f"./simulation_results/data/{number_of_turns}_turn_{number_of_games}_games_simulation_results.csv", index=False)

print(f"--- {round(time.time() - start_time, 2)} seconds ---")

# 1 = 0.52 seconds
# 10 = 3.91 seconds
# 100 = 3.91 seconds
# 1,000 = 38.09 seconds
# 10,000 = 374.36 seconds
# 100,000 = 3,750.36 seconds