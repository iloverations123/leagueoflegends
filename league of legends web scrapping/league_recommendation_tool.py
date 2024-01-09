import json
import random
from testing import get_latest_ddragon, get_champion_by_key, get_all_champions_in_list
from LEAGUE_DICTIONARY import league

# what to do tmr:
# start making the counter for the different roles e.g. top,mid,jg,ad,sp with the dict


# long-term -> upload this onto a website
" ok so heres how the idea is going to go: 1) filter most played champions, mastery wise and sort out the roles they belong to" 
"2) after finding out which role (for e.g. top lane) has the most no. of champions, sort them out according to tanks, bruisers, ranged "
"3) again, after finding out which subcategory has the most no. of champions (for e.g. bruisres), comb through the original list again"
"4) find out which champion matches these categories that is ==  mastery 5 or below it"


# Step 1.5: Import my own json file with my own champion mastery

class Champion_Recommendation_Tool:
    def __init__(self, champion_data):
        self.champion_data = champion_data
        self.my_champion_list_info= []
    
    def load_summoner_data(self):
        for i in self.champion_data:
            champions_name = get_champion_by_key(i['championId'])
            champion_info = (champions_name, i['championLevel']) # forms the tuple of (Champion ID, Champion Mastery)
            self.my_champion_list_info.append(champion_info) # adds it to the list
            
            #print(self.my_champion_list_info) # basically a big list of tuples so [(Gangplank,5), (Gwen,5)]
        return self.my_champion_list_info

            #  

