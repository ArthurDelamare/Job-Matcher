import spacy

class Resume:

    def __init__(self, text: str, model = 'en_core_web_sm'):
        self.text = text # Save initial text
        
        # Tokenized resume
        nlp = spacy.load(model, disable = ['ner'])
        self.doc = nlp(text)
