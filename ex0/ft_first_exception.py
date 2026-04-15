def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temp: int
    data: str

    data = "25"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
    except ValueError as error:
        print("Caught input_temperature error:", error)
    else:
        print(f"Temperature is now {temp}°C")

    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
    except ValueError as error:
        print("Caught input_temperature error:", error)
    else:
        print(f"Temperature is now {temp}°C")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
