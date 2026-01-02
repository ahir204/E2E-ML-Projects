from setuptools import find_packages , setup 
from typing import List 

Hypen_E_Dot = '-e .'
def get_Requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements = file_obj.readlines()
        Requirements =  [req.replace("\n"," ") for req in Requirements]
        
        if Hypen_E_Dot in Requirements:
            Requirements.remove(Hypen_E_Dot)
            
    return Requirements
            
setup(
    name = 'KN E2E ML PROJECTS',
    version= '0.0.1',
    author='Chetan',
    author_email='ahirahir204@gmail.com',
    packages=find_packages(),
    install_requires = get_Requirements('Requirements.txt')
    
      )