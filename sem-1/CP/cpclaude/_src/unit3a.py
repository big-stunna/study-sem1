from lib import *
s = []

# ================================================================= 1
s += H1('1. Arrays — Concept and One-Dimensional Arrays')
s += [P('Suppose a program must store the marks of 100 students. Declaring `m1, m2, … m100` is clumsy and impossible to loop over. An <b>array</b> solves this: it is a collection of elements of the <b>same data type</b> stored in <b>contiguous</b> (side-by-side) memory locations, and the whole collection has <b>one name</b>. Each element is picked out by an <b>index</b> (subscript) which starts at <b>0</b>.')]
s += SYNTAX('<b>data_type array_name[size];</b>   e.g. `int marks[10];`   `float price[5];`   `char name[20];` – the size must be a positive integer constant (or a constant expression).')
s += [H2('1.1 Declaring and initialising')]
s += BUL(['<b>At declaration</b> with braces: `int marks[5] = {90, 82, 78, 95, 88};`', '<b>Size left out:</b> `int a[] = {1, 2, 3};` – the compiler counts the values and makes the size 3.', '<b>Partial initialisation:</b> `int a[5] = {1, 2};` – the rest become 0. `int z[5] = {0};` zeroes the whole array.', '<b>By input</b> in a loop with `scanf("%d", &a[i]);` or <b>by assignment</b> element by element `a[0] = 10;`.'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int marks[5] = {90, 82, 78, 95, 88};
    int part[5] = {1, 2};                    /* remaining elements are 0 */
    int i;
    for (i = 0; i < 5; i++)
        printf("%d ", marks[i]);
    printf("\\n");
    for (i = 0; i < 5; i++)
        printf("%d ", part[i]);
    printf("\\n");
    printf("size = %zu bytes, elements = %zu\\n",
           sizeof(marks), sizeof(marks) / sizeof(marks[0]));
    return 0;
}
''', run=True)
s += WARN('The first element is `a[0]` and the last valid index is <b>size − 1</b>. C does <u>not</u> check bounds: reading or writing `a[10]` in an array of size 10 is <b>undefined behaviour</b> – it may crash, print garbage, or silently corrupt another variable. Also, you cannot copy arrays with `=` (`arr2 = arr1;` is illegal); copy element by element in a loop.')
s += [H2('1.2 How an array sits in memory – the address formula')]
s += [P('Because the elements are contiguous, the address of any element can be calculated. The <b>base address</b> is the address of the first element `a[0]` (and is what the array name stands for). With `w` bytes per element:')]
s += FORMULA('Address of A[k] = Base_Address(A) + w × (k − lower_bound)    (lower_bound = 0 in C, so &A[k] = Base + w × k).<br/>Length of an array = upper_bound − lower_bound + 1.')
s += NOTE('<b>Worked example.</b> `int marks[] = {99,67,78,56,88,90,34,85};` with Base = 1000 and w = 2 bytes (16-bit int). Address of marks[4] = 1000 + 2 × (4 − 0) = <b>1008</b>. On a modern machine int is 4 bytes, so marks[4] would be at 1000 + 4×4 = 1016.', 'EXAMPLE')
s += [H2('1.3 Common array operations')]
s += BUL(['<b>Traversal</b> – visit every element once with a `for` loop.', '<b>Sum / average / min / max</b> – keep a running value and update it while traversing.', '<b>Searching</b> – linear search compares each element with the key.', '<b>Reversing</b> – loop from `size − 1` down to 0, or swap `a[i]` with `a[n−1−i]` for half the array.', '<b>Copying</b> – `b[i] = a[i]` inside a loop.'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int a[6] = {14, 7, 29, 3, 18, 25};
    int i, min = a[0], max = a[0], sum = 0, key = 18, pos = -1;
    for (i = 0; i < 6; i++) {
        if (a[i] < min) min = a[i];
        if (a[i] > max) max = a[i];
        sum += a[i];
        if (a[i] == key && pos == -1) pos = i;     /* linear search */
    }
    printf("min=%d max=%d sum=%d avg=%.2f\\n", min, max, sum, (float)sum / 6);
    printf("%d found at index %d\\n", key, pos);
    for (i = 5; i >= 0; i--)                       /* reverse print */
        printf("%d ", a[i]);
    printf("\\n");
    return 0;
}
''', run=True, label='Min, max, sum, average, search and reverse in one pass')
s += [H2('1.4 Two-dimensional arrays')]
s += [P('A 2-D array has two subscripts – <b>row</b> and <b>column</b> – and models a matrix or table. C stores it in <b>row-major order</b>: all columns of row 0 first, then row 1, and so on, so `int m[2][3]` occupies 6 consecutive ints in the order m[0][0], m[0][1], m[0][2], m[1][0], m[1][1], m[1][2].')]
s += SYNTAX('<b>data_type name[rows][cols];</b>   e.g. `int var[3][4];`   `float matrix[20][25];`')
s += CODE('''
int d[2][4] = {{10, 11, 12, 13},
               {14, 15, 16, 17}};            /* recommended: one brace per row   */
int e[2][4] = {10, 11, 12, 13, 14, 15, 16, 17};   /* also valid: filled row by row */
int f[][4]  = {1, 2, 3, 4, 5, 6, 7, 8};      /* row count may be omitted         */
/* int g[][] = {...};   INVALID - the column size must always be given */
''', label='2-D initialisation')
s += FORMULA('Address of A[i][j] (row-major) = Base + w × (i × COLS + j).   Example: int A[3][4], Base = 2000, w = 4 → A[2][1] is at 2000 + 4 × (2×4 + 1) = <b>2036</b>.')
s += CODE('''
#include <stdio.h>

int main(void) {
    int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int t[3][2];
    int i, j;
    for (i = 0; i < 2; i++)                  /* transpose: rows become columns */
        for (j = 0; j < 3; j++)
            t[j][i] = a[i][j];
    printf("matrix          transpose\\n");
    for (i = 0; i < 3; i++) {
        if (i < 2) { for (j = 0; j < 3; j++) printf("%d ", a[i][j]); }
        else printf("      ");
        printf("        ");
        for (j = 0; j < 2; j++) printf("%d ", t[i][j]);
        printf("\\n");
    }
    return 0;
}
''', run=True, label='Transpose of a 2 x 3 matrix')
s += CODE('''
#include <stdio.h>

int main(void) {
    int a[2][2] = {{1, 2}, {3, 4}};
    int b[2][2] = {{5, 6}, {7, 8}};
    int c[2][2] = {{0, 0}, {0, 0}};
    int i, j, k;
    for (i = 0; i < 2; i++)
        for (j = 0; j < 2; j++)
            for (k = 0; k < 2; k++)
                c[i][j] += a[i][k] * b[k][j];      /* row of a  x  column of b */
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++)
            printf("%4d", c[i][j]);
        printf("\\n");
    }
    return 0;
}
''', run=True, label='Matrix multiplication (c = a x b)')
s += RECALL(['Array = same-type elements in contiguous memory; index starts at 0; last index = size − 1.', '`int a[] = {1,2,3};` – the compiler fixes the size; unfilled elements of a partial initialiser are 0.', 'No bounds checking in C; `arr2 = arr1` is illegal – copy in a loop.', 'Address of a[k] = Base + w × (k − lower_bound).', '2-D arrays are stored row-major; the column size must always be specified.', 'Address of A[i][j] = Base + w × (i × COLS + j).'])
s += QA('g', 'Write a C program to read 5 integers into an array and print them in reverse order.', [('steps', ['Declare `int a[5]`.', 'Read the values with a loop from index 0 to 4.', 'Print them with a loop from index 4 down to 0.'])],
        code=CODE('''
#include <stdio.h>

int main(void) {
    int a[5], i;
    for (i = 0; i < 5; i++)
        scanf("%d", &a[i]);
    for (i = 4; i >= 0; i--)
        printf("%d ", a[i]);
    printf("\\n");
    return 0;
}
''', run=True, stdin='10 20 30 40 50\n', label='input: 10 20 30 40 50'))
s += QA('y', 'Given `int marks[] = {99,67,78,56,88,90,34,85};` with base address 1000 and int = 2 bytes, find the address of `marks[6]`.', [('work', '''
Address of A[k] = Base + w x (k - lower_bound)
Address of marks[6] = 1000 + 2 x (6 - 0)
                    = 1000 + 12
                    = 1012
'''), 'Answer: <b>1012</b>.'])
s += QA('r', 'Write a C program to multiply two 2×2 matrices a = {{1,2},{3,4}} and b = {{5,6},{7,8}} and print the result.',
        [('steps', ['Each element c[i][j] is the sum over k of a[i][k] × b[k][j] (row of a times column of b).', 'This needs three nested loops (i, j, k) and c must start at 0.', 'Hand check: c[0][0] = 1×5 + 2×7 = 19; c[0][1] = 1×6 + 2×8 = 22; c[1][0] = 3×5 + 4×7 = 43; c[1][1] = 3×6 + 4×8 = 50.']), 'The program in section 1.4 prints exactly [[19, 22], [43, 50]].'])
