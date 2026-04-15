class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super(GardenError, self).__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super(PlantError, self).__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super(WaterError, self).__init__(message)


def raise_plant_error_exception() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error_exception() -> None:
    raise WaterError("Not enough water in the tank!")


def test_plant_error() -> None:
    print("\nTesting PlantError...")
    try:
        raise_plant_error_exception()
    except PlantError as error:
        print("Caught PlantError:", error)


def test_water_error() -> None:
    print("\nTesting WaterError...")
    try:
        raise_water_error_exception()
    except WaterError as error:
        print("Caught WaterError:", error)


def test_garden_error() -> None:
    print("\nTesting catching all garden errors...")

    try:
        raise_plant_error_exception()
    except GardenError as error:
        print("Caught GardenError:", error)

    try:
        raise_water_error_exception()
    except GardenError as error:
        print("Caught GardenError:", error)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    test_water_error()
    test_garden_error()
    print("\nAll custom error types work correctly!")
