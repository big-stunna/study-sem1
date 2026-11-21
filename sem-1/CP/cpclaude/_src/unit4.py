import sys
from lib import *
from unit4a import s

# ================================================================= 6
s += H1('6. Pointers — Basics')
s += [P('Every variable lives at some <b>address</b> in memory. A <b>pointer</b> is a variable that stores the <b>address of another variable</b>. Pointers let a function change its caller\'s data, let programs walk through arrays efficiently, and are the foundation of dynamic memory, strings, structures and data structures.')]
s += TABLE([['Operator', 'Name', 'Meaning'], ['`&`', 'address-of', '`&x` gives the address of variable x'], ['`*`', 'dereference (value-at)', '`*p` gives the value stored at the address held in p'], ['`*` in a declaration', 'pointer declarator', '`int *p;` declares p as "pointer to int"']], [1.6, 2, 3.9])
s += SYNTAX('<b>data_type *pointer_name;</b> &nbsp; declaration &nbsp;|&nbsp; <b>ptr = &variable;</b> &nbsp; initialisation &nbsp;|&nbsp; <b>value = *ptr;</b> &nbsp; dereference'.replace('&nbsp;', ' '))
s += CODE('''
name   address   value
xyz      1380      50        int xyz = 50;
ptr      2000     1380       int *ptr = &xyz;   (ptr holds xyz's address)

*ptr  ->  go to address 1380  ->  50       so  *ptr == 50  and  ptr == &xyz
''', label='Memory picture (addresses are illustrative)')
s += CODE('''
#include <stdio.h>

int main(void) {
    int x = 5, y = 20;
    int *p = &x;                         /* p points to x                      */
    printf("x = %d, *p = %d\\n", x, *p);
    *p = 10;                             /* change x THROUGH the pointer       */
    printf("x = %d\\n", x);
    p = &y;                              /* a pointer can be re-pointed        */
    *p += 1;
    printf("y = %d\\n", y);
    printf("pointer size = %zu bytes, int size = %zu bytes\\n", sizeof(p), sizeof(int));
    printf("p == &y ? %s\\n", p == &y ? "yes" : "no");
    return 0;
}
''', run=True)
s += BUL(['A pointer\'s <b>type</b> tells the compiler how many bytes to read and how to interpret them when it is dereferenced (`int *` reads 4 bytes as an int, `char *` reads 1 byte).', 'All pointers on one machine have the same size (8 bytes on a 64-bit system) regardless of what they point to.', 'Print an address with `%p` (cast to `void *`): `printf("%p", (void *)&x);` – the value differs from run to run.', '<b>NULL pointer:</b> `int *p = NULL;` points nowhere. Dereferencing NULL crashes the program, so always test `if (p != NULL)` before using a pointer that might be unset.', '<b>void pointer:</b> `void *` can hold the address of any type but must be cast before it is dereferenced (`malloc` returns one).'])
s += WARN('An <b>uninitialised pointer</b> holds garbage; `*p = 5;` then writes to a random address (undefined behaviour). Initialise every pointer – to a real address or to NULL. A <b>dangling pointer</b> points to memory that is no longer valid (a local variable of a finished function, or freed heap memory). Never use one.')
s += RECALL(['`&` gives the address; `*` gives the value at an address.', '`int *p;` – p is a pointer to int; `p = &x;` links it to x; `*p = v;` modifies x.', 'Always initialise pointers; check for NULL before dereferencing.', 'Pointer size is fixed per machine (8 bytes on 64-bit); the pointed-to type decides how data is read.', 'Print addresses with `%p`.'])
s += QA('g', 'What does the following print? `int x = 5, *p = &x; *p = 10; printf("%d", x);`', [('steps', ['`p` holds the address of x.', '`*p = 10;` writes 10 to the memory p points at – that is x.', 'So x becomes 10. Output: <b>10</b>.'])])

