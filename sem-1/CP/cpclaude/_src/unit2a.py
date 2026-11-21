from lib import *
s = []

# ================================================================= 1
s += H1('1. Structure of a C Program')
s += [P('C is a general-purpose, block-structured, procedural, imperative language. It was invented in the early 1970s at Bell Labs, standardised by ANSI in 1989 (<b>ANSI C / C89</b>) and revised in 1999 (<b>C99</b>). It is small (only 32 keywords in ANSI C, about 20 commonly used), fast (compiles close to the hardware) and portable (a program written on one system runs with little or no modification on another).')]
s += [H2('1.1 Sections of a C program')]
s += TABLE([['Section', 'Description', 'Example'],
            ['1. Documentation', 'Comments giving purpose, author, date', '`/* Author: A. Kumar, 2026 */`'],
            ['2. Preprocessor / link', '`#include` and `#define` lines, processed <i>before</i> compilation', '`#include <stdio.h>`  `#define PI 3.14159`'],
            ['3. Global declarations', 'Global variables and function prototypes, visible to the whole file', '`int global_var = 10;`  `int square(int x);`'],
            ['4. main() function', 'Entry point; every program has exactly one main(); contains local declarations and statements', '`int main(void) { ... return 0; }`'],
            ['5. User-defined functions', 'Other functions written by the programmer, called from main() or each other', '`int square(int x) { return x*x; }`']], [1.5, 3.4, 2.6])
s += CODE('''
/* ----- program to print the square of a number ----- */
#include <stdio.h>              /* preprocessor directive          */
#define PI 3.14159              /* symbolic constant               */
int square(int x);              /* function prototype              */
int global_var = 10;            /* global variable                 */

int main(void) {                /* main() function                 */
    int a = 10;                 /* local variable                  */
    printf("The square of %d is %d\\n", a, square(a));
    return 0;
}

int square(int x) {             /* user-defined function           */
    return x * x;
}
''', run=True, label='Full structure of a C program')
s += [H2('1.2 Comments')]
s += BUL(['`/* ... */` – multi-line comment; everything between the markers is ignored by the compiler.', '`// ...` – single-line comment (C99 onward).', 'Comments <b>cannot be nested</b>: `/* a /* b */ c */` is invalid because the first `*/` ends the comment.', 'Good practice: start every program with a comment giving its purpose, author and date.'])
s += [H2('1.3 Header files')]
s += [P('`#include <file>` includes a standard header (angle brackets – searched in the system directories); `#include "file"` includes a user-defined header (double quotes – searched in the current folder first). Header files end in `.h` and contain <i>declarations</i> of library functions; the actual code is brought in at the link stage.')]
s += TABLE([['Header', 'Purpose', 'Typical functions'],
            ['stdio.h', 'Standard input/output', 'printf, scanf, getchar, putchar, fopen'],
            ['math.h', 'Mathematical functions', 'sqrt, pow, sin, cos, fabs, floor, ceil'],
            ['string.h', 'String handling', 'strlen, strcpy, strcmp, strcat'],
            ['stdlib.h', 'Memory allocation, conversions, exit()', 'malloc, free, atoi, rand, exit'],
            ['ctype.h', 'Character tests', 'isdigit, isalpha, isupper, toupper'],
            ['limits.h / float.h', 'Limits of the integer / float types', 'INT_MAX, FLT_MAX']], [1.4, 2.8, 3.3])
s += NOTE('`main()` returns an `int`. `return 0;` tells the operating system the program finished successfully; a non-zero value signals an error. Every statement ends with a semicolon; `\\n` produces a newline.')
s += RECALL(['5 sections: documentation, link/preprocessor, global declarations, main(), user-defined functions.', 'Comments: `/* multi */` or `// single`; they never nest.', 'Every statement ends with `;`.', '`#include <stdio.h>` is needed for printf/scanf.', 'Exactly one `main()`; `return 0` = success.'])
s += QA('g', 'Write the simplest C program that prints "Hello, Adani!".', 'Include `stdio.h`, define `main()`, call `printf` and return 0.',
        code=CODE('''
#include <stdio.h>

int main(void) {
    printf("Hello, Adani!\\n");
    return 0;
}
''', run=True))
s += QA('y', 'Name the sections of a C program and give one example of each.', [('lines', ['<b>Documentation</b> – `/* Author: ... */`', '<b>Link / preprocessor</b> – `#include <stdio.h>`', '<b>Definition / global declarations</b> – `#define MAX 100`, `int g = 10;`', '<b>main() function</b> – `int main(void) { ... }`', '<b>User-defined functions</b> – `int sq(int x) { return x*x; }`'])])
s += QA('r', 'Write a program with a global variable, a `#define` constant and a user-defined function that returns the square of a number. Show the output.', 'The function is declared before main with a prototype, defined after it, and called with the global as argument.',
        code=CODE('''
#include <stdio.h>
#define PI 3.14
int global = 10;
int sq(int x);

int main(void) {
    printf("sq(%d) = %d, PI = %.2f\\n", global, sq(global), PI);
    return 0;
}

int sq(int x) { return x * x; }
''', run=True))

