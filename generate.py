import csv
import json
import openai
openai.api_key = "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"

# Open the CSV file containing the IPL match data
with open('output.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    data = []

    # Loop through each row in the CSV file
    for row in reader:
        # Generate the prompt and completion for the current match
        prompt = f"Match between {row['team1']} and {row['team2']} at {row['stadium']}."
        completion = f"The match was won by {row['winner']} by {row['margin']} runs. The toss was won by {row['toss_winner']} who chose to {row['toss_choice']}. The man of the match was {row['man_of_the_match']}. The final score was {row['team1_score']}/{row['team2_score']}."

        # Add the prompt and completion to the data list
        data.append({'prompt': prompt, 'completion': completion})

# Save the prompt and completion pairs to a JSON file
with open('ipl_data.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)