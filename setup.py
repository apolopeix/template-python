import io
from setuptools import setup, find_packages


def get_long_description():
    with io.open('README.rst', encoding='utf-8') as f:
        return "%s\n" % (f.read())


def main():
    setup(
        name='template-python-project',
        description='Template python project',
        long_description=get_long_description(),
        url='https://github.com/apolopeix/template-python-project',
        use_scm_version=True,
        license='http://opensource.org/licenses/MIT',
        author='apolopeix',
        author_email='apolopeix@gmail.com',
        package_dir={'': 'src'},
        packages=find_packages('src'),
        setup_requires=['setuptools_scm'],
        extras_require={'testing': ['pytest >= 3.3.0',
                                    'pytest-cov'],
                        'lint': ['flake8 == 3.4.1',
                                 'flake8-bugbear == 17.4.0',
                                 'pre-commit == 1.4.4']},
        classifiers=['Development Status :: 1 - Planning',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Topic :: Software Development :: Libraries']
    )


if __name__ == '__main__':
    main()
