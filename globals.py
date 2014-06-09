import utils

igrice = []
ramovi = []
graficke = []
procesori = []

def init():
  global igrice
  global ramovi
  global procesori
  global graficke
  igrice = utils.load_from_file('data/igrice.txt')
  ramovi = utils.load_from_file('data/ramovi.txt')
  graficke = utils.load_from_file('data/graficke.txt')
  procesori = utils.load_from_file('data/procesori.txt')
