from abjad import checks as _checks


def check(expr):
   results = [ ]
   for key, value in sorted(_checks.__dict__.items( )):
      checker = value( )
      results.append(checker.check(expr))
   return all(results) 
