import unittest
import wikitextparser as wtp
from wikiparser.parse_sections import check_is_nested_section, parse_section_text

TEST_PAGE = '''
'{{other uses|Answer (disambiguation)}}\n{{refimprove|date=August 2013}}\n{{Use mdy dates|date=June 2013}}\n\n\nIn law, an \'\'\'answer\'\'\' was originally a solemn assertion in opposition to someone
 or something, and thus generally any counter-statement or [[defense (legal)|defense]], a [[reply]] to a [[question]] 
 \n\nThe famous Latin \'\'Responsa Prudentium\'\' ("answers of the learned ones") were the accumulated views of many 
 successive generations of Roman [[lawyer]]s, a body of legal opinion which gradually became authoritative.
 <ref name="Chisholm1911"/>\n\nDuring debates of a contentious nature, deflection, colloquially known as \'changing the 
 topic\', has been widely observed, and is often seen as a failure to answer a question.<ref>{{cite book|last1=Baaske
 |first1=Kevin|title=Arguments and Arguing: The Products and Process of Human Decision Making|date=2015|page=246}}
 </ref>\n\n==Notes==\n{{Reflist}}\n\n==External links==\n* [https://answerssite.com/ Answers Site]\n* 
 [https://answerskey.com/ Answers key]\n\n[[Category:Common law]]\n[[Category:Legal documents]]'
'''

TEST_PARSED_TEXT = '''
'In law, an answer was originally a solemn assertion in opposition to someone
 or something, and thus generally any counter-statement or defense, a reply to a question The famous Latin Responsa Prudentium ("answers of the learned ones") were the accumulated views of many 
 successive generations of Roman lawyers, a body of legal opinion which gradually became authoritative.During debates of a contentious nature, deflection, colloquially known as 'changing the 
 topic', has been widely observed, and is often seen as a failure to answer a question.
'''

class TestParseCategorySection(unittest.TestCase):
    def test_check_is_nested_section(self):
        test_parsed_page = wtp.parse(TEST_PAGE)
        test_sections = test_parsed_page.sections

        check_results = [check_is_nested_section(section) for section in test_sections]
        assert check_results == [False, False, False]

    def test_parse_section_text(self):
        test_parsed_page = wtp.parse(TEST_PAGE)
        test_sections = test_parsed_page.sections

        parsed_text = parse_section_text(test_sections[0])
        assert parsed_text.split() == TEST_PARSED_TEXT.split()