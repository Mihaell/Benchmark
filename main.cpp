#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <functional>
#include <cassert>
#include <stack>
using namespace std;

class MenuItem;
class Menu;

Menu* main_menu;
Menu* menu1;


class MenuItem {
public:  
  function<void()> callback;
  string text;
  MenuItem() {}
  MenuItem(string _text, function<void()> _callback):
    text(_text),
    callback(_callback) {
  }
};

class Menu { 
public:  
  vector<MenuItem*> items;
  string name;
  Menu(string _name):
    name(_name) {
  }
  void add_item(string text, function<void()> callback) {
    items.push_back( new MenuItem(text, callback) ); 
  }
  void show() {
#ifdef __linux__
    system("clear");
#else
    system("cls");
#endif
    cout << " " << name << endl;
    cout << "---------------------" << endl;
    cout << endl;
    int cnt = 0;
    for(auto item: items) {
      ++cnt;
      cout << cnt << ") " << item->text << endl;
    }
    while(true) {
      int odabir;
      cout << "Vas odabir: ";
      cin >> odabir;
      --odabir;
      if( odabir >= items.size() ) {
        cout << "Nevaljan unos! Pokusajte ponovno. ";
      } else {
        items[odabir]->callback();
        break;
      }
    }
  }

};


class MenuManager {
public:
  stack<Menu*> menus;
  
};

void create_menus() {
  main_menu = new Menu("GLavni izbornik");
  menu1 = new Menu("Drugi izbornik");

  main_menu->add_item("Idi na 1. submenu!", [&] { menu1->show(); });
  main_menu->add_item("Izlaz", [&] { exit(0); });
  menu1->add_item("Povratak na glavni izbornik", [&] { main_menu->show(); });
}

int main(int argc, const char* argv[]) {

  create_menus();

  main_menu->show();

  return 0;
}
