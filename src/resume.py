import spacy
from .keyword import Keyword
from .options import Options
class Resume:

    def __init__(self, text: str, model = 'en_core_web_sm', options = Options()):
        # Save initial text
        self.text = text
        self.options = options 
        
        # Tokenized resume
        nlp = spacy.load(model, disable = ['ner'])
        self.doc = nlp(text)

        # Get general keywords from doc, as well as the context (the part of sentence it has been detected in)
        self.keywords = self._extract_keywords_from_doc()
        if self.options.domain_keywords:
            self.domains_keywords = self._extract_domain_keywords_from_keywords()

    def _extract_keywords_from_doc(self) -> dict:
        ''' Extract the keywords from the spacy doc by removing unwanted tokens as punctuations, symbols, spaces... '''

        tokens = [token for token in self.doc if not token.is_stop and token.pos_ not in ['X', 'PUNCT', 'SPACE', 'SYM', 'CCONJ', 'NUM', 'ADJ', 'ADV', 'VERB'] and token.text not in ['-', '|', '•']]
        tokens_with_context = dict()
        for token in tokens:
            for chunk in self.doc.noun_chunks:
                if token in chunk:
                    tokens_with_context[token.text] = chunk
        return tokens_with_context

    def _extract_domain_keywords_from_keywords(self):
        ''' Search domain keywords into the keyword list. 
        The domain_keywords list in options determines the keywords that are going to be matched. '''

        if not self.keywords:
            return []

        domain_keywords = list()
        for keyword in self.keywords.keys():
            if keyword in self.options.domain_keywords:
                domain_keywords.append(keyword)

        return domain_keywords
