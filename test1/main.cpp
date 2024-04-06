#include "test1.h"
using namespace std;

int main()
{
    list L1;
    list L2;
    list L3;
    adr p;
    adr q;

    createList(L1);
    createList(L2);
    createList(L3);

    p = createElmt(1);
    insertLast(L1, p);
    p = createElmt(4);
    insertLast(L1, p);
    p = createElmt(5);
    insertLast(L1, p);

    p = createElmt(1);
    insertLast(L2, p);
    p = createElmt(3);
    insertLast(L2, p);
    p = createElmt(4);
    insertLast(L2, p);

    p = createElmt(2);
    insertLast(L3, p);
    p = createElmt(6);
    insertLast(L3, p);

    p=merge(L1.first, L2.first);
    L1.first=p;

    p=merge(L1.first, L3.first);
    q=p;
    while (q!=NULL) {
        cout << q->angka << endl;
        q=q->next;
    }

    return 0;
}
