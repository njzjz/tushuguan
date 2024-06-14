import os
import sys
from pathlib import Path

import bibtexparser

def check_bibtex(filename: Path):
    with open(filename) as bibtex_file:
        bibtex_string = bibtex_file.read()
    bib_database = bibtexparser.parse_string(bibtex_string)
    rm = []
    for entry in bib_database.entries:
        entry_type = entry.entry_type
        entry_key = entry.key
        expected_filename = Path(entry_type)
        if entry_type.lower() == "article":
            short_journal = entry_key.split("_")[1]
            expected_filename /= short_journal
        expected_filename /= f"{entry_key}.bib"
        if filename != expected_filename:
            # make directory
            expected_filename.parent.mkdir(parents=True, exist_ok=True)
            # write to new file
            new_library = bibtexparser.Library([entry])
            new_bibtex_str = bibtexparser.write_string(new_library)
            with open(expected_filename, "w") as new_bibtex_file:
                new_bibtex_file.write(new_bibtex_str)
            rm.append(True)
        else:
            rm.append(False)
    if all(rm):
        os.remove(filename)
    elif rm.count(False) > 1:
        raise ValueError("More than one entry in the same file")


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        check_bibtex(Path(filename))
