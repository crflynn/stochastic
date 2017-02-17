from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='stochastic',
      version='0.1',
      description='Stochastic process realizations in python.',
      url='http://github.com/crf204/stochastic',
      author='crf204',
      author_email='crf204@gmail.com',
      license='MIT',
      packages=['stochastic'],
      install_requires=[
          'numpy',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
