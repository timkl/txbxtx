from setuptools import setup


setup(
    name='txbxtx',
    version='1.0',
    py_modules=['app'],
    install_requires=[
        'Click',
        'gtts',
        'pydub'
    ],
    entry_points='''
        [console_scripts]
        txbxtx=app:cli
    '''

)
