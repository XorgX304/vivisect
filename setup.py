from setuptools import setup, find_packages
from os import path

dirn = path.abspath(path.dirname(__file__))
with open(path.join(dirn, 'README.md'), 'r') as fd:
    desc = fd.read()

setup(
    name='vivisect',
    author='',
    author_email='',
    version='v0.0.20200804',
    url='https://github.com/vivisect/vivisect',
    description='Pure python disassembler, debugger, emulator, and static analysis framework',
    long_description=desc,
    long_description_content_type='text/markdown',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.dll', '*.dylib', '*.lyt', 'Makefile', '*.c', '*.h', '*.yes', '*.sh']
    },
    package_data={
        '': ['*.dll', '*.dylib', '*.yes', '*.cfg', '*.lyt',
             '*.c', '*.h', 'Makefile',],
        },
    entry_points={
        "console_scripts": [
            "vivbin=vivisect.vivbin:main",
            "vdbbin=vdb.vdbbin:main",
        ]
    },
    install_requires=[
        'pyasn1==0.4.5',
        'pyasn1-modules==0.2.4',
        'cxxfilt==0.2.1',
        'msgpack==1.0.0',
        'pycparser==2.20',
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2'
        'Topic :: Security',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Disassemblers',
    ]
    python_requires='<3',
)
