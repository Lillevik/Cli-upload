from setuptools import find_packages, setup
from upl import __version__

setup(
    name='upl',
    version=__version__,
    description='A file upload command line program.',
    url='http://github.com/Lillevik/Cli-upload',
    author='Marius Lillevik',
    license='GNU',
    keywords='cli',
    install_requires=['docopt', 'requests', 'clipboard'],
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'upl=upl.cli:main',
        ],
    }
)
