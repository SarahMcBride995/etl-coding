#Rest Lottery Exercise
#Sarah McBride
#July 30, 2022

from datetime import datetime
import pandas as pd
importnumpy as np
csv_data = pd.read_csv(powerball_winning_numbers.csv)
df = pd.DataFrame(csv_data)

#return winning numbers given date(s)
winners = pd.DataFrame()
def date_of_winners(date):
    for (date <= df['Draw Date'] <= date) in df:
        winners.append(df['Winning Numbers'])
    return winners


#return all instances of same multiplier as input
int(number)
Numbers = pd.DataFrame()
def multiplier(number):
    if number == df['miltiplier']:
        Numbers.append(df['multiplier'])
    else:
        pass
    return Numbers

#combination of winning numbers in other winning tickets and their draw dates
from itertools import combinations
def winning_combos(winner):
    4winners = np.array([combinations(winner,4)])
    5winnners = np.array([(combinations(winner, 5)])
    6winnners = np.array([(combinations(winner, 6)])
    
    winners = df['Winning Numbers']
    check4 = all(items in 4winners for items in winners)
    check4.join(winners['Draw Date'], lkey='Winning Numbers', rkey='Winning Numbers')
    check5 = all(items in 5winners for items in winners)
    check5.join(winners['Draw Date'], lkey='Winning Numbers', rkey='Winning Numbers')
    check6 = all(items in 6winners for items in winners)
    check6.join(winners['Draw Date'], lkey='Winning Numbers', rkey='Winning Numbers')
    check = check4
    check.append(check5)
    check.append(check6)
    return check


#date range input - find date of max sum of winning numbers
test_df = pd.DataFrame(['Draw Date', 'Sum']
def max_sum(date1, date2):
    while date1 <= date2:
        total = sum all items in df['Winning Numbers']
        test_df['Draw Date'].append(date1)
        test_df['Sum'].append(total)
    return test_df

#top 6 modes within date range
test1_df = pd.DataFrame(['Modes']
def modes(date1, date2):
    while date1 <= date2:
        test1_df = df['Winning Numbers'].value_counts()[:6].index.tolist()
    return test1_df


#Average multiplier over a month
def avgs(month, year):
    for df['Draw Date'].month == month and df['Draw Date'].year == year:
        xbar = mean(df['Multipliers'])
    return xbar


       

