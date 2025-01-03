# __build__.py

from setuptools import setup, find_packages

setup(
    name='PySafeVault',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'pysafevault=pysafevault.main:main',
        ],
    },
    author='AlexGRDev',
    author_email='alexgaro2015@gmail.com',
    description='Gestor de contraseñas seguro',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
