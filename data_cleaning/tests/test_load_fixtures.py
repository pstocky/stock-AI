# -*- coding: utf-8 -*-
import unittest

import load_fixtures

assertions = unittest.TestCase('__init__')


def test_load_open_days():
    testcases = [
        {
            'inputs': ['20080204', '20080213'],
            'expect': [
                '20080204',
                '20080205',
                '20080213',
            ],
        },
        {
            'inputs': ['20080203', '20080213'],
            'expect': [
                '20080204',
                '20080205',
                '20080213',
            ],
        },
        {
            'inputs': ['20080204', '20080212'],
            'expect': [
                '20080204',
                '20080205',
            ],
        },
    ]

    for case in testcases:
        inputs = case['inputs']
        expect = case['expect']

        real = load_fixtures.load_open_days(*inputs)

        assertions.assertItemsEqual(real, expect)
