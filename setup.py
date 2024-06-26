from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(path:str)->List[str]:
    req = []
    with open(path) as obj:
        req = obj.readlines()
        req = [x.replace("\n","") for x in req]
        if HYPHEN_E_DOT in req: req.remove(HYPHEN_E_DOT)
    return req


setup(
    name='end to end projs',
    version='0.0.1',
    author='Atul Anant',
    author_email='iamatulanant@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    )