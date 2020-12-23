from pymorphy2 import MorphAnalyzer
from pymorphy2.tokenizers import simple_word_tokenize
import spacy


class Preprocesser:

    def __init__(self, language):
        self.language = language
        if language == "rus":
            self.analyzer = MorphAnalyzer()
        elif language == "shake":
            self.analyzer = spacy.load("en_core_web_sm")
        elif language == "ger":
            self.analyzer = spacy.load("de_core_news_sm")

    def lemmatize(self, line):
        self.lemmas = []
        if self.language == "rus":
            play_lemmas = [self.analyzer.parse(token)[0].normal_form
                             for token in simple_word_tokenize(line)]
        else:
            play_lemmas = [token.lemma_ for token in self.analyzer(line)]
        self.lemmas += play_lemmas
        return " ".join(play_lemmas)

    def pos(self, line):
        self.pos_dict = {}
        # определение
        if self.language == "rus":
            play_pos = [self.analyzer.parse(token)[0].tag.POS
                             for token in simple_word_tokenize(line)]
        else:
            play_pos = [token.pos_ for token in self.analyzer(line)]
        # подсчёт
        for this_pos in play_pos:
            if this_pos not in self.pos_dict:
                self.pos_dict[this_pos] = 1
            else:
                self.pos_dict[this_pos] += 1
        # относительные величины
        for pos in self.pos_dict:
            self.pos_dict[pos] = self.pos_dict[pos]/len(play_pos)
        return self.pos_dict