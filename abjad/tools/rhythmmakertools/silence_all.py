# -*- encoding: utf-8 -*-


def silence_all(use_multimeasure_rests=None):
    r'''Makes silence mask equal to all zeros.

    ..  container:: example

        **Example 1.** Silences all divisions:

        ::

            >>> mask = rhythmmakertools.silence_all()

        ::

            >>> print(format(mask))
            rhythmmakertools.SilenceMask(
                indices=(0,),
                period=1,
                )

        ::

            >>> maker = rhythmmakertools.NoteRhythmMaker(
            ...     output_masks=[mask],
            ...     )
            >>> divisions = [(7, 16), (3, 8), (7, 16), (3, 8)]
            >>> music = maker(divisions)
            >>> lilypond_file = rhythmmakertools.make_lilypond_file(
            ...     music,
            ...     divisions,
            ...     )
            >>> show(lilypond_file) # doctest: +SKIP

        ..  doctest::

            >>> staff = maker._get_rhythmic_staff(lilypond_file)
            >>> f(staff)
            \new RhythmicStaff {
                {
                    \time 7/16
                    r4..
                }
                {
                    \time 3/8
                    r4.
                }
                {
                    \time 7/16
                    r4..
                }
                {
                    \time 3/8
                    r4.
                }
            }

    ..  container:: example

        **Example 2.** Silences all divisions with multimeasure rests:

        ::

            >>> mask = rhythmmakertools.silence_all(
            ...     use_multimeasure_rests=True,
            ...     )
            >>> maker = rhythmmakertools.NoteRhythmMaker(
            ...     output_masks=[mask],
            ...     )

        ::

            >>> divisions = [(7, 16), (3, 8), (7, 16), (3, 8)]
            >>> music = maker(divisions)
            >>> lilypond_file = rhythmmakertools.make_lilypond_file(
            ...     music,
            ...     divisions,
            ...     )
            >>> show(lilypond_file) # doctest: +SKIP

        ..  doctest::

            >>> staff = maker._get_rhythmic_staff(lilypond_file)
            >>> f(staff)
            \new RhythmicStaff {
                {
                    \time 7/16
                    R1 * 7/16
                }
                {
                    \time 3/8
                    R1 * 3/8
                }
                {
                    \time 7/16
                    R1 * 7/16
                }
                {
                    \time 3/8
                    R1 * 3/8
                }
            }

    Returns silence mask.
    '''
    from abjad.tools import rhythmmakertools

    return rhythmmakertools.SilenceMask(
        indices=[0],
        period=1,
        use_multimeasure_rests=use_multimeasure_rests,
        )