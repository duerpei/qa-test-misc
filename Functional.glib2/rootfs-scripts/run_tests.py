import pytest
import os
import sys
import json

sys.path.append("/usr/AGL/agl-test/plugins/")
import agl_test_conf
import agl_test_log
import agl_test_utils

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
    #
    #   to do:
    #        run the test by gnome
    #
    cmdline = "cd " + WORK_DIR + THIS_TEST + "/resource/glib2-test/glib-2.46.2/bin_porter/tests" + ";" + "sh glib2_test.sh > " + TMP_LOGS_DIR + THIS_TEST + "/log/" + THIS_TEST + ".log" + " 2>&1 "
    output = os.popen(cmdline)
    assert str(type(output)) == "<class 'os._wrap_close'>"
    output.close()

def test_glib2():
    global test_cases_values_and_status
    for l in test_cases_values_and_status:
        if(l[1] == "PASS"):
            l[2] = "passed"
        if(l[1] == "FAIL"):
            l[2] = "failed"

#Pack the log file and count the test results
def teardown_module():
    report.log_report(test_cases_values_and_status,THIS_TEST)

if __name__ == '__main__':
    pytest.main("run_tests")
