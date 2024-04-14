import google.cloud.language as language



def print_result(annotations):
    """Take text as document and analyze the sentiment, then return the sentiment."""

    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    sentiment = "Neutral"

    print("Overall Sentiment: score of", score, " with magnitude of", magnitude)
    if((score > 0.4) & (magnitude > 0.3)):
        sentiment = "Positive"
    elif((score < -0.4) & (magnitude > 0.3)):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment


def analyze(text):
    """Run a sentiment analysis request on passed in text."""
    client = language.LanguageServiceClient()

    # Convert text to document for annotation
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    # Run sentiment analysis on text
    annotations = client.analyze_sentiment(request={'document': document})

    return print_result(annotations)
