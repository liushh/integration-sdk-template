from setuptools import setup


setup(name='sdk',
      version='0.1',
      description='The best integration sdk template',
      url='https://github.com/liushh/integration-sdk-template.git',
      author='Liusha',
      author_email='hlswh1021@gmail.com',
      license='MIT',
      packages=['sdk'],
      install_requires=[
          'PyJWT',
      ],
      zip_safe=False)
