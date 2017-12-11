#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import jinja2
from jinja2 import Template
from tests.match import get_metadata_from_repo

__author__ = "knarfeh@outlook.com"


if __name__ == "__main__":
    print("\nBuilding index.html...\n")
    metadata_list = get_metadata_from_repo()

    loader = jinja2.FileSystemLoader('./index.jinja2.html')
    env = jinja2.Environment(loader=loader)
    template = env.get_template(name='')
    index_content = template.render(metadata_list=metadata_list)
    with open('./dist/index.html', 'w+') as result_file:
        result_file.write(index_content)
    print("Done.")

