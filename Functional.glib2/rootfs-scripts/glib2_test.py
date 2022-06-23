import pytest
import os
import sys
import json

sys.path.append("/usr/AGL/agl-test/plugins/")
import agl_test_dir_conf
import agl_test_log
import agl_test_utils

import glib2_parser
import glib2_report

WORK_DIR = agl_test_dir_conf.WORK_DIR
TMP_LOGS_DIR = agl_test_dir_conf.TMP_LOGS_DIR
#REPORT_LOGS_DIR =agl_test_dir_conf.REPORT_LOGS_DIR

THIS_TEST = "Functional.glib2"
test_cases_values_and_status = []

def setup_module():
    agl_test_utils.clean_env(THIS_TEST)
    run_test_fun()
    global test_cases_values_and_status
    test_cases_values_and_status = glib2_parser.log_process(TMP_LOGS_DIR,THIS_TEST)
#Run test, and redirect the log into the file of THIS_TEST.log  under TMP_LOGS_DIR/THIS_TEST/

def run_test_fun():
    cmdline = "cd " + WORK_DIR + THIS_TEST + "/resource/glib2-test/glib-2.46.2/bin_porter/tests" + ";" + "sh glib2_test.sh > " + TMP_LOGS_DIR + THIS_TEST + "/log/" + THIS_TEST + ".log" + " 2>&1 "
    output = os.popen(cmdline)
    assert str(type(output)) == "<class 'os._wrap_close'>"
    output.close()

def test_glib2():
    global test_cases_values_and_status
    for l in test_cases_values_and_status:
        if(l[1] == "OK"):
            l[2] = "passed"
        if(l[1] == "FAIL"):
            l[2] = "failed"

#Pack the log file and count the test results
def teardown_module():
    glib2_report.log_report(test_cases_values_and_status,THIS_TEST)

if __name__ == '__main__':
    pytest.main("-s test_rpm.py")
