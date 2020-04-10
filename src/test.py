import unittest
from .options import Options
from .position import Position
from .resume import Resume
from .sections import Certificate, Education, Experience, Skills, Summary, Requirements, Responsibilities, Volunteering


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
        self.assertEqual(resume.has_section(Volunteering.name.lower()), True)
        self.assertEqual(resume.has_section(Certificate.name.lower()), False)

    def test_init_position(self):
        position_text = '''
            We are looking for an enthusiastic Junior Software Developer to join our experienced software design team. You will report directly to the Development Manager and assist with all functions of software coding and design. Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers.

            To ensure success as a Junior Software Developer, you should have a good working knowledge of basic programming languages, the ability to learn new technology quickly, and the ability to work in a team environment. Ultimately, a top-class Junior Software Developer provides valuable support to the design team while continually improving their coding and design skills.

            Responsibilities:
            Assisting the Development Manager with all aspects of software design and coding.
            Attending and contributing to company development meetings.
            Learning the codebase and improving your coding skills.
            Writing and maintaining code.
            Working on minor bug fixes.
            Monitoring the technical performance of internal systems.
            Responding to requests from the development team.
            Gathering information from consumers about program functionality.
            Writing reports.
            Conducting development tests.
            
            Requirements:
            Bachelor's degree in Computer Science.
            Knowledge of basic coding languages including C++, HTML5, and JavaScript.
            Basic programming experience.
            Knowledge of databases and operating systems.
            Good working knowledge of email systems and Microsoft Office software.
            Ability to learn new software and technologies quickly.
            Ability to follow instructions and work in a team environment.
            Detail-oriented.
        '''

        options = Options(sections = [Requirements, Responsibilities, Volunteering])
        position = Position(text = position_text, options = options)
        self.assertEqual(position.text, position_text)
        self.assertEqual(position.has_section(Requirements.name.lower()), True)
        self.assertEqual(position.has_section(Responsibilities.name.lower()), True)
        self.assertEqual(position.has_section(Volunteering.name.lower()), False)


    def test_resume_compare(self):
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

        position_text = '''
            We are looking for an enthusiastic Junior Software Developer to join our experienced software design team. You will report directly to the Development Manager and assist with all functions of software coding and design. Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers.

            To ensure success as a Junior Software Developer, you should have a good working knowledge of basic programming languages, the ability to learn new technology quickly, and the ability to work in a team environment. Ultimately, a top-class Junior Software Developer provides valuable support to the design team while continually improving their coding and design skills.

            Responsibilities:
            Assisting the Development Manager with all aspects of software design and coding.
            Attending and contributing to company development meetings.
            Learning the codebase and improving your coding skills.
            Writing and maintaining code.
            Working on minor bug fixes.
            Monitoring the technical performance of internal systems.
            Responding to requests from the development team.
            Gathering information from consumers about program functionality.
            Writing reports.
            Conducting development tests.
            
            Requirements:
            Bachelor's degree in Computer Science.
            Knowledge of basic coding languages including C++, HTML5, and JavaScript.
            Basic programming experience.
            Knowledge of databases and operating systems.
            Good working knowledge of email systems and Microsoft Office software.
            Ability to learn new software and technologies quickly.
            Ability to follow instructions and work in a team environment.
            Detail-oriented.
        '''

        options = Options(domain_keywords = ['JavaScript', 'C++', 'HTML5'])

        resume = Resume(text = resume_text, options = options)
        position = Position(text = position_text, options = options)
        matching_general_keywords, missing_general_keywords = resume.compare_global_keywords(position)
        self.assertEqual('software' in matching_general_keywords.keys(), True)
        self.assertEqual('react' in matching_general_keywords.keys(), False)
        self.assertEqual('HTML5' in missing_general_keywords.keys(), True)
        self.assertEqual('C++' in missing_general_keywords.keys(), True)

        matching_domain_keywords, missing_domain_keywords = resume.compare_domain_keywords(position)
        self.assertEqual('JavaScript' in matching_domain_keywords, True)
        self.assertEqual('C++' in missing_domain_keywords, True)

    def test_position_compare(self):
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

        position_text = '''
            We are looking for an enthusiastic Junior Software Developer to join our experienced software design team. You will report directly to the Development Manager and assist with all functions of software coding and design. Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers.

            To ensure success as a Junior Software Developer, you should have a good working knowledge of basic programming languages, the ability to learn new technology quickly, and the ability to work in a team environment. Ultimately, a top-class Junior Software Developer provides valuable support to the design team while continually improving their coding and design skills.

            Responsibilities:
            Assisting the Development Manager with all aspects of software design and coding.
            Attending and contributing to company development meetings.
            Learning the codebase and improving your coding skills.
            Writing and maintaining code.
            Working on minor bug fixes.
            Monitoring the technical performance of internal systems.
            Responding to requests from the development team.
            Gathering information from consumers about program functionality.
            Writing reports.
            Conducting development tests.
            
            Requirements:
            Bachelor's degree in Computer Science.
            Knowledge of basic coding languages including C++, HTML5, and JavaScript.
            Basic programming experience.
            Knowledge of databases and operating systems.
            Good working knowledge of email systems and Microsoft Office software.
            Ability to learn new software and technologies quickly.
            Ability to follow instructions and work in a team environment.
            Detail-oriented.
        '''

        options = Options(domain_keywords = ['JavaScript', 'C++', 'HTML5'])

        resume = Resume(text = resume_text, options = options)
        position = Position(text = position_text, options = options)
        matching_general_keywords, missing_general_keywords = position.compare_global_keywords(resume)
        self.assertEqual('software' in matching_general_keywords.keys(), True)
        self.assertEqual('react' in matching_general_keywords.keys(), False)
        self.assertEqual('HTML5' in missing_general_keywords.keys(), True)
        self.assertEqual('C++' in missing_general_keywords.keys(), True)

        matching_domain_keywords, missing_domain_keywords = position.compare_domain_keywords(resume)
        self.assertEqual('JavaScript' in matching_domain_keywords, True)
        self.assertEqual('C++' in missing_domain_keywords, True)

if __name__ == "__main__":
    unittest.main()