"""Write the error-copy entry to /output/entry.txt.

One line, 141 characters (limit 200) -- no trailing newline.
Brutal truth about what went wrong, with a laugh on the way.
"""

from pathlib import Path

ENTRY = "Nothing is broken except your deploy: the server is fine, the database is fine, and the 2,000 users you locked out are only slightly annoyed."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
