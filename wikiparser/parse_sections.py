import wikitextparser as wtp
from .utils import remove_section_start_markup, remove_section_start_newlines


def parse_section_text(section):
    title = section.title

    parsed_section = wtp.parse(section.string)
    text = parsed_section.plain_text()

    text = remove_section_start_newlines(text)

    if title is not None:
        text = text.replace(title, '')
        text = remove_section_start_markup(text)

    return text


def check_is_nested_section(section):
    if len(section.sections) < 3:
        return False
    else:
        return True


def parse_section(section):
    is_nested = check_is_nested_section(section)
    if is_nested:
        return

    parsed_section = parse_section_text(section)
    section_title = section.title

    return [section_title, parsed_section]


def filter_parsed_sections(parsed_sections):
    return [section for section in parsed_sections
            if section is not None and section[1] != '']


def extract_sections(article):
    parsed_article = wtp.parse(article)
    sections = parsed_article.sections
    parsed_sections = [parse_section(section) for section in sections]
    parsed_sections = filter_parsed_sections(parsed_sections)

    return parsed_sections
