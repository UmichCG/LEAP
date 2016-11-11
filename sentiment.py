from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#n_instances = 100
#objective sentences
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')]#[:n_instances]]
#subjective sentences
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')]#[:n_instances]]
print len(subj_docs), len(obj_docs)

"""
subj_docs_encoded = []
for (item, label) in subj_docs:
	encoded_words = []
	for word in item:
		word = word.encode("utf-8").strip()
		encoded_words.append(word)
	subj_docs_encoded.append((encoded_words, label))


obj_docs_encoded = []
for (item, label) in obj_docs:
	encoded_words = []
	for word in item:
		word = word.encode("utf-8").strip()
		encoded_words.append(word)
	obj_docs_encoded.append((encoded_words, label))
"""

### TRAINING SET ###
#subjectivity
train_subj_docs = subj_docs[:4000]
test_subj_docs = subj_docs[4000:5000]

#objectivity
train_obj_docs = obj_docs[:4000]
test_obj_docs = obj_docs[4000:5000]

### TESTING SET ###
training_docs = train_subj_docs + train_obj_docs
testing_docs = test_subj_docs + test_obj_docs

sentim_analyzer = SentimentAnalyzer()

all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
print len(unigram_feats)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
	print('{0}: {1}'.format(key, value))
