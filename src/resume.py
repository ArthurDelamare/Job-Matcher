from .document import Document
from .position import Position

class Resume(Document):
    
    def compare(self, position: Position):
        missing_keywords = dict()
        matching_keywords = dict()

        d = [x.lower() for x in self.keywords] # make dict of list with less elements  
        for key, value in position.keywords.items():  # search against bigger list  
            if key.lower() in d:
                matching_keywords[key] = value
            else: 
                missing_keywords[key] = value
        return matching_keywords, missing_keywords