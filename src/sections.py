from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from typing import List

class Section:

    name = 'undefined' 
    
    keywords = {}

    @classmethod
    def get_pattern(cls, language: str):
        ''' Pattern to detect the certificate header of the education section '''
    
        if language not in cls.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(cls.keywords.keys())))

        return [{"LOWER": {"IN" : cls.keywords[language]}}]

    @classmethod
    def is_header(cls, matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a certificate keyword is found: check if the certificate keyword is a certificate header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=cls.name)
            doc.ents += (entity,)

class Certificate(Section):

    name = 'Certificate' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['certificate', 'certificates', 'certifications'],
    }

class Education(Section):

    name = 'Education' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['education'],
    } 

class Experience(Section):

    name = 'Experience' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['experience', 'experiences'],
    }

class Skills(Section):

    name = 'Skills' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['competencies', 'skills'],
    }

class Summary(Section):

    name = 'Summary' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['summary'],
    }

class Volunteering(Section):

    name = 'Volunteering' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['volunteer', 'volunteering', 'charity'],
    }

class Environment(Section):

    name = 'Environment' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['environment'],
    }

class Requirements(Section):

    name = 'Requirements' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['requirements'],
    }

class Responsibilities(Section):

    name = 'Responsibilities' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['responsibilities'],
    }

class Technologies(Section):

    name = 'Technologies' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['tech', 'technologies'],
    }