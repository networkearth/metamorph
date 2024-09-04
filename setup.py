from setuptools import setup, find_packages

setup(
    name='metamorph',
    version='0.0.1',
    author='Marcel Gietzmann-Sanders',
    author_email='marcelsanders96@gmail.com',
    packages=find_packages(include=['metamorph', 'metamorph*', 'transforms', 'transforms*']),
    install_requires=[
        'click==8.1.7',
    ]
)