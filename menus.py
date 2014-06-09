import utils
import globals

def games_list():
  igrica_list = globals.igrice[0:10]
  print(' ==+=============================================+================+========+==')
  for igrica in igrica_list:
    table = '   '
    table += '| '
    table += '{0:{width}}'.format(igrica['ime'], width = 45)
    table += ' | '
    table += '{0:{width}}'.format(igrica['zanr'], width = 15)
    table += ' | '
    table += '{0:{width}}'.format(igrica['min_cpu'], width = 6)
    table += ' |'
    table += '\n   +-----------------------------------------------+-----------------+--------+'
    print(table)
  choice = input()

def main_menu():
  utils.clear_screen()
  print( '' )
  print( len( globals.igrice ))
  print( '   +-------------------------------------------------+' )
  print( '   |                     Benchmark                   |' )
  print( '   +-------------------------------------------------+' )
  print( '' )
  print( '        1) Pregled igrica' )
  print( '        0) Izlaz' )
  print( '' )
  choice = int( input() )
  if choice == 1:
    games_list()
    return True
  else:
    return False

