#ifndef MENU_H
#define MENU_H

#include <cstdlib>
#include <cstring>
#include <functional>
#include <vector>
#include <iostream>
using namespace std;

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
