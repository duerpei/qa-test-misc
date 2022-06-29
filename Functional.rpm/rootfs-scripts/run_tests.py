import pytest
import os
import sys
import json

sys.path.append("/usr/AGL/agl-test/plugins")
import agl_test_conf
import agl_test_log
import agl_test_utils

import rpm.parser as parser
import rpm.report as report

WORK_DIR = agl_test_conf.WORK_DIR
TMP_LOGS_DIR = agl_test_conf.TMP_LOGS_DIR

THIS_TEST = "rpm"
test_cases_values_and_status = []

def setup_module():
    agl_test_utils.find_cmd("rpm")
    agl_test_utils.create_dir(THIS_TEST)
    run_test_fun()
    global test_cases_values_and_status
    test_cases_values_and_status = parser.log_process(TMP_LOGS_DIR,THIS_TEST)

#Run test, and redirect the log into the file of THIS_TEST.log  under TMP_LOGS_DIR/THIS_TEST/
def run_test_fun():
    cmdline = "cd " + WORK_DIR + THIS_TEST + "/resource/" + ";" + "sh rpm_test.sh > " + TMP_LOGS_DIR + THIS_TEST + "/log/" + THIS_TEST + ".log" + " 2>&1 "
    output = os.popen(cmdline)
    assert str(type(output)) == "<class 'os._wrap_close'>"
    output.close()

def test_rpm01():
    global test_cases_values_and_status
    assert test_cases_values_and_status[1][1] == "TEST-PASS"
    test_cases_values_and_status[1][2] = "passed"

def test_rpm02():
    global test_cases_values_and_status
    assert test_cases_values_and_status[2][1] == "TEST-PASS"
    test_cases_values_and_status[2][2] = "passed"

def test_rpm03():
    global test_cases_values_and_status
    assert test_cases_values_and_status[3][1] == "TEST-PASS"
    test_cases_values_and_status[3][2] = "passed"

#Pack the log file and count the test results
def teardown_module():
    report.log_report(test_cases_values_and_status,THIS_TEST)


if __name__ == '__main__':
    pytest.main("-s run_tests")
