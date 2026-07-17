from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            line=file.readlines()
            for data in line:
                requirement=data.strip()
                if requirement and requirement!="-e .":
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("file not found in the requiremenst.txt")
    return requirements_list
print(get_requirements())

setup(
    name="NETWORK SECURITY",
    version='0.0.1',
    author='Siddhant',
    author_email='sidcool0311@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)                         