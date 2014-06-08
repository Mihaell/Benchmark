import utils

def main_menu():
  utils.clear_screen()
  print( '' )
  print( '   +---------------------------------+' )
  print( '   |             Benchmark           |' )
  print( '   +---------------------------------+' )
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

