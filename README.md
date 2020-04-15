# Job-Matcher

## What is this project ?

A **resume parser** and **position parser** to help you perform **job matching based on keywords.**

The purpose of this project is to use the power of **Natural Language Processing to distinguish sections and keywords in a resume or position.** You then have all the information to conduct an optimal analysis.

## Get started

### Requirements
- Python 3
- Spacy version equal or greater than 2.2.3
- Spacy language model: en_core_web_sm

### Installation
If you do not have Spacy and its language model installed, here are the two commands:
1. ``` pip install -U spacy ```
2. ``` python -m spacy download en_core_web_sm ```

### Usage
The two main components (Resume and Position) are sharing common parameters:
1. **text**: the resume or position as a string.
2. **language**: the language of the resume or position. By default, it is "en" for "English".
3. **model**: the spacy model. By default, it is "en_core_web_sm" for the English model.
4. **options**: the parsing options, allow you to define how much features you want to execute.

By default, only the global keywords are extracted but, you can specify otherwise in the options.

Resume and Position are sharing the same structure and thus, you can use them in the same way. The following examples are made using the Resume class but it would be the same with the Position class.

#### Basic execution

```python
from resume import Resume

resume_text = 'All of your resume content here...'
resume = Resume(text = resume_text)
# resume.keywords now contains the keywords and their context as a dictionary of string and Span
```

#### Domain specific keywords
To **search for domain specific keywords**, use the **options**:
```python
from options import Options
from resume import Resume

options = Options(domain_keywords = ['Python', 'JavaScript', 'Agile', 'TypeScript', 'Java', 'Docker'])
resume = Resume(text = resume_text, options = options)
# resume.domain_keywords now contains the domains specific keywords that matched
```

#### Identify sections
To **identify sections**, use the **options**:
```python
from options import Options
from resume import Resume
from sections import Certificate, Education, Experience, Skills, Summary, Volunteering

options = Options(sections = [Certificate, Education, Experience, Skills, Summary, Volunteering])
resume = Resume(text = resume_text, options = options)
# resume.sections now contains the sections
```

To **check if a Section exist** in a resume or position (the education section for example), use:
```python
resume.has_section('education')
```

List of already defined sections:
1. Certificate
2. Education
3. Experience
4. Skills
5. Summary
6. Requirements
7. Responsibilities
8. Volunteering

#### Create a new section
In order to **create a new section**, you need to create a **class that extends the Section class**.

Let's say, we want to create a Competition section, here is an example of how to do it:

```python
class Competition(Section):

    name = 'Competition' # Section title is required by Spacy to use the matcher

    keywords = {
        'en': ['competition', 'competitive awards', 'awards'],
    }
```

Then, you can **import** it and **use it in the options**:
```python
options = Options(sections = [Competition])
resume = Resume(text = resume_text, options = options)
```

#### Compare keywords of resumes and positions
It is possible to **compare both global and domain specific keywords** between a resume and a position.

The compare_global_keywords returns two dictionaries meanwhile the compare_domain_keywords method returns two lists.

##### Global keywords comparison
```python
resume = Resume(text = resume_text)
position = Position(text = position_text)

matching_general_keywords, missing_general_keywords = resume.compare_global_keywords(position)
```

##### domain specific keywords comparison
```python
options = Options(domain_keywords = ['JavaScript', 'C++', 'HTML5'])
resume = Resume(text = resume_text, options = options)
position = Position(text = position_text, options = options)

matching_domain_keywords, missing_domain_keywords = position.compare_domain_keywords(resume)
```

## Features to come
- Link keywords to sections
- Machine Learning model for entities extraction (time required for a skill, job experience recognition...)
