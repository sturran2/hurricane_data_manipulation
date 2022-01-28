# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
#convert damage list to numbers using the format "Prefix-B/M" if it is a number
damages_num=[]
for damage in damages:
    last=damage[-1]
    if last=="M":
        damages_num.append(float(damage[:-1])*1000000)
    elif last=='d':
        damages_num.append(damage)
    else:
        damages_num.append(float(damage[:-1])*1000000000)



# write your construct hurricane dictionary function here:

def build_hur_dic (NAMES,mths,yrs,maxwind,areas,dmg,dth):
    dict={}
    for n in range(len(NAMES)):
        dict[NAMES[n]]={"Name":NAMES[n],"Month":mths[n],"Year":yrs[n],
                        "Max Sustained Wind":maxwind[n], "Damage":dmg[n], "Areas Affected":areas[n], "Death":dth[n]}
    return dict

hurr_dict=build_hur_dic(names,months,years,max_sustained_winds,areas_affected,damages_num,deaths)





# write your construct hurricane by year dictionary function here:
#want to create a dictionary where when input year, and you get a list of hurricane dictionaries (and corresponding data) in that year.

def build_year_dic (YEARS,dict):
    yr1x=[]
    [yr1x.append(yr) for yr in YEARS if yr not in yr1x]
    newdict={}
    #define the keys
    for yr in yr1x:
        newdict[yr]=[]
    #need to add hurricane dictionaries to the list in the key-year dictionary as values.
    for cane in dict.values():
        newdict[cane['Year']].append(cane)
    return newdict

yr_hur_dict=build_year_dic(years, hurr_dict)

    
        
    
    







# write your count that measure affected areas frequency function here:

def area_affected_count(areas):
    area_dict={}
    for cane in areas:
        for spot in cane:
            if spot in area_dict:
                area_dict[spot]+=1
            else:
                area_dict[spot]=1
    return area_dict
AA_count=area_affected_count(areas_affected)
#print(AA_count['Central America'])






# write your find most affected area function here:
def findkey(val, dict):
    for key, value in dict.items():
        if val== value:
            return key
    return "key does not exist"

def most_affected(AA_Dict):
    spots=AA_Dict.values()
    maxaffected=max(spots)
    maxspot=findkey(maxaffected,AA_Dict)
    numhits=AA_Dict[maxspot]
    return maxspot, numhits

worstspot,numhits=most_affected(AA_count)

print(f'The location that was affected by the most hurricanes was {worstspot} which was hit by {numhits} hurricanes.')






# write your function that identifies the hurricane that caused the most death and how much it caused.

def deadly_h(dict):
    numdead=0
    for cane in dict.values():
        if cane['Death']>numdead:
            hurri=findkey(cane,dict)
            numdead=cane['Death']
    return hurri, numdead
deadlyhur, maxdeaths=deadly_h(hurr_dict)

print(f'The deadliest hurricane recorded was Hurricane {deadlyhur}, which lead to {maxdeaths} deaths.')
    





# write your catgeorize by mortality function here:

#create a dictionary where keys are mortality rating and values are dictionaries for each hurricane so we can assess by mortality rating.

#mortality scale upper bounds: 0:0, 1:100, 2:500, 3:1000, 4:10000 5 everything else.

def mort_based_rating(dict):
    new_dict={}
    for i in range(6):
        new_dict[i]=[]
    for cane in dict.values():
        morts=cane['Death']
        if morts==0:
            new_dict[0].append(cane)
        elif morts<=100:
            new_dict[1].append(cane)
        elif morts<=500:
            new_dict[2].append(cane)
        elif morts<=1000:
            new_dict[3].append(cane)
        elif morts<=10000:
            new_dict[4].append(cane)
        else:
            new_dict[5].append(cane)
    return new_dict
mortdict=mort_based_rating(hurr_dict)
#print(mortdict[1])





# write your greatest damage function here:
#find the maximum damage. 

def most_damage(dict):
    maxdam=0
    for cane in dict.values():
        if type(cane['Damage'])== str:
            continue
        elif cane['Damage']>=maxdam:
            maxdam=cane['Damage']
            worstcane=cane
    return cane, maxdam
cane_mst_dmg, maxdam=most_damage(hurr_dict)

#print(f'The hurricane that caused the most damage was {cane_mst_dmg["Name"]} which caused ${str(maxdam)} in damage.')
    




# write your catgeorize by damage function here:

#This function works similar to mort_based_rating, but bases it on the damage amount.
#Upper bounds: cat 0: 0, cat 1:100000000, cat 2: 1000000000, cat 3: 10000000000, cat 4: 50000000000, cat 5: everything else.

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_based_rating(dict):
    new_dict={}
    for i in range(6):
        new_dict[i]=[]
    for cane in dict.values():
        dama=cane['Damage']
        if type(dama)==str:
            new_dict[0].append(cane)
        elif dama>damage_scale[4]:
            new_dict[5].append(cane)
        else:
            for i in range(5):
                if dama<damage_scale[i]:
                    new_dict[i].append(cane)
                    break
    return new_dict
damage_dict=damage_based_rating(hurr_dict)
print(damage_dict)







