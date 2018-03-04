# api-wordlist-generator
Simple Python script and shell script to utilize public resources to generate wordlists of methods/functions/variables. Uses the excellent AST parsing Python package as well as the simpler shell utils method

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

## Notes

This is just a simple, quick and dirty way to do this. There are many better ways. But this one is mine :>

This only finds functions in files with valid AST that the AST package can parse. Via some regex and some shell utils it's relatively easy to find class methods and other things. Try that out, it isn't terribly difficult, something like this works well:

```
$ find . -name \*.py -exec grep -Eo ' *def (.*) *\(' {} \; | sed -e 's/^ *def *//g' | cut -d '(' -f 1 | grep -v '^_' | grep -E -v '[=,\{}]' > funcs.lst
```

## License

3-clause BSD license, (C) 2018, copyright /at/ mzpqnxow.com

