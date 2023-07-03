# Following this URL: https://www.knowledgehut.com/blog/programming/how-to-publish-python-package-to-pypi
import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE/"README.md").read_text()

setup(
   name="qiskit_debugger", 
   version="0.1.0", 
   descp="Quantum Circuit debugger for the Qiskit SDK.", 
   long_descp=README,
   long_descp_content="text/markdown", 
   URL="https://github.com/salekinsirajus/qiskit_quantum_circuit_debugger", 
   author="Sirajus Salekin", 
   authoremail="ssalekin14@gmail.com", 
   license="MIT", 
   classifiers=[ 
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python :: 3", 
        "Programming Language :: Python :: 3.11", 
   ], 
   packages=["qiskit_debugger"], 
   includepackagedata=True, 
   installrequires=["feedparser","html2text"], 
   entrypoints={ 
       "console_scripts":[ 
           "realpython=reader.__main__:main", 
       ] 
   }, 
 ) 