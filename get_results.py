import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords


def plot_frequencies(corpus, num):
    plt.switch_backend('Agg')
    fig = plt.figure()
    df = pd.read_csv(f"./data/{corpus}.tsv", sep="\t", encoding="utf-8")
    pos_df = df[["year", "NOUN", "VERB", "ADJ", "ADVB", "PREP"]].sort_values(by="year").reset_index()
    pos_df.plot(x='year', y=["NOUN", "VERB", "ADJ", "ADVB", "PREP"], figsize=(12, 9))
    plt.savefig(f"./static/res/{num}.png")
    plt.close(fig)


def plot_words(corpus, num):
    plt.switch_backend('Agg')
    fig = plt.figure()
    df = pd.read_csv(f"./data/{corpus}.tsv", sep="\t", encoding="utf-8")
    stops_dict = {
        "rus": "russian",
        "shake": "english",
        "ger": "german"
    }
    stops = stopwords.words(stops_dict[corpus])
    text = ' '.join([word for word in df["lemmas"].values if word not in stops])
    wordcloud = WordCloud(
        background_color='white',
        width=1200,
        height=900,
    ).generate(text)

    plt.figure(figsize=(12, 9), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(f"./static/res/{num}.png")
    plt.close(fig)