# ================================================================= 2
s += H1('2. Compiling and Executing C Programs')
s += [P('A C source file (e.g. `prog.c`) is a high-level program. The CPU cannot run it directly; it must be translated into machine instructions by a <b>compiler</b>. The compiler translates the whole program and reports all errors at the end. The file must be saved with the `.c` extension.')]
s += [H2('2.1 The compilation pipeline')]
s += TABLE([['Stage', 'Tool', 'Input → Output', 'What happens'],
            ['1. Preprocessing', 'cpp', '.c → expanded .c (.i)', 'Expands `#include`, `#define`, macros; strips comments'],
            ['2. Compilation', 'cc1', '.i → .s', 'Checks syntax; converts to assembly source'],
            ['3. Assembly', 'as', '.s → .o', 'Converts assembly to machine (object) code'],
            ['4. Linking', 'ld', '.o + libraries → executable', 'Combines object files and library code into `a.out`'],
            ['5. Loading', 'loader / OS', 'executable → RAM', 'Copies the program into memory and starts it']], [1.3, 0.9, 2.2, 3.1])
s += CODE('''
gcc prog.c                 # compile + link; output is a.out by default
./a.out                    # run it
gcc -o prog prog.c         # choose the output name; run with ./prog
gcc -Wall prog.c           # switch on all common warnings (recommended)
gcc -E prog.c -o prog.i    # stop after preprocessing
gcc -S prog.c              # stop after compilation -> prog.s
gcc -c prog.c              # stop after assembling -> prog.o
gcc prog.c -lm             # link the maths library (needed for sqrt, pow)
''', label='GCC commands')
s += [H2('2.2 Kinds of errors')]
s += TABLE([['Error', 'When detected', 'Example'],
            ['Syntax error', 'Compile time – no executable is produced', 'Missing `;`, unbalanced braces, misspelt keyword'],
            ['Linker error', 'Link time', '`undefined reference to sqrt` (forgot `-lm`), misspelt function name'],
            ['Run-time error', 'While running', 'Division by zero, invalid memory access'],
            ['Logical error', 'Never reported – wrong output', 'Using `=` instead of `==`, wrong formula']], [1.4, 2.6, 3.5])
s += NOTE('If compilation fails, no `a.out` is created. Fix the errors and recompile. A program can compile without a single error and still give wrong answers – those are logical errors, found only by testing.')
s += RECALL(['Stages: preprocessing → compilation → assembly → linking → loading.', '`gcc prog.c` produces `a.out`; `./a.out` runs it.', '`gcc -o name prog.c` names the output.', 'Add `-lm` to link math.h functions.', 'The compiler reports all errors together at the end.'])
s += QA('g', 'What is the GCC command to compile `hello.c` into an executable named `hello`, and how do you run it?', '`gcc -o hello hello.c`, then run with `./hello`.')
s += QA('y', 'List the five stages from source code to running program and what each one produces.', [('steps', ['<b>Preprocessing</b> → expanded source (macros and includes replaced).', '<b>Compilation</b> → assembly code (.s).', '<b>Assembly</b> → object code (.o).', '<b>Linking</b> → executable file (a.out).', '<b>Loading</b> → the program is copied into RAM and runs.'])])
s += H1('3. Constants, Variables and Data Types')
s += [H2('3.1 Constants (literals)')]
s += [P('<b>Constants</b> (literals) are fixed values that do not change while the program runs; <b>variables</b>, by contrast, are named locations whose value can change.')]
s += TABLE([['Type', 'Examples', 'Notes'],
            ['Integer', '123, −321, 0, +78', 'Digits only – no spaces, commas or `$` (15 750, 20,000 and $1000 are invalid)'],
            ['Octal', '037, 0435', 'Leading 0; digits 0–7 only'],
            ['Hexadecimal', '0x2F, 0X9F, 0xbcd', 'Prefix `0x` or `0X`'],
            ['Real (floating)', '17.548, −0.75, 215., 0.65e4, 12e-2', '`e` means "× 10 to the power"; 0.65e4 = 6500'],
            ['Character', "'A', '5', ';'", 'Single quotes, exactly one character; stored as its ASCII integer'],
            ['String', '"Hello", "1234"', 'Double quotes; stored with a hidden `\\0` terminator']], [1.4, 2.4, 3.7])
