import requests

champion_json = {}

def get_latest_ddragon():
    global champion_json
    if champion_json:
        return champion_json

    versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
    latest = versions.json()[0]

    ddragon = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion.json")

    champions = ddragon.json()["data"]
    champion_json = champions
    return champions

def get_champion_by_key(key):
    champions = get_latest_ddragon()

    for champion_name in champions:
        if not champions[champion_name]: continue

        if champions[champion_name]["key"] == str(key):
            return champions[champion_name]['id']

    return False

def get_all_champions_in_list():
    champions = get_latest_ddragon()
    biggest_list = []

    for champion_names in champions: 
        if champions[champion_names]["key"].isdigit(): # if the key of the champions is a digit
            set_of_info = (champions[champion_names]['id'], champions[champion_names]['tags']) # add to the big list the champion's name
            biggest_list.append(set_of_info)
        
    return biggest_list


#print(get_all_champions_in_list()) # PRINTS OUT THEIR CHARACTER CLASS
# INSIDE THE BRACKET -> we put all of the champion ID and run it through here, then produce a list with the names of champions i usually play