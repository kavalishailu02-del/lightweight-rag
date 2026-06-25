import re

def split_sections(text):
    sections = re.split(
        r'(?=^#{1,6}\s)',
        text,
        flags=re.MULTILINE
    )

    return [
        section.strip()
        for section in sections
        if section.strip()
    ]