s += WARN('A leading zero makes an integer <b>octal</b>: `x = 0042;` stores 4×8 + 2 = <b>34</b>, not 42. Also, `\'A\'` is a character (one byte, value 65) but `"A"` is a string (two bytes: \'A\' and \'\\0\'). `char grade = "A";` is therefore wrong – write `char grade = \'A\';`.')
s += [H3('Escape sequences')]
s += TABLE([['Seq.', 'Meaning', 'Seq.', 'Meaning'], ['\\n', 'newline', '\\t', 'horizontal tab'], ['\\\\', 'backslash', "\\'", 'single quote'], ['\\"', 'double quote', '\\0', 'null character'], ['\\r', 'carriage return', '\\a', 'alert (bell)'], ['\\b', 'backspace', '\\?', 'question mark']], [0.7, 2, 0.7, 2])
s += CODE('''
#include <stdio.h>

int main(void) {
    char cvar = 'A';
    printf("%c %d\\n", cvar, cvar);       /* same value as char and as int */
    printf("octal 0042 = %d, hex 0x2F = %d\\n", 0042, 0x2F);
    printf("Name\\tMarks\\n\\"Asha\\"\\t95\\n");
    return 0;
}
''', run=True, label='Constants and escape sequences')
s += [H2('3.2 Variables and identifiers')]
s += [P('A <b>variable</b> is a named data location that holds exactly one value at a time, and that value may change during execution. Every variable has a <b>type</b> (what kind of value, how much memory) and must be <b>declared</b> before use.')]
s += TABLE([['Naming rule', 'Valid', 'Invalid'],
            ['Start with a letter or underscore, never a digit', 'A, marks, _temp, sn123', '1A'],
            ['Only letters, digits and underscore', 'stud_1, marks_test_1', 'cp-marks, %age, (test), test,marks'],
            ['No white space', 'studentName', 'student name'],
            ['Case-sensitive', '`Student` and `student` are different', '—'],
            ['Not a keyword; keep under 63 characters', 'count', 'int, while, float']], [3.2, 2.4, 2])
s += CODE('''
auto     break    case     char     const    continue  default  do
double   else     enum     extern   float    for       goto     if
int      long     register return   short    signed    sizeof   static
struct   switch   typedef  union    unsigned void      volatile while
''', label='The 32 keywords of ANSI C (cannot be used as names)')
s += CODE('''
#include <stdio.h>

int main(void) {
    int age;                 /* declaration            */
    int marks = 95;          /* declaration + initial value */
    float pi = 3.14f;
    char grade = 'A';
    int a, b, c;
    a = b = c = 5;           /* assignment is right-to-left: all become 5 */
    age = 19;
    printf("%d %d %.2f %c %d %d %d\\n", age, marks, pi, grade, a, b, c);
    return 0;
}
''', run=True, label='Declaring and initialising variables')
s += [H3('Read-only variables with const')]
s += [P('A variable declared with `const` can be given a value at declaration but cannot be changed afterwards; the compiler rejects any later assignment. This prevents accidental modification.')]
s += CODE('''
#include <stdio.h>

int main(void) {
    const float pi = 3.14;
    float area, rad = 2.5;
    area = pi * rad * rad;
    /* pi = 4.0;   <-- compile-time error: assignment of read-only variable */
    printf("Area = %f\\n", area);
    return 0;
}
''', run=True)
s += [H2('3.3 Data types')]
s += TABLE([['Category', 'Types'], ['Primary (basic)', 'char, int, float, double'], ['Derived', 'array, function, pointer'], ['User-defined', 'struct, union, enum, typedef'], ['Void', '`void` – "no value"; used for functions that return nothing']], [1.6, 5.8])
s += TABLE([['Type', 'Size (bits)', 'Range', 'Format'],
            ['char', '8', '−128 to 127', '%c'], ['int', '16 (old) / 32 (modern)', '−32768 to 32767 (16-bit);  −2³¹ to 2³¹−1 (32-bit)', '%d'],
            ['float', '32', '≈ 1.17×10⁻³⁸ to 3.40×10³⁸', '%f'], ['double', '64', '≈ 2.22×10⁻³⁰⁸ to 1.79×10³⁰⁸', '%lf (scanf), %f (printf)'], ['void', '—', 'valueless', '—']], [1, 1.8, 3.5, 1.7])
