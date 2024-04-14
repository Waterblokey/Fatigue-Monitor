import argparse
import google.cloud.language as language
from STTTrial import *
import random


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    print("Overall Sentiment: score of", score, " with magnitude of", magnitude)
    f = open("Speech-to-text/outro.txt", "a")
    f.write(str(random.randint(0, 1000)))
    f.close()
    return score

def analyze(text):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    return print_result(annotations)

#analyze(STT())