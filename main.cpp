#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <functional>
#include <cassert>
#include <stack>
using namespace std;

#include "menu.h"

Menu* main_menu;
Menu* menu1;

void create_menus() {
  main_menu = new Menu("GLavni izbornik");
  menu1     = new Menu("Drugi izbornik");

  main_menu->add_item("Idi na 1. submenu!", [&] { menu1->show(); });
  main_menu->add_item("Izlaz", [&] { exit(0); });
  
  menu1->add_item("Povratak na glavni izbornik", [&] { main_menu->show(); });
}

int main(int argc, const char* argv[]) {
  create_menus();
  main_menu->show();
  return 0;
}