s += TABLE([['Modifier', 'Applies to', 'Effect'],
            ['short / long', 'int, double (long double)', 'Smaller / larger range'],
            ['signed / unsigned', 'int, char', 'signed (default) allows negatives; unsigned is non-negative only and doubles the positive maximum'],
            ['const', 'any', 'Value cannot change after initialisation'],
            ['volatile', 'any', 'Value may change outside the program (hardware register)']], [1.6, 2.2, 3.7])
s += FORMULA('n-bit <b>signed</b> integer: −2<super>n−1</super> to 2<super>n−1</super> − 1.  n-bit <b>unsigned</b> integer: 0 to 2<super>n</super> − 1.  (16 bits: −32768…32767 signed, 0…65535 unsigned.)')
s += CODE('''
#include <stdio.h>
#include <limits.h>

int main(void) {
    printf("char   : %zu byte(s)\\n", sizeof(char));
    printf("short  : %zu byte(s)\\n", sizeof(short));
    printf("int    : %zu byte(s)\\n", sizeof(int));
    printf("long   : %zu byte(s)\\n", sizeof(long));
    printf("float  : %zu byte(s)\\n", sizeof(float));
    printf("double : %zu byte(s)\\n", sizeof(double));
    printf("INT_MAX = %d, INT_MIN = %d\\n", INT_MAX, INT_MIN);
    return 0;
}
''', run=True, label='Sizes on this machine (64-bit Linux, GCC) – on other systems int/long may differ')
s += RECALL(['Constants are fixed literals; variables are named memory locations.', "'A' is a char (65); \"A\" is a string with a hidden '\\0'.", 'A leading 0 means octal (0042 = 34).', 'Variable names: start with letter/underscore, no spaces, no keywords, case-sensitive.', '4 type categories: primary, derived, user-defined, void.', '`const` forbids later changes; modifiers: short/long, signed/unsigned.'])
s += QA('g', 'Which of these are invalid variable names: `1name`, `_test`, `my-var`, `float`, `test1`?', [('lines', ['`1name` – invalid (starts with a digit)', '`_test` – valid', '`my-var` – invalid (hyphen is not allowed)', '`float` – invalid (reserved keyword)', '`test1` – valid'])])
s += QA('y', 'Declare: an integer age = 20, a float GPA = 8.5, a char grade = \'A\' and a constant integer MAX = 100.', 'Note the single quotes for the char.',
        code=CODE('''
int age = 20;
float GPA = 8.5f;
char grade = 'A';
const int MAX = 100;
'''))
s += QA('y', 'A student writes `int x = 0042;` and expects 42. What does x hold and why?', [('steps', ['A leading 0 makes the literal an <b>octal</b> constant.', 'Octal 0042 = 4×8 + 2×1 = 32 + 2 = <b>34</b>.', 'So x holds 34, not 42. Write `42` (no leading zero) for decimal.'])])
s += QA('r', 'What is the difference between `signed int` and `unsigned int`? Give the 2-byte ranges.', [('lines', ['Both use the same 16 bits but interpret them differently.', '<b>signed</b> – the most significant bit is the sign; range −32768 to 32767.', '<b>unsigned</b> – all 16 bits carry value; range 0 to 65535 (2¹⁶ − 1).'])])
s += H1('4. Operators and Expressions')
s += [P('<b>Operators</b> are symbols that perform operations on <b>operands</b>. An <b>expression</b> combines operators, variables, constants and function calls to produce a value. C has eight broad groups: arithmetic, relational, logical, assignment, increment/decrement, conditional, bitwise and special operators.')]
s += [H2('4.1 Arithmetic operators')]
s += TABLE([['Operator', 'Meaning', 'a = 13, b = 5', 'Result'], ['+', 'Addition', 'a + b', '18'], ['-', 'Subtraction', 'a - b', '8'], ['*', 'Multiplication', 'a * b', '65'], ['/', 'Division', 'a / b', '2 (integer division truncates)'], ['%', 'Modulo (remainder)', 'a % b', '3']], [1, 2, 2, 2.5])
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = 13, b = 5;
    printf("a + b = %d\\n", a + b);
    printf("a - b = %d\\n", a - b);
    printf("a * b = %d\\n", a * b);
    printf("a / b = %d\\n", a / b);
    printf("a %% b = %d\\n", a % b);
    printf("13.0 / 5 = %.1f\\n", 13.0 / 5);
    printf("-13 / 5 = %d, -13 %% 5 = %d\\n", -13 / 5, -13 % 5);
    return 0;
}
''', run=True)
s += NOTE('Integer division discards the fraction (13/5 = 2). `%` works only with integers, and in C the result takes the sign of the <i>left</i> operand (−13 % 5 = −3). Division or modulo by zero is a run-time error.')
s += [H2('4.2 Relational and logical operators')]
s += [P('Relational operators compare two values and give <b>1 (true)</b> or <b>0 (false)</b>: `<`, `<=`, `>`, `>=`, `==`, `!=`. Logical operators combine conditions: `&&` (AND – true when <i>both</i> are non-zero), `||` (OR – true when <i>at least one</i> is non-zero) and `!` (NOT – inverts). In C any non-zero value counts as true.')]
s += WARN('Never write `=` when you mean `==`. `if (a = 5)` <i>assigns</i> 5 to a and is always true. Also `&&` and `||` use <b>short-circuit evaluation</b>: in `a && b`, if a is false b is never evaluated; in `a || b`, if a is true b is never evaluated.')
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = 5, b = 0;
    printf("%d %d %d\\n", a > 3, a == 4, a != b);
    printf("%d %d %d\\n", a && b, a || b, !a);
    if (b != 0 && 10 / b > 1)       /* 10/b is never evaluated */
        printf("big\\n");
    else
        printf("safe: no division by zero\\n");
    return 0;
}
''', run=True)
s += [H2('4.3 Assignment and shorthand operators')]
s += TABLE([['Shorthand', 'Equivalent', 'a = 10, b = 3 →'], ['a += b', 'a = a + b', 'a = 13'], ['a -= b', 'a = a - b', 'a = 7'], ['a *= b', 'a = a * b', 'a = 30'], ['a /= b', 'a = a / b', 'a = 3'], ['a %= b', 'a = a % b', 'a = 1']], [1.5, 2, 2.5])
s += [H2('4.4 Increment and decrement')]
s += BUL(['<b>Pre</b>-increment/decrement `++i`, `--i`: the variable is changed <i>first</i>, then the new value is used.', '<b>Post</b>-increment/decrement `i++`, `i--`: the old value is used <i>first</i>, then the variable is changed.'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int x, a = 10, b = 20;
    x = 50 + ++a;          /* a becomes 11 first, x = 61 */
    printf("x=%d a=%d\\n", x, a);
    a = 10;
    x = 50 + a++;          /* uses 10, then a becomes 11, x = 60 */
    printf("x=%d a=%d\\n", x, a);
    a = 10;
    x = a++ + --b;         /* 10 + 19 = 29; a = 11, b = 19 */
    printf("x=%d a=%d b=%d\\n", x, a, b);
    return 0;
}
''', run=True)
s += [H2('4.5 Conditional (ternary) operator')]
s += SYNTAX('<b>condition ? expr_if_true : expr_if_false</b> – the only ternary (3-operand) operator in C; a compact form of if-else that yields a value.')
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = 7, b = 12, x = 10, y;
    y = (x > 9) ? 100 : 200;
    int max = (a > b) ? a : b;
    printf("y = %d, max = %d\\n", y, max);
    return 0;
}
''', run=True)
s += [H2('4.6 Bitwise operators')]
s += [P('Bitwise operators work on the individual bits of <i>integer</i> operands. Take a = 5 = 00000101 and b = 9 = 00001001.')]
s += TABLE([['Operator', 'Name', 'Example', 'Result'], ['&', 'AND (1 only if both bits 1)', 'a & b', '00000001 = 1'], ['|', 'OR (1 if either bit 1)', 'a | b', '00001101 = 13'], ['^', 'XOR (1 if bits differ)', 'a ^ b', '00001100 = 12'],
            ['~', "One's complement (flip all bits)", '~a', '…11111010 = −6'], ['<<', 'Left shift', 'b << 1', '00010010 = 18'], ['>>', 'Right shift', 'b >> 1', '00000100 = 4']], [1, 2.8, 1.5, 2.2])
