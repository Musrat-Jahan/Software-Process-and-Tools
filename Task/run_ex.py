import nltk

from nltk.tokenize import sent_tokenize
#from nltk.tokenize import WordPuncttokenizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
sentence=[("a","DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
          ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
grammar = "NP:{<DT>?<JJ>*<NN>}"
parser_chunking = nltk.RegexpParser(grammar)
parser_chunking.parse(sentence)
Output_chunk = parser_chunking.parse(sentence)
Output_chunk.draw()