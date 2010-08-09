def namesakes_forward_from_component(component, start = 0, stop = None):
   r'''Yield left-to-right namesakes of `component` starting
   from `component`. ::

      abjad> container = Container(Staff(leaftools.make_repeated_notes(2)) * 2)
      abjad> container.parallel = True
      abjad> container[0].name = 'staff 1'
      abjad> container[1].name = 'staff 2'
      abjad> score = Score([ ])
      abjad> score.parallel = False
      abjad> score.extend(container * 2)
      abjad> pitchtools.set_ascending_diatonic_pitches_on_nontied_pitched_components_in_expr(score)
      abjad> print score.format
      \new Score {
              <<
                      \context Staff = "staff 1" {
                              c'8
                              d'8
                      }
                      \context Staff = "staff 2" {
                              e'8
                              f'8
                      }
              >>
              <<
                      \context Staff = "staff 1" {
                              g'8
                              a'8
                      }
                      \context Staff = "staff 2" {
                              b'8
                              c''8
                      }
              >>
      }

   ::

      abjad> for staff in iterate.namesakes_forward_from_component(score[0][0]):
      ...     print staff.format
      ... 
      \context Staff = "staff 1" {
              c'8
              d'8
      }
      \context Staff = "staff 1" {
              g'8
              a'8
      }

   .. versionchanged:: 1.1.2
      renamed ``iterate.namesakes_forward_from( )`` to
      ``iterate.namesakes_forward_from_component( )``.
   '''

   cur_component = component
   total_components = 0

   while cur_component is not None:
      if start <= total_components:
         if stop is not None:
            if total_components < stop:
               yield cur_component 
         else:
            yield cur_component
      total_components += 1
      cur_component = cur_component._navigator._next_namesake
