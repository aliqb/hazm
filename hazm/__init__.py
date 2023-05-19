"""entry point for the package."""

from typing import List

from .chunker import Chunker, RuleBasedChunker, tree2brackets
from .corpus_readers import (BijankhanReader, DadeganReader, DegarbayanReader,
                             HamshahriReader, MirasTextReader, PersicaReader,
                             PeykareReader, QuranReader, SentiPersReader,
                             TNewsReader, TreebankReader, VerbValencyReader,
                             WikipediaReader)
from .dependency_parser import DependencyParser, MaltParser, TurboParser
from .informal_normalizer import InformalLemmatizer, InformalNormalizer
from .lemmatizer import Conjugation, Lemmatizer
from .normalizer import Normalizer
from .pos_tagger import POSTagger, StanfordPOSTagger
from .sentence_tokenizer import SentenceTokenizer
from .sequence_tagger import IOBTagger, SequenceTagger
from .stemmer import Stemmer
from .token_splitter import TokenSplitter
from .utils import default_verbs, default_words, stopwords_list, words_list
from .word_tokenizer import WordTokenizer


def sent_tokenize(text: str) -> List[str]:
    """Sentence Tokenizer."""
    if not hasattr(sent_tokenize, "tokenizer"):
        sent_tokenize.tokenizer = SentenceTokenizer()
    return sent_tokenize.tokenizer.tokenize(text)


def word_tokenize(sentence: str) -> List[str]:
    """Word Tokenizer."""
    if not hasattr(word_tokenize, "tokenizer"):
        word_tokenize.tokenizer = WordTokenizer()
    return word_tokenize.tokenizer.tokenize(sentence)
