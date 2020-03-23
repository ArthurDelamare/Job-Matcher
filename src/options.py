from typing import List

class Options: 

    def __init__(self, domain_keywords: List[str] = [], sections = False):
        self.domain_keywords = domain_keywords
        self.sections = sections