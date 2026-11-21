from lib import *
s = []

# ================================================================= 1
s += H1('1. Structures — Basics')
s += [P('An array holds many values of the <i>same</i> type. Real data is usually a mixture: a student has a roll number (int), a name (string) and fees (float). A <b>structure</b> is a user-defined data type that groups related variables of <b>different types</b> under one name. The individual items are called <b>members</b> (or fields).')]
s += SYNTAX('<b>struct tag_name { data_type member1; data_type member2; ... };</b> &nbsp; declares the new type. &nbsp; <b>struct tag_name var1, var2;</b> &nbsp; declares variables. The closing brace must be followed by a <b>semicolon</b>.'.replace('&nbsp;', ' '))
s += NOTE('A structure <i>definition</i> only describes a layout – it allocates <b>no memory</b>. Memory is allocated when you declare a <i>variable</i> of that type. The members of one variable sit one after another in memory (with possible padding), and `sizeof` the whole struct is at least the sum of the members.')
s += [H2('1.1 Initialising and accessing members')]
s += BUL(['<b>Dot operator:</b> `variable.member` reads or writes a member: `s.fees = 45000.0;`', '<b>Initialiser list</b> (in declaration order): `struct student s = {1, "Rahul", 45000};`', '<b>Designated initialisers</b> (C99, any order): `struct student s = {.roll = 1, .name = "Rahul"};` – unmentioned members become 0.', '<b>Assignment</b> member by member: `s.roll = 1; strcpy(s.name, "Rahul");` – a char-array member cannot be assigned with `=`, use `strcpy`.', 'A whole struct <b>can be copied</b> with `=` (`s2 = s1;` copies every member, including arrays), but two structs <b>cannot be compared</b> with `==` – compare member by member.'])
s += CODE('''
#include <stdio.h>
#include <string.h>

struct student {
    int   roll;
    char  name[20];
    float fees;
};

int main(void) {
    struct student s1 = {1, "Rahul", 45000.0f};          /* initialiser list     */
    struct student s2 = {.name = "Asha", .roll = 2};      /* designated, fees = 0 */
    struct student s3;

    s3 = s1;                                              /* whole-struct copy    */
    strcpy(s3.name, "Meera");                             /* s1 is unaffected     */
    s3.fees += 1500;

    printf("%d %s %.2f\\n", s1.roll, s1.name, s1.fees);
    printf("%d %s %.2f\\n", s2.roll, s2.name, s2.fees);
    printf("%d %s %.2f\\n", s3.roll, s3.name, s3.fees);
    printf("sizeof(struct student) = %zu\\n", sizeof(struct student));
    return 0;
}
''', run=True)
s += [H2('1.2 Reading input into a structure')]
s += CODE('''
#include <stdio.h>

struct student { int roll; char name[20]; float fees; };

int main(void) {
    struct student s;
    scanf("%d", &s.roll);              /* & needed for int/float members       */
    scanf("%19s", s.name);             /* no & for a char-array member         */
    scanf("%f", &s.fees);
    printf("%d %s %.2f\\n", s.roll, s.name, s.fees);
    return 0;
}
''', run=True, stdin='7 Rahul 45000\n', label='input: 7 Rahul 45000')
s += [H2('1.3 typedef — a shorter type name')]
s += [P('`typedef` gives an existing type a new name. With structures it removes the need to write the word `struct` every time.')]
s += CODE('''
#include <stdio.h>

typedef struct {
    float real;
    float imag;
} COMPLEX;                              /* COMPLEX is now a type name */

int main(void) {
    COMPLEX a = {3.0f, 4.0f}, b = {1.5f, -2.0f};
    printf("a = %.1f + %.1fi,  b = %.1f + %.1fi\\n", a.real, a.imag, b.real, b.imag);
    return 0;
}
''', run=True)
s += [H2('1.4 Memory layout and padding')]
s += [P('For speed, a compiler aligns each member to a multiple of its own size, inserting unused <b>padding</b> bytes. So the size of a struct can be larger than the sum of its members, and <b>member order</b> can change it. Never assume `sizeof` equals the sum.')]
s += CODE('''
#include <stdio.h>

struct A { char c; int i; char d; };     /* c + 3 pad, i, d + 3 pad  */
struct B { int i; char c; char d; };     /* i, c, d + 2 pad          */

int main(void) {
    printf("sizeof(struct A) = %zu\\n", sizeof(struct A));
    printf("sizeof(struct B) = %zu\\n", sizeof(struct B));
    return 0;
}
''', run=True, label='Same members, different order → different size (typical 4-byte int)')
s += RECALL(['A struct groups members of different types; the definition allocates no memory, a variable does.', 'Access members with the dot operator: `var.member`.', 'Structs can be assigned with `=` but not compared with `==`.', 'Char-array members need `strcpy`, not `=`.', '`typedef` removes the need to write `struct` each time.', 'Padding can make `sizeof(struct)` bigger than the sum of its members.'])
s += QA('g', 'Declare a structure `book` with title (char[50]), price (float) and pages (int). In `main()`, declare one variable, initialise it and print all fields.', [('steps', ['Define the struct with the three members (and the closing semicolon).', 'Declare a variable and use an initialiser list in the same order as the members.', 'Print the members with the dot operator.'])],
        code=CODE('''
#include <stdio.h>

struct book {
    char  title[50];
    float price;
    int   pages;
};

int main(void) {
    struct book b = {"C Programming", 299.0f, 400};
    printf("%s  Rs %.0f  %d pages\\n", b.title, b.price, b.pages);
    return 0;
}
''', run=True))
s += QA('y', 'Store name, roll number and three subject marks of a student in a structure, compute the total and average and display all details.', [('steps', ['Define `struct student` with `name`, `roll` and `float m[3]` (an array inside a structure is allowed).', 'Read each mark in a loop, adding it to a running total.', 'Average = total / 3; print everything.'])],
        code=CODE('''
#include <stdio.h>

struct student {
    char  name[30];
    int   roll;
    float m[3];
};

int main(void) {
    struct student s;
    float tot = 0;
    scanf("%29s %d", s.name, &s.roll);
    for (int i = 0; i < 3; i++) {
        scanf("%f", &s.m[i]);
        tot += s.m[i];
    }
    printf("%s (%d)  total = %.1f  average = %.2f\\n", s.name, s.roll, tot, tot / 3);
    return 0;
}
''', run=True, stdin='Asha 12 78 85 91\n', label='input: Asha 12 78 85 91'))
s += QA('y', 'Why does `if (s1 == s2)` not compile for two structures, and how do you compare them?', [('steps', ['C defines no `==` for structure types (padding bytes may hold garbage, so a raw comparison would be unreliable).', 'Compare the members one by one: `s1.roll == s2.roll && strcmp(s1.name, s2.name) == 0 && s1.fees == s2.fees`.'])])

