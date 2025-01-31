import json
import os

from flair.nn import Classifier
from flair.data import Sentence


IN_FILE = "/veld/input/data/" + os.getenv("in_file")
OUT_FILE = "/veld/output/" + os.getenv("out_file")
DO_SPLIT_SENTENCES = os.getenv("do_split_sentences") == "true"
# DO_INFER_NER = os.getenv("do_infer_ner") == "true"
# DO_INFER_SENTIMENT = os.getenv("do_infer_sentiment") == "true"
MODEL_INFER_NER = os.getenv("model_infer_ner")
MODEL_INFER_SENTIMENT = os.getenv("model_infer_sentiment")
MODEL_INFER_LINKS = os.getenv("model_infer_links")


with open(IN_FILE, "r") as f:
    text = f.read()


def split_sentences():
    from flair.splitter import SegtokSentenceSplitter
    splitter = SegtokSentenceSplitter()
    global text
    text = splitter.split(text)


def infer_ner():
    classifier = Classifier.load(MODEL_INFER_NER)
    classifier.predict(text)


def infer_sentiment():
    classifier = Classifier.load(MODEL_INFER_SENTIMENT)
    classifier.predict(text)


def infer_links():
    pass


def infer_pos():
    pass


def infer_frame():
    pass


def infer_chunk():
    pass


def infer_relations():
    pass


def persist_inference_data():
    global text
    if type(text) is list:
        text = [s.to_dict() for s in text]
    elif type(text) is Sentence:
        text = text.to_dict()
    with open(OUT_FILE, "w") as f:
        json.dump(text, f, indent=4, ensure_ascii=False)


def main():
    if DO_SPLIT_SENTENCES:
        split_sentences()
    if MODEL_INFER_NER is not None:
        infer_ner()
    if MODEL_INFER_SENTIMENT is not None:
        infer_sentiment()
    if MODEL_INFER_LINKS is not None:
        infer_links()
    persist_inference_data()


if __name__ == "__main__":
    main()

