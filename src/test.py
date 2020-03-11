import unittest
from .resume import Resume

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
        resume = Resume(resume_text)

        self.assertEqual(resume_text, resume.text)
        self.assertEqual(resume.doc[1].text, 'Name')
        self.assertEqual(resume.keywords['CMS'].text, 'Random CMS Company')

if __name__ == "__main__":
    unittest.main()