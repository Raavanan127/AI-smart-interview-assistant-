def voice_confidence(answer_text):
    words = len(answer_text.split())

    if words > 25:
        return "High Confidence"
    elif words > 10:
        return "Medium Confidence"
    else:
        return "Low Confidence"