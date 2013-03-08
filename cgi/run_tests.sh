#!/bin/bash

echo "You'll need to install the package python-profiler"

python -m cProfile call_py.py 
python -m cProfile call_native.py 