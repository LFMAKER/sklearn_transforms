from setuptools import setup


setup(
      name='maratonaibm_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/LFMAKER/sklearn_transforms/',
      author='Leonardo Oliveira',
      author_email='lfmaker@outlook.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      zip_safe=False,
      install_requires=[
            'imbalanced-learn==0.4.2',
      ],
      
)
