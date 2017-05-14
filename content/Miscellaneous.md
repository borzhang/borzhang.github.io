Title: Miscellaneous
Date: 20161002
tags: tips


**About Git, mintty, and Console**

The official [Git for Windows](https://git-scm.com/download/win) uses [mintty](https://mintty.github.io/) as the terminal by default. 
Mintty is [a quite good console for general use on windows](https://chadaustin.me/2009/10/reasons-why-mintty-is-the-best-terminal-on-windows/), 
it's used as a part of Cygwin, Msys or Msys2. It can be install with Cygwin or Mingw. 
If you directly install mintty from Cygwin or Mingw, then there's quite a few things to do in the future, especially in the case you need 
other languages than English, say, in the case of Chinese, you may need to refer to [this article](https://jerry2yang.wordpress.com/2011/08/30/mintty-%E5%8F%AF%E4%BB%A5%E5%9C%A8windows-%E4%BD%9C%E6%A5%AD%E7%B3%BB%E7%B5%B1%E4%B8%8A%E9%81%8B%E8%A1%8C%E9%9D%9E%E5%B8%B8%E4%B8%8D%E9%8C%AF%E7%9A%84console/). 
And the main problems with mintty are in total two: the look and the interactive property. 
The first one can be tackled easily. 
The main idea of both Cygwin and Mingw is making a virtual directory structure as Linux including `/bin`, `/etc`, `/doc` and so on. 
And you can just create a file in you home directory as `.bashrc` or `.vimrc` in Linux, named `.minttyrc`, containing info about the font and color settings. 
Refer to [this link](http://ciembor.github.io/4bit/#) for the color settings and [this link](https://www.trueneutral.eu/2014/win-proper-term.html) for fonts.
But the second one cannot be tackled perfectly as far as I know. 
It means that you cannot use mintty as an alternative of the Windows command line to run Python interactive interface, because it cannot respond you correctly. 

The best choice to install mintty, if your original goal is just to use Git Bash, is to install the official Git for Windows. 
It includes a Mingw environment itself, and must with customization as much as possible against the interactive problem. 
So at least some basic operation of Git can be done with it. 
If you are not satisfied with the color/font settings, just modify it using the trick mentioned above. 

But I still found some problems with mintty bounding with Git Bash in terms of interaction. 
My best practice is using an alternative of Windows command line named [Console](http://www.hanselman.com/blog/Console2ABetterWindowsCommandPrompt.aspx). 
After customization on color schemes, it can be quite convenient, I can use it smoothly with Python virtualenv and Git. 
The only con is that there's no reminder indicating which branch you are in currently. 
I prefer it anyway. 

**About virtualenv**

The best references are [the Hitchhiker's Guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and 
[the official document](https://virtualenv.readthedocs.io/en/latest/userguide/). 
The former is preferred for a quick glance. 
And another trick is to avoid installing packages in non-virtual environment, which can be done by 
editing (creating) `%HOME%/pip/pip.ini` with following lines:

		[global]
		require-virtualenv = true
For all operating systems, refer to [the Hitchhiker's Guide](http://docs.python-guide.org/en/latest/dev/pip-virtualenv/). 
By the way, the default value of variable `%HOME%` on Windows is `C:\users\yourname\`, at least in my case. 
All configuration files should be put there, such as `.vimrc` and `.minttyrc`. 


**About Kile on Windows**

First install Tex live, just google and run the installer. It takes quite a long time.
At the same time, download the [installer of KDE for Windows](http://download.kde.org/stable/kdewin/installer/kdewin-installer-gui-latest.exe.mirrorlist). Here's [a reference](http://kile.sourceforge.net/wiki/index.php?title=KileOnWindows).


**About Intel MKL, numpy and others**

Intel MKL has been released for free again, you can find it on the official website. 
I tried to follow [this guide](https://software.intel.com/en-us/articles/building-numpyscipy-with-intel-mkl-and-intel-fortran-on-windows) to build manually numpy with Intel MKL, but failed for unknown reason. 
I was told that I'd better install Intel python. Refer to [my post](https://software.intel.com/en-us/comment/1886592#comment-1886592) on Intel MKL forum. 
Intel python is a standalone python distribution including everything related to science computation installed. 
You can install it, activate it, then install virtualenv with pip, in order to create virtual environments under this distribution. 
To install development version of scikit-learn, just uninstall scikit-learn first, then create a virtual env, follow [this note](./notes-of-installing-the-development-version-of-scikit-learn.html).