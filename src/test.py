import unittest
from .options import Options
from .resume import Resume
from .sections import Certificate, Education, Experience, Skills, Summary, Volunteering


class TestProject(unittest.TestCase):

    def test_init_resume(self):
        resume_text = '''
            Name : John Doe
            Title : Software Engineer

            Summary :
            My name is John Doe, I am software engineer with 3 years experience. Especially comfortable in web development, I'm open to job offers.
            
            Skills : 
            Java, Python, Php, JavaScript, TypeScript, Golang
            
            Education :
            2016 - 2021 : Master in Computer Science, Random School

            Experience :
            2018 - Now : Software Engineer at My Dream Company

            2016 - 2018 : Frontend Developer at Random CMS Company

            Volunteering :
            2017 - Now : Equal right activist
        '''
        options = Options(domain_keywords = ['Python', 'JavaScript', 'Agile', 'TypeScript', 'Java', 'Docker'], sections = [Certificate, Education, Experience, Skills, Summary, Volunteering])

        resume = Resume(text = resume_text, options = options)

        self.assertEqual(resume.text, resume_text)
        self.assertEqual(resume.doc[1].text, 'Name')
        self.assertEqual(resume.keywords['CMS'].text, 'Random CMS Company')
        self.assertEqual(resume.domains_keywords, ['Java', 'Python', 'JavaScript', 'TypeScript'])

if __name__ == "__main__":
    unittest.main()