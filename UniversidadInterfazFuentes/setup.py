from setuptools import setup
from setuptools import find_packages

setup(name='universidad',
      version='1.0',
      description='Proyecto Complejidad y Optimización, Escuela de Ingeniería de Sistemas y Computación',
      url='https://github.com/nijamaDev/Universidad-GUIFuentes',
      author='nijama, Git-Fanfo, SJMC29, AlejoCx2',
      license='MIT',
      packages=find_packages(),
      package_data={p: ["*"] for p in find_packages()},
      install_requires=[
          'PySimpleGUIQt',
          'minizinc',
      ],
      zip_safe=False
      )
