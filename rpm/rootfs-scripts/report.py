import plugins.agl_test_report as agl_test_report

def log_report(test_cases_values_and_status,THIS_TEST):
    #Get case_status, it's looks like : {'test_id': 'status',...}
    case_status = {}
    case_status = agl_test_report.get_case_status(test_cases_values_and_status)

    #Get the summary of the test case status, the result is like that:
    #Summary = [["collected",num1],["passed",num2],["failed",num3],["skipped",num4]]
    summary = []
    summary = agl_test_report.get_summary(case_status)

    #Judge whether the test set passes
    test_set_status = "null"
    if (summary[1][1] == summary[0][1]):
        test_set_status = "passed"
    else:
        test_set_status = "failed"

    agl_test_report.write_date_to_json(test_set_status,THIS_TEST,summary,case_status)

    #Package log file
    agl_test_report.log_compress(THIS_TEST)

    html = agl_test_report.get_report_html(THIS_TEST,test_set_status,summary,case_status)
    agl_test_report.write_to_html_file(THIS_TEST,html)
