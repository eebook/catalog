#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json
import os

def _get_json_content(path):
    """
    Read a json file and return its content(Python object)
    :param path: json file path
    """
    with open(path, 'r') as f:
        return json.load(f)


def get_metadata_from_repo():
    result = list()
    for _, _, files in os.walk('/src/json', followlinks=False):
        file_path_list = ['/src/json/'+item for item in files]
        print('Supported website: {}\n'.format(files))
    for item in file_path_list:
        result_item = _get_json_content(item)
        result.append(result_item)
    return result


def get_regex_dict():
    metadata_list = get_metadata_from_repo()
    site_regex_dict = {item['name']: item['regex'] for item in metadata_list}
    return site_regex_dict


def get_website_type(url, _site_regex=None):
    if _site_regex is None:
        _site_regex = get_regex_dict()
    for k, v in _site_regex.items():
        if isinstance(v, str):
            search_result = re.search(v, url)
            if search_result is not None:
                return k
        elif isinstance(v, list):
            for item in v:
                search_result = re.search(item, url)
                if search_result is not None:
                  return k
    return 'unknown'


if __name__ == "__main__":
    site_regex = get_regex_dict()

    website_type1 = get_website_type('https://talkpython.fm/episodes/asdf/', site_regex)
    print('website type: {}'.format(website_type1))

    website_type2 = get_website_type('https://zhihu.com/people/knarfeh', site_regex)
    print('website type: {}'.format(website_type2))

    test_github = get_website_type('https://github.com/travisjeffery/jocko/issues', site_regex)
    print('test_github: {}'.format(test_github))
