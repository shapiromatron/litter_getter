#!/usr/bin/env python
# -*- coding: utf-8 -*-
from get_litter.utils import get_author_short_text

from unittest import TestCase


class TestAuthor(TestCase):

    def test_parsing(self):
        # 0 test
        self.assertEqual(
            u'',
            get_author_short_text([]))

        # 1 test
        self.assertEqual(
            u'Smith J',
            get_author_short_text(['Smith J']))

        # 2 test
        self.assertEqual(
            u'Smith J and Smith J',
            get_author_short_text(['Smith J'] * 2))

        # 3 test
        self.assertEqual(
            u'Smith J, Smith J, and Smith J',
            get_author_short_text(['Smith J'] * 3))

        # 4 test
        self.assertEqual(
            u'Smith J et al.',
            get_author_short_text(['Smith J'] * 4))
