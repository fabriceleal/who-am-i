# who-am-i

Simple Python CGI script that prints some system information and tests a native module. 

Almost a pythoninfo(). Almost.

## Ugly hacks to make this work on x86_64

* 1. on  `...\include\python2.7\pyport.h`, comment like 849 (should be `#error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."`)
* 2. 