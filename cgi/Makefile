FLAGS=
FLAGS_MOD=-O2 -fPIC -I/usr/include/python2.7

.PHONY=clean module

# --------------------------------------------------------
# make module
# --------------------------------------------------------

module: _dummy.so

_dummy.so: dummy.o dummy_wrap.o
	gcc -shared $^ -o $@

# This one doesnt have a .h, so we need a specific rule
dummy_wrap.o: dummy_wrap.c
	gcc $(FLAGS_MOD) -c $<

%.o: %.c %.h
	gcc $(FLAGS_MOD) -c $<

dummy_wrap.c: dummy.i
	swig -python -o dummy_wrap.c dummy.i

clean:
	rm -f *.o *.so
