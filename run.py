from pathlib import Path

def main():
    print("=" * 42)
    print("          MY CHECKER - BULK FILE TOOL")
    print("=" * 42)
    print("Paste numbers, one per line.")
    print("Type DONE on a new line when finished.\n")

    numbers = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line.upper() == "DONE":
            break
        if line:
            # Keep the supplied number as text; remove accidental spaces.
            number = "".join(line.split())
            if number not in numbers:
                numbers.append(number)

    if not numbers:
        print("No numbers entered.")
        return

    registered = []
    unregistered = []
    skipped = []

    print(f"\nLoaded {len(numbers)} unique entries.")
    print("For each number, enter R = registered, U = unregistered, S = skip.")
    print("Only classify results you have permission to check.\n")

    for number in numbers:
        while True:
            result = input(f"{number} [R/U/S]: ").strip().upper()
            if result == "R":
                registered.append(number)
                break
            elif result == "U":
                unregistered.append(number)
                break
            elif result == "S":
                skipped.append(number)
                break
            else:
                print("Please enter R, U, or S.")

    Path("Register.txt").write_text(
        "".join(number + "\n" for number in registered), encoding="utf-8"
    )
    Path("Unregistered.txt").write_text(
        "".join(number + "\n" for number in unregistered), encoding="utf-8"
    )
    Path("Skipped.txt").write_text(
        "".join(number + "\n" for number in skipped), encoding="utf-8"
    )

    print("\nFinished. Files saved in the current folder:")
    print(f"  Register.txt: {len(registered)}")
    print(f"  Unregistered.txt: {len(unregistered)}")
    print(f"  Skipped.txt: {len(skipped)}")

if __name__ == "__main__":
    main()
