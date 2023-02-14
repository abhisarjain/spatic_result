import pandas as pd
# reading csv file(given dataset)
csvfile = pd.read_csv('assignment_data.csv')
# making it a dataframe
df = pd.DataFrame(csvfile)
# Here, we are using Levenshtein library to calculate the distance
from Levenshtein import distance as lev
# r is a list that will contain the result (o or 1)
r = []
# we have created dic0 which will contain key and value as names which does not satify the  given condition
# and we have created dic1 which will contain key and value as names but it satifies the  given condition
dic0 = {}
dic1 = {}
chk = False
# here we have initialized two loops and with the help of two dictionaries, we have implemented Dynamic Programming(memorization)
for x in range(0,len(df)):
    for y in range(x+1,len(df)):
        if(x!=y): 
            if(df.loc[y,'name'] in dic0  and dic0.get(df.loc[y,'name'])==df.loc[x,'name']):
                pass # here we are saving time by just searching the hashmap(dictionary in python) as time complexity for lookups is O(1)
            elif(df.loc[y,'name'] in dic1 or df.loc[x,'name'] in dic1):
                r.append(1)
                chk = True
                break
            else:
                a = (df.loc[x,'latitude'], df.loc[x,'longitude'])
                b = (df.loc[y,'latitude'], df.loc[y,'longitude'])
                if(lev(df.loc[x,'name'], df.loc[y,'name'])<5 and distance.distance(a, b).km/1000 < 200): #here we are checking the conditions
                    dic1[df.loc[x,'name']] = df.loc[y,'name']
                    dic1[df.loc[y,'name']] = df.loc[x,'name']
                    r.append(1)
                    chk = True #here we have got the needed pair,hence we have appended 1 to the list
                    break
                else:
                    dic0[df.loc[x,'name']] = df.loc[y,'name']
    if chk == False: #that means we couldn't find any pair that satisties the condition
        r.append(0)
    else :
        chk = False
df['is_similar'] = r #adding new column and adding all the resultant values
df.to_csv('result.csv') #adding the new dataframe to new csv file
