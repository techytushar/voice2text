import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(name='voice2text',
      description='Better and Smarter way to convert speech to text.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      version='0.1',
      url='https://github.com/techytushar/voice2text',
      author='Tushar Mittal',
      author_email='chiragmittal.mittal@gmail.com',
      license='GNU General Public License v3 (GPLv3)',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3'
      ],
      keywords='speech api python voice machine learning deep learning nlp',
      packages=setuptools.find_packages(),
      install_requires=[
          'nltk',
          'SpeechRecognition'
      ],
      python_requires='>=3.6'
)
