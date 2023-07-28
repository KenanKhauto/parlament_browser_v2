
import spacy

class SpacyTextAnalyzer:


    def __init__(self, model_name="de_core_news_lg"):
        self.pipline = spacy.load(model_name)

    def analyze(self, text):
        analyzed_doc = self.pipline(text)
        return analyzed_doc
    
    def get_tokens(self, analyzed_doc):
        tokens = []

        for token in analyzed_doc:
            token_dict = {
                "text":token.text,
                "pos":token.pos_,
                "dependency":token.dep_,
                "dependency_description":spacy.explain(token.dep_),
                "dependent_to":token.head.text
            }
            tokens.append(token_dict)

        return tokens


    def get_entities(self, analyzed_doc):
        entities = []

        for entity in analyzed_doc.ents:
            entity_dict = {
                "text":entity.text,
                "label":entity.label_,
                "start_char":entity.start_char,
                "end_char":entity.end_char
            }
            entities.append(entity_dict)

        return entities


    def get_sentences(self, analyzed_doc):
        sentences = []

        for sent in analyzed_doc.sents:
            sentence = {
                "text":sent.text,
                "start_char":sent.start_char,
                "end_char":sent.end_char
            }
            sentences.append(sentence)
        
        return sentences


if __name__ == "__main__":
    model = SpacyTextAnalyzer()
    text = """Traurigkeit ist ein Gefühl oder eine Art von Gefühl, das ein Mensch in verschiedenen Lebenssituationen haben kann. Traurige Zitate werden von den großen Autoren der Geschichte geschrieben und helfen dir deine Gefühle auszudrücken.
Traurigkeit ist ein Gefühl, dem fast jeder Mensch in seinem Leben gegenübersteht. Diese Zitate, Weisheiten und traurige Sprüche regen zum Nachdenken an und fördern die Sichtweise auf das Leben.
"""
    doc = model.analyze(text)
    print(len(model.get_entities(doc)))
    for item in model.get_entities(doc):
        print(item)