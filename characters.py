import pandas as pd

# Read in the data
dice_data = pd.read_html("https://miketendo64.com/2018/10/08/super-mario-party-character-dice-guide/")[0]

# Clean up column names
snake_case_columns = {str(i): str(i.replace(' ', '_').lower()) for i in dice_data.columns}
dice_data.rename(columns=snake_case_columns, inplace=True)

# Split dice rolls into their own columns
dice_data[['die_side_1', 'die_side_2', 'die_side_3', 'die_side_4', 'die_side_5', 'die_side_6']] = dice_data["dice_block"].str.split(',', expand=True)
dice_data.drop(columns=["dice_block"], inplace=True)

# Clean Text
dice_data[['die_side_1', 'die_side_2', 'die_side_3', 'die_side_4', 'die_side_5', 'die_side_6']] = dice_data[['die_side_1', 'die_side_2', 'die_side_3', 'die_side_4', 'die_side_5', 'die_side_6']].apply(lambda series: series.str.replace("( )+", '', regex=True).str.replace("coins", "c", regex=False).str.replace("coin", "c").str.replace("+", "", regex=False).str.replace("–", "-", regex=False))

dice_data.to_csv("super_mario_party_characters_and_dice.csv", index=False)