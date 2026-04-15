class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super(GardenError, self).__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super(PlantError, self).__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super(WaterError, self).__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name[0].islower():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("carrots")
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
