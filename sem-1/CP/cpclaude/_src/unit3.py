import sys
from lib import *
from unit3a import s

# ================================================================= 4
s += H1('4. Functions — Concept, Prototype, Definition and Call')
s += [P('A <b>function</b> is a self-contained block of statements that performs one specific task and can be used (<i>called</i>) from anywhere in the program. Every C program is a collection of functions, and execution starts at `main()`.')]
s += [H2('4.1 Why use functions?')]
s += BUL(['<b>Avoid repetition</b> – write the code once, call it many times.', '<b>Modularity</b> – split a large problem into small, manageable pieces (top-down design).', '<b>Readability and debugging</b> – each function can be understood and tested on its own.', '<b>Reuse and abstraction</b> – the caller needs to know <i>what</i> a function does, not <i>how</i>.'])
s += BUL(['<b>Library functions</b> – already written and compiled: `printf`, `scanf`, `sqrt`, `strlen`.', '<b>User-defined functions</b> – written by the programmer for a specific need.'])
s += [H2('4.2 Anatomy of a function')]
s += CODE('''
/* 1. Prototype (declaration): tells the compiler name, return type, parameter types */
return_type function_name(type1 param1, type2 param2);

/* 2. Definition: header + body */
return_type function_name(type1 param1, type2 param2) {
    /* body */
    return value;
}

/* 3. Call */
result = function_name(arg1, arg2);
''', label='General form')
s += TABLE([['Term', 'Meaning'], ['<b>Prototype</b>', 'Declaration placed before the first call. Parameter names are optional (`int sum(int, int);`). Required when the definition comes <i>after</i> the call, so the compiler can check argument types.'],
            ['<b>Definition</b>', 'The header (return type, name, parameter list) plus the body in braces.'], ['<b>Formal parameters</b>', 'Variables in the definition (`int a, int b`) that receive the values.'], ['<b>Actual arguments</b>', 'The values or expressions in the call (`sum(x, y)`).'],
            ['<b>Return value</b>', '`return expr;` sends one value back <i>and</i> ends the function. A `void` function returns nothing.']], [1.6, 5.9])
s += BUL(['A function returns <b>only one value</b> (use pointers or arrays to hand back more).', 'Variables declared inside a function (and its parameters) are <b>local</b> – they exist only while the function runs and are invisible to other functions.', 'Calling a function that was never declared, or with the wrong argument types, is a common compile-time error.'])
s += CODE('''
#include <stdio.h>

int sum(int, int);                       /* prototype */
float circle_area(float r);
void print_div7(int n);

int main(void) {
    int x = 3, y = 4;
    printf("%d\\n", sum(x, y));
    printf("%.2f\\n", circle_area(2.0f));
    print_div7(21);
    print_div7(10);
    return 0;
}

int sum(int a, int b) {                  /* definition */
    return a + b;
}

float circle_area(float r) {
    return 3.14159f * r * r;
}

void print_div7(int n) {                 /* void: returns nothing */
    if (n % 7 == 0) printf("%d is divisible by 7\\n", n);
    else            printf("%d is NOT divisible by 7\\n", n);
}
''', run=True)
s += [H3('Functions calling functions – nCr')]
s += CODE('''
#include <stdio.h>

int fact(int n);
int ncr(int n, int r);

int main(void) {
    printf("C(5,2) = %d\\n", ncr(5, 2));
    return 0;
}

int ncr(int n, int r) { return fact(n) / fact(r) / fact(n - r); }

int fact(int n) {
    int i, t = 1;
    for (i = 1; i <= n; i++) t *= i;
    return t;
}
''', run=True, label='main → ncr → fact (nested calls)')
s += RECALL(['Prototype = declaration, placed before the first call; definition = header + body.', '`return` sends a value back and terminates the function; `void` functions need no value.', 'Parameters and local variables exist only inside the function.', 'A function can return only one value.', 'Execution always starts at `main()`.'])

