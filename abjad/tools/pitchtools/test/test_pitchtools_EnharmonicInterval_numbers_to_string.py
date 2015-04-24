# -*- encoding: utf-8 -*-
from abjad.tools import pitchtools


def test_pitchtools_EnharmonicInterval_numbers_to_string_01():

    procedure = pitchtools.EnharmonicInterval.numbers_to_string

    assert 'ddd1' == procedure(1, 0, 1, -3)
    assert 'dd1' == procedure(1, 0, 1, -2)
    assert 'd1' == procedure(1, 0, 1, -1)
    assert 'P1' == procedure(1, 0, 1, 0)
    assert 'A1' == procedure(1, 0, 1, 1)
    assert 'AA1' == procedure(1, 0, 1, 2)
    assert 'AAA1' == procedure(1, 0, 1, 3)

    assert 'ddd2' == procedure(1, 0, 2, -2)
    assert 'dd2' == procedure(1, 0, 2, -1)
    assert 'd2' == procedure(1, 0, 2, 0)
    assert 'm2' == procedure(1, 0, 2, 1)
    assert 'M2' == procedure(1, 0, 2, 2)
    assert 'A2' == procedure(1, 0, 2, 3)
    assert 'AA2' == procedure(1, 0, 2, 4)
    assert 'AAA2' == procedure(1, 0, 2, 5)

    assert 'ddd3' == procedure(1, 0, 3, 0)
    assert 'dd3' == procedure(1, 0, 3, 1)
    assert 'd3' == procedure(1, 0, 3, 2)
    assert 'm3' == procedure(1, 0, 3, 3)
    assert 'M3' == procedure(1, 0, 3, 4)
    assert 'A3' == procedure(1, 0, 3, 5)
    assert 'AA3' == procedure(1, 0, 3, 6)
    assert 'AAA3' == procedure(1, 0, 3, 7)

    assert 'ddd4' == procedure(1, 0, 4, 2)
    assert 'dd4' == procedure(1, 0, 4, 3)
    assert 'd4' == procedure(1, 0, 4, 4)
    assert 'P4' == procedure(1, 0, 4, 5)
    assert 'A4' == procedure(1, 0, 4, 6)
    assert 'AA4' == procedure(1, 0, 4, 7)
    assert 'AAA4' == procedure(1, 0, 4, 8)

    assert 'ddd5' == procedure(1, 0, 5, 4)
    assert 'dd5' == procedure(1, 0, 5, 5)
    assert 'd5' == procedure(1, 0, 5, 6)
    assert 'P5' == procedure(1, 0, 5, 7)
    assert 'A5' == procedure(1, 0, 5, 8)
    assert 'AA5' == procedure(1, 0, 5, 9)
    assert 'AAA5' == procedure(1, 0, 5, 10)

    assert 'ddd6' == procedure(1, 0, 6, 5)
    assert 'dd6' == procedure(1, 0, 6, 6)
    assert 'd6' == procedure(1, 0, 6, 7)
    assert 'm6' == procedure(1, 0, 6, 8)
    assert 'M6' == procedure(1, 0, 6, 9)
    assert 'A6' == procedure(1, 0, 6, 10)
    assert 'AA6' == procedure(1, 0, 6, 11)
    assert 'AAA6' == procedure(1, 0, 6, 12)

    assert 'ddd7' == procedure(1, 0, 7, 7)
    assert 'dd7' == procedure(1, 0, 7, 8)
    assert 'd7' == procedure(1, 0, 7, 9)
    assert 'm7' == procedure(1, 0, 7, 10)
    assert 'M7' == procedure(1, 0, 7, 11)
    assert 'A7' == procedure(1, 0, 7, 12)
    assert 'AA7' == procedure(1, 0, 7, 13)
    assert 'AAA7' == procedure(1, 0, 7, 14)

    assert 'ddd8' == procedure(1, 1, 1, -3)
    assert 'dd8' == procedure(1, 1, 1, -2)
    assert 'd8' == procedure(1, 1, 1, -1)
    assert 'P8' == procedure(1, 1, 1, 0)
    assert 'A8' == procedure(1, 1, 1, 1)
    assert 'AA8' == procedure(1, 1, 1, 2)
    assert 'AAA8' == procedure(1, 1, 1, 3)

    assert 'ddd9' == procedure(1, 1, 2, -2)
    assert 'dd9' == procedure(1, 1, 2, -1)
    assert 'd9' == procedure(1, 1, 2, 0)
    assert 'm9' == procedure(1, 1, 2, 1)
    assert 'M9' == procedure(1, 1, 2, 2)
    assert 'A9' == procedure(1, 1, 2, 3)
    assert 'AA9' == procedure(1, 1, 2, 4)
    assert 'AAA9' == procedure(1, 1, 2, 5)

    assert 'ddd10' == procedure(1, 1, 3, 0)
    assert 'dd10' == procedure(1, 1, 3, 1)
    assert 'd10' == procedure(1, 1, 3, 2)
    assert 'm10' == procedure(1, 1, 3, 3)
    assert 'M10' == procedure(1, 1, 3, 4)
    assert 'A10' == procedure(1, 1, 3, 5)
    assert 'AA10' == procedure(1, 1, 3, 6)
    assert 'AAA10' == procedure(1, 1, 3, 7)

    assert 'ddd11' == procedure(1, 1, 4, 2)
    assert 'dd11' == procedure(1, 1, 4, 3)
    assert 'd11' == procedure(1, 1, 4, 4)
    assert 'P11' == procedure(1, 1, 4, 5)
    assert 'A11' == procedure(1, 1, 4, 6)
    assert 'AA11' == procedure(1, 1, 4, 7)
    assert 'AAA11' == procedure(1, 1, 4, 8)

    assert 'ddd12' == procedure(1, 1, 5, 4)
    assert 'dd12' == procedure(1, 1, 5, 5)
    assert 'd12' == procedure(1, 1, 5, 6)
    assert 'P12' == procedure(1, 1, 5, 7)
    assert 'A12' == procedure(1, 1, 5, 8)
    assert 'AA12' == procedure(1, 1, 5, 9)
    assert 'AAA12' == procedure(1, 1, 5, 10)

    assert 'ddd13' == procedure(1, 1, 6, 5)
    assert 'dd13' == procedure(1, 1, 6, 6)
    assert 'd13' == procedure(1, 1, 6, 7)
    assert 'm13' == procedure(1, 1, 6, 8)
    assert 'M13' == procedure(1, 1, 6, 9)
    assert 'A13' == procedure(1, 1, 6, 10)
    assert 'AA13' == procedure(1, 1, 6, 11)
    assert 'AAA13' == procedure(1, 1, 6, 12)

    assert 'ddd14' == procedure(1, 1, 7, 7)
    assert 'dd14' == procedure(1, 1, 7, 8)
    assert 'd14' == procedure(1, 1, 7, 9)
    assert 'm14' == procedure(1, 1, 7, 10)
    assert 'M14' == procedure(1, 1, 7, 11)
    assert 'A14' == procedure(1, 1, 7, 12)
    assert 'AA14' == procedure(1, 1, 7, 13)
    assert 'AAA14' == procedure(1, 1, 7, 14)

    assert 'ddd15' == procedure(1, 2, 1, -3)
    assert 'dd15' == procedure(1, 2, 1, -2)
    assert 'd15' == procedure(1, 2, 1, -1)
    assert 'P15' == procedure(1, 2, 1, 0)
    assert 'A15' == procedure(1, 2, 1, 1)
    assert 'AA15' == procedure(1, 2, 1, 2)
    assert 'AAA15' == procedure(1, 2, 1, 3)
