"""Search Engine"""
lst1 = ["Python is a good language","C is eveen better","Python programming language doesn't address the snake python","Python is easy","You are a beginner in programming"]
a = input("Enter your query string\n")
def Match_words(sentence1,sentence2):
    words1 = sentence1.split(" ")    
    words2 = sentence2.split(" ")
    score = 0 
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score
score_list = []
for i in range(len(lst1)):
    score_list.append(Match_words(a,lst1[i]))
sorted_sentences_scores = [items for items in sorted(zip(score_list,lst1), reverse = True) if items[0] != 0]
print(f"{len(sorted_sentences_scores)} results found")
i = 1
for score,sentences in sorted_sentences_scores:
    print(f"Result {i}:",sentences)
    i += 1