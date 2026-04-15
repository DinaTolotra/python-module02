def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "4" + 2


def test_error_types() -> None:
    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except ValueError as error:
            print("Caught ValueError:", error)
        except ZeroDivisionError as error:
            print("Caught ZeroDivisionError:", error)
        except FileNotFoundError as error:
            print("Caught FileNotFoundError:", error)
        except TypeError as error:
            print("Caught TypeError:", error)
        else:
            print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
