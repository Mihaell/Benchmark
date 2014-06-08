#include "data.h"

Data::Data() {
}

void Data::load(const char* path) {
  filepath = string(path);
  //parse();
  ifstream file(path, std::fstream::in);
  assert(file.is_open());
  
  while(file.good()) {
    string line;
    getline(file, line);
    DataLine tmp;
    parse(line, tmp);
    if(tmp.size() < 2) break;
    lines.push_back(tmp);
  }

  file.close();
}

void Data::parse(string line, DataLine& vec) {
  line += "|";
  string tmp = "";
  for(auto c: line) {
    if(c == '|') {
      vec.push_back(DataItem(tmp));
      tmp = "";
    } else {
      tmp = tmp + c;
    }
  }
}
