import google.cloud.language as language



def print_result(annotations):
    """Take text as document and analyze the sentiment, then return the sentiment."""

    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    sentiment = "Neutral"

#    print("Overall Sentiment: score of", score, " with magnitude of", magnitude)
    if((score > 0.5) & (magnitude > 0.25)):
        sentiment = "Positive"
    elif((score < -0.5) & (magnitude > 0.25)):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment


def analyze(text):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    return print_result(annotations)
