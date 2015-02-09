from __future__ import division, print_function, unicode_literals

# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

pytest_plugins = str('pytester')


TESTSUITE = """
from hypothesis import given

@given(int)
def test_this_one_is_ok(x):
    pass

@given([int])
def test_always_sorted(xs):
    assert sorted(xs) == xs

@given([int])
def test_never_sorted(xs):
    assert sorted(xs) != xs
"""


def test_runs_reporting_hook(testdir):
    script = testdir.makepyfile(TESTSUITE)
    result = testdir.runpytest(script, '--verbose')
    out = '\n'.join(result.stdout.lines)
    assert 'test_this_one_is_ok' in out
    assert 'Captured stdout call' not in out
    assert 'Falsifying example' in out
    assert result.ret != 0
