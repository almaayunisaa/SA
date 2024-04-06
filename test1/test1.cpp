#include "test1.h"

adr createElmt(int angka) {
    adr p = new Elm;
    p->angka = angka;
    p->next = NULL;
}

void createList(list &L) {
    L.first=NULL;
}

void insertLast(list &L, adr p) {
    adr last = L.first;
    if (L.first==NULL) {
        L.first=p;
    } else {
        while (last->next!=NULL) {
            last=last->next;
        }
        last->next=p;
    }
}

adr merge(adr p, adr q) {
    adr h = createElmt(0);
    if (p==NULL) {
        return q;
    } else if (q==NULL) {
        return p;
    } else {
        if (p->angka>=q->angka) {
            h=q;
            h->next=merge(p, q->next);
        } else {
            h=p;
            h->next=merge(p->next, q);
        }
        return h;
    }
}