class Comparison_Tool():
    def __init__(self, champion_mastery_list, all_champions):
        self.champion_mastery_list = champion_mastery_list
        self.all_champions = all_champions
        self.top_champions_played = []
        self.mid_champions_played = []
        self.jungle_champions_played = [] 
        self.adc_champions_played = [] 
        self.support_champions_played = []
  

    def get_most_played(self):
        self.similarities = []
        for mastery_item in self.champion_mastery_list:
            for all_champs in self.all_champions:
                if mastery_item[0] == all_champs[0]:
                    self.similarities.append((mastery_item[0], mastery_item[1]))

        # ok so this prints out all of the champs that ive played before and have gotten a mastery on in a list
        print(self.similarities)
        return self.similarities
        # now i think i might have to create a dictionary whereby it shows the champion, identity: tank for example, role: top/jg etc

    def my_champions_played_classified(self):
        #self.a_list = []
        for champions_played in self.similarities:
            for champions in league:
                if champions_played[0] == champions['champion name']:
                    #self.a_list.append(champions['position']) 
                    "The above prints out the roles of the champions i play in order of mastery"

                    if champions['position'] == 'Top':
                        self.top_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == 'Mid':
                        self.mid_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == 'ADC':
                        self.adc_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == "Support":
                        self.support_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == "Jungle":
                        self.jungle_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == "Mid/Top":
                        self.mid_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                        self.top_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == "Support/Mid":
                        self.mid_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                        self.support_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == "Top/Jungle":
                        self.top_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                        self.jungle_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == "Support/Jungle":
                        self.support_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                        self.jungle_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                    if champions['position'] == "Top/Support":
                        self.top_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
                        self.support_champions_played.append((champions['champion name'], champions['class'], champions_played[1]))
        

        return self.top_champions_played, self.mid_champions_played, self.adc_champions_played, self.support_champions_played, self.jungle_champions_played
        # ok i want the website to look like this: enter summoner name, champion recommendations for which role --> produce results of champions they usually play and what we recommend.

        # ok maybe we dont need a counter, instead we classify the champions i play into their roles, e.g. top = [ornn, nasus]
        # then afterwards, i loop through the list to categorize the top champions into their classes. [maybe have a class counter]


        # i just realized i need to reclassify ADC's identities, they are all marksmen but serve different purposes
    
    def top_classes_counter(self): # start making other methods for other classes
        #print(self.top_champions_played)
        top_class_counter = {'Tank': 0, 'Bruiser': 0, 'Marksman': 0, 'Mage': 0, 'Assassin':0 } # basically sets up a scoreboard to keep track of the different classes
        mastery_count = []

        for top_champ, top_class, top_mastery in self.top_champions_played: # iterates through each tuple and assigns top_champ to the first element, top_class to the second element (Gragas, Mage)
            mastery_count.append(top_mastery)
            maximum = max(mastery_count)

            if 4 <= maximum:
                top_class_counter[top_class] += 1

            if 5 <= top_mastery <= 7:
                top_class_counter[top_class] += 1 # accesses the key in the dict that should match the top_class e.g. Tanks, Bruisers

        top_class_counts = [(cls, count) for cls, count in top_class_counter.items()] # items() returns the dictionary's key and value in a tuple 
            # so e.g. class_counts = [(Tank,5)(Bruiser,4)(Mage,9),(Marksman,2)]

        top_class_counts.sort(key=lambda x: x[1], reverse=True)  # sort is a method that allows me to arrange shit in the order i want
             # lambda x: x[1] takes a tuple x and returns x[1] so (tank,5) returns 5, then reverse = True (arranges it in descending order)

        majority_class_counts = top_class_counts[0][1]
        tied_classes = [cls for cls,value in top_class_counts if value == majority_class_counts]

        if len(tied_classes) > 1:
            randomized = random.choice(tied_classes)
            majority_class = randomized

        else:
            majority_class = top_class_counts[0][0]  # ok this basically gives me the first tuple and first element. e.g. (Mage)
            # is there a way to add second majority class?

        return [top_champ for top_champ, top_class, top_mastery in self.top_champions_played if top_class == majority_class and top_mastery < 5]
        

        # ok settled the mastery issue, now i need to recategorize ADCS (they are different types of marksmen) + start working on the other roles e.g. mid,jg,sp
    def mid_classes_counter(self):
        #print(self.mid_champions_played)
        mid_class_counting = {'Mage': 0, 'Assassin': 0, 'Tank': 0, 'Bruiser': 0, 'Marksman': 0}
        mastery_count = []
        
        for mid_champ, mid_class, mid_mastery in self.mid_champions_played:
            mastery_count.append(mid_mastery)
            maximum = max(mastery_count)

            if maximum <= 4: 
                mid_class_counting[mid_class] += 1

            if 5 <= mid_mastery <= 7:
                mid_class_counting[mid_class] += 1
            

        mid_class_counts = [(cls,value) for cls, value in mid_class_counting.items()]


        mid_class_counts.sort(key = lambda x: x[1], reverse = True)
        #print(mid_class_counts)

        majority_class_count = mid_class_counts[0][1]
        tied_classes = [cls for cls,value in mid_class_counts if value == majority_class_count ]

        if len(tied_classes) > 1:
            randomized = random.choice(tied_classes)
            majority_mid_class = randomized
        
        else:
            majority_mid_class = mid_class_counts[0][0]


        return [mid_champ for mid_champ, mid_class, mid_mastery in self.mid_champions_played if mid_class == majority_mid_class and mid_mastery < 5]
        

    
    def support_class_counter(self):
        #print(self.support_champions_played)
        support_class_counter = {'Enchanter': 0, 'Engager': 0, 'Marksman': 0, 'Tank': 0, 'Mage':0}
        # if i put pyke as engager, it says too many values to unpack at cls, _
        mastery_count = []
        

        for support_champ, support_class, support_mastery in self.support_champions_played:
            mastery_count.append(support_mastery)
            maximum = max(mastery_count)

            if maximum <= 4:
                support_class_counter[support_class] += 1
                
            if 5 <= support_mastery <= 7:
                support_class_counter[support_class] += 1
            
        support_class_counts = [(cls,value) for cls, value in support_class_counter.items()]
        support_class_counts.sort(key = lambda x: x[1], reverse = True)


        majority_class_counts = support_class_counts[0][1]

        tied_classes = [cls for cls, value in support_class_counts if value == majority_class_counts] # check if theres a tie
        
        if len(tied_classes) > 1:
            randomized = random.choice(tied_classes)
            majority_class = randomized
        
        else:
            majority_class = support_class_counts[0][0]
        
        return [support_champ for support_champ, support_class, support_mastery in self.support_champions_played if support_class == majority_class and support_mastery < 5 ]

    def jungle_class_counter(self):
        #print(self.jungle_champions_played)

        jungle_class_counting = {'Tank': 0, 'Assassin': 0, 'Bruiser': 0, 'Mage': 0, 'Marksman': 0, 'Enchanter': 0}
        
        mastery_count = []

        for jungle_champ, jungle_class, jungle_mastery in self.jungle_champions_played:
            mastery_count.append(jungle_mastery)
            maximum = max(mastery_count)

            if maximum <= 4:
                if jungle_class == 'Bruiser/Assassin':
                    jungle_class_counting['Bruiser'] += 1
                    jungle_class_counting['Assassin'] += 1 

                else:
                    jungle_class_counting[jungle_class] += 1                
                

            if 5 <= jungle_mastery <= 7: 
                if jungle_class == 'Bruiser/Assassin':
                    jungle_class_counting['Bruiser'] += 1
                    jungle_class_counting['Assassin'] += 1 

                else:
                    jungle_class_counting[jungle_class] += 1
            

                           
            
        
        jungle_class_counts = [(cls, value) for cls, value in jungle_class_counting.items()]
        #print(jungle_class_counts)
        jungle_class_counts.sort(key = lambda x: x[1], reverse = True)


        majority_class_counts = jungle_class_counts[0][1] # the top count

        tied_classes = [cls for cls, value in jungle_class_counts if value == majority_class_counts] # check if theres a tie

        if len(tied_classes) > 1:
            randomized = random.choice(tied_classes)
            majority_class = randomized

        else:    
            majority_class = jungle_class_counts[0][0]


        updated_jungle_champions = [] # we need a new list because kayn asssumes both assassin, bruiser role --> in this list, he will only have one value

        for jungle_champ, jungle_class, jungle_mastery in self.jungle_champions_played: # this makes a new list im not using self.jungle_champions played in the returned list
            if jungle_champ == 'Kayn':
                if majority_class == 'Bruiser':
                    jungle_class = 'Bruiser'
                elif majority_class == 'Assassin':
                    jungle_class = 'Assassin'
    
            updated_jungle_champions.append((jungle_champ, jungle_class, jungle_mastery))

        return [jungle_champ for jungle_champ, jungle_class, jungle_mastery in updated_jungle_champions if majority_class == jungle_class and jungle_mastery < 5]

    def adc_class_counter(self):
        #print(self.adc_champions_played)
        adc_class_counting = {'Burst': 0, 'Poke': 0, 'Utility': 0, 'Hypercarry': 0}
        mastery_count = []
        
        for adc_champ, adc_class, adc_mastery in self.adc_champions_played:
            mastery_count.append(adc_mastery)
            maximum = max(mastery_count)
        
            if maximum <= 4: 
                adc_class_counting[adc_class] += 1
            
            if 5 <= adc_mastery <= 7:
                adc_class_counting[adc_class] += 1

        adc_class_counts = [(cls,value) for cls, value in adc_class_counting.items()]
        adc_class_counts.sort(key = lambda x: x[1], reverse = True)


        majority_class_counts = adc_class_counts[0][1]

        tied_classes = [cls for cls, value in adc_class_counts if value == majority_class_counts] # check if theres a tie
        
        if len(tied_classes) > 1:
            randomized = random.choice(tied_classes)
            majority_class = randomized
        
        else:
            majority_class = adc_class_counts[0][0]
        
        return [adc_champ for adc_champ, adc_class, adc_mastery in self.adc_champions_played if adc_class == majority_class and adc_mastery < 5 ]        





