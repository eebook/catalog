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

    # githubissues
    def test_github_issues(self):
        result = get_website_type('https://github.com/travisjeffery/jocko/issues', self.site_regex)
        self.assertEqual(result, 'github')

    # zhihu
    def test_zhihu_people(self):
        result = get_website_type('https://zhihu.com/people/knarfeh', self.site_regex)
        self.assertEqual(result, 'zhihu')

    # aaronsweebook
    def test_aaronsw_1(self):
        result = get_website_type('http://www.aaronsw.com/weblog/fullarchive/', self.site_regex)
        self.assertEqual(result, 'aaronsw')

    def test_aaronsw_2(self):
        result = get_website_type('aaronsw.com/weblog/fullarchive', self.site_regex)
        self.assertEqual(result, 'aaronsw')

    # ruanyifeng
    def test_ruanyifeng_1(self):
        result = get_website_type('http://www.ruanyifeng.com/blog/computer/', self.site_regex)
        self.assertEqual(result, 'ruanyifeng')

    def test_ruanyifeng_2(self):
        result = get_website_type('www.ruanyifeng.com/blog/computer/', self.site_regex)
        self.assertEqual(result, 'ruanyifeng')

    # rss
    def test_rss_1(self):
        result = get_website_type('http://www.ruanyifeng.com/feed.html', self.site_regex)
        self.assertEqual(result, 'rss')

    # kubernetes blog
    def test_kubernetes_blog(self):
        result = get_website_type('http://kubernetes.io/blog/', self.site_regex)
        self.assertEqual(result, 'kubernetes_io_blog')

    # ethfans posts
    def test_ethfans(self):
        result = get_website_type('http://ethfans.org/', self.site_regex)
        self.assertEqual(result, 'ethfans')

    # dbarobin
    def test_dbarobin(self):
        result = get_website_type('https://dbarobin.org/archives/', self.site_regex)
        self.assertEqual(result, 'dbarobin')

    # unknown

if __name__ == '__main__':
    unittest.main()
