from typing import List
import os.path as osp
import requests
import spacy

spacy_nlp = {
    'xsd:string': spacy.load("en_core_web_sm"),
    'en': spacy.load("en_core_web_sm"),
    'de': spacy.load("de_core_news_sm"),
    'ru': spacy.load("ru_core_news_sm"),
    'zh': spacy.load("zh_core_web_md"),
    'fr': spacy.load('fr_core_news_sm'),
    'it': spacy.load('it_core_news_sm'),
    'pl': spacy.load('pl_core_news_sm'),
    'pt': spacy.load('pt_core_news_sm'),
    'ja': spacy.load('ja_core_news_sm'),
    'nl': spacy.load('nl_core_news_sm'),
    'es': spacy.load('es_core_news_sm')
}

def preprocess_string(value, lowercasing, lemmaticeing, spacy_nlp, datatype):
    if value[0] in ['"', "'"] and value[-1] in ['"', "'"]:
        value = value[1:-1]  # remove quotes
    if lowercasing:
        value = value.lower()
        if lemmaticeing:
            try:
                doc = spacy_nlp[datatype](value)
                value = ' '.join([token.lemma_ for token in doc]).rstrip().lstrip()
                return value
            except KeyError:
                return value

    return value

def download_files(urls: List[List], target_dir: str) -> None:
    for file, url in urls:
        r = requests.get(url, allow_redirects=True)
        open(osp.join(target_dir, file), 'wb').write(r.content)