def repeating_words(text):
    repList = {}
    text = text.split().lower()
    for item in text:
        if item in repList:
            repList.append(item)
            