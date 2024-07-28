from setuptools import setup, find_packages

setup(
    name='pastebinlib',
    version='1.1.1',
    packages=find_packages(),
    install_requires=['requests'],
    description='This is a library for accessing pastebin easly. Also pastelib was token',
long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='TheDiamondOG',
    author_email='thediamondogness@gmail.com',
    url='https://github.com/thediamondog/pastelib',
)