# api-wordlist-generator
Simple Python script and shell script to utilize public resources to generate wordlists of methods/functions/variables. Uses the excellent AST parsing Python package

## Usage

First, build and activate the virtual environment

```
$ make
$ source venv/bin/activate
```

Now, try this, assuming you have a project containing Python files in ~/Zope:

```
$ ./wrapper.sh ~/Zope/ | sort -u > wordlist.lst
```

## Usage against pip installed packages in the built-in virtualenv

```
$ make
$ source venv/bin/activate
$ pip install <some/framework/or/app>
$ ./wrapper.sh venv/lib/python2.7/site-packages/ | sort -u > worlist.out
```

## License

3-clause BSD license, (C) copyright /at/ mzpqnxow.com
