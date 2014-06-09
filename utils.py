import os
import sys
import json

def save_to_file( path, data ):
  fp = open( path, "w" )
  fp.write( json.dumps( data ) )
  fp.close()

def load_from_file( path ):
  fp = open( path, "r" )
  ret = json.loads( fp.read() )
  fp.close()
  return ret

def clear_screen():
  if sys.platform == "linux" or sys.platform == "linux2":
    os.system( "clear" )
  else:
    os.system( "cls" )


def draw_table(data, start, length, formating):
  data_list = data[start:(start + length)]
