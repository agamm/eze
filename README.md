# velocity
Velocity brings your development up to speed with a minimalist set of commonly used functions.

## TODO:
- add examples for each function, and a link to the implementation for usage outside of the lib.

## Usage
`pip install velocity`  

`import velocity as vc`

### Strings
- `b64` - base 64 encodes to a string (no bytes needed!)
- `b64d` - base 64 decodes a string/byte
- `s` - to string
- `b` - to bytes
- `regex` - match
```Example
match = regex(r'hello (.*?)', 'hello world') # (' world', (' world'))
```
- `json` - json encode 
- `jsond` - json decode

### IO
- `write` - write something to a file
- `read` - read something from a file

### Runtime
- `eq` - checks if 2 vars/objects/classes are the same in memeory (might be used for something else)
- `stack` - gets the stack up to here in a human readable fasion.
- `dir` - shows all of the uninhereted functions of an object (no need to see `__init_subclass__`)
- `break` - poorman's break point - will exit and print the current varaibles in a human readable fasion.

### Printing things
- `pp`/`pretty_print` - pretty print objects/classes/functions.
- `nl`/`new_line` - craete a new line string for terminal usage
- `tbl`/`table` - create an ascii table and print it out of lists/generators.
- `diff` - show the difference between vars/functions/classes/objects can also be colored.

### Imports
- `import_all` - imports the whole directory - good for `__init__.py`
- `import` - imports a python file during runtime
```Example
module = input('What module do you want?')
import(module)
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
together(fetch_that, (url for url in ['https://google.com', 'https://facebook.com']), {
  'tasks': 4,
  'done': done_callback
})
```

### Misc
- `disable` - disables all of velocity's functions - for production usage.