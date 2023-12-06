/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  const char *name;
  int x, y;
} City;

City cities[] = {
    {"Clean", 1336, 536}, {"Prosy", 977, 860},  {"Rabbi", 6, 758},    {"Addle", 222, 261},
    {"Smell", 1494, 836}, {"Quite", 905, 345},  {"Lives", 72, 714},   {"Cross", 23, 680},
    {"Synth", 1529, 785}, {"Tweak", 1046, 426}, {"Medic", 1485, 514}, {"Glade", 660, 476},
    {"Breve", 1586, 448}, {"Hotel", 1269, 576}, {"Toing", 398, 561},  {"Scorn", 617, 373},
    {"Tweet", 1253, 403}, {"Zilch", 1289, 29},  {"React", 296, 659},  {"Fiche", 787, 278},
};

void City_print(City *c)
{
  printf("%s(%d,%d)", c->name, c->x, c->y);
}
void City_printAll(City *p, int count)
{
  for (int i = 0; i < count; i++, p++) {
    City_print(p);
    putchar(' ');
  }
  putchar('\n');
}

int City_compare_name(const void* a, const void* b)
{
    City *c1 = (City*) a;
    City *c2 = (City*) b;
    return strcmp(c1->name, c2->name);
}

int cmp_cnt;
int City_compare_y(const void* a, const void* b)
{
    City *c1 = (City*) a;
    City *c2 = (City*) b;
    printf("#%d." ,++cmp_cnt);
    City_print(c1);
    printf(" vs ");
    City_print(c2);
    printf("\n");
    return c1->y - c2->y;
}

int main(void) 
{
  printf("--- Original Data ---\n");
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));

  // sort here by name
  qsort(cities, sizeof(cities) / sizeof(cities[0]), sizeof(cities[0]), City_compare_name);
  printf("--- By Name ---\n");
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));

  // sort here by y coordinate
  qsort(cities, sizeof(cities) / sizeof(cities[0]), sizeof(cities[0]), City_compare_y);
  printf("--- By Y Coordinate ---\n");
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));

  return 0;
}
