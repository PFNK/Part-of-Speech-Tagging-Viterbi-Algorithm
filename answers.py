a1a=['.', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'VERB', 'X']
a1b=2649
a1c=12.05988565013656
a1d='function'
a2a=13
a2b=2.4630453700815003
a4a3=0.8689827219809665
a4b1=[("I'm", 'PRT'), ('useless', 'ADJ'), ('for', 'ADP'), ('anything', 'NOUN'), ('but', 'CONJ'), ('racing', 'ADJ'), ('cars', 'NOUN'), ('.', '.')]
a4b2=[("I'm", 'PRT'), ('useless', 'ADJ'), ('for', 'ADP'), ('anything', 'NOUN'), ('but', 'ADP'), ('racing', 'VERB'), ('cars', 'NOUN'), ('.', '.')]
a4b3="Meaning of racing cars in the given context is not clear. It seems like ADJ+NOUN but if we focus on the whole sentence it makes more sense that it's VERB+NOUN.\nThis is an ambiguity problem and also could be caused because it occurs more frequent as ADJ+NOUN than as VERB+NOUN"
a4c=56.630575309531835
a4d=308.7122785474796
a4e=['DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'VERB', 'ADV']
a5='If there is unseen word, emmision probability would be 0. If we are using probabilities, entire cell in viterbi would be zero.\nTo avoid this, we could avoid using emission probability in such case. We could proceed as usual, get the maximum value over all possible tags using previous viterbi values multiplied by transition probabilities.\nPossibly we could do better because for unseen data, now the table value would be 0 but using this there would be some value which could lead to better accuracy'
a6='Our dataset is not very big it might happen that if we have too many tags but not many train sentences this could result in possible 0 counts for some tags.\nAlso when there is a smaller tagset, there is smaller number of choices that tagger can make so there is less space for mistake and so the accuracy could be higher.'
a3c=16.79319240474419
a3d='<s>'
