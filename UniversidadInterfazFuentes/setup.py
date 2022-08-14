from setuptools import setup
from setuptools import find_packages

setup(name='universidad',
      version='0.1',
      description='Proyecto Complejidad y Optimización, Escuela de Ingeniería de Sistemas y Computación',
      url='https://github.com/nijamaDev/Universidad-GUIFuentes',
      author='nijama, Git-Fanfo, SJMC29, learningalone',
      license='MIT',
      packages=find_packages(),
      package_data={p: ["*"] for p in find_packages()},
      install_requires=[
          'PySimpleGUIQt',
      ],
      zip_safe=False
      )
