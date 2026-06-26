import re


def split_sections(markdown_text):
    pattern = r'(?=^#{1,6}\s)'
    sections = re.split(pattern, markdown_text, flags=re.MULTILINE)

    return [s.strip() for s in sections if s.strip()]
