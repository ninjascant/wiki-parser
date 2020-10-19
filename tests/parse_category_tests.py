import unittest
from wikiparser.parse_categories import get_category_section_start, get_category_list, extract_categories

TEST_CAT_STRING = '''
\n[http://www.amphibiaweb.org/ AmphibiaWeb]\n* [http://www.globalamphibians.org/ Global Amphibian Assessment]\n* 
\n[http://sounds.bl.uk/Browse.aspx?category=Environment&collection=Amphibians Amphibian vocalisations on Archival \n
Sound Recordings]\n\n{{Amphibians}}\n{{Chordata}}\n{{Taxonbar|from=Q10908}}\n{{Authority control}}\n\n
{{Featured article}}\n\n[[Category:Amphibians| ]]\n[[Category:Amphibious organisms]]\n\n[[Category:Extant Late 
Devonian first appearances]]\n\n[[Category:Taxa named by John Edward Gray]]\n
'''

TEST_STRING_WITHOUT_CAT = '''
[http://www.amphibiaweb.org/ AmphibiaWeb]\n* [http://www.globalamphibians.org/ Global Amphibian Assessment]\n* 
[http://sounds.bl.uk/Browse.aspx?category=Environment&collection=Amphibians Amphibian vocalisations on Archival 
Sound Recordings]\n\n{{Amphibians}}\n{{Chordata}}\n{{Taxonbar|from=Q10908}}\n{{Authority control}}\n
{{Featured article}}\n
'''

TEST_CAT_LIST = [
    'Amphibians',
    'Amphibious organisms',
    'Extant Late Devonian first appearances',
    'Taxa named by John Edward Gray'
]

TEST_CAT_STRING_WITH_COMMENT = '''
[http://www.amphibiaweb.org/ AmphibiaWeb]\n* [http://www.globalamphibians.org/ Global Amphibian Assessment]\n* 
[http://sounds.bl.uk/Browse.aspx?category=Environment&collection=Amphibians Amphibian vocalisations on Archival 
Sound Recordings]\n\n{{Amphibians}}\n{{Chordata}}\n{{Taxonbar|from=Q10908}}\n{{Authority control}}\n
{{Featured article}}\n\n[[Category:Amphibians| ]]\n[[Category:Amphibious organisms]]\n<!-- 
[[Category:Animal classes]] moved to Latin name redirect -->\n[[Category:Extant Late Devonian first appearances]]
\n[[Category:Taxa named by John Edward Gray]]
'''


class TestParseCategorySection(unittest.TestCase):
    def test_get_category_start_page_with_category(self):
        cat_start = get_category_section_start(TEST_CAT_STRING)
        assert cat_start == 345

    def test_get_category_start_page_without_category(self):
        cat_start = get_category_section_start(TEST_STRING_WITHOUT_CAT)
        assert cat_start == -1

    def test_get_category_list(self):
        cat_start = get_category_section_start(TEST_CAT_STRING)
        cat_section = TEST_CAT_STRING[cat_start:]
        cat_list = get_category_list(cat_section)
        print(cat_list)
        assert cat_list == TEST_CAT_LIST

    def test_extract_categories(self):
        cat_list = extract_categories(TEST_CAT_STRING_WITH_COMMENT)
        assert cat_list == TEST_CAT_LIST
