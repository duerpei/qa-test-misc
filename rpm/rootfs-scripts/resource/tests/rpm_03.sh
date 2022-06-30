#!/bin/sh

#  The testscript checks the following options of the command file
#  1) Option qi

test="rpm03"
test_manual="test-manual-1.2.3.noarch"

if rpm -qi $test_manual | grep ".*1.2.3.*"
then
    echo " -> $test: TEST-PASS"
else
    echo " -> $test: TEST-FAIL"
fi;
