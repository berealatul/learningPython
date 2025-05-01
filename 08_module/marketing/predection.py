from hr.people import get_employee_count
print("IMPORTED: ", __name__)


def future_sales():
    print(100)


# from ..hr.people import get_employee_count # it is not working
# from hr.people import get_employee_count # it is working
"""
Explanation:
Relative Import Issue:

The line from ..hr.people import get_employee_count in predection.py uses a relative import.
Relative imports rely on the module being executed as part of a package. However, when you run app.py directly, Python treats it as a top-level script, and the relative import in predection.py fails because Python doesn't recognize the package structure.
Standalone Script Execution:

When you run python .\app.py, Python doesn't treat the 08_module folder as a package. Instead, it treats app.py as a standalone script, which breaks relative imports.

Solution: from hr.people import get_employee_count
This assumes that the 08_module folder is in your PYTHONPATH or the current working directory when running the script.
"""


def calc_marketing_expense():
    print(get_employee_count()*98)


"""
if __name__ == "__main__":
    print("Predection of future sales:", future_sales())

here it will not work due to hr.people is outside its scope
"""
