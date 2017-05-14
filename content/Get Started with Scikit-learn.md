Title: Notes on Installing the Development Version of Scikit-learn
Date: 20161002 15:00
tags: scikit-learn

I'm trying to install the development version of scikit-learn on Windows 7. Here's some notes. 

**About setup.py**

In short, python _Distutils_ is responsible for both packaging/distributing packages and installing packages. Document says: First, both developers and installers have the same basic user interface, i.e. the setup script. The difference is which Distutils commands they use: the `sdist` command is almost exclusive for module developers, while `install` is more often for installers. 

The core function in the setup script (setup.py by convention) is the `setup` module in `distutils.core`. In the script, developers call this function with many arguments which represent different parameters or goals. `sdist` will create an archive file (e.g., tarball on Unix, ZIP file on Windows) containing the setup script and the functional modules. For users to install packages, they only need to download and unzip, then use `install` to complete installation by copying modules to the appropriate directory in python installation. 

For development version of a package like scikit-learn, we can install it in two ways, one is to add the scikit-learn directory to `PYTHONPATH` and run `python setup.py build_ext --inplace`, the other is to run `python setup.py develop` directly. Basically they are similar, `develop` calls `build_ext -i` implicitly and creates a link from the staging area (by default the site-packages dir) to the scikit-learn dir and also does a little more. The `develop` mode is more convenient for virtualenv. Some references: [setuptools document](https://pythonhosted.org/setuptools/setuptools.html#develop-deploy-the-project-source-in-development-mode), [scikit-learn document](http://scikit-learn.org/stable/developers/contributing.html#retrieving-the-latest-code) and [a question in stackoverflow](http://stackoverflow.com/questions/34408734/whats-the-advantage-of-building-extensions-inplace-when-installing-scikit-learn/34415373). Notice that _Setuptools_ is a collection of enhancements to Distutils, it can be viewed as a superset of Distutils. The setup.py file of scikit-learn tries the setup function first in Setuptools. 

**The rough process of installing**

1. Prepare the complier. This is for the `python setup.py` commands. The MS official VC for python 2.7 doesn't work well on my computer. After searching on web, I got things done with following steps, copied from [this link](http://stackoverflow.com/questions/13596407/errors-while-building-installing-c-module-for-python-2-7/19915585#19915585):  

    * Install the [Visual C++ 2008 Express Edition](https://go.microsoft.com/?linkid=7729279)
		* Here comes another issue: this VC is free but needs registration, however the registration webpage doesn't work any more. So we have to do some hacking to register. This link is the [instruction](http://stackoverflow.com/questions/4422745/how-do-i-get-the-serial-key-for-visual-studio-express/30540370#30540370), basically just delete the relevant term in registry. 
	* Install the Microsoft Windows SDK for Windows Server 2008 and .NET Framework 3.5, which can be found [here](https://www.microsoft.com/en-us/download/details.aspx?id=24826). 
	* To verify the installation, confirm that the Microsoft SDK contains the "amd64" version of the C/C++ compiler "cl.exe". This is usually installed into 
	
			C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\bin\amd64\cl.exe
	
	* copy .../VC/bin/vcvars64.bat to .../VC/bin/vcvarsamd64.bat  
	* copy .../VC/bin/vcvars64.bat to .../VC/bin/amd64/vcvarsamd64.bat

1. Create an account on GitHub.

1. Fork the [project repository](http://github.com/scikit-learn/scikit-learn): click on the `Fork` button near the top of the page. This creates a copy of the code under my account on the GitHub server.

1. Clone this copy to my local disk:

		git clone https://github.com/MyAccount/scikit-learn.git
	
1. Get into the specific virtualenv: go to the virtualenv directory, then

		activate
	For virtualenv, refer to [the documents](https://virtualenv.readthedocs.org/en/latest/userguide.html). I used the `--system-site-packages` option.  
	We are in the virtualenv now.
	
1. Get into the scikit-learn directory which contains setup.py, then

		python setup.py develop
	Don't forget the starting command `python`. Otherwise this line can still run but the virtualenv won't work. 

1. Now the installing is done. For Pycharm users, when creating a new project, we need to choose the interpreter in the virtualenv. Refer to [this link](https://www.jetbrains.com/pycharm/help/adding-existing-virtual-environment.html).




