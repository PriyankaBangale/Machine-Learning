import pandas as pd
import matplotlib.pyplot as plt
content = pd.read_csv(r'C:\Users\Jatin Sir\Dropbox\6th August 2017 Python - Afternoon\Day 16\NSE-IDEA.csv')

#print content[['Date', 'Open', 'Close']].head(4)
#print "Max Value of Idea share", content['Close'].max()
#print content[content['Close'] == content['Close'].max()]['Date']

content['DateTime'] = pd.to_datetime(content['Date'])
content['Year'] = content['DateTime'].dt.year
print (content[content['Year'] == 2016]['Close'].mean()) # Using Filter
#yearFrame = set(list(content['Year']))
#print yearFrame
content = content[['Year', 'Close']]
content.groupby('Year').mean().plot(kind='bar')
plt.show()
