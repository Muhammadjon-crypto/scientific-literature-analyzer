def read_paper(filename):
    with open(filename, "r") as file:
        return file.read()


def count_words(paper_text):
    return len(paper_text.split())


def count_sentences(paper_text):
    return len(paper_text.split(".")) - 1


def find_keyword_counts(paper_text):
    words = paper_text.lower().split()
    counts = {}

    for word in words:
        word = word.strip(".,!?()")

        if len(word) > 4:
            counts[word] = counts.get(word, 0) + 1

    return counts


def save_report(word_count, sentence_count, top_keywords):
    with open("analysis_report.txt", "w") as file:
        file.write("SCIENTIFIC LITERATURE ANALYSIS\n")
        file.write("------------------------------\n")
        file.write(f"Word Count: {word_count}\n")
        file.write(f"Sentence Count: {sentence_count}\n\n")
        file.write("Top Keywords:\n")

        for word, count in top_keywords:
            file.write(f"{word}: {count}\n")


paper_text = read_paper("paper.txt")

word_count = count_words(paper_text)
sentence_count = count_sentences(paper_text)
keyword_counts = find_keyword_counts(paper_text)
top_keywords = sorted(keyword_counts.items(), key=lambda item: item[1], reverse=True)[:5]

print("\nSCIENTIFIC LITERATURE ANALYSIS")
print("------------------------------")
print("Word Count:", word_count)
print("Sentence Count:", sentence_count)

print("\nTop Keywords:")
for word, count in top_keywords:
    print(word, ":", count)

save_report(word_count, sentence_count, top_keywords)

print("\nReport saved to analysis_report.txt")