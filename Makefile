C=g++
CC=g++
CFLAGS=-O3 -std=c++0x -pg -D_DEBUG -g -c -Wall
LDFLAGS=
SOURCES=main.cpp menu.cpp data.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=benchmark.exe

.PHONY: all clean

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@


clean:
	rm -f $(OBJECTS)
