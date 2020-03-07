# How to write/compile/run C/C++ code in Linux

## Write

First of all, writing code is quite straightforward, and my personal recommended editor would be [Visual Studio Code](https://code.visualstudio.com/), which is a open source editor produced by Microsoft. It retains almost all the debug ability from its predecessor, Visual Studio, a very commonly used IDE across the universe. 

## Compile

Simply use ```gcc``` or ```g++``` to compile the C/C++ code:

```
gcc/g++ program-source-code.c -o execute-file-name
```

OR

```
gcc/g++ -o execute-file-name program-source-code.c
```

When the executable-file-name.c exists, we can just use

```
make executable-file-name
```

## Run

After compilation and when the executable file is produced, simply run the executable file by

```
./execute-file-name
```

## ```gcc``` vs ```g++```

```gcc``` and ```g++``` are compiler-drivers of the GNU Compiler Collection.

* ```gcc```: GNU C Compiler
* ```g++```: GNU C++ Compiler

The most important difference in their defaults is which libraries they link against automatically.

According to GCC's online documentation link options and how g++ is invoked, ```g++``` is equivalent to ```gcc -xc++ -lstdc++ -shared-libgcc```. In other words, ```g++``` will automatically link the standard C++ libraries (while gcc does not do so).

In addition, ```gcc``` will compile *.c and *.cpp files as C and C++ respectively. ```g++``` will compile *.c and *.cpp files but they will all be treated as C++ files.

## Reference:

1. https://www.cyberciti.biz/faq/howto-compile-and-run-c-cplusplus-code-in-linux/
2. https://stackoverflow.com/questions/172587/what-is-the-difference-between-g-and-gcc
