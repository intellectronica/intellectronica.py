from setuptools import setup, find_packages

setup(
    name='intellectronica',
    version='0.1.202407111800',
    author='Eleanor Berger',
    author_email='eleanor@intellectronica.net',
    description="Eleanor's Python Package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/intellectronica/intellectronica.py',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[],
)