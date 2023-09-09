from typing import List
from setuptools import find_packages, setup


def get_requirements(file_path: str) -> List[str]:
    # this function will return the list of requirements

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]

    return requirements


setup(
    name="mlProjects",
    version="0.1",
    author="Arman Habib",
    author_email="armanhabibmain@gmail.com",
    packages=find_packages(),
    install_require=['numpy', 'pandas']

)