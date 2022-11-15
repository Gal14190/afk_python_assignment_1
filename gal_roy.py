# Afeka college 2022
# Assignment 1
##
# Create at 13/11/2022
# Authors:  Gal Ashkenazi
#           Roy Vaygue
##
import re

# Question 1 Starter
def Question1():
    ## a
    # <flour> ::= 'F'
    # <egg>   ::= 'E'
    # <suger> ::= 'S'

    # <pancake> ::= <egg>+ <pancake-parts> <sugar>?
    # <pancake-parts> ::= (<flour> <egg> | <egg> <flour>) <pancake-parts>

    # <crepe> ::= <eeg>+ <crepe-parts> <sugar>?
    # <crepe-parts> ::= (<flour> <egg> <egg> | <egg> <egg> <flour> | <egg> <flour> <egg>) <crepe-parts>

    ## b
    # <flour> ::= 'F'
    # <egg>   ::= 'E'
    # <suger> ::= 'S'

    # <pancake> ::= <egg>+ <pancake-parts> <sugar>?
    # <pancake-parts> ::= (<flour> <egg> | <egg> <flour>) <pancake-parts>

    # <crepe> ::= <eeg>+ <crepe-parts> <sugar>?
    # <crepe-parts> ::= (<flour> <egg> <egg> | <egg> <egg> <flour> | <egg> <flour> <egg>) (IF TERM > 3 <crepe-parts> ELSE empty)

    # x ::= 3
    # TERM ::= x-1
    pass

# Question 2
class Question2:
    # Question 2 constartor
    def __init__(self, type):
        # type validation

        if 'DFS' != type and 'BFS' != type:
            print("TYPE INVALIDE")
            return
        else:
            self.type = type

        # graph dictionary init 
        my_graph = {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': ['a'], 'e': ['d']}

        # print the reachable list result
        print(
            self.reachable(my_graph, 'a')
        )
    
    def reachable(self, graph, node):
        visit = set() # set init

        # decision reachable method
        if     self.type == 'DFS': self.DFS(graph, node, visit)
        elif   self.type == 'BFS': self.BFS(graph, node, visit)

        return list(visit)  # convert and return set result to list

    # DFS method
    def DFS(self, graph, node, visit):
        visit.add(node)

        for child in graph[node]:
            if child not in visit:
                self.DFS(graph, child, visit)

    # BFS method
    def BFS(self, graph, node, visit):
        pass
        
        
# Question 3
class Question3:
    # Question 3 constartor
    def __init__(self):
        self.movies = dict()    # global movives dict

        self.readMovies("movies.txt")

        self.playedWith('Anthony Hopkins')

        print(r"find - ^B")
        self.find(r'^B')

        print(r"find - \b\w{10}\b")
        self.find(r'\b\w{10}\b')

    # read movives file method
    def readMovies(self, file_name):
        for line in open(file= file_name):  # run over all lines in the files
            line = line.rsplit()

            moviesSet = set()
            key_flag = True
            key = ""
            value = ""
            
            for n in line: # run over all words in the line
                if value != "": value += " "            # add space from the second word
                value += re.search(r"[^,]*", n).group() # add words exept ',' char

                # keep the key and movies if ',' char detact
                if re.search(r"\,", n):
                    if key_flag:    
                        key = value
                        key_flag = False
                    else:
                        moviesSet.add(value)    # add movie to the set

                    value = ""                  # reuse the value var

            self.movies[key] = moviesSet        # add the actor and ther movies into the global dict
    
    def playedWith(self, actor):
        pass

    def find(self, pattern):
        print()
        actorsSet = self.movies.keys()
        moviesSet = self.movies.values()

        print("actors")
        for actor in actorsSet:
            if re.search(pattern, actor):
                print(actor)

        duplicateSet = set()
        print("movies")
        for movies in moviesSet:
            for m in movies:
                if re.search(pattern, m) and m not in duplicateSet:
                    duplicateSet.add(m)
                    print(m)

        print()

# Main call Questions method
if __name__ == "__main__":
    print("---- Question 1 ----")
    print("Question 1 in comments")

    print("\n---- Question 2 ----\n")
    Question2('DFS') # strat question 2 - DFS
    Question2('BFS') # strat question 2 - BFS

    print("\n---- Question 3 ----\n")
    Question3() # strat question 3