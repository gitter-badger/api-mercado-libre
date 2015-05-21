from setuptools import setup

setup(name='mercado-libre',
      version='0.1',
      description='Simple mercado libre API for python',
      url='https://github.com/hudsonbrendon/api-mercado-libre',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['mercado-libre'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
