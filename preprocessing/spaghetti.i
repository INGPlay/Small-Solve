# 1 "d:/SourceTree/projectC/spaghetti/spaghetti.c"
# 1 "d:/SourceTree/projectC/spaghetti/spaghetti.h" 1


typedef struct {  bool memberBool;  int memberInt;  word memberWord;  }structure;
# 1 "d:/SourceTree/projectC/spaghetti/spaghetti.c" 2


int zi = 0;
int rw = 3;

extern int relocate = 3;

extern structure recipes [3];

int add(int a, int b);

main () {
int stack;
volatile int local,local2,local3;
local = 3;
locall = 4;
local2 =
add (local, local2);
stack += local3;
return stack;
}

int add (int a, int b) {
    return (a+b);
}
