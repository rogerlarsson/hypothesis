# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Most of this work is copyright (C) 2013-2019 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import absolute_import, division, print_function

from hypothesis import given, strategies as st

# Tests that convert_keyword_arguments in reflection.py can handle
# composites that only have keyword-only arguments.
# See https://github.com/HypothesisWorks/hypothesis/issues/1999


@st.composite
def kwonlyargs_composites(draw, *, kwarg1=None):
    return draw(st.fixed_dictionaries({"kwarg1": st.just(kwarg1), "i": st.integers()}))


@given(
    st.lists(
        st.one_of(kwonlyargs_composites(kwarg1="test")), unique_by=lambda x: x["i"]
    )
)
def test_composite_with_keyword_only_args(a):
    assert True