#!/bin/sh

#  The testscript checks the following options of the command file
#  1) Option ql

test="rpm02"
test_manual="test-manual-1.2.3.noarch"

if rpm -qa | grep $test_manual
then
    rpm -e $test_manual
fi

rpm -ivh ${test_manual}.rpm --nodeps

if rpm -ql $test_manual | grep '.*/home/test/rpm-test/text1.txt.*'
then
    echo " -> $test: TEST-PASS"
else
    echo " -> $test: TEST-FAIL"
fi;
