#include "menu.h"

Menu::Menu(string _name):
  name(_name) {
}

void Menu::add_item(string text, function<void()> callback) {
  items.push_back(new MenuItem(text, callback));
}

void Menu::show() {
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
