#ifndef DATA_H
#define DATA_H

#include <fstream>
#include <cstring>
#include <string>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iostream>
using namespace std;

struct DataItem {
  string value;
  
  DataItem() {}
  DataItem(string _value):
    value(_value) {
  }

  int to_int() {
    int ret = 0;
    for(auto c: value) {
      assert(isdigit(c));
      ret *= 10;
      ret += c - '0';
    }
    return ret;
  }
  
  double to_double() {
    long long ret = 0;
    bool dot = false;
    for(auto c: value) {
      ++dot;
      if(c == '.') {
        dot = 0;
        continue;
      }
      assert(isdigit(c));
      ret *= 10;
      ret += c - '0';
    }
    double ret_double = (double)ret;
    if(dot != value.size()) {
      for(int i = 0; i < dot; ++i) {
        ret_double /= 10.0;
      }
    }
    return ret_double;
  }
  
  bool to_bool() {
    if(value == "true" || value == "True" || value == "TRUE" || value == "1") return true;
    return false;
  }

  string to_string() {
    return value;
  }
};

typedef vector<DataItem*> DataLine;

class Data {
public: 
 
  string filepath;
  
  vector<DataLine> lines;

  Data();
  
  void save(const char* path = NULL);
  void load(const char* path);
  
  void parse(string line, DataLine& vec);

};

#endif