# ================================================================= 2
s += H1('2. Nested Structures')
s += [P('A structure may contain another structure as a member. Members of the inner structure are reached by chaining dot operators: `outer.inner.member`. Declare the inner structures <b>before</b> the outer one (inside-out order) so the compiler knows their size.')]
s += CODE('''
#include <stdio.h>

typedef struct { int dd, mm, yy; } DATE;
typedef struct { char first[20], last[20]; } NAME;

typedef struct {
    int   r_no;
    NAME  name;                      /* structure inside a structure */
    DATE  dob;
    float fees;
} STUDENT;

int main(void) {
    STUDENT s1 = {101, {"Asha", "Verma"}, {25, 9, 2007}, 45000.0f};
    s1.dob.mm = 10;                               /* chain of dots */
    printf("%d %s %s\\n", s1.r_no, s1.name.first, s1.name.last);
    printf("born %02d-%02d-%d, fees %.0f\\n", s1.dob.dd, s1.dob.mm, s1.dob.yy, s1.fees);
    return 0;
}
''', run=True)
s += CODE('''
#include <stdio.h>

struct point { float x, y; };
struct triangle { struct point A, B, C; };

int main(void) {
    struct triangle T = {{0, 0}, {4, 0}, {0, 3}};
    /* area = 1/2 |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| */
    float area = 0.5f * (T.A.x * (T.B.y - T.C.y) + T.B.x * (T.C.y - T.A.y)
                       + T.C.x * (T.A.y - T.B.y));
    if (area < 0) area = -area;
    printf("area = %.1f\\n", area);
    return 0;
}
''', run=True, label='Nested structure: triangle made of three points')
s += WARN('A structure <b>cannot contain itself</b> as a member (its size would be infinite). It <i>can</i> contain a <b>pointer to its own type</b> – `struct node { int data; struct node *next; };` – the basis of linked lists.')
s += RECALL(['Nested struct = a struct used as a member of another struct.', 'Access with a chain of dots: `outer.inner.field`.', 'Declare inner structures before outer ones.', 'No recursive containment, but a self-referencing <i>pointer</i> is allowed.'])

