import requests


def get_play_meta(corpus):
        play_names = []
        play_years = []
        request_url = f"https://dracor.org/api/corpora/{corpus}"
        response = requests.get(request_url)
        if response:
            for play in response.json()["dramas"]:
                play_names.append(play["name"])
                play_years.append(play["yearNormalized"])
        return play_names, play_years


def get_play_text(corpus, play_name):
    overall_text = ""
    spoken_url = f"https://dracor.org/api/corpora/{corpus}/play/{play_name}/spoken-text"
    stage_url = f"https://dracor.org/api/corpora/{corpus}/play/{play_name}/stage-directions"
    response = requests.get(spoken_url)
    if response:
        overall_text += response.text
    response = requests.get(stage_url)
    if response:
        overall_text += response.text
    return overall_text