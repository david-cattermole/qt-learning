from distutils.core import setup

setup(name='qt-learning',
      version='0.1',
      description='Learning project for Qt framework.',
      author='David Cattermole',
      author_email='cattermole91@gmail.com',
      url='https://github.com/david-cattermole/qt-learning',
      license='BSD 3-Clause',
      packages=['qtLearn'],
      package_dir={'': 'python', 'qtLearn': 'python/qtLearn'},
      require=['Qt.py==0.6.9', 'coverage']
)