# ================================================================= 3
s += H1('3. Array of Structures')
s += [P('To keep many records (students, employees, products) declare an <b>array of structures</b>: `struct student st[50];`. Element `st[i]` is one whole record; `st[i].cgpa` is a member of it; `st[i].name[j]` is the j-th character of the name of the i-th student. Note that `&st[i].cgpa` means `&(st[i].cgpa)`.')]
s += SYNTAX('<b>struct student arr[N];</b> &nbsp;  initialise: <b>struct student st[3] = {{8.5, "A"}, {9.0, "B"}, {7.8, "C"}};</b> &nbsp; access: <b>arr[i].member</b>'.replace('&nbsp;', ' '))
s += CODE('''
#include <stdio.h>

struct emp { char name[20]; int id; float sal; };

int main(void) {
    struct emp e[3] = {{"Ravi", 1, 42000.0f},
                       {"Neha", 2, 58000.0f},
                       {"Omar", 3, 51000.5f}};
    int i, mx = 0;
    float total = 0;
    for (i = 0; i < 3; i++) {
        total += e[i].sal;
        if (e[i].sal > e[mx].sal) mx = i;          /* running maximum */
    }
    printf("Highest: %s (%.2f)\\n", e[mx].name, e[mx].sal);
    printf("Average salary: %.2f\\n", total / 3);
    return 0;
}
''', run=True)
s += CODE('''
#include <stdio.h>

struct student { char name[10]; float cgpa; };

int main(void) {
    struct student st[4] = {{"Asha", 8.2f}, {"Bala", 9.1f},
                            {"Chitra", 7.4f}, {"Dev", 8.8f}};
    struct student tmp;
    int i, j;
    for (i = 0; i < 3; i++)                /* bubble sort by cgpa, high to low */
        for (j = 0; j < 3 - i; j++)
            if (st[j].cgpa < st[j + 1].cgpa) {
                tmp = st[j];                       /* whole records are swapped */
                st[j] = st[j + 1];
                st[j + 1] = tmp;
            }
    for (i = 0; i < 4; i++)
        printf("%-8s %.1f\\n", st[i].name, st[i].cgpa);
    return 0;
}
''', run=True, label='Sorting records – a whole struct can be swapped with =')
s += RECALL(['`struct S arr[N]` stores N records contiguously.', 'Access: `arr[i].member` (index first, then dot).', '`arr[i].name[j]` = j-th character of the i-th record\'s string.', 'Initialise: `struct S a[2] = {{v1, v2}, {v3, v4}};`', 'Whole records can be copied/swapped with `=`.'])
s += QA('y', 'Create an array of 3 employee structures (name, id, salary), read the data and print the employee with the highest salary.', [('steps', ['Declare `struct emp e[3]`.', 'Read each record in a loop: `scanf("%19s %d %f", e[i].name, &e[i].id, &e[i].sal);`.', 'Keep the index `mx` of the largest salary: start with 0 and update when a larger one is found.', 'Print `e[mx]`.']), 'The same logic runs on built-in data in the first program of this section.'])

