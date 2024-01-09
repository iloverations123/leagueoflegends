import requests
import json
import os




def get_mastery_data(api_key, summoner_name):
    url = f"https://sg2.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {
        "X-Riot-Token": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        encrypted_account_id = data["id"]

        url = f"https://sg2.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encrypted_account_id}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            mastery_data = response.json()

            with open('champion_mastery_data.json', 'w') as file:
                json.dump(mastery_data, file)

            print("Champion mastery data saved successfully.")
        else:
            print("ERROR HERE")
            print(f"Error getting mastery data: {response.status_code}")
        
        if os.path.exists('champion_mastery_data.json'):
            with open('champion_mastery_data.json', 'r') as file:
                champion_data = json.load(file)
                return champion_data
        else:
            print("Error: champion_mastery_data.json not found")

    else:
        print(f"Error getting summoner data: {response.status_code}")
