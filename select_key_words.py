from rutermextract import TermExtractor


def select_key_words(text):
    term_extractor = TermExtractor()
    key_words = []
    for term in term_extractor(text):
        key_words.append(term.normalized)
    return key_words

