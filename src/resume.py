import spacy
from .keyword import Keyword

class Resume:

    def __init__(self, text: str, model = 'en_core_web_sm'):
        self.text = text # Save initial text
        
        # Tokenized resume
        nlp = spacy.load(model, disable = ['ner'])
        self.doc = nlp(text)
        self.keywords = self._extract_keywords_from_doc()

    def _extract_keywords_from_doc(self) -> dict:
        tokens = [token for token in self.doc if not token.is_stop and token.pos_ not in ['X', 'PUNCT', 'SPACE', 'SYM', 'CCONJ', 'NUM', 'ADJ', 'ADV', 'VERB'] and token.text not in ['-', '|', '•']]
        tokens_with_context = dict()
        for token in tokens:
            for chunk in self.doc.noun_chunks:
                if token in chunk:
                    tokens_with_context[token.text] = chunk
        return tokens_with_context