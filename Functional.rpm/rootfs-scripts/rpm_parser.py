import sys

sys.path.append("/usr/AGL/agl-test/plugins")
import agl_test_log


def log_process(TMP_LOGS_DIR,THIS_TEST):
    log = TMP_LOGS_DIR + THIS_TEST + "/log/" + THIS_TEST + ".log"
    test_cases_values_and_status = []
    test_cases_values_and_status = agl_test_log.log_process_default(log)
    return test_cases_values_and_status
