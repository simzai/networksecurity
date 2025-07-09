
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('my requirements.txt is not found')

    return requirement_lst

setup(
    name='networksecurity',
    version='0.0.1',
    author='Simran Juneja',
    author_email='ksimranjuneja19@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
