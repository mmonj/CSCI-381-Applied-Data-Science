import re

PEOPLE_TEXT = (
    "555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco"
    "tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
)


def main() -> None:
    extract_numbers(PEOPLE_TEXT)
    print()

    names = extract_names(PEOPLE_TEXT)
    print()

    standardized = standardize_names(names)
    print()

    task4_has_title(standardized)
    print()

    task5_has_middle_name(standardized)
    print()

    task6()
    print()

    print()


def extract_numbers(text: str) -> None:
    """Task 1"""
    numbers = re.findall(r"\(?\d{3}\)?[- ]?\d{3}[-]?\d{4}|\d{3}[-]?\d{4}", text)
    print("Numbers:", numbers)


def extract_names(text: str) -> list[str]:
    """Task 2"""
    names = re.findall(r"(?<=[0-9()])[^0-9()]{5,}(?=[0-9()]|$)", text)
    names = [name.replace("\n", "").strip() for name in names if name.strip()]

    print("Names:", names)
    return names


def standardize_names(names: list[str]) -> list[str]:
    """Task 3"""
    standardized = []
    for name in names:
        if "," in name:
            parts = name.split(",")
            standardized.append(parts[1].strip() + " " + parts[0].strip())
        else:
            standardized.append(name.strip())

    print("Standardized Names:", standardized)
    return standardized


def task4_has_title(names: list[str]) -> None:
    titles = [bool(re.match(r"(Dr\.|Rev\.)", name.strip())) for name in names]
    print("Has Title:", titles)


def task5_has_middle_name(names: list[str]) -> None:
    results = []
    for name in names:
        name_wo_title = re.sub(r"^(\w+\.)\s*", "", name.strip())
        parts = name_wo_title.split()
        has_middle_name = len(parts) > 2

        results.append(has_middle_name)
    print("Has Middle Name:", results)


def task6() -> None:
    """Task 6"""
    explanation = """
For the HTML string '<title>+++BREAKING NEWS++<title>', the regex pattern '<.+>' fails because
the '+' quantifier is greedy. This means it will eat as many of that character as possible.

When applied to '<title>+++BREAKING NEWS++<title>', the pattern '<.+>' keeps matching all characters
until the last occurrence of >, capturing <title>+++BREAKING NEWS++<title> instead of just <title>.

the correct expression would be '<[^>]+>'.
this would correctly match '<title>'
    """
    print("Task 6 - HTML Tag Regex:")
    print(explanation)

    # Demonstrate with code
    html = "<title>+++BREAKING NEWS++<title>"
    wrong_match = re.findall(r"<.+>", html)
    correct_match1 = re.findall(r"<[^>]+>", html)

    print(f"Original string: {html}")
    print(f"Matches (from using the incorrect regex): {wrong_match}")
    print(f"Matches (from using the regex '<[^>]+>'): {correct_match1}")


if __name__ == "__main__":
    main()
