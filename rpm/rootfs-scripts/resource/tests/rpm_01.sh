#!/bin/sh

#  The testscript checks the following options of the command file
#  1) Option help

test="rpm01"

if rpm --help | grep .*Usage.*
then
    echo " -> $test: TEST-PASS"
else
    echo " -> $test: TEST-FAIL"
fi;
