def input_temperature(temp_str: str) -> int:
    try:
        temp_int: int = int(temp_str)
        if temp_int < 0:
            raise ValueError(f"{temp_int}°C  is too cold for plants (min 0°C)")
        elif temp_int > 40:
            raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    except ValueError as error:
        raise ValueError(error)
    else:
        return temp_int


def try_test_temperature(data: str) -> None:
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
    except ValueError as error:
        print("Caught input_temperature error:", error)
    else:
        print(f"Temperature is now {temp}°C")


def test_temperature() -> None:
    try_test_temperature("25")
    try_test_temperature("abc")
    try_test_temperature("100")
    try_test_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
