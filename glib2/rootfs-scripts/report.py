import sys

from plugins.agl_test_report import get_case_status
from plugins.agl_test_report import get_summary
from plugins.agl_test_report import write_date_to_json

def log_report(test_cases_values_and_status,THIS_TEST):
    #Get case_status, it's looks like : {'test_id': 'status',...}
    case_status = {}
    case_status = get_case_status(test_cases_values_and_status)

    #Get the summary of the test case status, the result is like that:
    #Summary = [["collected",num1],["passed",num2],["failed",num3],["skipped",num4]]
    summary = []
    summary = get_summary(case_status)

    #Judge whether the test set passes
    test_set_status = "null"
    if (summary[1][1] == summary[0][1]):
        test_set_status = "passed"
    else:
        test_set_status = "failed"

    write_date_to_json(test_set_status,THIS_TEST,summary,case_status)