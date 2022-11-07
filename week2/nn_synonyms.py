import fasttext

words = []
with open("/workspace/datasets/fasttext/top_words.txt") as f:
    for word in f:
        words.append(word.strip())

skipgram = fasttext.load_model("/workspace/datasets/fasttext/title_model.bin")
synonym_lists = []
for word in words:
    neighbors = skipgram.get_nearest_neighbors(word)
    closest_neighbors = [
        neighbor
        for distance, neighbor in neighbors
        if distance > 0.75
    ]
    if closest_neighbors:
        synonym_lists.append([word] + closest_neighbors)

with open("/workspace/datasets/fasttext/synonyms.csv", "w") as f:
    for synonyms in synonym_lists:
        f.write(f"{','.join(synonyms)}\n")
