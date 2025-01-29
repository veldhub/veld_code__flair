

text = None


def split_sentences():
    from flair.splitter import SegtokSentenceSplitter
    splitter = SegtokSentenceSplitter()
    global text
    text = splitter.split(text)


def infer_ner():
    pass


def infer_sentiment():
    pass


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


def main():
    if DO_SPLIT_SENTENCES:
        split_sentences()
    if DO_INFER_NER:
        infer_ner()
    if DO_INFER_SENTIMENT:
        infer_sentiment()


if __name__ == "__main__":
    main()

