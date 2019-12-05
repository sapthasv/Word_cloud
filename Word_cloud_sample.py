
'''
word cloud is mainly used to get collection 
of most repeated words from the text document.

this technique is used in various industry to determine 
complaints,queries,reviews and other most repeated useful 
information from millions of customers.

'''



from wordcloud import WordCloud ,STOPWORDS
#import collections
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Word_cloud_sample.csv', encoding = 'latin-1' )
df.columns

df1 = df.iloc[2500:,4:5]
text = ' '.join(df1['text'].str.lower()) 

stopwords = STOPWORDS
#stopwords.add('will')

wordcloud = WordCloud(stopwords=stopwords,background_color='white',max_words=100).generate(text)


# plot the WordCloud image                        
plt.figure(figsize = (10, 12)) 
plt.imshow(wordcloud) 
plt.show() 

#################################################################################

filtered_words = [word for word in text.split() if word not in stopwords]
counted_words = collections.Counter(filtered_words)

words = []
counts = []
for letter, count in counted_words.most_common(20):
    words.append(letter)
    counts.append(count)
    

plt.title('Top words in the headlines vs their count')
plt.xlabel('Count')
plt.ylabel('Words')
plt.barh(words,counts) # barh is used beacuse we are passing ore than 3 argumensts(i.e 10)
