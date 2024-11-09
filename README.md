<p align="center">
  <h1>rPython</h1>
  <p><i>Python</i> Reimagined in <i>Rust</i></p>
  <img src="https://img.shields.io/badge/rPython-Python_Reimagined_in_Rust-yellow?style=for-the-badge" alt="Welcome Badge">
</p>

### `Hello` from `rPython`:
--------------------------

> ### Built with `Rust`, but I’m not the original creator. I’ve borrowed the concept and supercharged it! Currently, I’m working on making this version of `Python` faster than `cPython`. 🚀
> ### Honestly, I wasn’t a fan of `Rust` at first, but this project has made me a believer. Trust me, you’ll love it too! 😎

### Examples:
-------------

# `Repl`

```shell
root@karnal::G:\s-cat\RustPython-main\Release-Version % ./rustpython/rustpython.exe
Welcome to the magnificent Rust Python 0.4.0 interpreter 😱 🖖
RustPython 3.12.0
Please, type "help", "copyright", "credits" or "license" for more information.
>>>>> print("hello rPython")
hello rPython
>>>>> 999.000 + 56387 - 64329 / 563247.5342
57385.885789113854
>>>>> help()

Welcome to Python 3.12's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> exit()
No Python documentation found for 'exit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help>

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>>>> exit()
```

# `Rust` from `rPython`
```python
from rust_py_module import RustStruct, rust_function

class PythonPerson:
    def __init__(self, name):
        self.name = name

def python_callback():
    python_person = PythonPerson("Peter Python")
    rust_object = rust_function(42, "This is a python string", python_person)
    print("Printing member 'numbers' from rust struct: ", rust_object.numbers)
    rust_object.print_in_rust_from_python()

def take_string(string):
    print("Calling python function from rust with string: " + string)

```
