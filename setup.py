try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Vocabulario',
    'author': 'Roberth Marcano',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'marcanoroberth98@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'random','numpy','pandas','datetime','pyttsx3'],
    'packages': ["vocabulario"],
    'scripts': [],
    'name': 'projectname'
}        

setup(**config)
