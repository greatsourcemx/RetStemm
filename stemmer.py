from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk import FreqDist as frecu
import sys
import re
from collections import Counter

palabra = sys.argv[1]
# palabra = "komo avrir la ordn"
respuesta = ''

try:
    def words(text):
        return re.findall(r'\w+', text.lower())


    WORDS = Counter(words(open('C:/Python27/21leyes.txt').read()))
    #WORDS = Counter(words(open('D:/SitiosWEB/IMA_SITES/manualesax/Python/21leyes.txt').read()))


    def P(word, N=sum(WORDS.values())):
        "Probability of `word`."
        return WORDS[word] / N


    def correction(word):
        "Most probable spelling correction for word."
        return max(candidates(word), key=P)


    def candidates(word):
        "Generate possible spelling corrections for word."
        return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


    def known(words):
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in WORDS)


    def edits1(word):
        "All edits that are one edit away from `word`."
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)


    def edits2(word):
        "All edits that are two edits away from `word`."
        return (e2 for e1 in edits1(word) for e2 in edits1(e1))


    palabra = palabra.replace(r"%20", " ")
    palabra = palabra.replace("sion", "sión")
    palabra = palabra.replace("cion", "ción")
    tokens = word_tokenize(palabra, "spanish")
    tokens = [word.lower() for word in tokens if word.isalpha()]

    # Eliminar palabras de parada
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stopwords.words('spanish') or token == 'clic':
            clean_tokens.remove(token)


        # Derivacion regresiva

    stemmer = PorterStemmer()
    es_stemmer = SnowballStemmer('spanish')
    clean_tokens_sin_stems = [es_stemmer.stem(token) for token in clean_tokens]
    freq = frecu(clean_tokens_sin_stems)

    lista = []
    for word in freq.most_common(5):
        # freqword[i] = word[0]
        if (respuesta == ''):
            respuesta = word[0]
        else:
            respuesta = respuesta + "," + word[0]
except  Exception as e:
    archivo = open("D:/SitiosWEB/IMA_SITES/manualesax/Python/error.txt", "w")
    archivo.write(str(e))
    archivo.close()
    print(0)
if ('creacion' in respuesta):
    respuesta = respuesta.replace("creacion", "cre")
print(respuesta)




