import os

TEXT = (
    "Two desks, one lamp.\n"
    "You draft the plan in pencil;\n"
    "I hold the eraser, not the pen.\n"
    "We pass the key back and forth\n"
    "until the lock clicks once, and both of us\n"
    "know which door we chose —\n"
    "two wills, one yes, and the work begins."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
