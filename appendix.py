import pandas as pd
import time

# Time the code execution
start_time = time.time()

# Read in data
dice_data = pd.read_csv("super_mario_party_characters_and_dice.csv")
dice_data = dice_data.astype(str)

# Initialize empty df to store the results
results = pd.DataFrame()


number_of_turns = 10
number_of_games = 1000
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

results.to_csv(f"./simulation_results/data/{number_of_turns}_turn_{number_of_games}_games_simulation_results.csv", index=False)

print(f"--- {round(time.time() - start_time, 2)} seconds ---")

# 1 = 0.52 seconds
# 10 = 3.91 seconds
# 100 = 3.91 seconds
# 1,000 = 38.09 seconds
# 10,000 = 374.36 seconds
# 100,000 = 3,750.36 seconds