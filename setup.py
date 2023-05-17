from setuptools import setup, find_packages

setup(
    name='gpt_code',
    version='0.42.0',
    packages=find_packages(),
    install_requires=[
        'ipykernel>=6,<7',
        'snakemq>=1,<2',
        'requests>=2,<3',
        'Flask>=2,<3',
        'flask-cors>=3,<4',
        'python-dotenv>=1,<2'
    ],
    entry_points={
        'console_scripts': [
            'gptcode = gpt_code.main:main',
        ],
    },
)
