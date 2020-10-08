from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='keitaropy',
    version='0.1.6',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    package_data={
        '': ['*.py']
    },
    author='Alex Malykh',
    author_email='alexeyheather@gmail.com',
    description='Simple and easy to use API wrapper library for Keitaro Admin API written in Python3 and requests',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Infvmous/keitaropy',
    keywords='keitaro api requests api-wrapper api-client python python3 admin-api',
    project_urls={
        'Source Code': 'https://github.com/Infvmous/keitaropy/tree/master/keitaropy',
        'Documentation': 'https://github.com/Infvmous/keitaropy#-getting-started',
        'Keitaro Admin API Documentation': 'https://admin-api.docs.keitaro.io/'
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=6.1.1'],
    test_suite='tests',
)