s += QA('y', 'Why does `int a[5]; a[5] = 10;` compile but is still a bug?', [('lines', ['The valid indices of `a` are 0 to 4.', '`a[5]` is one element past the end; the compiler does not check array bounds.', 'The write overwrites whatever memory follows the array (another variable, or the return address) – <b>undefined behaviour</b>.'])])

# ================================================================= 2
s += H1('2. Strings — Concept and Storage')
s += [P('C has no separate string type. A <b>string</b> is simply a <b>character array that ends with the null character `\\0`</b> (ASCII value 0). The null terminator is how every library function knows where the string ends, so the array must always have room for one extra character.')]
s += SYNTAX('<b>char name[size];</b> – holds up to size − 1 characters plus `\\0`.   <b>char str[] = "Hello";</b> – the compiler adds `\\0`, so 6 bytes are used.   <b>char str[6] = {\'H\',\'e\',\'l\',\'l\',\'o\',\'\\0\'};</b> – the explicit form.')
s += TABLE([['Index', '0', '1', '2', '3', '4', '5'], ['Character', "'H'", "'e'", "'l'", "'l'", "'o'", "'\\0'"], ['ASCII', '72', '101', '108', '108', '111', '0']], [1.4, 1, 1, 1, 1, 1, 1])
s += BUL(['`"Hello"` needs <b>6</b> bytes: five characters plus the terminator. `strlen("Hello")` is 5; `sizeof("Hello")` is 6.', "`'A'` is a single character (one byte, value 65); `\"A\"` is a string of two bytes ('A' and '\\0').", 'A string constant can be assigned only at declaration: `char s[10] = "Hi";` is fine but `s = "Hi";` later is illegal – use `strcpy`.'])
s += [H2('2.1 Reading and writing strings')]
s += TABLE([['Task', 'Function', 'Behaviour'], ['Read a word', '`scanf("%s", str)`', 'Stops at the first whitespace; no `&` needed (the array name is the address)'], ['Read a whole line', '`fgets(str, size, stdin)`', 'Reads up to size−1 characters including spaces; keeps the trailing `\\n`; <b>safe</b>'],
            ['Read a character', '`getchar()`', 'One character at a time'], ['Write a string', '`printf("%s", str)`', 'Prints characters up to `\\0`'], ['Write + newline', '`puts(str)`', 'Prints the string and adds a newline automatically']], [1.4, 2.4, 3.7])