# ================================================================= 4
s += H1('4. Structures and Functions')
s += [P('A structure can be passed to a function and returned from one. By default it is passed <b>by value</b>: the function gets a <i>copy</i> of the whole struct (all members), so the original is unchanged. To let the function modify the original (and to avoid copying a big struct), pass a <b>pointer</b> and use the <b>arrow operator</b> `->`: `ptr->member` is exactly `(*ptr).member`.')]
s += CODE('''
#include <stdio.h>

typedef struct { float r, i; } COMPLEX;

COMPLEX add(COMPLEX a, COMPLEX b) {               /* by value, returns a struct */
    COMPLEX t;
    t.r = a.r + b.r;
    t.i = a.i + b.i;
    return t;
}

void swap_val(COMPLEX a, COMPLEX b) {             /* swaps copies: no effect */
    COMPLEX t = a; a = b; b = t;
}

void add_ptr(const COMPLEX *x, const COMPLEX *y, COMPLEX *res) {   /* by pointer */
    res->r = x->r + y->r;
    res->i = x->i + y->i;
}

void scale(COMPLEX *z, float k) {                 /* modifies the caller's struct */
    z->r *= k;
    z->i *= k;
}

int main(void) {
    COMPLEX x = {4, 5}, y = {10, 15}, z, w;
    z = add(x, y);
    printf("add        : %.1f + %.1fi\\n", z.r, z.i);
    swap_val(x, y);
    printf("after swap_val x = %.1f + %.1fi (unchanged)\\n", x.r, x.i);
    add_ptr(&x, &y, &w);
    printf("add_ptr    : %.1f + %.1fi\\n", w.r, w.i);
    scale(&x, 2);
    printf("after scale: %.1f + %.1fi\\n", x.r, x.i);
    return 0;
}
''', run=True)
s += WARN('<b>Operator precedence with pointers to structs:</b> `ptr->roll` and `(*ptr).roll` are identical, but `*ptr.roll` is an error (the dot binds tighter than `*`). `++ptr->roll` increments the <i>member</i> roll, not ptr. `(++ptr)->roll` moves ptr to the next struct first, then reads roll.')
s += BUL(['Declare the struct <b>outside</b> `main()` so every function can see the type.', 'Prefer passing a pointer (`const struct S *p` when the function only reads) for large structures – it passes 8 bytes instead of copying everything.', 'A struct can also be returned by value (as `add` does); arrays inside it are copied too.'])
s += RECALL(['Structs are passed by value – the function works on a copy.', 'To modify the original pass a pointer and use `->` inside.', '`ptr->member` ≡ `(*ptr).member`; never write `*ptr.member`.', 'Functions can return structs by value.', 'Declare the struct globally when several functions use it.'])
s += QA('y', 'Write a function that adds two complex numbers represented by a struct and returns the result. Show the output for (4 + 5i) + (10 + 15i).', [('steps', ['Define `COMPLEX` with `float r, i` members.', 'In `add`, build a local `COMPLEX t`, set `t.r = a.r + b.r` and `t.i = a.i + b.i`.', 'Return `t` by value; in main store it in `z` and print.', 'Result: (4 + 10) + (5 + 15)i = <b>14 + 20i</b>.']), 'This function is part of the program above, which prints exactly 14.0 + 20.0i.'])
s += QA('r', 'What is the difference between `p->x`, `(*p).x`, `*p.x` and `++p->x`?', [('lines', ['`p->x` and `(*p).x` – identical: member x of the struct p points to.', '`*p.x` – <b>error</b>: the dot binds first, so it tries `*(p.x)` and p is a pointer, not a struct.', '`++p->x` – increments the <i>member</i> x (it is `++(p->x)`), not the pointer.'])])

