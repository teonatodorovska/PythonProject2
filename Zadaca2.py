def reverse_words(sentence):


    words = sentence.split()


    reversed_sentence = ' '.join(word[::-1] for word in words)

    return reversed_sentence