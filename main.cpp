#include "defines.h"
#include "menu.h"
#include "data.h"

Menu* main_menu;
Menu* menu1;

Data* games;

void create_menus() {
  main_menu = new Menu("GLavni izbornik");
  menu1     = new Menu("Drugi izbornik");

  main_menu->add_item("Idi na 1. submenu!", [&] { menu1->show(); });
  main_menu->add_item("Izlaz", [&] { exit(0); });
  
  menu1->add_item("Povratak na glavni izbornik", [&] { main_menu->show(); });
}

int main(int argc, const char* argv[]) {
  create_menus();
  //main_menu->show();

  games = new Data();
  games->load("Baza podataka/igrice.txt");
  for(auto it: games->lines) {
    cout << it[I_IME]->to_string() << " -- ";
    cout << it[I_MIN_RAM]->to_int() << " -- ";
    cout << it[I_OCJENA]->to_double() << endl;
  }

  //cout << data->lines[0][0]->to_string() << endl;
  return 0;
}
