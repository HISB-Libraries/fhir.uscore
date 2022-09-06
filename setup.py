'''Setup file for fhir.uscore package'''
from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ["fhir.resources>=6.4.0", "requests==2.28.1"]

setup(
    name="fhir.uscore",
    version="0.1.2",
    author="Andrew Stevens",
    author_email="andrew.stevens@gtri.gatech.edu",
    description="Model classes for US Core FHIR Resources",
    install_requires=requirements,
    url="https://github.com/SmartChartSuite/fhir.uscore",
    project_urls={
        "Bug Tracker": "https://github.com/SmartChartSuite/fhir.uscore/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Typing :: Typed"
    ],
    packages=find_namespace_packages(include=["fhir*"]),
    python_requires=">=3.6",
)
