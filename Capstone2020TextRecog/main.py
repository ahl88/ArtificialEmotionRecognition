
import string
#import speech_recognition
from collections import Counter
from collections import OrderedDict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np

#wavFile = “03-01-01-01-01-01-06.wav”

# Initialize the recognition engine
#rec = speech_recognition.Recognizer();

# Convert the audio to text now

#with speech_recognition.AudioFile(wavFile) as source: audio = rec.record(source)

# Output the transcript as text
#output = rec.recognize_google(audio)



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

    print("A more detailed view of sentiment analysis: ", score)



x = sum(w.values())
rkeys = list(w.keys())
rList = list(w.values())
print("The percentages of each emotions appearance are as follows:")


if len(rList) > 0:
    a = (rList[0]/x)
    print("%.3f" % round(a, 3), rkeys[0])
if len(rList) > 0:
    q = [a]
else:
    q = 0


if len(rList) > 1:
    b = (rList[1]/x)
    print("%.3f" % round(b, 3), rkeys[1])
if len(rList) > 1:
    r = [b]
else:
    r = 0


if len(rList) > 2:
    c = (rList[2]/x)
    print("%.3f" % round(c, 3), rkeys[2])
if len(rList) > 2:
    s = [c]
else:
    s = 0


if len(rList) > 3:
    d = (rList[3]/x)
    print("%.3f" % round(d, 3), rkeys[3])
if len(rList) > 3:
    t = [d]
else:
    t = 0


if len(rList) > 4:
    e = (rList[4]/x)
    print("%.3f" % round(e, 3), rkeys[4])
if len(rList) > 4:
    u = [e]
else:
    u = 0


if len(rList) > 5:
    f = (rList[5]/x)
    print("%.3f" % round(f, 3), rkeys[5])
if len(rList) > 5:
    v = [f]
else:
    v = 0


if len(rList) > 6:
    g = (rList[6]/x)
    print("%.3f" % round(g, 3), rkeys[6])
if len(rList) > 6:
    j = [g]
else:
    j = 0


if len(rList) > 7:
    h = (rList[7]/x)
    print("%.3f" % round(h, 3), rkeys[7])
if len(rList) > 7:
    k = [h]
else:
    k = 0


#print(q,r,s,t,u,v,j,k)


'''class OrderedCounter(Counter, OrderedDict):
    pass
counter = OrderedCounter(emotion_list)
for key, value in counter.items():
    print(key, value)'''

#'neutral','calm','happy','sad','angry','fearful','disgust','surprise'


countNeutral = w[' neutral']
countCalm = w[' calm']
countHappy = w[' happy']
countSad = w[' sad']
countAngry = w[' angry']
countFearful = w[' fearful']
countDisgust = w[' disgust']
countSurprise = w[' surprise']

print(countNeutral/x, countCalm/x, countHappy/x, countSad/x, countAngry/x, countFearful/x, countDisgust/x, countSurprise/x)

#def secondFrequent(emotion_list):
#    dict = Counter(emotion_list)
#    value = sorted(dict.values(), reverse=True)
#    secondLarge = value[1]
#   for (key, val) in dict.items():
#        if val == secondLarge:
#            print(rkeys[1], b)
#            return

#def thirdFrequent(emotion_list):
#    dict = Counter(emotion_list)
#    value = sorted(dict.values(), reverse=True)
#    thirdLarge = value[2]
#    for (key, val) in dict.items():
#        if val == thirdLarge:
#            print(rkeys[2], c)
#            return

#def fourthFrequent(emotion_list):
#    dict = Counter(emotion_list)
#    value = sorted(dict.values(), reverse=True)
#    fourthLarge = value[3]
#    for (key, val) in dict.items():
#        if val == fourthLarge:
#            print(rkeys[3], d)
#            return

#def fifthFrequent(emotion_list):
#    dict = Counter(emotion_list)
#    value = sorted(dict.values(), reverse=True)
#    fifthLarge = value[4]
#    for (key, val) in dict.items():
#        if val == fifthLarge:
#            print(rkeys[4], e)
#            return

#def sixthFrequent(emotion_list):
#    dict = Counter(emotion_list)
#    value = sorted(dict.values(), reverse=True)
#    sixthLarge = value[5]
#    for (key, val) in dict.items():
#        if val == sixthLarge:
#            print(rkeys[5], f)
#           return

#def seventhFrequent(emotion_list):
#    dict = Counter(emotion_list)
#    value = sorted(dict.values(), reverse=True)
#    seventhLarge = value[6]
#    for (key, val) in dict.items():
#        if val == seventhLarge:
#            print(rkeys[6], g)
#            return

#def eighthFrequent(emotion_list):
#    dict = Counter(emotion_list)
#    value = sorted(dict.values(), reverse=True)
#    eighthLarge = value[7]
#    for (key, val) in dict.items():
#        if val == eighthLarge:
#            print(rkeys[7], h)
#            return

#print(i, "%.3f" % round(a, 3), "(Most Common)")
#print(secondFrequent(w))
#print(thirdFrequent(w))
#print(fourthFrequent(w))
#print(fifthFrequent(w))
#print(sixthFrequent(w))
#print(seventhFrequent(w))
#print(eighthFrequent(w))




sentiment_analyze(cleaned_text)

# fig, ax1 = plt.subplots()
# ax1.bar(w.keys(),w.values())
# fig.autofmt_xdate()

# plt.savefig('graph.png')
# plt.show()