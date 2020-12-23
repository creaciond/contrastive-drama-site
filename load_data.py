from tqdm import tqdm
import pandas as pd

from corpusloader import *
from preprocessing import *


parts = ["NOUN", "VERB", "ADJ", "ADVB", "PREP"]

for corpus in ["rus", "shake", "ger"]:
    plays = {"play": [], "year": [], "text": [], "lemmas": [],
             "NOUN": [], "VERB": [], "ADJ": [], "ADVB": [], "PREP": []}
    play_names, play_years = get_play_meta(corpus)
    plays["play"] = play_names
    plays["year"] = play_years
    for play in tqdm(play_names):
        play_text = get_play_text("ger", play)
        plays["text"].append(play_text)

    preprocesser = Preprocesser(corpus)
    for text in tqdm(plays["text"]):
        plays["lemmas"].append(preprocesser.lemmatize(text))
        play_pos = preprocesser.pos(text)
        for p in parts:
            if p in play_pos:
                plays[p].append(play_pos[p])
            else:
                plays[p].append(0)

    df = pd.DataFrame.from_dict(plays)
    df.to_csv(f"./data/{corpus}.tsv", sep="\t", encoding="utf-8", index=None)