# ================================================================= 7
s += H1('7. Pointer Arithmetic')
s += [P('Pointers support a small set of operations. The key rule is the <b>scale factor</b>: adding 1 to a pointer moves it by `sizeof(type)` bytes – to the <i>next element</i> – not by 1 byte.')]
s += TABLE([['Operation', 'Allowed?', 'Effect'], ['`p + n`, `p - n`', 'Yes', 'Moves p forward/back by n × sizeof(*p) bytes (n elements)'], ['`p++`, `p--`', 'Yes', 'Next / previous element'], ['`p1 - p2`', 'Yes (same array)', 'Number of <i>elements</i> between them (type `ptrdiff_t`)'], ['`p1 < p2`, `p1 == p2`', 'Yes', 'Comparison of addresses'],
            ['`p1 + p2`', 'No', 'Adding two addresses is meaningless'], ['`p * n`, `p / n`', 'No', 'Not allowed on pointers']], [1.8, 1.5, 4.2])
s += FORMULA('New address = old address + n × sizeof(type). &nbsp;Example: int *p at address 1000 → p + 3 is at 1000 + 3 × 4 = 1012 (4-byte int).'.replace('&nbsp;', ' '))
s += CODE('''
#include <stdio.h>

int main(void) {
    int x[5] = {10, 20, 30, 40, 50};
    int *p = &x[1];                              /* points to x[1] */
    printf("%d\\n", *p);                          /* 20 */
    p++;                                         /* now x[2]       */
    printf("%d\\n", *p);                          /* 30 */
    p = p + 2;                                   /* now x[4]       */
    printf("%d\\n", *p);                          /* 50 */
    printf("distance x[4]-x[1] = %ld elements\\n", (long)(p - &x[1]));
    printf("bytes between consecutive ints = %ld\\n",
           (long)((char *)(x + 1) - (char *)x));
    return 0;
}
''', run=True)
s += TABLE([['Pointer type', 'p + 1 moves by (typical 64-bit)'], ['`char *`', '1 byte'], ['`short *`', '2 bytes'], ['`int *`, `float *`', '4 bytes'], ['`double *`, `long *`', '8 bytes']], [2.5, 5])
s += RECALL(['`p++` moves by `sizeof(*p)` bytes, not 1.', '`p1 - p2` = number of elements between them (same array only).', 'Adding two pointers is illegal; subtracting is fine.', 'The pointer type determines the scale factor – use `sizeof` for the exact size.'])

# ================================================================= 8
s += H1('8. Pointers and Arrays')
s += [P('In C the <b>name of an array is the address of its first element</b> – effectively a constant pointer. So `A` and `&A[0]` are the same address, and array indexing is just pointer arithmetic in disguise.')]
s += TABLE([['Expression', 'Meaning'], ['`A`', 'address of A[0] (the base address)'], ['`A + i`', 'address of A[i]  (same as `&A[i]`)'], ['`*(A + i)`', 'value of A[i]  (same as `A[i]`)'], ['`p = A;` then `p[i]` or `*(p + i)`', 'a pointer can be indexed like an array']], [2.6, 4.9])
s += CODE('''
#include <stdio.h>

int main(void) {
    int A[5] = {1, 2, 3, 4, 5}, *p = A, i;
    for (i = 0; i < 5; i++)
        printf("%d ", *(p + i));                     /* same as A[i] and p[i] */
    printf("\\n");
    for (p = A; p < A + 5; p++)                      /* walk with p++         */
        printf("%d ", *p);
    printf("\\n");
    printf("A[2]=%d  *(A+2)=%d  2[A]=%d\\n", A[2], *(A + 2), 2[A]);
    printf("sizeof(A) = %zu, sizeof(p) = %zu\\n", sizeof(A), sizeof(p));
    return 0;
}
''', run=True)
s += NOTE('<b>Array name vs pointer variable:</b> `p = A; p++;` is fine, but `A++` or `A = p;` is an error – the array name is a constant address. Also `sizeof(A)` is the whole array (20 bytes) whereas `sizeof(p)` is just the pointer (8 bytes).')
s += [H2('8.1 Pointer to an array')]
s += [P('`int *p = arr;` points to the first <i>element</i> (one int); `p + 1` moves 4 bytes. `int (*q)[5] = &arr;` is a <b>pointer to the whole array of 5 ints</b>; `q + 1` moves a full 5 × 4 = 20 bytes. The parentheses matter: `int *q[5]` is an <i>array of 5 pointers</i>, which is a different thing.')]
s += CODE('''
#include <stdio.h>

int main(void) {
    int A[5] = {1, 2, 3, 4, 5};
    int *p = A;                          /* pointer to the first int          */
    int (*q)[5] = &A;                    /* pointer to the whole array of 5   */
    printf("A[2] via q = %d\\n", (*q)[2]);
    printf("p+1 moves %ld bytes\\n", (long)((char *)(p + 1) - (char *)p));
    printf("q+1 moves %ld bytes\\n", (long)((char *)(q + 1) - (char *)q));
    return 0;
}
''', run=True)
s += RECALL(['Array name = constant pointer to the first element: `A ≡ &A[0]`, `A + i ≡ &A[i]`, `*(A + i) ≡ A[i]`.', '`p = A;` makes p walk the array; `A` itself cannot be changed.', '`int (*q)[N]` is a pointer to an array of N ints and advances a whole array per step.', '`sizeof(A)` = whole array; `sizeof(p)` = pointer size.'])
s += QA('g', 'Given `int A[4] = {2, 3, 5, 7}; int *p = A;` find `p + 2`, `*(p + 2)` and `p[3]`.', [('lines', ['`p + 2` = the address of `A[2]` (base + 2 × 4 bytes)', '`*(p + 2)` = `A[2]` = <b>5</b>', '`p[3]` = `A[3]` = <b>7</b>'])])

