import sys

from plugins.agl_test_log import log_process_gnome_result

def log_process(TMP_LOGS_DIR,THIS_TEST):
    log = TMP_LOGS_DIR + THIS_TEST + "/log/" + THIS_TEST + ".log"
    test_cases_values_and_status = []
    test_cases_values_and_status = log_process_gnome_result(log)
    return test_cases_values_and_status