"TO DO THIS WEEK:"
# after finishing adc class, make adjustments to only compare champions between 5-7 in the counter cause it indicates proficiency



#recommend = Champion_Recommendation_Tool('C:\\Users\\benel\\Downloads\\champion_mastery for CircleOfLies.json') 
#recommendations = recommend.load_summoner_data() # this is a list of tuples [(Gangplank,6), (Yasuo,7)]

#print(recommendations) # ok now after SETTLING THE CLASSIFICATION OF BRUISERS/TANKS/RANGED, i need to work on the tuple 
# so lets say if i play a lot of tanks the next function will scour through the recommendations tuple and find tanks that arent high on my mastery list

#all_champion_list = get_all_champions_in_list() # this is a list of every champion in LOL


#comparison = Comparison_Tool(recommendations, all_champion_list) # this cross references both lists
#most_played = comparison.get_most_played() # to produce the list of champion names that i play a lot

#print(comparison.my_champions_played_classified()) #separates the champions i play according to mastery and into their roles, with their class also stated


#print(comparison.mid_classes_counter())
#print(comparison.top_classes_counter())
#print(comparison.support_class_counter())
#print(comparison.jungle_class_counter())
#print(comparison.adc_class_counter())

# sejuani and rammus can go both top and jg

# FUTURE REFINEMENTS TO MAKE:
# make a secondary suggestion as to what classes they should play depending on the frequency of the other alternative classes e.g. assassins, bruisers