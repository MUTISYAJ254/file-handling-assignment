from pathlib import Path

INPUT = Path("input.txt")
OUTPUT = Path("output.txt")

def transform_lines(lines: list[str]) -> list[str]:
    """Clean, uppercase, and number each non-empty line."""
    cleaned = []
    for i, line in enumerate(lines, start=1):
        text = line.strip()
        if not text:
            continue  # skip empty lines
        cleaned.append(f"{i:02d}. {text.upper()}")
    return cleaned

def main():
    # 1) Read
    text = INPUT.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 2) Transform
    new_lines = transform_lines(lines)

    # 3) Write
    OUTPUT.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    # 4) Show a quick summary
    print(f"Read {len(lines)} line(s) from {INPUT.name}")
    print(f"Wrote {len(new_lines)} line(s) to {OUTPUT.name}")
    print("Preview:")
    print("-" * 20)
    for preview in new_lines[:3]:
        print(preview)
    if len(new_lines) > 3:
        print("...")

if __name__ == "__main__":
    main()