s += WARN('`gets(str)` has no bounds check and was <b>removed from the C11 standard</b> – never use it. Use `fgets(str, sizeof str, stdin)` and, if needed, strip the newline with `str[strcspn(str, "\\n")] = \'\\0\';`. Also remember `scanf("%s")` stops at a space, so "Debashish Roy" would read only "Debashish".')
s += CODE('''
#include <stdio.h>
#include <string.h>

int main(void) {
    char word[20], line[40];
    scanf("%19s", word);                      /* one word  */
    getchar();                                /* eat the newline left in the buffer */
    fgets(line, sizeof line, stdin);          /* whole line */
    line[strcspn(line, "\\n")] = '\\0';         /* remove trailing newline */
    printf("word = %s\\n", word);
    printf("line = %s\\n", line);
    puts("puts adds a newline");
    char name[] = "Klinsman";
    int i = 0;
    while (name[i] != '\\0') {                 /* traversal until the terminator */
        printf("%c", name[i]);
        i++;
    }
    printf("\\n");
    return 0;
}
''', run=True, stdin='Hello\nDebashish Roy\n', label='input: Hello  (then a second line)  Debashish Roy')

# ================================================================= 3
s += H1('3. Built-in String Functions (string.h)')
s += [P('All standard string functions are declared in `<string.h>`. They work on the assumption that every string ends with `\\0`, so they are fast but trust you completely about buffer sizes.')]
s += TABLE([['Function', 'Purpose', 'Example'], ['`strlen(s)`', 'Length of s, not counting `\\0` (returns `size_t`)', '`strlen("Hello")` → 5'], ['`strcpy(d, s)`', 'Copy s (with its `\\0`) into d', '`strcpy(d, "Hi")` → d = "Hi"'], ['`strncpy(d, s, n)`', 'Copy at most n characters (safer; may not add `\\0`)', '`strncpy(d, s, 4)`'],
            ['`strcat(d, s)`', 'Append s to the end of d', 'd = "Hi", s = "!" → "Hi!"'], ['`strcmp(a, b)`', '0 if equal, negative if a < b, positive if a > b', '`strcmp("ab","ac")` → negative'], ['`strchr(s, c)`', 'Pointer to the first c in s (NULL if none)', '`strchr("hello",\'l\')` → "llo"'],
            ['`strstr(h, n)`', 'Pointer to the first occurrence of n in h', '`strstr("hello","ll")` → "llo"'], ['`strrev`, `strupr`, `strlwr`', '<b>Non-standard</b> (Turbo C / Windows only) – not available with GCC on Linux; write loops or use `toupper()`', '—']], [1.7, 3.9, 2.4])