s += FORMULA('Left shift by n multiplies by 2<super>n</super> (b &lt;&lt; 1 = 9 × 2 = 18); right shift by n divides by 2<super>n</super> (9 &gt;&gt; 1 = 4). `n & 1` is 1 for odd numbers and 0 for even numbers.'.replace('&lt;', '<').replace('&gt;', '>'))
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = 5, b = 9;
    printf("%d %d %d %d %d %d\\n", a & b, a | b, a ^ b, ~a, b << 1, b >> 1);
    return 0;
}
''', run=True)
s += [H2('4.7 Special operators, L-value and R-value')]
s += TABLE([['Operator', 'Name', 'Usage'], ['`,`', 'Comma', '`val = (x = 10, y = 5, x + y);` evaluates left to right; the rightmost value is the result (15)'], ['`sizeof`', 'Size of', '`sizeof(int)` – size in bytes, computed at compile time'],
            ['`&` `*`', 'Address-of, dereference', '`&var` gives the address; `*ptr` gives the value at that address'], ['`.` `->`', 'Member access', '`s.field`, `p->field` for structures and unions'], ['`[ ]`', 'Array subscript', '`arr[i]`']], [1, 1.8, 4.6])
s += [P('<b>L-value</b>: an expression that refers to a modifiable memory location – it can appear on the <i>left</i> of `=`. <b>R-value</b>: a data value, any expression – it appears on the right.')]
s += TABLE([['Valid', 'Invalid and why'], ['`A = A + 10;`', '`1 = x;` – a constant is not a memory location'], ['`fx = x*x + 2*x;`', '`x + y = a + b;` – an expression cannot be on the left'], ['`x = (a + b) * (c + d);`', '`x + b = 5;` – an expression cannot be on the left']], [3, 4.4])
s += CODE('''
#include <stdio.h>

