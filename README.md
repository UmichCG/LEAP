# LEAP

Source code for the MIDAS LEAP project

The current implementation focuses on sentiment and emotion analysis. 

1) <b>Sentiment Analysis Experiments</b>

*sentiment.py* includes experiments carried on the NLTK subjectivity dataset, consisting of 5,000 objective and 5,000 subjective tweets.

The dataset was split into:
- training: 4,000 objective and 4,000 subjective tweets
- testing: 1,000 objective and 1,000 objective tweets

<b>Features:</b>
 
Unigram features: 4,180 in total 

<b>Learning method:</b>
 
Naive Bayes classifier

<b>Results:</b>

*Accuracy:* 0.91

| Class| F1 score      | Precision     | Recall|
| ---  | --- |---| ---|
| `Subjective` | 0.9116781158  | 0.894990366089| 0.929 |
| `Objective`  | 0.908256880734| 0.926195426195| 0.891 |


*sentiment_intensity_analyzer.py* contains code for classifying tweets into one of the classes **positive/negative/neutral**, based on the **Vader Sentiment Analsys lexicon** [1].

*software-psycho-demographics* contains code sentiment and emotion detection based on this paper [2].

**References:**

[1] Hutto, Clayton J., and Eric Gilbert. "Vader: A parsimonious rule-based model for sentiment analysis of social media text." Eighth International AAAI Conference on Weblogs and Social Media. 2014.

http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf

[2] Volkova, Svitlana, and Yoram Bachrach. "Inferring Perceived Demographics from User Emotional Tone and User-Environment Emotional Contrast." Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics, ACL. 2016.

http://www.cs.jhu.edu/~svitlana/papers/VB_ACL16.pdf

[3] Twitter Sentiment Dataset, consisting of 1,578,627 classified tweets, each row is marked as 1 for positive sentiment and 0 for negative sentiment:

http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/

[4] Opinion lexicon 
Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.

- Negative words: https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/blob/master/data/opinion-lexicon-English/negative-words.txt

- Positive words: https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/blob/master/data/opinion-lexicon-English/positive-words.txt

[5] LSTM Networks for Sentiment Analysis:

http://deeplearning.net/tutorial/lstm.html

[6] Pang, Bo, and Lillian Lee. "Opinion mining and sentiment analysis." Foundations and trends in information retrieval 2.1-2 (2008): 1-135.

http://www.cs.cornell.edu/home/llee/omsa/omsa.pdf
