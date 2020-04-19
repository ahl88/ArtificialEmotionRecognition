
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np

text = open('read.txt',encoding='utf-8').read()

lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = word_tokenize(cleaned_text,"english")


final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')



        if word in final_words:
            emotion_list.append(emotion)


#print(emotion_list)
w = Counter(emotion_list)
print("The considered emotions are:",w,'\n')
max = 0
res = emotion_list[0]
for i in emotion_list:
    freq=emotion_list.count(i)
    if freq>max:
        max=freq
        res=i




#print most common emotion
print("The emotion mostly expressed is:" + str(res),'\n')

#print the sentiment type
def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("This is a Negative Sentiment",'\n')
    elif pos > neg:
        print("This is a Positive Sentiment",'\n')
    else:
        print("This is a Neutral Sentiment",'\n')

    print("A more detailed view of sentiment analysis: ",score)












x = sum(w.values())
# print(w.values())
rList = list(w.values())
print("The percentages of each emotions appearance are as follows:")
a = (rList[0]/x*100)
print("%.3f" % round(a, 3), "(Most Common):", i)
b = (rList[1]/x*100)
print("%.3f" % round(b, 3))
c = (rList[2]/x*100)
print("%.3f" % round(c, 3))
d = (rList[3]/x*100)
print("%.3f" % round(d, 3))
e = (rList[4]/x*100)
print("%.3f" % round(e, 3))
f = (rList[5]/x*100)
print("%.3f" % round(f, 3))
g = (rList[6]/x*100)
print("%.3f" % round(g, 3))
h = (rList[7]/x*100)
print("%.3f" % round(h, 3))







sentiment_analyze(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()

plt.savefig('graph.png')
plt.show()