def sentiment_analysis(text):
    from dataset import positive_words , negative_words

    words = text.lower().split()
    
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)

    if pos_count > neg_count:
        return "Positive"
    elif pos_count < neg_count:
        return "Negative"
    else:
        return "Neutral"

text = input("Enter a Sentence\n")
print("Sentiment: ", sentiment_analysis(text))