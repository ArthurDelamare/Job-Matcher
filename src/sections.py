from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from typing import List

class Section:
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


class Certificate(Section):

    title = 'Certificate' # Section title is required by Spacy to use the matcher

    label = 'CERTIFICATE'

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a certificate keyword is found: check if the certificate keyword is a certificate header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Certificate.label)
            doc.ents += (entity,)

class Education(Section):

    title = 'Education' # Section title is required by Spacy to use the matcher

    label = 'EDUCATION'

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a education keyword is found: check if the education keyword is a education header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Education.label)
            doc.ents += (entity,)

class Experience(Section):

    title = 'Experience' # Section title is required by Spacy to use the matcher

    label = 'EXPERIENCE'

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a experience keyword is found: check if the experience keyword is a experience header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Experience.label)
            doc.ents += (entity,)

class Skills(Section):

    title = 'Skills' # Section title is required by Spacy to use the matcher

    label = 'SKILLS'

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a skills keyword is found: check if the skills keyword is a skills header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Skills.label)
            doc.ents += (entity,)

class Summary(Section):

    title = 'Summary' # Section title is required by Spacy to use the matcher

    label = 'SUMMARY'

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a summary keyword is found: check if the summary keyword is a summary header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Summary.label)
            doc.ents += (entity,)

class Volunteering(Section):

    title = 'Volunteering' # Section title is required by Spacy to use the matcher

    label = 'VOLUNTEERING'

    @staticmethod
    def is_header(matcher: Matcher, doc: Doc, i: int, matches: List[tuple]):
        ''' callback when a volunteering keyword is found: check if the volunteering keyword is a volunteering header '''

        _, start, end = matches[i]
        if ('\n\n' in doc[start-3 : start].text.replace(" ", "") and '\n' in doc[start : start+3].text):
            entity = Span(doc, start, end, label=Volunteering.label)
            doc.ents += (entity,)