from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from typing import List

class Section:

    name = 'undefined'

    # Keywords to detect sections
    keywords = {
        'en': {
            'certificate': ['certificate', 'certificates', 'certifications'],
            'education': ['education'],
            'environment': ['environment'],
            'experience': ['experience', 'experiences'],
            'requirements' : ['requirements'],
            'skills': ['competencies', 'skills'],
            'summary': ['summary'],
            'technologies': ['tech', 'technologies'],
            'volunteering': ['volunteer', 'volunteering', 'charity']
        }
    } 
    
    @staticmethod
    def get_pattern(language: str, section: str):
        ''' Pattern to detect the experience header of the experience section '''
    
        return [{"LOWER": {"IN" : Section.keywords[language][section]}}]

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
    
        return [{"LOWER": {"IN" : Volunteering.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a volunteering keyword is found: check if the volunteering keyword is a volunteering header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Volunteering.name)
            doc.ents += (entity,)

class Requirements:

    name = 'Requirements' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['requirements'],
    }

    @staticmethod
    def get_pattern(language: str):
        ''' Pattern to detect the requirements header of the requirements section '''
    
        return [{"LOWER": {"IN" : Volunteering.keywords[language]}}]

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a requirements keyword is found: check if the requirements keyword is a requirements header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Requirements.name)
            doc.ents += (entity,)