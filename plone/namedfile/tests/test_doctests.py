# -*- coding: utf-8 -*-
from plone.namedfile.testing import PLONE_NAMEDFILE_FUNCTIONAL_TESTING
from plone.testing import layered

import doctest
import unittest


TEST_FILES = [
    'usage.rst',
    'handler.rst',
    'marshaler.rst',
    'utils.rst',
]


def test_suite():
    return unittest.TestSuite(
        [
            layered(
                doctest.DocFileSuite(
                    testfile,
                    package='plone.namedfile',
                ),
                PLONE_NAMEDFILE_FUNCTIONAL_TESTING
            ) for testfile in TEST_FILES
        ]

    )


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
