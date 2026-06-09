information = """
Limitless is a 24/7 community-focused gym.
Limitless will offer free weights, cardio equipment, and childcare.
Limitless is for families, hardcore lifters, and elderly members.
Future expansion ideas include a basketball court and a pool.
"""

stop_words = [
    "the", "is", "a", "an", "and", "what", "who", "will", "for",
    "about", "are", "there", "be", "does", "it", "have"
]

translations = {
    "offer": ["free", "weights", "cardio", "childcare"],
    "offers": ["free", "weights", "cardio", "childcare"],
    "provide": ["free", "weights", "cardio", "childcare"],
    "provides": ["free", "weights", "cardio", "childcare"],

    "future": ["future", "expansion", "basketball", "court", "pool"],
    "plans": ["future", "expansion", "basketball", "court", "pool"],
    "expand": ["future", "expansion", "basketball", "court", "pool"],
    "pool": ["pool", "expansion"],
    "basketball": ["basketball", "court", "expansion"],

    "who": ["families", "lifters", "elderly"],
    "people": ["families", "lifters", "elderly"],
    "members": ["families", "lifters", "elderly"],

    "childcare": ["childcare", "families"],
    "kids": ["childcare", "families"],
    "children": ["childcare", "families"]
}

while True:
    question = input("\nAsk a question about Limitless: ")

    if question.lower() == "quit":
        break

    sentences = information.split(".")

    question_words = question.lower().replace("?", "").split()

    search_words = []

    for word in question_words:

        if word not in stop_words:
            search_words.append(word)

        if word in translations:
            search_words.extend(translations[word])

    best_sentence = ""
    best_score = 0

    for sentence in sentences:

        score = 0

        for word in search_words:
            if word in sentence.lower():
                score += 1

        if score > best_score:
            best_score = score
            best_sentence = sentence

    if best_score > 0:
        print("\nAnswer:")
        print(best_sentence.strip())
        print(f"\nConfidence Score: {best_score}")
    else:
        print("\nI don't have enough information to answer that.")