# ================================================================= 5
s += H1('5. Parameter Passing — By Value and By Reference')
s += [P('In C, arguments are passed <b>by value</b> by default: the function receives a <i>copy</i> of each argument, so changing the parameter inside the function does <b>not</b> affect the caller\'s variable. To let a function modify the caller\'s variable, pass its <b>address</b> using a pointer (`&var` in the call, `*param` in the function). This is called <b>simulated pass by reference</b>.')]
s += TABLE([['Basis', 'Call by value', 'Call by reference (pointer)'], ['What is passed', 'A copy of the value', 'The address of the variable'], ['Effect on the original', 'None', 'Original can be changed through `*p`'], ['Call syntax', '`f(x)`', '`f(&x)`'], ['Parameter declaration', '`void f(int n)`', '`void f(int *n)`'], ['Typical use', 'Calculations, read-only input', 'swap, modify in place, return several results']], [1.6, 2.8, 3.1])
s += CODE('''
#include <stdio.h>

void add_val(int n) { n = n + 10; printf("inside (value): %d\\n", n); }
void add_ref(int *n) { *n = *n + 10; printf("inside (ref)  : %d\\n", *n); }

void swap_val(int a, int b) {            /* swaps copies only */
    int t = a; a = b; b = t;
}
void swap_ref(int *a, int *b) {          /* swaps the originals */
    int t = *a; *a = *b; *b = t;
}

int main(void) {
    int num = 2, a = 1, b = 2, c = 3, d = 4;
    add_val(num);  printf("outside        : %d\\n", num);
    add_ref(&num); printf("outside        : %d\\n", num);
    swap_val(a, b); printf("after swap_val : a=%d b=%d\\n", a, b);
    swap_ref(&c, &d); printf("after swap_ref : c=%d d=%d\\n", c, d);
    return 0;
}
''', run=True)
s += [H2('5.1 Passing arrays to functions')]
s += [P('An array name, when used as an argument, stands for the <b>address of its first element</b>, so the function works on the <i>original</i> array – changes made inside are visible to the caller. Because the function receives only an address, it cannot know the length; pass the size as a separate parameter. (`void f(int x[], int n)` and `void f(int *x, int n)` mean exactly the same thing.)')]
s += CODE('''
#include <stdio.h>

int find_min(int x[], int size) {
    int min = x[0];
    for (int i = 1; i < size; i++)
        if (x[i] < min) min = x[i];
    return min;
}

void double_all(int x[], int size) {            /* modifies the caller's array */
    for (int i = 0; i < size; i++) x[i] *= 2;
}

int main(void) {
    int a[] = {5, 2, 8, 1, 9};
    printf("min = %d\\n", find_min(a, 5));
    double_all(a, 5);
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);
    printf("\\n");
    return 0;
}
''', run=True)
s += RECALL(['By value: function gets a copy, the original is unchanged.', 'By reference: pass `&var`, dereference with `*` inside the function.', 'Arrays are effectively passed by reference (the base address is passed).', 'Always pass the array size as a separate parameter.', 'Use call by reference for swap, in-place modification and multiple results.'])
s += QA('g', 'Write a function `isPrime(int n)` that returns 1 if n is prime and 0 otherwise.', [('steps', ['Numbers below 2 are not prime – return 0.', 'Test divisors i = 2, 3, … while i × i ≤ n (a factor larger than √n would pair with one smaller than √n).', 'If any i divides n exactly, return 0; if none do, return 1.'])],
        code=CODE('''
#include <stdio.h>

int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return 0;
    return 1;
}

int main(void) {
    for (int n = 1; n <= 20; n++)
        if (isPrime(n)) printf("%d ", n);
    printf("\\n");
    return 0;
}
''', run=True))
s += QA('y', 'Write a function that swaps two integers using call by reference and show that the originals change in `main()`.', [('steps', ['The parameters are pointers: `int *a, int *b`.', 'Save `*a` in a temporary, copy `*b` into `*a`, then copy the temporary into `*b`.', 'In main, pass the addresses: `swap(&x, &y);`.'])],
        code=CODE('''
#include <stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void) {
    int x = 10, y = 20;
    swap(&x, &y);
    printf("x = %d, y = %d\\n", x, y);
    return 0;
}
''', run=True))
s += QA('y', 'Why does `void swap(int a, int b)` fail to swap the caller\'s variables?', [('steps', ['Arguments are passed by value, so a and b are <i>copies</i> of the caller\'s variables.', 'The function swaps the copies; they are destroyed when it returns.', 'The caller\'s variables were never touched. Use pointers to change them.'])])
s += QA('r', 'Write a function to compute nCr = n! / (r! (n−r)!) using a recursive factorial, and use it in `main()` to compute C(5,2).', [('work', '''
C(5,2) = 5! / (2! x 3!)
       = 120 / (2 x 6)
       = 120 / 12
       = 10
'''), 'The program below confirms the value.'],
        code=CODE('''
#include <stdio.h>

int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
int ncr(int n, int r) { return fact(n) / (fact(r) * fact(n - r)); }

int main(void) {
    printf("C(5,2) = %d\\n", ncr(5, 2));
    return 0;
}
''', run=True))

