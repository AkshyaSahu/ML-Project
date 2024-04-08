from setuptools import find_packages,setup
from typing import List

HYPEN_e_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.

    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]


        if HYPEN_e_DOT in requirements:
            requirements.remove(HYPEN_e_DOT)
    return requirements


    


setup(
    name='ML-Project',
    author='Akshya Sahu',
    version='0.0.0.1',
    author_email='aks.thespy21@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)