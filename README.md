# api-wordlist-generator
Simple shellscript to utilize public resources to generate wordlists of methods/functions/variables

## Usage

Try this, assuming you have a project containing Python files in ~/Zope:

```
$ ./wrapper.sh ~/Zope/ | sort -u > wordlist.lst
```
