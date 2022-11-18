# Afeka college 2022
# Assignment 1
##
# Create at 13/11/2022
# Authors:  Gal Ashkenazi   (315566752)
#           Roy Vaygue      (318860848)
##
import re

# Question 1 Starter
def Question1():
    print("Question 1 in comments")
    ### a)

    ##      <recipe> ::= <pancake> | <crepe> | <pancake>S | <crepe>S 
    #
    # <pancake>         ::= EF | E<pancake-parts>F | EF<pancake-parts> | <pancake>
    # <pancake-parts>   ::= empty | EF | FE | E<pancake-parts>F | F<pancake-parts>E 
    #
    # <crepe>           ::= EEF | EFE | EE<crepe-parts>F | EF<crepe-parts>E | E<crepe-parts>EF | <crepe>
    # <crepe-parts>     ::= empty | EEF| EFE| FEE | EE<crepe-parts>F | F<crepe-parts>EE | E<crepe-parts>FE | E<crepe-parts>EF | EF<crepe-parts>E

    ### b) Without the recursive

    ##      <recipe> ::= <pancake> | <crepe> | <pancake>S | <crepe>S 
    #
    # <pancake>         ::= EF | E<pancake-parts>F | EF<pancake-parts>
    # <pancake-parts>   ::= empty | EF | FE | E<pancake-parts>F | F<pancake-parts>E 
    #
    # <crepe>           ::= EEF | EFE | EE<crepe-parts>F | EF<crepe-parts>E | E<crepe-parts>EF
    # <crepe-parts>     ::= empty | EEF| EFE| FEE | EE<crepe-parts>F | F<crepe-parts>EE | E<crepe-parts>FE | E<crepe-parts>EF | EF<crepe-parts>E
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
        queue = list()  # init queue to containe the child of node

        visit.add(node)
        queue.append(node)

        while queue:          # check the queue until its empty
            q = queue.pop()

            for child in graph[q]:
                if child not in visit:
                    visit.add(child)
                    queue.append(child)
        
        
# Question 3
class Question3:
    # Question 3 constartor
    def __init__(self):
        self.movies = dict()    # movives dict

        self.readMovies("movies.txt")       # read movies

        print(r"@playedWith - Anthony Hopkins") 
        print(
            self.playedWith('Anthony Hopkins')  # play with Anthony Hopkins 
          )  

        # find with ^B
        print(r"@find - ^B") 
        self.find(r'^B')

        # find with \b\w{10}\b
        print(r"@find - \b\w{10}\b")
        self.find(r'\b\w{10}\b')

        # find ^(((\w)+?[ \t]){2}(\w)+)$
        print(r"@find - ^(((\w)+?[ ]){2}(\w)+)$")
        self.find(r'^(((\w)+[ ]+){2}(\w)+)$')

    # read movives file method
    def readMovies(self, file_name):
        for line in open(file= file_name):  # run over all lines in the files
            line = line.rsplit()

            moviesSet = set()
            key_flag = True
            key = ""
            value = ""
            
            for i, n in enumerate(line): # run over all words in the line
                if value != "": value += " "            # add space from the second word
                value += re.search(r"[^,]*", n).group() # add word exept ',' char

                # keep the key and movies if ',' char detact and the last word (the last word is without ',' char)
                if re.search(r"\,", n) or i == len(line) - 1:
                    if key_flag:    
                        key = value
                        key_flag = False
                    else:
                        moviesSet.add(value)    # add movie to the set

                    value = ""                  # reuse the value var

            self.movies[key] = moviesSet        # add the actor and their movies into the self dict

    # play with method
    def playedWith(self, actor):
        resList = list()
        moviesPlayed = self.movies[actor]

        for name in self.movies.keys():
            if name == actor:
                continue
            elif any((match := item) in self.movies[name] for item in moviesPlayed):
                resList.append((name, match))

        return resList

    # find method
    def find(self, pattern):
        print()
        # get actors and movies 
        actorsSet = self.movies.keys()
        moviesSet = self.movies.values()

        # print actors
        print("actors")
        for actor in actorsSet:
            if re.search(pattern, actor):
                print(actor)

        # print movies
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
    Question1()

    print("\n---- Question 2 ----\n")
    Question2('DFS') # strat question 2 - DFS
    Question2('BFS') # strat question 2 - BFS

    print("\n---- Question 3 ----\n")
    Question3() # strat question 3