from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='keitaro',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    package_data={
        '': ['*.py']
    },
    author='Alex Malykh',
    author_email='alexeyheather@gmail.com',
    description='Unofficial Keitaro Admin API client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ysomad/keitaro',
    keywords='python python3 api-client requests api-wrapper keitaro keitaro-tracker',
    project_urls={
        'Source Code': 'https://github.com/ysomad/keitaropy/tree/master/keitaro',
        'Documentation': 'https://github.com/ysomad/keitaro#-getting-started',
        'Keitaro Admin API Documentation': 'https://admin-api.docs.keitaro.io/'
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    tests_require=['pytest']
)
