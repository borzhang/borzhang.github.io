Title: Procedure of Blogging with Pelican and Github on Windows
Date: 20161002 14:45
tags: pelican

First of all, writting this note highly depends on [a tutorial](https://spapas.github.io/2013/10/07/pelican-static-windows/). Many thanks to the author.

**The Pelican Part**

1. If you are writing articles with markdown, namely your blog article files are ended with `.md`, then you need to install `markdown` package in addition to `pelican`, 
namely `pip install pelican markdown`, otherwise your articles cannot be identified. 

1. Create directory `username.github.io` (main directory) under your working directory.

1. Under `username.github.io\` run `cmd`, then `pelican-quickstart`. 
Answer a bunch of questions, note that url is `username.github.io`. 
Then there will be several dirs/files created in current directory.

1. Under `content` directory, edit your article, say `test.md`. 
Notice that you should at least add the meta data `Title: the article title` at the head of file. 
`Date` is also required, or adding the following lines to `pelicanconf.py`:

        DEFAULT_DATE = 'fs'
        DATE_FORMATS = {
            'en': ('usa','%a, %d %b %Y'),
        }

1. Pick a theme. I chose `pelican-boostrap3`. 
Just find it on internet and `git clone` it as a folder nearby the main directory, then add 

        THEME = "../pelican-bootstrap3"
in `pelicanconf.py`.

1. Back to main directory. 
Run the `pelican` command to generate your site:

        pelican content
Or instead create a bat file, say, `pelrun.bat`:

        pelican content --debug --autoreload  --output output --settings pelicanconf.py
Then run `start pelrun.bat`. 
That will genereate your site to `output`.
Don't cut down this bat command, because it's in debug mode.

1. Get into `output` then run `python -m pelican.server` to preview your site.
Or instead create another bat file, say, `pelserve.bat`:

        pushd output
        python -m pelican.server
        popd
Then run `start pelserve.bat`.
You can preview the site through [http://localhost:8000/](http://localhost:8000/), and you can even dynamically update it if you use the bat files above.

1. Actually the basic process of blogging involving the content is done. 
After editting and debugging, you may want a final version to be published. 
Back to main directory. 
There's a subtle part of the configuration file `publishconf.py`:

        SITEURL = 'https://username.github.io'
        RELATIVE_URLS = False
`RELATIVE_URLS` needs to be `False` and `SITEURL` needs to be started with `https://`, otherwise problems may appear, especially with Disqus.
Create another bat file, say, `pelpub.bat`:

        pelican content --output output --settings publishconf.py
Notice here we use a different configuration file where some publishing information stored. 
Notice that `from pelicanconf import *` has been added in that conf file.

1. In order to print math formula, you need a plugin named `render_math`. 
I also added a plugin named `summary` whose function I really cannot remember.
Download and configure them just like themes:

        PLUGIN_PATHS = ['../pelican-plugins']
        PLUGINS = ['summary', 
                    'render_math',
                    'tag_cloud',
                    ]
Notice that `tag_cloud` is used together with 

        DISPLAY_TAGS_ON_SIDEBAR = True
        DISPLAY_TAGS_INLINE = True
in the special case that pelican-bootstrap3 theme is used.
Refer to [the readme of this theme](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3). 
I prefer to use tags than catagories.
Btw, for this very theme, set 

        DISPLAY_ARTICLE_INFO_ON_INDEX = True
to display date and tags info on the default index page.

1. There's other terms and options in `pelicanconf.py` including links and social. 
You should refer to the official site of pelican as well as readme of the theme you are using.

1. To add comment function, add following line in `publishconf.py`:

        DISQUS_SITENAME = "username"
Of course you have to resgister a Disqus account. 
Just sign up then "get started" and input your site url.







**The Github Part**

1. Create a repository on github, refer to [the site of github pages](https://pages.github.com/), only the first step is enough. 
The name will be `username.github.io`.

1. My strategy of building blog on github is like this: 
There're two branches in the remote origin: 
one is master, which contains the real website stuff, the other is source, which contains the source code. 
Accordingly, there should be two branches in local repo, but `output` is a subdirectory under main directory, it's hard to arrange one single local repo because of that file structure. 
So it's reasonable to create two local repos pointing to the same remote repo `origin`, one corresponding to `origin/master` branch, the other with `origin/source` branch. 
The git procedure will first push the website to remote, then push the source (acutally the order does not matter). 

1. Get into `output` first.
Initialize the site repo, namely `output`. 
Then connect to remote repo `origin`, push your site to it. 
Your local branch (the unique branch you have in this local repo) `master` will be copied to `origin/master` branch.

        git init
        git add .
        git commit -m Initial
        git remote add origin https://github.com/username/username.github.io.git
        git push origin master --force
Now you can visit you blog on http://username.github.io. 

1. Back to main directory. 
In order to get the source code to cloud, you can push the whole source to github, though a non-master branch. 
Then the url username.github.io still corresponds to `origin/master`, namely your site files, but you also have the source code hiding in another branch.
First add a `.gitignore` file in main directory:

        output
        cache
        *.pyc
Then do all the git procedure:

        git init
        git add .
        git commit -m Initial
        git branch -m master source
        git remote add origin https://github.com/username/username.github.io.git
        git push origin source
An `origin/source` branch will be created afterwards.




**Sync the blog with a new computer**

1. If you are going to another place with another computer, then you need to sync the blog to your new computer. 
The intuitive method is `git clone`:

        git clone https://github.com/username/username.github.io.git
Then a directory `username.github.io` will be built in your current path. 
But it seems to include only the `output` content, namely the `remote/master` branch. 
Actually everything has been downloaded, as the word clone means, but only `master` branch appears by default. 
You can check all downloaded branches by `git branch -a`.
Now you need to first switch to `source` branch, by creating a new branch with a same name in your local `origin` repo:

        git checkout -b source origin/source
Then the content in the main directory will be the `source` branch. 
Now you can just delete `.git` file to completely get rid of git structure. 
We will construct a same structure as in the original computer later.

1. As the actions mentioned previously, use those batch processing files to generate and edit blog articles and publish them:

		start pelrun.bat
		start pelserve.bat
		start pelpub.bat

1. Then just do the same thing as previous github part: in the `output` directory, 

        git init
        git add .
        git commit -m "your message"
        git remote add origin https://github.com/username/username.github.io.git
        git push origin master --force
And in the main directory, 

        git init
        git add . 
        git commit -m "your message"
        git branch -m master source
        git remote add origin https://github.com/username/username.github.io.git
        git push origin source 