int main(void) {
    int x = 10, y = 5;
    int val = (x = 10, y = 5, x + y);        /* comma operator */
    printf("sizeof int = %zu, sizeof double = %zu\\n", sizeof(int), sizeof(double));
    printf("val = %d\\n", val);
    return 0;
}
''', run=True)
s += RECALL(['8 operator groups: arithmetic, relational, logical, assignment, inc/dec, conditional, bitwise, special.', 'Pre (`++i`): change, then use. Post (`i++`): use, then change.', 'Ternary: `cond ? a : b`.', '`&&` and `||` short-circuit.', 'Integer division truncates; `%` needs integers.', 'L-value = modifiable location; R-value = value.'])
s += QA('g', 'What is printed by: `int a = 5, b; b = a++; printf("%d %d", a, b);`?', [('steps', ['`b = a++` is post-increment: the <i>old</i> value of a (5) is assigned to b.', 'Then a is incremented to 6.', 'Output: <b>6 5</b> (a first, then b).'])])
s += QA('y', 'Evaluate `x = 100 + 200/10 - 3*10;` step by step.', [('work', '''
x = 100 + 200/10 - 3*10
Step 1:  200/10  = 20          (/ and * come before + and -)
Step 2:  3*10    = 30
Step 3:  100 + 20 = 120        (+ and - left to right)
Step 4:  120 - 30 = 90
'''), 'So x = <b>90</b>.'])
s += QA('y', 'Given a = 10 and b = 20, find x after `x = a++ + --b;` and the final values of a and b.', [('steps', ['`a++` yields the old value 10; afterwards a becomes 11.', '`--b` first makes b = 19 and yields 19.', 'x = 10 + 19 = <b>29</b>.', 'Final values: a = 11, b = 19.'])])
s += QA('r', 'Write a program that uses a bitwise operator to check whether a number is even or odd and explain the trick.', 'The least significant bit of an odd number is 1 and of an even number is 0, so `n & 1` is non-zero exactly for odd numbers.',
        code=CODE('''
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    if (n & 1) printf("%d is odd\\n", n);
    else       printf("%d is even\\n", n);
    return 0;
}
''', run=True, stdin='13\n', label='input: 13'))
