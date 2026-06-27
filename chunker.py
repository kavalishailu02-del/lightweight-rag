import re

def split_sections(markdown):

    pattern = r'(?=^#{1,6}\s)'

    sections = re.split(
        pattern,
        markdown,
        flags=re.MULTILINE
    )

    return [
        s.strip()
        for s in sections
        if s.strip()
    ]
