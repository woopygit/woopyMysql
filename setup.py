from setuptools import setup, find_packages

setup(
    name='woopyMysql',
    version='0.1',
    author='Pigi - WpPy.net',
    author_email='woopygit@icloud.com',
    description='Simple class to manage multiple Mysql Db with mysql-connector-python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://www.wppy.net/woopy-mysql-connector',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6, <3.13',
    install_requires=[
        'mysql-connector-python',
        'python-dotenv'
    ],
)