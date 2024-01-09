from flask import Flask, render_template, request
from get_summoner_data import get_mastery_data
from league_recommendation_tool import Champion_Recommendation_Tool, Comparison_Tool
from testing import get_latest_ddragon, get_champion_by_key, get_all_champions_in_list

import os 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():

    api_key = os.getenv('API_KEY')
    username = request.form.get('username')
    json_file = get_mastery_data(api_key, username) # this code returns the json file for the user's champion_mastery_data in riots api
    print(json_file)
    if json_file is None:
        return render_template('error.html', message="Invalid username. Please try again.")
    
    else:
        recommend = Champion_Recommendation_Tool(json_file)# Use the username to get champion recommendations
        recommendations= recommend.load_summoner_data()
    

        all_champion_list = get_all_champions_in_list() # this is a list of every champion in LOL
        comparison = Comparison_Tool(recommendations, all_champion_list) # this cross references both lists
        most_played = comparison.get_most_played() # to produce the list of champion names that i play a lot
        comparison.my_champions_played_classified()

        mid_recommendations = comparison.mid_classes_counter()
        top_recommendations = comparison.top_classes_counter()
        support_recommendations = comparison.support_class_counter()
        jungle_recommendations = comparison.jungle_class_counter()
        adc_recommendations = comparison.adc_class_counter()

        print(mid_recommendations)
    # Call your existing code for recommendations here

    # Assuming `recommendations` is a list of recommended champions
        return render_template('recommendations.html', mid_recommendations=mid_recommendations, top_recommendations=top_recommendations, support_recommendations=support_recommendations, adc_recommendations=adc_recommendations, jungle_recommendations=jungle_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
