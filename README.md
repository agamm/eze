# eze

![Work in progress](https://img.shields.io/badge/-Work%20in%20progress-orange)
![Versions](https://img.shields.io/pypi/pyversions/eze)
![MIT](https://img.shields.io/pypi/l/eze)

A super simple library for common tasks in python 3. 
- **No extra dependencies** required, you can go use `eze.py`and that's it!
- Great for scripting something fast.
- You are free to copy implementations for specific functions (see `get_eze`).
- Qucik debbugging functions (see `Runtime` and `Printing things`)

## TODO:
- add examples for each function, and a link to the implementation for usage outside of the lib.

## Usage
`pip install eze`  

`import eze as e`

### Strings / JSON & CSV
- `b64` - base 64 encodes to a string (no bytes needed!)
- `b64d` - base 64 decodes a string/byte
- `s` - to string
- `b` - to bytes
- `regex` - match
```Example
match = e.regex(r'hello (.*?)', 'hello world') # (' world', (' world'))
```
- `json` - json encode 
- `jsond` - json decode
- `csv` - dict/list to csv
- `csvd` - decode a csv file/string into a dict.

### IO
- `write` - write something to a file
- `read` - read something from a file

### Runtime
- `eq` - checks if two vars/objects/classes are the same in-memory (might be used for something else)
- `stack` - gets the stack up to here in a human-readable fashion.
- `dir` - shows all of the inherited functions of an object (no need to see `__init_subclass__`)
- `break` - poor man's breakpoint - will exit and print the current variables in a human-readable fashion.
- `@timeit` decorator - prints the seconds it took to run a function.
- `get_time` - returns the seconds it took to run a function.

### Printing things
- `pp`/`pretty_print` - pretty print objects/classes/functions.
- `nl`/`new_line` - create a new line string for terminal usage
- `tbl`/`table` - create an ascii table and print it out of lists/generators.
- `diff` - show the difference between vars/functions/classes/objects can also be colored.

### Imports
- `import_all` - imports the whole directory - good for `__init__.py`
- `import` - imports a python file during runtime
```Example
module = input('What module do you want?')
e.import(module)
# Use `module` functions
```
- `show_loaded` - shows the currently loaded modules.

### Web
- `get` - GET request to a URL.

### Concurrency 
- `together` - run a function concurrently.
```Example
def fetch_that(url):
  print(requests.get(url).text)
 
# together executes 
e.together(fetch_that, ['https://google.com', 'https://facebook.com'], {
  'tasks': 4,
  'done': done_callback
})
```

### Misc
- `get_eze` - prints out the implementation of a function here for production usage (without extra eze code).
- `disable` - disables all of velocity's functions - for production usage.
