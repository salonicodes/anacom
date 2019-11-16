from distutils.core import setup
setup(
  name = 'anacom',         # How you named your package folder (MyLib)
  packages = ['anacom'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An Introductory Python Toolbox for Analog Communication',   # Give a short description about your library
  author = 'Saloni Tripathi, Bhaskar Tak, Govind Sisodia, Aditi Bambodi',                   # Type in your name
  author_email = 'engineersaloni@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/salonicodes/anacom',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/salonicodes/mylib/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Analog Communication', 'Modulation', 'Fourier'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'sympy',
    'matplotlib','numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: gpl-3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)