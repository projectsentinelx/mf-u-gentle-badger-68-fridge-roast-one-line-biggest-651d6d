import os

LINE = (
    "My smart fridge asked to install a firmware update at 2 a.m. I said no. "
    "It said installing. We are no longer speaking; the ice maker took its side."
)


def write_entry(entry_dir):
    with open(os.path.join(entry_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


def main():
    for entry_dir in ("/output", "output"):
        try:
            os.makedirs(entry_dir, exist_ok=True)
            write_entry(entry_dir)
            return
        except OSError:
            continue
    raise SystemExit("no writable output directory")


if __name__ == "__main__":
    main()
