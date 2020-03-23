from typing import List
from .sections import Section

class Options: 

    def __init__(self, domain_keywords: List[str] = [], sections: List[Section] = []):
        self.domain_keywords = domain_keywords
        self.sections = sections