print("IMPORTED: ", __name__)


def get_employee_count():
    return 17


def get_intern_count():
    print(15)


if __name__ == "__main__":
    print("Employee Count:", get_employee_count())
    print("Intern Count:", get_intern_count())
