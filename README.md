Problem 1 (A Number Picking Game).

Alice and Bob are playing a game. They see n numbers lying on a row where n is an even number. The
numbers can be arbitrary integers: positive or negative or zero. The game proceeds in rounds and Alice goes
first. In each round, a player picks the number either at the front of the row or at the end of the row. Then
the next player does the same. The game goes on till there are numbers remaining. At the end, Alice would
have n/2 numbers and Bob would have n/2 numbers. Their winnings are the sum of these numbers.
Your goal is to find the best strategy for Alice assuming the best strategy of Bob. In particular, you need
to write code which takes input these n numbers as an array, and returns the largest number W such that no
matter how Bob plays, Alice always gets a winning of at least W.

For instance, suppose n = 4 and the numbers given are [2, 3, 8, 5]. Then, the answer should be 10. There is
a way for Alice to play such that no matter how Bob plays, Alice makes a winning of at least 10. Indeed,
Alice starts by picking 2. Bob is left with [3, 8, 5] and no matter what he does, Alice will get 8, thus getting
a total of 10. Of course, this problem is too small to capture all the intricacies of the game. When n = 6 or
larger, then Alice needs to think of the best play of Bob and so on and so forth.
In this project you have to do the following.

• First, write code which takes input a list A of an even number of integers and output the
largest W which is always guaranteed to Alice.
• Second, code an interactive version. Here, your code will play Alice’s move, and then
ask the user to input Bob’s move. If all goes well, then no matter how the user plays you should be
getting ≥ W.

Problem 2 (Word Pyramids).
Maybe you have seen the following kind of puzzle before:
I was having – – – with my best – – – – . We were watching a game of cricket, but both the
– – – – – were terrible. It was the – – – – – – game ever. The losing team captain’s post-match
– – – – – – – were pretty pathetic. I wonder what – – – – – – – – the players were suffering;
maybe, they had over-stretched their – – – – – – – – – .
In each blank you have to fill in a word. The number of blanks indicates the number of letters the word
has. Furthermore, every word (other than the first) can be obtained by adding one letter to the previous
word and then scrambling/anagramming. So, one possible answer to the puzzle is : (TEA, MATE, TEAMS,
LAMEST, LAMENTS, AILMENTS, LIGAMENTS). Note you add M to TEA and scramble to get MATE,
you add S to MATE and scramble to get TEAMS, and so on. Such a sequence of words is called a word
pyramid.
Given a dictionary1 SOWPODS.txt, write code which
a. Finds a longest word-pyramid in the (given) dictionary. How long a pyramid could you find?
b. Finds the number of such longest length word pyramids.
Clarification: I actually need the number of the “tips” of the pyramids. In the example above,
LIGAMENTS is the tip. If the answer to part (a) is L, I want to know how many words in the
dictionary can be the tip of an L-length pyramid.
c. Takes input a valid word in the dictionary, and then finds the longest pyramid containing that word.Problem 2 (Word Pyramids). (2 points)

Problem 3 (Reconstituting String ... but now with Anagrams).
Remember the problem from PSet 4? You were given a string s[1 : n] and a dictionary D() and you were
asked whether the string could be split into valid words. For instance, alltheworldisastage could be
reconstituted into all, the, world, is, a, stage.
In this problem, you have to do this, except, we are allowed to scramble the string first! So, we are
asking if there is some ordering of the string which can be reconstituted into valid words in the dictionary.
The dictionary is the SOWPODS.txt available in Canvas. Can you write code to do this?
To make life easier for you, I will change the problem slightly. Firstly, every word in your reconstitution
should be at least 3 letters long, and the number of words that you break your string into is at most 3. So,
the string algorithm can be broken down into (algorithm) or (logarithm) or goal, mirth,
but not as la, go, mirth as the word go is only a two letter word.
After taking the string as input, you should return (a) the number of possible ways of reconstituting the
string with anagrams, and (b) also return a list which contains all these anagrams.
So, if we run on the string dynamic, your answer should be 13 and the list2
is [’cyma din’, ’cyma nid’,
’cad miny’, ’cany dim’,’cany mid’, ’cyan dim’,’cyan mid’, ’many cid’,’myna cid’,
’cay mind’, ’damn icy’, ’mand icy’, ’dynamic’]
