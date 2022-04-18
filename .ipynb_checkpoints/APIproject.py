import requests
from datetime import datetime
from itertools import groupby
from operator import itemgetter

class Meetings():
    base_url = 'https://ct-mock-tech-assessment.herokuapp.com/'
    calls = []
    
    def __init__(self): 
        self.data = None
        self.calls.append(self)
        
    def __repr__(self):
        return f'<APICall: works>'
    def run(self):
        response = requests.get(f'{self.base_url}')
        self.data = response.json()
        
    def country_dic(count, emails, country, date):
        invitation = {
            'AttendeeCount': count,
            'Attendees': emails,
            'Name': country,
            'Start Date': date
        }
        return invitation
    def most_common(_list):
        return max(set(_list), key = _list.count)
    
    def ranges(nums):
        gaps = [[s,e] for s, e in zip(nums,num[1:]) if s+1 < e]
        edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
        return list(zip(edges, edges))
    
    #US
    
#countries
united_states  = []
ireland = []
spain = []
mexico = []
canada = []
singapore = []
japan = []
united_kingdom = []
france = []

    
meetings = Meetings()
meetings.run()
meetings.calls
partners = meetings.data
#print(partners)
partner = partners['partners']

country = partners['partners'][0]['country']
#print(country)




dates = []
good_dates = []

for citizens in united_states:
    for date in citizens['availableDates']:
        dates.append(date)
        consecutive_dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
        date_ints = set([d.toordinal() for d in consecutive_dates])
        

similar_dates = meetings.range(dates_ints)

best_dates = Meetings.most_common(similar_dates)
meeting_dates = []
for days in best_dates:
    meeting_dates.append(datetime.fromordinal(days))
    
str_dates = []

print(meeting_dates)
for dayss in meeting_dates:
    str_dates.append(dayss.strftime("%Y-%m-%d"))
    print(str_dates)
    


for individual in partner: 
    # country = partners['partners'][0]['country']
    if individual ['country'] == 'United States':
        united_states.append(individual)
        
    elif individual ['country'] == 'France':
        france.append(individual)
        
    elif individual ['country'] == 'Ireland':
        ireland.append(individual)
        
    elif individual ['country'] == 'United Kingdom':
        united_kingdom.append(individual)
        
    elif individual ['country'] == 'Singapore':
        singapore.append(individual)
        
    elif individual ['country'] == 'Japan':
        japan.append(individual)    
        
    elif individual ['country'] == 'Mexico':
        mexico.append(individual)
        
    elif individual ['country'] == 'Spain':
        spain.append(individual)
        
    elif individual ['country'] == 'Canada':
        canada.append(individual)
        
    #print(len(united_states))
    
# United States

american_emails = []

for email in united_states:
    if str_dates[0] and str_dates[1] in email ['availableDates']:
        
        american_emails.append(email['email'])

        
free_units = len(american_emails)

american_invitation = Meetings.country_dict(free_units, american_emails, 'United States', str_dates[0])
american_invitation
    

    