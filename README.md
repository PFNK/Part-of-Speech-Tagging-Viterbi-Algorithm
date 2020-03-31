# Part of Speech Tagging - Viterbi Algorithm

This assignment will make use of the Natural Language Tool Kit (NLTK) for Python. NLTK is a platform
for writing programs to process human language data, that provides both corpora and modules. For more
information on NLTK, please visit: http://www.nltk.org/.

## Section A: Training a Hidden Markov Model (20 Marks)
In this part of the assignment you have to train a Hidden Markov Model (HMM) for part-of-speech (POS)
tagging. Look at the solutions from Lab 3, Exercise 3 and Exercise 4 as a reminder for what you have to
compute.
You will need to create and train two models—an Emission Model and a Transition Model as described in
lectures.
Use labelled sentences from the ‘news’ part of the Brown corpus. These are annotated with parts of speech,
which you will convert into the Universal POS tagset (NLTK uses the smaller version of this set defined by
Petrov et al.6
). Having a smaller number of labels (states) will make Viterbi decoding faster.
Use the last 500 sentences from the corpus as the test set and the rest for training. This split corresponds
roughly to a 90/10% division. Do not shuffle the data before splitting.

## Section B: Implementing The Viterbi Algorithm (55 Marks)
In this part of the assignment you have to implement the Viterbi algorithm. The pseudo-code of the algorithm
can be found in the Jurafsky & Martin 3rd edition book in Appendix A7 Figure A.9 in section A.4: use it as a
guide for your implementation.
However you will need to add to J&M’s algorithm code to make use of the transition probabilities to </s>
which are also now in the a matrix.
In the pseudo-code the b probabilities correspond to the emission model implemented in part A, question 1
and the a probabilities correspond to the transition model implemented in part A, question 2. You should use
costs (negative log probabilities). Therefore instead of multiplication of probabilities (as in the pseudo-code)
you will do addition of costs, and instead of max and argmax you will use min and argmin.

## Section C: Short answer questions (25 Marks)


### RESULTS: 93/100 
7 points lost on section C open questions
