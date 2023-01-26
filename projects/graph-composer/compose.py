import string
import random
from graph import Graph

def get_text_words(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    return words

def make_graph(words):
    g = Graph()
    prev_word = None

    for word in words:
        # get or add vertex to graph
        word_vertex = g.get_vertex(word)

        if prev_word:
            # word_ vertex is next word
            prev_word.incr_edge(word_vertex)
        # set word_vertex if prev is none
        prev_word = word_vertex 

    # create graph
    g.create_probability_mappings()
    return g

def compose(graph, words, length=50):
    composition = []
    # set vertex from random word in graph
    word = graph.get_vertex(random.choice(words))

    for _ in range(length):
        # add word to composition
        composition.append(word.val)
        # update word var to next word
        word = graph.get_next_word(word)

    return composition

def main():
    words = get_text_words('texts/example.txt')
    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition)


if __name__ == '__main__':
    print(main())