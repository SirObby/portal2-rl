from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Portal2 gym environment'
LONG_DESCRIPTION = 'This is a package for creating an OpenAI gym environment for the video game Portal 2.'

setup(
       # the name must match the folder name 'verysimplemodule'
        name="portal2-rl", 
        version=VERSION,
        author="Samuel Hautamäki",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['gym', 'numpy'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'portal2', 'openai', 'gym'],
        classifiers= [
        ]
)
