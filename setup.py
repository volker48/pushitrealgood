from setuptools import setup


setup(
    name="pirg",
    version="0.0.2",
    license='MIT',
    url='https://github.com/volker48/pushitrealgood',
    description="Simple push notification",
    author="Marcus McCurdy",
    py_modules=['pirg'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