# ================================================================= 9
s += H1('9. Pointer to Pointer (Double Pointer)')
s += [P('A <b>double pointer</b> stores the address of another <i>pointer</i>. Following the chain takes two dereferences: `**dptr` → `*ptr` → the original variable.')]
s += SYNTAX('<b>data_type **ptr_name;</b> &nbsp; e.g. `int a = 100; int *ptr = &a; int **dptr = &ptr;`'.replace('&nbsp;', ' '))
s += CODE('''
  a    = 100       address 1000
  ptr  = 1000      address 2000        (ptr  = &a)
  dptr = 2000      address 3000        (dptr = &ptr)

  **dptr  ->  *ptr  ->  a  ->  100
''', label='Chain of indirection (illustrative addresses)')
s += CODE('''
#include <stdio.h>

/* changes the int the pointer points to */
void set(int **pp) { **pp = 99; }
/* changes the POINTER itself */
void retarget(int **pp, int *other) { *pp = other; }

int main(void) {
    int a = 100, b = 7;
    int *ptr = &a;
    int **dptr = &ptr;
    printf("a=%d *ptr=%d **dptr=%d\\n", a, *ptr, **dptr);
    **dptr = 200;                              /* changes a */
    printf("a now = %d\\n", a);
    set(&ptr);
    printf("a after set = %d\\n", a);
    retarget(&ptr, &b);                        /* ptr now points to b */
    printf("*ptr = %d\\n", *ptr);
    return 0;
}
''', run=True)
s += BUL(['<b>Uses:</b> letting a function change a <i>pointer</i> in its caller (e.g. allocate memory and hand it back), dynamic 2-D arrays, arrays of strings, and `char **argv` in `main(int argc, char **argv)`.', 'Each `*` in the declaration adds one level of indirection; each `*` in an expression removes one.'])
s += RECALL(['`int **dptr` is a pointer to a pointer to int; `dptr = &ptr;`.', '`**dptr` reaches the original variable; `*dptr` is the inner pointer.', 'Main use: modifying a pointer from inside a called function.'])
s += QA('r', 'Write a program that uses a double pointer to change the value of a variable from inside a function whose parameter is `int **`.', [('steps', ['The function takes `int **pp` – the address of a pointer.', '`*pp` is the pointer, so `**pp` is the int it points to; assign 99 to `**pp`.', 'In main, create `int x = 1; int *p = &x;` and call `set(&p);`.', 'x becomes 99.'])], code=CODE('''
#include <stdio.h>

void set(int **pp) { **pp = 99; }

int main(void) {
    int x = 1;
    int *p = &x;
    set(&p);
    printf("%d\\n", x);
    return 0;
}
''', run=True))

