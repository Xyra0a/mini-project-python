def transformSentence(sentence):
    words = sentence.split(' ')
    result = []

    for word in words:
        new_word = word[0]
        for i in range(1, len(word)):
            x = word[i]
            y = word[i - 1]

            if y.lower() < x.lower():
                new_word += x.upper()
            elif x.lower() < y.lower():
                new_word += x.lower()
            else:
                new_word += x
        result.append(new_word)

    return ' '.join(result)


if __name__ == '__main__':
    sentence = input()          # you type the sentence in the terminal
    print(transformSentence(sentence))