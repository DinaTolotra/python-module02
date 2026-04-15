def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_data_as_input_temperature(data: str) -> None:
    print(f"Input data is '{data}'")
    try:
        res: int = input_temperature(data)
    except ValueError:
        print("Caught input_temperature error:",
              f"invalid literal for int() with base 10: '{data}'")
    else:
        print(f"Temperature is now {res}°C")


def test_temperature() -> None:
    test_data_as_input_temperature("25")
    test_data_as_input_temperature("abc")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
