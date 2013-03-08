%module dummy

%{
#define SWIG_FILE_WITH_INIT 1
#include "dummy.h"
%}


char* hello_world(int times);
