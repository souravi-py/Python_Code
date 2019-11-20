# Importing Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
from twilio.rest import Client

# Get Content from the WebPage

try:
    page = sys.argv[1]
except:
    page = str(1)

url = "https://news.ycombinator.com/news?p=" + page
response = requests.get(url)
if response.status_code != 200:
    print("The Webpage is not reachable at the moment")
soup = BeautifulSoup(response.text, "html.parser")

# Select and Get only links, Tittles and Votes

Links = soup.select(".storylink")
Votes = soup.select(".score")
if len(Links) != len(Votes):
    print("Some of the News don't have score")



# Select only tittles with vote greater than 99 points

def my_news(Links, Votes):
    news = []
    for idx, item in enumerate(Links):
        tittle = item.getText()
        href = item.get('href', None)
        points = int(Votes[idx].getText().replace(" points",""))

        if points > 99 :
            news.append({'tittle': tittle, 'href' : href, 'points' : points})

    # Sort the list according to highest points first
    news.sort(key=lambda K: K['points'], reverse=True)
    return news


# Schedule it for everyday 9 am


# Display in a good way



def Main():
    try:

        News_List = my_news(Links,Votes)
        News_Count = len(News_List)
        # Send an SMS saying, "you have News_Count of news to read today"

        account_sid = 'AC8aa67092a648d7c2b3a0e8b032404cdf'
        auth_token = '1d82f6308229ca38170ed9e48b384e68'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_ ='+13343267046',
            body = f'you have {News_Count} of news to read today',
            to = '+919503738431'
        )
    # Export to csv

        df = pd.DataFrame(News_List)
        df.to_csv("News.csv", index=False)
        return 0
    except:
        print("Sorry Error occured, No data Today, Please Check !!")
        return 1



Main()

