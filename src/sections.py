from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from typing import List

class Section:

    name = 'undefined' 
    
    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the experience header of the experience section '''
        pass

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a section keyword is found: check if the section keyword is a section header '''
        pass

class Certificate(Section):

    name = 'Certificate' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['certificate', 'certificates', 'certifications'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the certificate header of the education section '''
    
        if language not in Certificate.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Certificate.keywords.keys())))

        return [{"LOWER": {"IN" : Certificate.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a certificate keyword is found: check if the certificate keyword is a certificate header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Certificate.name)
            doc.ents += (entity,)

class Education(Section):

    name = 'Education'

    keywords = {
        'en': ['education'],
    } 

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the education header of the education section '''

        if language not in Education.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Education.keywords.keys())))
    
        return [{"LOWER": {"IN" : Education.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a education keyword is found: check if the education keyword is a education header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Education.name)
            doc.ents += (entity,)

class Experience(Section):

    name = 'Experience' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['experience', 'experiences'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the experience header of the experience section '''
    
        if language not in Experience.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Experience.keywords.keys())))

        return [{"LOWER": {"IN" : Experience.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a experience keyword is found: check if the experience keyword is a experience header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Experience.name)
            doc.ents += (entity,)

class Skills(Section):

    name = 'Skills' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['competencies', 'skills'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the skills header of the skills section '''

        if language not in Skills.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Skills.keywords.keys())))
    
        return [{"LOWER": {"IN" : Skills.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a skills keyword is found: check if the skills keyword is a skills header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Skills.name)
            doc.ents += (entity,)

class Summary(Section):

    name = 'Summary' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['summary'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the summary header of the summary section '''
    
        if language not in Summary.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Summary.keywords.keys())))

        return [{"LOWER": {"IN" : Summary.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a summary keyword is found: check if the summary keyword is a summary header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Summary.name)
            doc.ents += (entity,)

class Volunteering(Section):

    name = 'Volunteering' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['volunteer', 'volunteering', 'charity'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the volunteering header of the volunteering section '''

        if language not in Volunteering.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Volunteering.keywords.keys())))
    
        return [{"LOWER": {"IN" : Volunteering.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a volunteering keyword is found: check if the volunteering keyword is a volunteering header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Volunteering.name)
            doc.ents += (entity,)

class Environment(Section):

    name = 'Environment' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['environment'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the environment header of the environment section '''

        if language not in Environment.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Environment.keywords.keys())))
    
        return [{"LOWER": {"IN" : Environment.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a environment keyword is found: check if the environment keyword is a environment header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Environment.name)
            doc.ents += (entity,)

class Requirements(Section):

    name = 'Requirements' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['requirements'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the requirements header of the requirements section '''

        if language not in Requirements.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Requirements.keywords.keys())))
    
        return [{"LOWER": {"IN" : Requirements.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a requirements keyword is found: check if the requirements keyword is a requirements header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Requirements.name)
            doc.ents += (entity,)

class Technologies(Section):

    name = 'Technologies' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['tech', 'technologies'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the technologies header of the technologies section '''

        if language not in Technologies.keywords:
            raise Exception('The language code {} is undefined. Correct languages: {}'.format(language, ', '.join(Technologies.keywords.keys())))
    
        return [{"LOWER": {"IN" : Technologies.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a technologies keyword is found: check if the technologies keyword is a technologies header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Technologies.name)
            doc.ents += (entity,)