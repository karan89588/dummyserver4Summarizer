import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
from string import punctuation


def generateExtractiveSummary(text, mode):
    select = 0.15
    stopwords = list(STOP_WORDS)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokens = [token.text for token in doc]
    print("token", tokens)
    print(punctuation)
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    print("word fre", word_frequencies)
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency
    sentence_tokens = [sent for sent in doc.sents]
    print("sent toke", sentence_tokens)
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    print("sen score", sentence_scores)
    select_length = int(len(sentence_tokens) * select)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    print(summary)
    final_summary = [word.text for word in summary]
    print(final_summary)
    extract_summary = " ".join(final_summary)
    print(extract_summary)
    text = extract_summary
    if mode == "title":
        doc = nlp(text)
        text = doc[0].text
    return text
