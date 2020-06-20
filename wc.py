import numpy
import scipy
import scipy.sparse

def word_index(words):
    D = {}
    i = 0
    for word in words:
        if word not in D:
            D[word] = i
            i += 1
    return D


def word_count(texts):
    words = []
    for text in texts:
        for word in text:
            words.append(word)
    vocab = word_index(words)
    M = scipy.sparse.dok_matrix((len(texts), len(vocab)), dtype='int32')
    # fill the matrix
    for i in range(len(texts)):
        for word in texts[i]:
            j  = vocab[word]
            M[i, j] += 1
    return vocab, M