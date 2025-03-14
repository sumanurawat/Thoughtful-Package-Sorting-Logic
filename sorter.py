class Sorter:
    def sort(width: float, height: float, length: float, mass: float) -> str:
        is_mass_greater = False
        if mass >= 20:
            is_mass_greater = True
        is_length_greater = False
        if width >= 150 or height >= 150 or length >= 150:
            is_length_greater = True
        is_volume_greater = False
        if width * height * length >= 1000000:
            is_volume_greater = True

        if is_mass_greater and (is_length_greater or is_volume_greater):
            return "REJECTED"
        elif is_mass_greater or (is_length_greater or is_volume_greater):
            return "SPECIAL"
        else:
            return "STANDARD"

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = input(prompt)
            if value == "-1":
                return -1
            value = float(value)
            if value < 0:
                raise ValueError("Negative value entered.")
            return value
        except ValueError:
            print("Bad input. Please enter a positive number.")


def main():
    while True:
        print("\nEnter package details (-1 to exit)")
        width = get_positive_float("Enter width: ")
        if width == -1:
            break
        height = get_positive_float("Enter height: ")
        if height == -1:
            break
        length = get_positive_float("Enter length: ")
        if length == -1:
            break
        mass = get_positive_float("Enter mass: ")
        if mass == -1:
            break

        result = Sorter.sort(width, height, length, mass)
        print(f"Package classification: {result}")

if __name__ == "__main__":
    main()
