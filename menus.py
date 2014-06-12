import utils
import globals
import games

def sort_list( w ):
  if w == 0:
    sorted( globals.igrice, key = operator.methodcaller('broj') )
  elif w == 1:
    sorted( globals.igrice, key = operator.methodcaller('ime') )
  elif w == 2:
    sorted( globals.igrice, key = operator.methodcaller('zanr') )
  elif w == 3:
    sorted( globals.igrice, key = operator.methodcaller('cijena') )
  else:
    sorted( globals.igrice, key = operator.methodcaller('ocjena'), reverse = True )

def num_page():
  z = len( globals.igrice )
  if z % 10 != 0:
    return z // 10 + 1
  else:
    return z // 10

def WIP():
  utils.clear_screen()
  print( '' )
  print( '   +-------------------------------------------------+' )
  print( '   |                     WIP                         |' )
  print( '   +-------------------------------------------------+' )
  print( '' )
  fdfdsjfs=0
  input(fdfdsjfs)
  utils.clear_screen()
  return False


def games_list():
  utils.clear_screen()
  way = 0
  choice = 1
  choice2 = -100
  while choice2 != 0:
    print( ' Stranica ' + str( choice ) + '/' + str( num_page() ) + ' ' )
    print( '' )
    fro = (choice - 1) * 10
    igrica_list = globals.igrice[fro:fro + 10]
    print(' ==+====================================================+=================+============+========+==')
    print('   |                                                    |                 |            |        |  ')
    print('   |                         IME                        |       ZANR      |   CIJENA   | OCJENA |  ')
    print('   |                                                    |                 |            |        |  ')
    print(' ==+====================================================+=================+============+========+==')
    z = 0
    for igrica in igrica_list:
      z += 1
      table = '   '
      table += '| '
      table += '{0:{width}}'.format(igrica['ime'], width = 50)
      table += ' | '
      table += '{0:{width}}'.format(igrica['zanr'], width = 15)
      table += ' | '
      table += '{0:{width}}'.format(igrica['cijena'], width = 10)
      table += ' | '
      table += '{0:{width}}'.format(igrica['ocjena'], width = 6)
      table += ' |'
      if z < 10:
        table += '\n   '  
        table += '+----------------------------------------------------+-----------------+------------+--------+'
      print(table)
    print(' ==+====================================================+=================+============+========+==')
    print( '' )
    print( '        1) - ' + str( num_page() ) + ') Stranice liste' )
    print( '        -1) - -10) Izabiranje igrice' )
    print( '        100) Sortiranje liste') 
    print( '        0) Izlaz')
    print( '' )
    choice2 = int( input() )
    if choice2 == 100:
      utils.clear_screen()
      print(' Kako zelite sortirati igrice? ' )
      if way != 0:
        print( '   0) Po rednom broju ' )
      if way != 1:
        print( '   1) Po imenima ' )
      if way != 2:
        print( '   2) Po zanru ' )
      if way != 3:
        print( '   3) Po cijeni ' )
      if way != 4:
        print( '   4) Po ocjeni ' )
      print( '' )
      way = int( input() )
      sort_list( way )
      utils.clear_screen()
      choice = 1
    elif choice2 < 0:
      if choice2 < -10:
        utils.clear_screen()
        print( ' Pogreska! Ta igrica ne postoji na ovoj stranici! ' )
        print( ' Pritisnite bilo koju tipku za povratak na stranicu. ' )
        print( '' )
        afajlfja = input()
        utils.clear_screen()
      else:
        games.choose_game( 10*(choice-1)-choice2-1 )
        utils.clear_screen()
        WIP()
    elif choice2 != 0:
      if choice2 > num_page():
        utils.clear_screen()
        print( ' Pogreska! Prekoracen broj stranica! ' )
        print( ' Pritisnite bilo koju tipku za povratak na prethodno gledanu stranicu. ' )
        print( '' )
        afalkjfa = input()
        utils.clear_screen()
      else:
        utils.clear_screen()
        choice = choice2
  sort_list( 0 )

def main_menu():
  utils.clear_screen()
  print( '' )
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

