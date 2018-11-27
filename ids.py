import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("german_election.csv");

#print(data.groupby('state')["registered.voters"].describe());
states=data.groupby('state');

print('State with maximum total votes')
print(states['total_votes'].sum().idxmax() +' - ') #State name with max total votes
print(states['total_votes'].sum().max())	#Max total votes out of states
print ('------------------------------------------')
print('State with minimum total votes')
print(states['total_votes'].sum().idxmin() +' - ') #State name with min total votes
print(states['total_votes'].sum().min())	#Min total votes out of states    
print('------------------------------------------')


print('State with maximum registered voters')
print(states['registered.voters'].sum().idxmax() +' - ')
print(states['registered.voters'].sum().max())    
print('------------------------------------------')
print('State with minimum registered voters')
print(states['registered.voters'].sum().idxmin()  +' - ')
print(states['registered.voters'].sum().min())    
print('------------------------------------------')


print('State with maximum valid voters')
print('First valid votes')
print(states['valid_first_votes'].sum().idxmax()  +' - ')
print(states['valid_first_votes'].sum().max())    
print('Second valid votes')
print(states['valid_second_votes'].sum().idxmax() +' - ')
print(states['valid_second_votes'].sum().max() )
print('------------------------------------------')
print('State with minimum valid voters')
print('First valid votes')
print(states['valid_first_votes'].sum().idxmin()  +' - ')
print(states['valid_first_votes'].sum().min()	)
print('Second valid votes')
print(states['valid_second_votes'].sum().idxmin() +' - ')
print(states['valid_second_votes'].sum().min()	)
print('------------------------------------------' )  

print('State with maximum invalid voters')
print('First invalid votes')
print(states['invalid_first_votes'].sum().idxmax() +' - ')
print(states['invalid_first_votes'].sum().max()	)
print('Second invalid votes')
print(states['invalid_second_votes'].sum().idxmax()  +' - ')
print(states['invalid_second_votes'].sum().max()	)
print('------------------------------------------')

print('State with minimum invalid voters')
print('First invalid votes')
print(states['invalid_first_votes'].sum().idxmin()  +' - ')
print(states['invalid_first_votes'].sum().min()	)
print('Second invalid votes')
print(states['invalid_second_votes'].sum().idxmin()  +' - ')
print(states['invalid_second_votes'].sum().min() )
print('------------------------------------------')
print('Statewise_Sum')
statewise_sum= states.agg({'area_id':'count','registered.voters':'sum','total_votes':'sum','valid_first_votes':'sum','valid_second_votes':'sum','invalid_first_votes':'sum','invalid_second_votes':'sum'}) \
    .rename(columns={'area_id':'Number of Areas'})
statewise_sum['valid_votes']=(statewise_sum['valid_first_votes']+statewise_sum['valid_second_votes'])/2
statewise_sum['invalid_votes']=(statewise_sum['invalid_first_votes']+statewise_sum['invalid_second_votes'])/2
statewise_sum_table=statewise_sum[['Number of Areas','registered.voters','total_votes','valid_votes','invalid_votes']]
print(statewise_sum_table)

statewise_sum_table.to_csv('statewise_sum.csv')

print('------------------------------------------')

print('StateWise Mean')
statewise_mean= states.agg({'area_id':'count','registered.voters':'mean','total_votes':'mean','valid_first_votes':'mean','valid_second_votes':'mean','invalid_first_votes':'mean','invalid_second_votes':'mean'}) \
    .rename(columns={'area_id':'Number of Areas'})
statewise_mean['valid_votes']=(statewise_mean['valid_first_votes']+statewise_mean['valid_second_votes'])/2
statewise_mean['invalid_votes']=(statewise_mean['invalid_first_votes']+statewise_mean['invalid_second_votes'])/2
statewise_mean_table=statewise_mean[['Number of Areas','registered.voters','total_votes','valid_votes','invalid_votes']]
print(statewise_mean_table)

statewise_mean_table.to_csv('statewise_mean.csv')

print('------------------------------------------')

print('StateWise Turnout')
statewise_turnout= states.agg({'area_id':'count','registered.voters':'sum','total_votes':'sum'}) \
    .rename(columns={'area_id':'Number of Areas'})
statewise_turnout['Turnout']=100*statewise_turnout['total_votes']/statewise_turnout['registered.voters']
print(statewise_turnout)

statewise_turnout.to_csv('statewise_turnout.csv')
statewise_turnout['Turnout'].plot()
plt.show()

print('-----------------------------')
print('State with Minimum turnout')
print(statewise_turnout['Turnout'].idxmin() +' - ')
print(statewise_turnout['Turnout'].min())
print('State with Maximum turnout')
print(statewise_turnout['Turnout'].idxmax() +' - ')
print(statewise_turnout['Turnout'].max())
print('------------------------------------------')