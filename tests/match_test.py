#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from .match import get_website_type, get_regex_dict


class TestMetadata(unittest.TestCase):
    """
    Metadata are not big now, temporarily be loaded into memory at once.
    """

    site_regex = get_regex_dict()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_github_issues(self):
        result = get_website_type('https://github.com/travisjeffery/jocko/issues', self.site_regex)
        self.assertEqual(result, 'github')

    def test_zhihu_people(self):
        result = get_website_type('https://zhihu.com/people/knarfeh', self.site_regex)
        self.assertEqual(result, 'zhihu')


if __name__ == '__main__':
    unittest.main()
