from distutils.core import setup

requirements = ['opentele==1.15.1', "aiosqlite==0.17.0", "pyrogram"]

setup(name='tgconvert',
      version='0.0.1',
      description='',
      long_description="",
      long_description_content_type='text/markdown',
      author='',
      author_email='',
      url='',
      packages=['tgconvert', "tgconvert/manager", "tgconvert/manager/sessions"],
      install_requires=requirements,
      classifiers=[
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.9',
      )
