from setuptools import setup, find_packages

from src import patch

VERSION = '0.0.1' 
DESCRIPTION = 'Portal2 gym environment'
LONG_DESCRIPTION = 'This is a package for creating an OpenAI gym environment for the video game Portal 2.'
DEFAULT_PORTAL2_PATH = '~/.local/share/Steam/steamapps/common/Portal 2/'

patch.patch_portal2(DEFAULT_PORTAL2_PATH)

setup(
        name="portal2-rl", 
        version=VERSION,
        author="Samuel Hautamäki",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['gym', 'numpy'],  
        keywords=['python', 'portal2', 'openai', 'gym'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
)
