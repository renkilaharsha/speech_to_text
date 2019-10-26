from setuptools import setup,find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here,'README.md'),encoding='utf-8') as f:
    long_description = f.read()


setup(
        name ='speech_2_text',
        version = '0.0.1',
        description = "A python project which converts the Spoken English to Written English",
        long_description =  long_description,
        long_description_content_type="text/markdown",
        url = 'https://github.com/renkilaharsha/speech_to_text',
        author = 'Harsha Renkila',
        author_email = 'renkilaharsha1@gmail.com',
        packages=['speech_2_text','speech_2_text.submodule'],
        #install_requires=['SpeechRecognition','pyaudio'],
        project_urls = {
            'Bug Reports' : 'https://github.com/renkilaharsha/speech_to_text/issues',
            'Source' : 'https://github.com/renkilaharsha/speech_to_text'
            }

        )
