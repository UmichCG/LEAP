# LEAP

Source code for the MIDAS LEAP project

The current implementation focuses on sentiment and emotion analysis. 

1) *Sentiment*
Experiments carried on the NLTK subjectivity dataset, consisting of 5,000 objective and 5,000 subjective tweets.
The dataset was split into:
- training: 4,000 objective and 4,000 subjective tweets
- testing: 1,000 objective and 1,000 objective tweets

*Features:* Unigram features, 4,180 in total 

*Learning method:* Naive Bayes classifier

*Results:*

Accuracy: 0.91

F1 score: [obj]: 0.908256880734
F1 score: [subj]: 0.9116781158

Precision: [obj]: 0.926195426195
Precision: [subj]: 0.894990366089

Recall: [obj]: 0.891
Recall: [subj]: 0.929