s += FORMULA('`strcmp` compares character by character using ASCII codes and returns the <b>difference of the first pair that differs</b> (or just a sign – the exact number is implementation-dependent, so test only `== 0`, `< 0` or `> 0`).')
s += CODE('''
#include <stdio.h>
#include <string.h>

int main(void) {
    char arr[] = "Bamboozled";
    char source[] = "Sayonara", target[20];
    char greet[30] = "Hello", tail[] = " Folks!";
    printf("%s has length %zu\\n", arr, strlen(arr));

    strcpy(target, source);                    /* target must be big enough */
    printf("copied: %s\\n", target);

    strcat(greet, tail);                       /* greet has room for both  */
    printf("joined: %s\\n", greet);

    if (strcmp("Jerry", "Jerry") == 0)
        printf("identical strings: strcmp returns 0\\n");
    if (strcmp("Jerry", "Ferry") > 0)
        printf("Jerry is greater than Ferry\\n");
    printf("strstr -> %s\\n", strstr("hello world", "wor"));
    return 0;
}
''', run=True)
s += WARN('<b>Buffer overflow:</b> `strcpy` and `strcat` never check sizes. If `target` is smaller than `source` (or has no room for `\\0`), memory beyond the array is overwritten. Always make the destination large enough: for `strcat`, size ≥ strlen(d) + strlen(s) + 1.')
s += [H2('3.1 String manipulation without library functions')]
s += [P('Exam questions often forbid the library functions, so the underlying loops must be known. Every one of them is a traversal that stops at `\\0`.')]
s += CODE('''
#include <stdio.h>

int my_len(const char s[]) {                 /* strlen */
    int i = 0;
    while (s[i] != '\\0') i++;
    return i;
}

void to_upper(char s[]) {                    /* strupr */
    for (int i = 0; s[i] != '\\0'; i++)
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] -= 32;                      /* ASCII gap between 'a' and 'A' */
}

int main(void) {
    char s[] = "programming";
    printf("length = %d\\n", my_len(s));
    to_upper(s);
    printf("upper  = %s\\n", s);
    return 0;
}
''', run=True)
s += CODE('''
#include <stdio.h>
#include <string.h>

int main(void) {
    char str[100], rev[100];
    int n, i, vowels = 0;
    scanf("%99s", str);
    n = strlen(str);
    for (i = 0; i < n; i++) {
        rev[i] = str[n - 1 - i];                 /* reverse into rev */
        char c = str[i] | 32;                    /* lower-case trick */
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') vowels++;
    }
    rev[n] = '\\0';                               /* never forget the terminator */
    printf("reversed = %s, vowels = %d\\n", rev, vowels);
    printf("%s\\n", strcmp(str, rev) == 0 ? "Palindrome" : "Not a palindrome");
    return 0;
}
''', run=True, stdin='madam\n', label='Reverse, palindrome check and vowel count (input: madam)')
s += RECALL(['String = char array ending with `\\0`; `char s[] = "Hi"` uses 3 bytes.', '`scanf("%s")` stops at whitespace; use `fgets` for a full line; never use `gets`.', 'Include `<string.h>` for strlen, strcpy, strcat, strcmp, strchr, strstr.', '`strcmp` returns 0 for equal strings – never compare strings with `==`.', 'strrev/strupr/strlwr are non-standard; write loops instead.', 'Make the destination of strcpy/strcat large enough.'])
s += QA('g', 'Write a function to find the length of a string without using `strlen()`.', [('steps', ['Start a counter i at 0.', 'Move forward while `s[i]` is not the null character.', 'Return i – the number of characters before `\\0`.'])],
        code=CODE('''
#include <stdio.h>

int my_len(const char s[]) {
    int i = 0;
    while (s[i] != '\\0')
        i++;
    return i;
}

int main(void) {
    printf("%d\\n", my_len("Programming"));
    return 0;
}
''', run=True))
s += QA('y', 'Reverse the string "Programming" and check whether it is a palindrome.', [('work', '''
Original : P r o g r a m m i n g
Reversed : g n i m m a r g o r P
strcmp("Programming", "gnimmargorP") != 0
'''), 'The two strings differ (and also differ in the case of the first letter), so "Programming" is <b>not a palindrome</b>. A word like "madam" reads the same both ways, so `strcmp(str, rev) == 0` holds for it.'])
s += QA('r', 'Write a function to extract a substring from position p for n characters. If n = 0, extract from p to the end.', [('steps', ['Find the length of the source string.', 'If n is 0, set n = length − p (everything from p to the end).', 'Copy characters src[p] … src[p+n−1] (stopping at the end of the source) into the result.', 'Write `\\0` after the last copied character.'])],
        code=CODE('''
#include <stdio.h>
#include <string.h>

void substr(const char src[], int p, int n, char res[]) {
    int len = strlen(src), i, j = 0;
    if (n == 0) n = len - p;
    for (i = p; i < p + n && i < len; i++)
        res[j++] = src[i];
    res[j] = '\\0';
}

int main(void) {
    char r[20];
    substr("Programming", 3, 4, r);  printf("[%s]\\n", r);
    substr("Programming", 3, 0, r);  printf("[%s]\\n", r);
    return 0;
}
''', run=True))
s += QA('y', 'What does `strcmp("Jerry", "Ferry")` return in sign, and why?', [('steps', ['The first characters differ: \'J\' (ASCII 74) and \'F\' (ASCII 70).', 'The difference 74 − 70 = 4 is positive, so the result is <b>positive</b>. (Some compilers return the difference itself, 4; others, such as the current glibc, return just 1 – so test only the <i>sign</i>.)', 'A positive value means the first string is "greater" than the second in ASCII order.'])])
