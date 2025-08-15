from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
    name="AI Travel Planner",
    version="0.1",
    author="Prince Gupta",
    packages=find_packages(),
    install_requires=requirements,
    
)