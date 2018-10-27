#!/bin/sh

# Extracted from: https://stackoverflow.com/questions/47882916/how-to-make-the-shebang-be-able-to-choose-the-correct-python-interpreter-between/47886254#47886254
# Shell commands follow
# Next line is bilingual: it starts a comment in Python, and is a no-op in shell
""":"

# Find a suitable python interpreter (adapt for your specific needs) 
for cmd in python3.5 python3 /opt/myspecialpython/bin/python3.5.99 ; do
   command -v > /dev/null $cmd && exec $cmd $0 "$@"
done

echo "OMG Python not found, exiting!!!!!11!!eleven" >2

exit 2

":"""
# Previous line is bilingual: it ends a comment in Python, and is a no-op in shell
# Shell commands end here
# Python script follows (example commands shown)

import sys
print ("running Python!")
print (sys.argv)
