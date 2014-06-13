import utils
import globals

def choose_game( x ):
  utils.clear_screen()
  print ( globals.igrice[x] )

  igra = globals.igrice[x]

  print ( '==+' + '='*100 + '+==' )
  print ( '  |' + ' '*100 + '|  ' )
  print ( '  |' + igra['ime'].center( 100, ' ' ) + '|  ' )
  print ( '  |' + ' '*100 + '|  ' )
  print ( '  |' + ('*'*int(igra['ocjena'])).center( 100, ' ' ) + '|  ' )
  print ( '  |' + ' '*100 + '|  ' )
  print ( '==+' + '='*20 + '+' + '='*79 + '+==' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '  |' + 'ZANR'.center( 20, ' ' ) + '|' + igra['zanr'].center( 79, ' ' ) + '|  ' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '==+' + '-'*20 + '+' + '-'*79 + '+==' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '  |' + 'MINIMALNI CPU'.center( 20, ' ' ) + '|' + (str(igra['min_cpu']) + ' MHz').center( 79, ' ' ) + '|  ' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '==+' + '-'*20 + '+' + '-'*79 + '+==' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '  |' + 'MINIMALNI GPU'.center( 20, ' ' ) + '|' + (str(igra['min_gra_cpu']) + ' MHz').center( 79, ' ' ) + '|  ' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '==+' + '-'*20 + '+' + '-'*79 + '+==' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '  |' + 'MINIMALNI GPU_RAM'.center( 20, ' ' ) + '|' + (str(igra['min_gra_ram']) + ' MB').center( 79, ' ' ) + '|  ' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '==+' + '-'*20 + '+' + '-'*79 + '+==' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '  |' + 'MINIMALNI RAM'.center( 20, ' ' ) + '|' + (str(igra['min_ram']) + ' MB').center( 79, ' ' ) + '|  ' )
  print ( '  |' + ' '*20 + '|' + ' '*79 + '|  ' )
  print ( '==+' + '-'*20 + '+' + '-'*79 + '+==' )
  print ( '  |' + ' '*100  + '|  ' )
  print ( '  |' + ('Cijena: ' + str(igra['cijena']) + ' kn').center( 100, ' ' ) + '|  ' )
  print ( '  |' + ' '*100  + '|  ' )
  print ( '==+' + '='*100 + '+==' )
  print ( '' )
  print ( '        1) Benchmark')
  print ( '        0) Izlaz')

  choice = 0;
  int( input( choice ) )

  if choice == 0:
    return False
  if choice == 1:
    print("TADAAAAA")
  input(x)
