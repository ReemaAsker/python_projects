import  string
from collections import Counter
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open("read.txt",encoding="utf-8").read()

lower_case = text.lower()

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = word_tokenize(cleaned_text,'english')

final_words =[]
for word in tokenized_words: #remove stop words
    if word not in stopwords.words('english') :
        final_words.append(word)

print(final_words)

emotion_list = []

with open('emotions.txt','r') as file :
    for line in file :
        clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()#to remove the new line between each line
        # print(clear_line)
        word,emotion = clear_line.split(':')
        # print("word :"+word +" "+ "Emotion :"+emotion)
        if word in final_words :
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print('Negative Sentiment')
    elif pos > neg:
        print('Positive Sentiment')
    else:
        print('Netural Vibe')


sentiment_analyse(cleaned_text)
fig,axl = plt.subplots()
axl.bar(w.keys(),w.values())
fig.autofmt_xdate()# automatic update x and y axis
plt.savefig('graph5.png')
plt.show()


# plt.bar(w.keys(),w.values())
# plt.savefig('graph.png')
# plt.show()
