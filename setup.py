from setuptools import setup


setup(
    name='txbxtx',
    version='1.0',
    py_modules=['txbxtx'],
    install_requires=[
        'Click',
        'gtts',
        'pydub'
    ],
    entry_points='''
        [console_scripts]
        txbxtx=txbxtx:cli
    '''

)
