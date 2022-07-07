import pytest
import os
import sys
import json

import plugins.agl_test_conf as agl_test_conf
import plugins.agl_test_log as agl_test_log
import plugins.agl_test_utils as agl_test_utils

import glib2.parser as parser
import glib2.report as report

WORK_DIR = agl_test_conf.WORK_DIR
TMP_LOGS_DIR = agl_test_conf.TMP_LOGS_DIR

THIS_TEST = "glib2"
test_cases_values_and_status = []

def setup_module():
    agl_test_utils.create_dir(THIS_TEST)
    run_test_fun()
    global test_cases_values_and_status
    test_cases_values_and_status = parser.log_process(TMP_LOGS_DIR,THIS_TEST)

#Run test, and redirect the log into the file of THIS_TEST.log  under TMP_LOGS_DIR/THIS_TEST/
def run_test_fun():
    cmdline = "ptest-runner glib-2.0 > " + TMP_LOGS_DIR + THIS_TEST + "/log/" + THIS_TEST + ".log" + " 2>&1 "
    output = os.popen(cmdline)
    assert str(type(output)) == "<class 'os._wrap_close'>"
    output.close()

def check_status(test_name):
    global test_cases_values_and_status
    for item in test_cases_values_and_status:
        if(item[0]==test_name):
            if(item[1] == "PASS"):
                item[2] = "passed"
                return 1
            if(item[1] == "FAIL"):
                item[2] = "failed"
                return 0

def test_glib2_gdbus_names():
    assert check_status("glib/gdbus-names.test")

def test_glib2_rand():
    assert check_status("glib/rand.test")

def test_glib2_base64():
    assert check_status("glib/base64.test")

#TODO
#Complete all test cases

#Pack the log file and count the test results
def teardown_module():
    report.log_report(test_cases_values_and_status,THIS_TEST)

if __name__ == '__main__':
    pytest.main("run_tests")