# ================================================================= 6
s += H1('6. Macros and the Pre-Processor')
s += [P('The <b>pre-processor</b> runs <i>before</i> the compiler. Lines starting with `#` are <b>directives</b>: they are instructions for text substitution and file inclusion, not C statements, and they do not end with a semicolon.')]
s += TABLE([['Directive', 'Meaning'], ['`#include <file.h>`', 'Replace the line with the contents of a system header'], ['`#include "file.h"`', 'Same, but search the current folder first (your own headers)'], ['`#define NAME value`', 'Object-like macro: replace every `NAME` with `value` (no memory is used)'],
            ['`#define F(x) expr`', 'Function-like macro: replace `F(arg)` with `expr` using the argument text'], ['`#undef NAME`', 'Remove a macro definition'], ['`#ifdef` / `#ifndef` / `#else` / `#endif`', 'Conditional compilation – keep or drop a block of code']], [2.4, 5.1])
s += [H2('6.1 Object-like macros (symbolic constants)')]
s += CODE('''
#include <stdio.h>
#define PI   3.1415926
#define MAXN 100

int main(void) {
    float r = 2.0f;
    float area = PI * r * r;       /* becomes 3.1415926 * r * r before compiling */
    printf("area = %.3f, MAXN = %d\\n", area, MAXN);
    return 0;
}
''', run=True)
s += [H2('6.2 Function-like macros – and their traps')]
s += [P('A macro argument is substituted as <i>text</i>, so operator precedence can silently change the meaning. Put parentheses around <b>every</b> use of a parameter <b>and</b> around the whole expression.')]
s += CODE('''
#include <stdio.h>
#define SQR_BAD(x)  x * x
#define SQR(x)      ((x) * (x))
#define MAX(a, b)   ((a) > (b) ? (a) : (b))
#define MAX3(a,b,c) MAX(MAX(a, b), c)

int main(void) {
    printf("SQR_BAD(2+3) = %d   (expands to 2+3*2+3)\\n", SQR_BAD(2 + 3));
    printf("SQR(2+3)     = %d   (expands to ((2+3)*(2+3)))\\n", SQR(2 + 3));
    printf("MAX(3,7)     = %d\\n", MAX(3, 7));
    printf("MAX3(3,7,5)  = %d\\n", MAX3(3, 7, 5));
    int i = 3;
    printf("SQR(i++) = %d   (result unspecified: i++ is evaluated twice)\\n", SQR(i++));
    return 0;
}
''', run=True, warn_ok=True)
s += WARN('Macros are <b>not functions</b>: no type checking, no call, and an argument with a side effect (`SQR(i++)`) is evaluated more than once. Prefer a real function when the logic is more than a short expression.')
s += [H2('6.3 Conditional compilation')]
s += [P('`#ifdef NAME … #endif` keeps the enclosed code only if the macro is defined – handy for debug output. `#ifndef` is the opposite and is used as an <b>include guard</b> in headers so a header is not processed twice.')]
s += CODE('''
/* mylib.h */
#ifndef MYLIB_H
#define MYLIB_H
int add(int a, int b);
#endif

/* in a .c file */
#define DEBUG
#ifdef DEBUG
    printf("x = %d\\n", x);          /* compiled only when DEBUG is defined */
#endif
''', label='Include guard and a debug switch')
s += TABLE([['Basis', 'Macro', 'Function'], ['Processed by', 'Pre-processor (text substitution)', 'Compiler (real code)'], ['Type checking', 'None', 'Yes'], ['Speed', 'No call overhead (inline text)', 'Call and return overhead'], ['Code size', 'Grows with every use', 'One copy in memory'],
            ['Side effects', 'Argument may be evaluated several times', 'Argument evaluated exactly once'], ['Recursion', 'Not possible', 'Possible'], ['Best for', 'Constants, tiny speed-critical expressions', 'Anything with logic, loops or recursion']], [1.5, 3, 3])
