import json
import os
import utils


games = []
graficke = []
ramovi = []
procesori = []


fp = open('Baza podataka/igrice.txt')
lines = fp.readlines()
for line in lines:
  line = line.strip()
  values = line.split('|')
  if len( values ) != 8: break
  item = {
    'ime': values[0],
    'zanr': values[1],
    'min_cpu': int( values[2] ),
    'min_ram': int( values[5] ),
    'min_gra_cpu': int( values[3] ),
    'min_gra_ram': int( values[4] ),
    'ocjena': float( values[6] ),
    'cijena': float( values[7] )
  }
  games.append( item )

fp.close()
fp = open('Baza podataka/graficke.txt')
lines = fp.readlines()
for line in lines:
  line = line.strip()
  values = line.split('|')
  if len( values ) != 5: break
  item = {
    'ime': values[0],
    'cpu': int( values[1] ),
    'ram': int( values[2] ),
    'ocjena': float( values[3] ),
    'cijena': float( values[4] )
  }
  graficke.append(item)

fp.close()
fp = open('Baza podataka/ramovi.txt')
lines = fp.readlines()
for line in lines:
  line = line.strip()
  values = line.split('|')
  if len(values) != 4: break
  item = {
    'ime': values[0],
    'ram': int( values[1] ),
    'ocjena': float( values[2] ),
    'cijena': float( values[3] )
  }
  ramovi.append(item)


fp.close()
fp = open('Baza podataka/procesori.txt')
lines = fp.readlines()
for line in lines:
  line = line.strip()
  values = line.split('|')
  if len(values) != 4: break
  item = {
    'ime': values[0],
    'cpu': int( values[1] ),
    'ocjena': float( values[2] ),
    'cijena': float( values[3] )
  }
  procesori.append(item)

utils.save_to_file('data/igrice.txt', games)
utils.save_to_file('data/ramovi.txt', ramovi)
utils.save_to_file('data/graficke.txt', graficke)
utils.save_to_file('data/procesori.txt', procesori)


