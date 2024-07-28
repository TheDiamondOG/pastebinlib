from setuptools import setup, find_packages

setup(
    name='pastebinlib',
    version='1.1.1',
    packages=find_packages(),
    install_requires=['requests'],
    description='This is a library for accessing pastebin easily. Also pastelib was already taken',
long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='TheDiamondOG',
    author_email='thediamondogness@gmail.com',
    url='https://github.com/thediamondog/pastelib',
)