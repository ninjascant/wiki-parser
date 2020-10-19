import re
import wikitextparser as wtp


XML_COMMENT_PATTERN = re.compile(r'<!--(.|\s|\n)*?-->')
ARTICLE_START_PATTERN = re.compile('\n\s+\n')
SECTION_TITLE_PATTERN = re.compile('=.+=')


def remove_xml_comments(page):
    return XML_COMMENT_PATTERN.sub('', page, re.DOTALL)


def remove_section_start_newlines(section):
    return ARTICLE_START_PATTERN.sub('', section)


def remove_section_start_markup(section):
    return SECTION_TITLE_PATTERN.sub('', section)


def mark_named_entities(text):
    replaced = []
    for link in wtp.parse(text).wikilinks:
        if link.title not in replaced:
            text = text.replace(str(link), f'<NE>{link.plain_text()}</NE>')
            replaced.append(link.title)

    wrong_patterns = set(re.findall('</NE>\w+', text))
    for pattern in wrong_patterns:
        fixed_pattern = pattern.replace('</NE>', '') + '</NE>'
        text = text.replace(pattern, fixed_pattern)
    text = text.replace('<NE></NE>', '')
    return text