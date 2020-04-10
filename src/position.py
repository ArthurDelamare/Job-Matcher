from .document import Document

class Position(Document):
    
    def compare_global_keywords(self, resume: 'Resume'):
        missing_keywords = dict()
        matching_keywords = dict()

        d = [x.lower() for x in resume.keywords] # make dict of list with less elements  
        for key, value in self.keywords.items():  # search against bigger list  
            if key.lower() in d:
                matching_keywords[key] = value
            else: 
                missing_keywords[key] = value
        return matching_keywords, missing_keywords

    def compare_domain_keywords(self, resume: 'Resume'):
        missing_keywords = list()
        matching_keywords = list()

        d = [domain_keyword.lower() for domain_keyword in resume.domains_keywords] # make dict of list with less elements  
        for value in self.domains_keywords:  # search against bigger list  
            if value.lower() in d:
                matching_keywords.append(value)
            else: 
                missing_keywords.append(value)
        return matching_keywords, missing_keywords