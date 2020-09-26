from setuptools import setup


setup(
    name='keitaropy',
    version='0.1',
    packages=['keitaropy'],
    install_requires=[
        'requests'
    ],
    package_data={
        '': ['*.py']
    },
    author='Alex M',
    author_email='alexeyheather@gmail.com',
    description='Python3 library based on Keitaro Admin API',
    url='https://github.com/Infvmous/keitaropy',
    keywords='keitaro admin api requests',
    project_urls={
        'Source Code': 'https://github.com/Infvmous/keitaropy',
        'Documentation': 'https://github.com/Infvmous/keitaropy/blob/master/README.md',
        'Keitaro Admin API Documentation': 'https://admin-api.docs.keitaro.io/'
    },
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]
)