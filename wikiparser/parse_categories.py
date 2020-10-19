import re
from .utils import remove_xml_comments


def get_category_section_start(page):
    try:
        cat_start = page.index('[[Category:')
    except ValueError:
        cat_start = -1
    return cat_start


def clean_category_string(string):
    string = re.sub(r'[^A-Za-z0-9 ]+', '', string)
    string = ' '.join([item for item in string.split() if item != ' '])
    return string


def get_category_list(category_section):
    category_section = category_section
    category_list = category_section.split(']]')
    category_list = [cat.split(':') for cat in category_list]
    category_list = [cat[1] for cat in category_list if len(cat) > 1]
    category_list = [clean_category_string(cat) for cat in category_list]
    category_list = [cat for cat in category_list if len(cat) > 0]
    return category_list


def extract_categories(page):
    page = remove_xml_comments(page)
    cat_start = get_category_section_start(page)
    if cat_start == -1:
        return []
    cat_section = page[cat_start:]
    cat_list = get_category_list(cat_section)
    return cat_list