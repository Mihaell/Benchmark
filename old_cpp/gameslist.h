#ifndef GAMESLIST_H
#define GAMESLIST_H

#include "defines.h"

class GamesList {
  Data* games;
  GamesList ();
  void RegisterList ( Data* data );
  void Sort ( ParametarIgrice p );
};


#endif
