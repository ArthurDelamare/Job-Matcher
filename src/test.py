import unittest
from .resume import Resume
from .options import Options

class TestProject(unittest.TestCase):

    def test_init_resume(self):
        resume_text = '''
            Name : John Doe
            Title : Software Engineer
            
            Skills : 
            Java, Python, Php, JavaScript, TypeScript, Golang
            
            Education :
            2016 - 2021 : Master in Computer Science, Random School

            Experience :
            2018 - Now : Software Engineer at My Dream Company

            2016 - 2018 : Frontend Developer at Random CMS Company
        '''
        options = Options(domain_keywords = ['Python', 'JavaScript', 'Agile', 'TypeScript', 'Java', 'Docker'], sections = True)

        resume = Resume(text = resume_text, options = options)

        self.assertEqual(resume.text, resume_text)
        self.assertEqual(resume.doc[1].text, 'Name')
        self.assertEqual(resume.keywords['CMS'].text, 'Random CMS Company')
        self.assertEqual(resume.domains_keywords, ['Java', 'Python', 'JavaScript', 'TypeScript'])

if __name__ == "__main__":
    unittest.main()