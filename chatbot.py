import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text


# -----------------------------------
# STEP 1: Load FAQ dataset
# -----------------------------------

data = pd.read_csv("faq_data.csv")


# -----------------------------------
# STEP 2: Preprocess FAQ questions
# -----------------------------------

data["processed_question"] = data["question"].apply(preprocess_text)


# -----------------------------------
# STEP 3: Create TF-IDF vectorizer
# -----------------------------------

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    data["processed_question"]
)


# -----------------------------------
# STEP 4: Get user question
# -----------------------------------

user_question = input("\nAsk your question: ")


# -----------------------------------
# STEP 5: Preprocess user question
# -----------------------------------

processed_user_question = preprocess_text(user_question)


# -----------------------------------
# STEP 6: Convert user question to vector
# -----------------------------------

user_vector = vectorizer.transform(
    [processed_user_question]
)


# -----------------------------------
# STEP 7: Calculate cosine similarity
# -----------------------------------

similarity_scores = cosine_similarity(
    user_vector,
    faq_vectors
)


# -----------------------------------
# STEP 8: Find best matching FAQ
# -----------------------------------

best_match = similarity_scores.argmax()


# -----------------------------------
# STEP 9: Get similarity score
# -----------------------------------

best_score = similarity_scores[0][best_match]


# -----------------------------------
# STEP 10: Display chatbot result
# -----------------------------------

print("\n==============================")
print("       COLLEGE FAQ CHATBOT")
print("==============================")


print("\nUser:")
print(user_question)


# -----------------------------------
# STEP 11: Check similarity
# -----------------------------------

if best_score < 0.20:

    print("\nChatbot:")
    print("Sorry, I could not find a suitable answer.")

else:

    best_question = data.iloc[best_match]["question"]
    best_answer = data.iloc[best_match]["answer"]

    print("\nBest Matching FAQ:")
    print(best_question)

    print("\nSimilarity Score:")
    print(round(best_score, 2))

    print("\nChatbot:")
    print(best_answer)


print("\n==============================")