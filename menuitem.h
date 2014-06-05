#ifndef MENUITEM_H
#define MENUITEM_H

#include <cstring>
#include <iostream>
#include <functional>
using namespace std;

struct MenuItem {  
  function<void()> callback;
  string text;
  MenuItem() {}
  MenuItem(string _text, function<void()> _callback):
    text(_text),
    callback(_callback) {
  }
};

#endif
