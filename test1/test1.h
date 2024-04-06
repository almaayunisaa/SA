#include <iostream>

using namespace std;

typedef struct Elm *adr;

struct Elm {
    int angka;
    adr next;
};

struct list {
    adr first;
};

adr createElmt(int angka);
void createList(list &L);
void insertLast(list &L, adr p);
adr merge(adr p, adr q);
