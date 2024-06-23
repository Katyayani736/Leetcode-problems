class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionary.sort(key=len)
        sentence_words = sentence.split()
        replaced_words = []

        for word in sentence_words:
            is_replaced = False
            for root in dictionary:
                if word.startswith(root):
                    replaced_words.append(root)
                    is_replaced = True
                    break
            if not is_replaced:
                replaced_words.append(word)

        return " ".join(replaced_words)

def main():
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"

    solution = Solution()
    replaced_sentence = solution.replaceWords(dictionary, sentence)

    print("Replaced sentence:", replaced_sentence)

if __name__ == "__main__":
    main()
