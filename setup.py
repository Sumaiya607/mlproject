from setuptools import setup, find_packages
from typing import List

HYPEN_e_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        
        if HYPEN_e_DOT in requirements:
            requirements.remove(HYPEN_e_DOT)

    return requirements

setup(
    name='mlproject',
    author='Sumaiya',
    author_email='sumaiyaowais607@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

