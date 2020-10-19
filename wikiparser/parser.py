from .parse_categories import extract_categories
from .parse_sections import extract_sections
from .utils import remove_xml_comments


def parse_page(page):
    if 'redirect' in page.keys():
        return

    page_text = page['revision']['text']['#text']
    page_text = remove_xml_comments(page_text)

    title = page['title']
    categories = extract_categories(page_text)
    try:
        sections = extract_sections(page_text)
    except:
        return title, 'Can not parse', None, None
    return title, sections, categories