# ================================================================= 5
s += H1('5. Union')
s += [P('A <b>union</b> is declared like a structure, but <b>all its members share the same memory location</b>. Its size is the size of the <i>largest</i> member (plus padding), and only <b>one member holds a valid value at a time</b>: writing one member overwrites the others. Unions save memory when a value can be one of several types but never more than one at once.')]
s += SYNTAX('<b>union union_name { data_type var1; data_type var2; ... };</b> – members accessed with the same `.` and `->` operators as a struct.')
s += CODE('''
#include <stdio.h>

union height {
    char  fps[8];        /* feet-inches text, e.g. "5'10"   */
    int   cgs;           /* centimetres                     */
    float mks;           /* metres                          */
};

struct person {
    int  id;
    char kind;           /* flag: 'f', 'c' or 'm' - says which member is valid */
    union height h;
};

int main(void) {
    union height u;
    u.cgs = 178;
    printf("as int   : %d\\n", u.cgs);
    u.mks = 1.78f;                           /* overwrites the same bytes  */
    printf("as float : %.2f\\n", u.mks);
    printf("int now  : %d  (garbage - the bytes were overwritten)\\n", u.cgs);
    printf("sizeof(union height) = %zu, sizeof(struct person) = %zu\\n",
           sizeof(union height), sizeof(struct person));
    return 0;
}
''', run=True)
s += TABLE([['Parameter', 'Structure', 'Union'], ['Keyword', '`struct`', '`union`'], ['Size', 'Sum of all members (+ padding)', 'Size of the largest member (+ padding)'], ['Memory', 'Each member has its own storage', 'All members share the same storage'], ['Data overlap', 'None – members are independent', 'Full overlap – writing one corrupts the others'],
            ['Access', 'All members usable at the same time', 'Only the last written member is valid'], ['Use case', 'Store several fields together', 'Save memory when only one alternative is needed']], [1.4, 3, 3])
s += CODE('''
#include <stdio.h>

typedef struct {
    char name[20];
    char htype;                          /* 'f' = text, 'c' = int cm, 'm' = float m */
    union { char fps[8]; int cgs; float mks; } h;
} PERSON;

void show(const PERSON *p) {
    printf("%s: ", p->name);
    if (p->htype == 'f')      printf("%s\\n", p->h.fps);
    else if (p->htype == 'c') printf("%d cm\\n", p->h.cgs);
    else                      printf("%.2f m\\n", p->h.mks);
}

int main(void) {
    PERSON a = {"Asha", 'c', {.cgs = 165}};
    PERSON b = {"Ravi", 'm', {.mks = 1.78f}};
    PERSON c = {"Omar", 'f', {.fps = "5'10"}};
    show(&a); show(&b); show(&c);
    return 0;
}
''', run=True, label='Union inside a struct with a type flag – the standard pattern')
s += RECALL(['Union members share one memory block; size = largest member (+ padding).', 'Writing one member overwrites all others – only the last written one is valid.', 'Keep a "type flag" next to the union to know which member is valid.', 'Same `.` and `->` operators as a struct.'])
s += QA('r', 'A system stores a height as feet-inches text (FPS), centimetres (int) or metres (float). Design the data type with a union inside a structure and explain the flag.', [('steps', ['Put the three representations in a `union` – they share 8 bytes instead of using 8 + 4 + 4 = 16.', 'Wrap it in a `struct` together with a `char htype` flag (\'f\', \'c\' or \'m\').', 'When storing, set the matching union member and the flag; when reading, test the flag first and read only that member.', 'Without the flag the program cannot know which member is valid.']), 'The `PERSON` program above does exactly this.'])
s += QA('y', 'Give three differences between a structure and a union.', [('lines', ['<b>Memory:</b> struct members have separate storage; union members share one location.', '<b>Size:</b> struct = sum of members (+ padding); union = largest member (+ padding).', '<b>Validity:</b> all struct members are valid together; only the last written union member is valid.'])])
