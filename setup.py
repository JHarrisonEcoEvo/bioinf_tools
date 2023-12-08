from setuptools import setup, find_packages

setup(
    name='bioinf_tools',
    version='0.1.0',
    description='Simple tools to do routine bioinformatics tasks',
    url='https://github.com/JHarrisonEcoEvo/bioinf_tools',
    author='Joshua Harrison',
    license='WTFPL',
    packages=find_packages(),
    install_requires=['click',
                      'pytest-warnings',
                      'numpy',
                      'pandas'
                      ],
    entry_points={
        'console_scripts': [
            'count_nuc = seq_tools.nucleotide_counter:main',
            'rev_comp = seq_tools.rev_complement:main',
        ],
    },
)