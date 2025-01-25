from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    ''' This will return the list of requirements '''
    HYPEN_E_DOT = '-e .'
    with open(file_path) as file_obj:
        # Read the file into a list of stripped strings
        requirements = [
            req.strip()
            for req in file_obj.readlines()
            if req.strip()  # Exclude empty lines/spaces
        ]
        # Remove '-e .' if present in the list
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


    # the code below did not work because: e issue with your setup.py script is that you're using a generator expression
    # (req.replace("\n","") for req in requirements)
    #  for requirements, and then attempting to call .remove() on it. However,
    #  generators don’t support operations like .remove() because they are lazy iterables, not lists.

    # requirements=[]
    # with open(file_path) as file_obj:
    #     requirements=file_obj.readlines()
    #     requirements=(req.replace("\n","") for req in requirements)
    #     HYPEN_E_DOT='-e .'
    #     if HYPEN_E_DOT in requirements:
    #         requirements.remove(HYPEN_E_DOT)
        
    #     return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Neeharika Jugran',
    author_email='neeharikajugran@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')    

)