# ================================================================= 10
s += H1('10. Array of Pointers')
s += [P('An <b>array of pointers</b> is an array in which every element is itself a pointer: `type *arr[size];`. `arr[i]` is a pointer and `*arr[i]` is the value it points to. The most common use is an <b>array of strings</b>, where each element points to a string of its own length (a "ragged" table).')]
s += CODE('''
#include <stdio.h>
#include <string.h>

int main(void) {
    int v1 = 10, v2 = 20, v3 = 30;
    int *pa[3] = {&v1, &v2, &v3};                 /* array of 3 int pointers */
    for (int i = 0; i < 3; i++)
        printf("%d ", *pa[i]);
    printf("\\n");
    *pa[1] = 99;                                   /* changes v2 */
    printf("v2 = %d\\n", v2);

    char *days[] = {"Mon", "Tuesday", "Wed"};      /* each string has its own length */
    for (int i = 0; i < 3; i++)
        printf("%s (%zu chars)\\n", days[i], strlen(days[i]));
    return 0;
}
''', run=True)
s += TABLE([['Declaration', 'Meaning'], ['`int *arr[3];`', 'array of 3 pointers to int'], ['`int (*arr)[3];`', 'pointer to an array of 3 ints'], ['`char *s[] = {"a", "bc"};`', 'array of strings (each element points to a string literal)'], ['`char s[2][4] = {"a", "bc"};`', '2-D char array: always 2 × 4 bytes, wasting space on short strings']], [3, 4.5])
s += RECALL(['`int *arr[3]` – array of 3 int pointers; `arr[i]` is a pointer, `*arr[i]` the value.', '`char *s[]` is the usual way to store a list of strings.', 'Do not confuse with `int (*arr)[3]` – a pointer to an array.'])

# ================================================================= 11
s += H1('11. Pointer to Function')
s += [P('Functions also live in memory, so a <b>function pointer</b> can store a function\'s address and call it later. This allows <i>callbacks</i>, menus and dispatch tables, and generic routines such as `qsort`.')]
s += SYNTAX('<b>return_type (*ptr_name)(param_types);</b> &nbsp; e.g. `int (*fp)(int, int) = add;` &nbsp; call: <b>fp(3, 4)</b> or <b>(*fp)(3, 4)</b>. The function name alone (without `&`) already yields its address. The parentheses in `(*fp)` are essential: `int *fp(int, int)` would declare a function returning an int pointer.'.replace('&nbsp;', ' '))
s += CODE('''
#include <stdio.h>

void greet(int x)        { printf("Value: %d\\n", x); }
int  add(int a, int b)   { return a + b; }
int  square(int x)       { return x * x; }
int  twice(int x)        { return 2 * x; }

void apply(int arr[], int n, int (*fn)(int)) {        /* function pointer as argument */
    for (int i = 0; i < n; i++) arr[i] = fn(arr[i]);
}

int main(void) {
    void (*fp1)(int) = &greet;
    int (*fp2)(int, int) = add;
    int (*table[2])(int) = {square, twice};            /* array of function pointers */
    int a[4] = {1, 2, 3, 4};

    (*fp1)(42);
    printf("3+4 = %d\\n", fp2(3, 4));
    apply(a, 4, square);
    for (int i = 0; i < 4; i++) printf("%d ", a[i]);
    printf("\\n");
    printf("table[1](21) = %d\\n", table[1](21));
    return 0;
}
''', run=True)
s += RECALL(['`int (*fp)(int, int)` – pointer to a function taking two ints and returning int.', '`fp = func;` and `fp = &func;` are both valid; call with `fp(args)` or `(*fp)(args)`.', 'The signature of the pointer must match the function exactly.', 'Uses: callbacks, runtime dispatch, generic algorithms (`qsort`).'])
s += QA('y', 'Declare a function pointer for `int max(int, int)`, assign it and call through it.', [('steps', ['Declaration: `int (*fp)(int, int);` – fp points to a function taking two ints and returning int.', 'Assignment: `fp = max;` (or `fp = &max;`).', 'Call: `int result = fp(10, 20);` – or `(*fp)(10, 20)`.'])],
        code=CODE('''
#include <stdio.h>

int max(int a, int b) { return a > b ? a : b; }

int main(void) {
    int (*fp)(int, int) = max;
    int result = fp(10, 20);
    printf("%d\\n", result);
    return 0;
}
''', run=True))

