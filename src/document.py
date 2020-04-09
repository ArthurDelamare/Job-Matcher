import spacy
from spacy.matcher import Matcher
from .keyword import Keyword
from .options import Options
from .sections import Certificate, Education, Experience, Skills, Summary, Volunteering

class Document:

    def __init__(self, text: str, language = 'en', model = 'en_core_web_sm', options = Options()):
        # Save initial text
        self.text = text
        self.options = options 
        
        # Tokenized resume
        nlp = spacy.load(model, disable = ['ner'])
        self.doc = nlp(text)

        # Get general keywords from doc, as well as the context (the part of sentence it has been detected in)
        self.keywords = self._extract_keywords_from_doc()

        # Get domain keywords if specified in options
        if self.options.domain_keywords:
            self.domains_keywords = self._extract_domain_keywords_from_keywords()

        # Process section detection if specified in options
        if self.options.sections:
            self.sections = {}
            matcher = Matcher(nlp.vocab)
            for section in self.options.sections:
                matcher.add(section.name, section.is_header, section.get_pattern(language))
            matcher(self.doc)

            
            section_list = [] # holds the sections, in order

            # Get the sections, their start and end
            for ent in self.doc.ents:
                if ent.label_ in [section.name for section in self.options.sections]:
                    if section_list:
                        section_list[len(section_list) - 1]['end'] = ent.start - 1
                        section_list[len(section_list) - 1]['end_char'] = ent.start_char - 1
                    section_list.append({'name': ent.label_.lower(), 'start': ent.start, 'start_char': ent.start_char})

            # Save the sections into a dictionary 
            for index, section in enumerate(section_list):
                if index != len(section_list) - 1:
                    self.sections[section['name']] = {'tokens': self.doc[section['start'] : section['end']], 'start': section['start'], 'end': section['end'], 'start_char': section['start_char'], 'end_char': section['end_char']}
                else:
                    self.sections[section['name']] = {'tokens': self.doc[section['start'] :], 'start': section['start'], 'end': len(self.doc), 'start_char': section['start_char'], 'end_char': len(self.doc.text)}



    def _extract_keywords_from_doc(self) -> dict:
        ''' Extract the keywords from the spacy doc by removing unwanted tokens as punctuations, symbols, spaces... '''

        tokens = [token for token in self.doc if not token.is_stop and token.pos_ not in ['X', 'PUNCT', 'SPACE', 'SYM', 'CCONJ', 'NUM', 'ADJ', 'ADV', 'VERB'] and token.text not in ['-', '|', '•']]
        tokens_with_context = dict()
        for token in tokens:
            for chunk in self.doc.noun_chunks:
                if token in chunk:
                    tokens_with_context[token.text] = chunk
        return tokens_with_context

    def _extract_domain_keywords_from_keywords(self) -> list:
        ''' Search domain keywords into the keyword list. 
        The domain_keywords list in options determines the keywords that are going to be matched. '''

        if not self.keywords:
            return []

        domain_keywords = list()
        for keyword in self.keywords.keys():
            if keyword in self.options.domain_keywords:
                domain_keywords.append(keyword)

        return domain_keywords

    def has_section(self, section: str) -> bool:
        ''' Return True if the section exists in the resume. Otherwise, return False.'''

        return self.sections and section in self.sections
