from setuptools import setup


def version():
    with open('pillow_mbm/version.py') as f:
        exec(f.read())
        return __version__


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='pillow-mbm',
    description="A pillow plugin that adds support for KSP's MBM textures",
    version=version(),
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=['Pillow'],
    extras_require={
        'cli': ['click']
    },
    package_dir={'': '.'},
    entry_points='''
        [console_scripts]
        convert-mbm=pillow_mbm.__main__:main [cli]
    ''',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Games/Entertainment :: Simulation',
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
)
