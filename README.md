# LEAP

Source code for the MIDAS LEAP project

The current implementation focuses on sentiment and emotion analysis. 

1) <b>Sentiment Analysis Experiments</b>

Experiments carried on the NLTK subjectivity dataset, consisting of 5,000 objective and 5,000 subjective tweets.

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


