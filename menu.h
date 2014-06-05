#ifndef MENU_H
#define MENU_H


#include "defines.h"

#include "menuitem.h"

class Menu {
public:
  
  string name;
  vector<MenuItem*> items;
  
  Menu(string _name);
  void add_item(string text, function<void()> callback);
  void show();
  
};

#endif