# ================================================================= 12
s += H1('12. Passing Pointers to Functions and Returning Pointers')
s += [P('All arguments in C are passed by value. To let a function modify the caller\'s variable, pass its <b>address</b>; inside the function `*p` reaches the original. This is also why `scanf` needs `&var`.')]
s += CODE('''
#include <stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int compute(int a, int b, int *psum, int *pdiff) {   /* "returns" three values */
    *psum = a + b;
    *pdiff = a - b;
    return a * b;
}

int *larger(int *p, int *q) { return *p > *q ? p : q; }   /* returning a pointer */

int main(void) {
    int x = 5, y = 20, s, d, prod;
    swap(&x, &y);
    printf("%d %d\\n", x, y);
    prod = compute(10, 3, &s, &d);
    printf("sum=%d diff=%d prod=%d\\n", s, d, prod);
    printf("larger = %d\\n", *larger(&x, &y));
    return 0;
}
''', run=True)
s += WARN('<b>Never return a pointer to a local variable.</b> `int *f(void) { int x = 5; return &x; }` returns the address of memory that no longer exists once `f` returns (a dangling pointer). Return a pointer to a global/static variable, to something passed in (as `larger` does), or to heap memory from `malloc`.')
s += QA('y', 'Write a function that swaps two integers using pointers and explain why passing by value does not work.', [('steps', ['Pass the addresses: `swap(&x, &y);` with parameters `int *a, int *b`.', 'Inside, use a temporary: `t = *a; *a = *b; *b = t;`.', 'With pass-by-value the function receives <i>copies</i>; swapping the copies has no effect on the caller\'s variables.']), 'The `swap` function in the program above demonstrates it (x = 5, y = 20 become 20 and 5).'])

# ================================================================= 13
s += H1('13. Dynamic Memory in Brief — malloc and free')
s += [P('An array declared as `int a[100];` has a size fixed at compile time. `malloc` asks the operating system for a block of <b>heap</b> memory <i>at run time</i> and returns a pointer to it (full treatment – `calloc`, `realloc`, leaks – is in Unit 5).')]
s += SYNTAX('<b>ptr = (type *) malloc(n * sizeof(type));</b> – returns `void *` (cast to the needed type), or NULL if there is not enough memory. <b>free(ptr);</b> releases the block.')
s += CODE('''
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, i;
    scanf("%d", &n);
    int *A = (int *) malloc(n * sizeof(int));
    if (A == NULL) {                               /* always check */
        printf("No memory\\n");
        return 1;
    }
    for (i = 0; i < n; i++) A[i] = i * i;
    for (i = 0; i < n; i++) printf("%d ", A[i]);
    printf("\\n");
    free(A);                                       /* give it back; never free twice */
    return 0;
}
''', run=True, stdin='5\n', label='input: 5')
s += RECALL(['`malloc(n)` returns a `void *` to n bytes of heap memory (or NULL).', 'Always check the result for NULL; always `free` what you allocate, exactly once.', 'Heap memory stays allocated until freed or the program ends.'])
s += QA('r', 'What is the difference between `int *p[3]`, `int (*p)[3]` and `int **p`?', [('lines', ['`int *p[3]` – an <b>array of 3 pointers</b> to int.', '`int (*p)[3]` – a <b>pointer to an array</b> of 3 ints (p + 1 moves 12 bytes).', '`int **p` – a <b>pointer to a pointer</b> to int.'])])

ok = build(sys.argv[1] if len(sys.argv) > 1 else '/home/sleepy/STUDY:)/sem-1/CP/cpclaude/Unit4_Notes.pdf', 4, 'Recursion & Pointers', '', '8 hrs · 20% weightage · C language',
           'Recursion (factorial, Fibonacci, Ackermann …) · pointers · pointer to pointer · pointers and arrays · pointer to array · array of pointers · pointers to functions', '#0b6fa4', s)
print('BUILD OK' if ok else 'BUILD HAS PROBLEMS')