s += RECALL(['The pre-processor runs before compilation; directives start with `#` and have no semicolon.', '`#define PI 3.14` – textual substitution, no memory, no type.', 'Function-like macros need parentheses: `#define SQR(x) ((x)*(x))`.', '`#ifdef` / `#ifndef` give conditional compilation and include guards.', 'Macros are fast but have no type safety and can repeat side effects.'])
s += QA('g', 'What does `#define SQR(x) x*x` give for `SQR(2+3)`? How do you fix it?', [('steps', ['The text is substituted: `SQR(2+3)` becomes `2+3*2+3`.', '`*` binds tighter than `+`: 2 + (3×2) + 3 = 2 + 6 + 3 = <b>11</b>, not 25.', 'Fix: `#define SQR(x) ((x)*(x))` → `((2+3)*(2+3))` = <b>25</b>.'])])
s += QA('y', 'Write a macro `MAX3(a,b,c)` that returns the largest of three numbers.', [('steps', ['First define a two-argument macro: `#define MAX(a,b) ((a)>(b)?(a):(b))`.', 'Then build on it: `#define MAX3(a,b,c) MAX(MAX(a,b),c)`.', 'Trace `MAX3(3,7,5)`: MAX(3,7) = 7, then MAX(7,5) = <b>7</b>.'])])
s += QA('r', 'Explain the difference between a macro and a function and when you would prefer each.', [('lines', ['<b>Macro:</b> textual substitution by the pre-processor; no type checking; no call overhead; code is repeated at every use.', '<b>Function:</b> compiled code with type checking and a stack frame; single copy in memory; evaluates arguments once; can be recursive.', '<b>Prefer a macro</b> for constants and very short, speed-critical expressions (SQR, MAX).', '<b>Prefer a function</b> for complex logic, recursion and whenever type safety matters.'])])

# ================================================================= 7
s += H1('7. Quick Reference — Syntax Cheat Sheet')
s += TABLE([['Construct', 'Syntax / example'], ['1-D array', '`int a[10];`   `int a[] = {1,2,3};`   access `a[i]`'], ['2-D array', '`int m[3][4];`   `int m[2][3] = {{1,2,3},{4,5,6}};`   access `m[i][j]`'], ['String declare', '`char s[20];`   `char s[] = "Hello";`'], ['String input', '`scanf("%s", s);`   `fgets(s, sizeof s, stdin);`'],
            ['String output', '`printf("%s", s);`   `puts(s);`'], ['Library', '`strlen(s)`  `strcpy(d,s)`  `strcat(d,s)`  `strcmp(a,b)`  (0 = equal)'], ['Prototype', '`return_type fname(type1, type2);`'], ['Definition', '`int add(int a, int b) { return a + b; }`'], ['Call', '`int s = add(3, 4);`'],
            ['By value', '`void f(int x) { x = 0; }`  – caller unchanged'], ['By reference', '`void f(int *x) { *x = 0; }`  call `f(&v)` – caller changed'], ['Constant macro', '`#define PI 3.14159`'], ['Function macro', '`#define SQR(x) ((x)*(x))`'], ['Conditional', '`#ifdef DEBUG ... #endif`']], [1.6, 5.9])

ok = build(sys.argv[1] if len(sys.argv) > 1 else '/home/sleepy/STUDY:)/sem-1/CP/cpclaude/Unit3_Notes.pdf', 3, 'Arrays, Strings & Functions', '', '8 hrs · 25% weightage · C language',
           'Arrays (1-D, 2-D) · strings and string functions · user-defined functions · prototypes · parameter passing · macros and the pre-processor', '#1b7a43', s)
print('BUILD OK' if ok else 'BUILD HAS PROBLEMS')
