# -*- coding: utf-8 -*-
 
import random #import random
import csv #import csv
 
w_Cleveland = 0 #variable for counter
w_Oakland = 0 #variable for counter
w_Warriors = 0 #variable for counter
 
# with open('C:\Users\HiperFlasH\data3.csv') as csvfile:
with open('data3.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if 'Cleveland' in row['Location']:
            w_Cleveland = w_Cleveland + 1
        if 'Oakland' in row['Location']:
            w_Oakland = w_Oakland + 1
    print 'Number Of wins for Cleveland: ', w_Cleveland #prints number of wins
    print 'Number Of wins for Oakland: ', w_Oakland #prints number of wins
   
print '------------------------------------'
 
 
# warriors home = oakland
# cavaliers home = cleaveland
 
city_winner=['Oakland-Warriors', 'Cleveland-Cavaliers', 'Oakland-Warriors', 'Oakland-Cavaliers', 'Cleveland-Cavaliers', 'Cleveland-Warriors', 'Oakland-Warriors','Cleveland-Warriors',
'Oakland-Warriors', 'Cleveland-Warriors', 'Oakland-Warriors', 'Oakland-Warriors', 'Cleveland-Cavaliers', 'Cleveland-Warriors', 'Oakland-Cavaliers', 'Cleveland-Cavaliers',
'Oakland-Cavaliers', 'Cleveland-Cavaliers', 'Oakland-Warriors', 'Oakland-Warriors', 'Oakland-Warriors', 'Cleveland-Warriors', 'Cleveland-Cavaliers', 'Oakland-Warriors',
'Oakland-Warriors', 'Cleveland-Warriors']

h_w_warriors=0
h_w_Cavaliers=0

#Home wins
for i in city_winner:
    if i == 'Oakland-Warriors':
        h_w_warriors = h_w_warriors +1
print 'Warriors home wins: ', h_w_warriors
for i in city_winner:
    if i == 'Cleveland-Cavaliers':
        h_w_Cavaliers = h_w_Cavaliers +1
print 'Cavaliers home wins: ', h_w_Cavaliers

print '------------------------------------'

#Away wins
a_w_warriors = 0
a_w_Cavaliers = 0

for i in city_winner:
    if i == 'Cleveland-Warriors':
        a_w_warriors = a_w_warriors +1
print 'Warriors away wins: ', a_w_warriors

for i in city_winner:
    if i == 'Oakland-Cavaliers':
        a_w_Cavaliers = a_w_Cavaliers +1
print 'Cavaliers away wins: ', a_w_Cavaliers
print '------------------------------------'


s_warriors = 0
s_cavaliers = 0
numGames = 0

# with open('C:\Users\HiperFlasH\data3.csv') as csvfile:
with open('data3.csv') as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        numGames = numGames + 1
        if 'Warriors' in row['Winner']:
            s_warriors = s_warriors + int(row['winnerScore'])
            s_cavaliers = s_cavaliers + int(row['loserScore'])
        else:
            s_warriors = s_warriors + int(row['loserScore'])
            s_cavaliers = s_cavaliers + int(row['winnerScore'])
    print numGames
    avgr_s_warriors = s_warriors / numGames
    avgr_s_cavaliers = s_cavaliers / numGames
    print 'Number Of wins for Warriors: ', s_warriors #prints number of wins
    print 'Number Of wins for Cavaliers: ', s_cavaliers #prints number of wins

print '------------------------------------'

print 'Average score for Warriors', avgr_s_warriors
print 'Average score for Cavaliers', avgr_s_cavaliers

print '------------------------------------'

def pred_war():
    ran_1 = random.randint(1, 20)
    ran_2 = random.randint(1, 20)
    ran_3 = random.randint(0, 1)
    ran_4 = random.randint(0, 1)
    if ran_3 is 0:
        pred_war = avgr_s_warriors + ran_1
    else:
        pred_war = avgr_s_warriors - ran_1
    return pred_war
print 'predicted score for next Warrriors game: ', pred_war()

def pred_cav():
    ran_1 = random.randint(1, 20)
    ran_2 = random.randint(1, 20)
    ran_3 = random.randint(0, 1)
    ran_4 = random.randint(0, 1)
    if ran_4 is 0:
        pred_cav = avgr_s_cavaliers + ran_2
    else:
        pred_cav = avgr_s_cavaliers - ran_2
    return pred_cav
print 'predicted score for next Cavaliers game: ', pred_cav()

print '------------------------------------'

avg_sum_war = 0
avg_sum_cav = 0

for i in range(10000):
    avg_sum_war = avg_sum_war + pred_war()
print 'Average prediction of the games after 10000 games for war: ', avg_sum_war / 10000

for i in range(10000):
    avg_sum_cav = avg_sum_cav + pred_cav()
print 'Average prediction of the games after 10000 games for cav: ', avg_sum_cav / 10000

print '------------------------------------'

user_pred_h=input('Please input your prediction for Home team: ')
user_pred_a=input('Please input your prediction for Away team: ')

print user_pred_h, '-', user_pred_a

user_winnings = 0

if user_pred_h == '122-103':
    user_winnings = user_winnings + 10

pw_h = False
pw_a = False

w_h = True
w_a = False

if user_pred_h > user_pred_a:
    pw_h = True
elif user_pred_h < user_pred_a:
    pw_a = True

if pw_h is w_h:
    user_winnings = user_winnings + 10
print 'You won', user_winnings
