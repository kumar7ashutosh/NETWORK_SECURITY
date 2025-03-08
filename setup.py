from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    req_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for i in lines:
                requirement=i.strip()
                if requirement and requirement!='-e .':
                    req_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')
    
    return req_lst                            

print(get_requirements())
setup(
    name="NETWORK SECURITY",
    version="0.0.1",
    author="Kumar Ashutosh",
    author_email="kumarashutoshbtech2023@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)