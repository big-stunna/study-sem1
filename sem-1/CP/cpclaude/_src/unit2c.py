import sys
from lib import *
from unit2 import s

# ================================================================= 8
s += H1('8. Control Structures')
s += [P('By default a program runs statement after statement (<b>sequence</b>). Control structures change that order: <b>decision-making</b> statements choose between paths, <b>loops</b> repeat a block, and <b>jump</b> statements transfer control. Together with sequence they are all that is needed to express any algorithm – the same four structures from the flowchart chapter.')]
s += [H2('8.1 Simple and compound statements')]
s += BUL(['A <b>simple statement</b> is one instruction ending with a semicolon: `a = a + 1;`.', 'A <b>compound statement</b> (block) is a group of statements in braces `{ }`. Wherever C allows one statement – the body of an `if` or a loop – a block of many statements can be used. A block is treated as a single unit and may declare its own local variables.'])
s += [H2('8.2 The if statement')]
s += SYNTAX('<b>if (condition) statement;</b>  or  <b>if (condition) { statement1; statement2; }</b> – the block runs only when the condition is non-zero (true).')
s += WARN('A semicolon right after the condition – `if (a > 5);` – is an <b>empty statement</b>: the if has an empty body and the following statement(s) run <i>always</i>. Without braces only the <i>first</i> statement belongs to the if; indentation does not matter to the compiler.')
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = -4;
    if (a > 0)
        printf("positive\\n");
    printf("a = %d  (this line always runs)\\n", a);   /* not part of the if */
    if (a > 5);                                       /* bug: empty body    */
        printf("printed even though a is not > 5\\n");
    return 0;
}
''', run=True, warn_ok=True)
s += [H2('8.3 if-else, if-else-if ladder and nested if')]
s += SYNTAX('<b>if (cond) { ... } else { ... }</b> – exactly one of the two branches runs; <b>else</b> is optional. <b>Ladder:</b> if (c1) {...} else if (c2) {...} else if (c3) {...} else {...} – conditions are tested top to bottom and the <i>first</i> true one is executed; the rest are skipped.')
s += BUL(['In a ladder, order matters: test the most specific / highest cut-off first.', 'In nested ifs, an `else` belongs to the <i>nearest</i> unmatched `if` (the "dangling else" rule) – use braces to be explicit.'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int marks, num;
    char grade;
    scanf("%d %d", &marks, &num);
    if (marks >= 90)      grade = 'A';
    else if (marks >= 80) grade = 'B';
    else if (marks >= 70) grade = 'C';
    else if (marks >= 60) grade = 'D';
    else                  grade = 'F';
    printf("Grade: %c\\n", grade);

    if (num % 3 == 0) {                       /* nested if */
        printf("%d is divisible by 3\\n", num);
        if (num % 5 == 0)
            printf("%d is divisible by 3 AND 5\\n", num);
    }
    return 0;
}
''', run=True, stdin='85 15\n', label='input: 85 15')
s += [H2('8.4 The switch statement')]
s += SYNTAX('<b>switch (expression) { case const1: statements; break; case const2: statements; break; default: statements; }</b>')
s += BUL(['The expression must be of an <b>integer</b> type (`int`, `char`) – not `float`.', 'Case labels must be <b>constants</b> (not variables) and unique.', '`break` transfers control out of the switch. Without it execution <b>falls through</b> into the next case – useful on purpose for grouping cases, a bug otherwise.', '`default` is optional and runs when no case matches.', '`switch` only tests equality; use if-else-if for ranges (`>`, `<`).'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int marks, n1, n2;
    char grade, op;
    scanf("%d", &marks);
    switch (marks / 10) {            /* fall-through groups the cases */
        case 10:
        case 9:
        case 8: grade = 'A'; break;  /* 80-100 */
        case 7:
        case 6: grade = 'B'; break;  /* 60-79  */
        case 5: grade = 'C'; break;  /* 50-59  */
        default: grade = 'F'; break; /* below 50 */
    }
    printf("Grade %c\\n", grade);

    scanf("%d %c %d", &n1, &op, &n2);
    switch (op) {                    /* a calculator */
        case '+': printf("%d\\n", n1 + n2); break;
        case '-': printf("%d\\n", n1 - n2); break;
        case '*': printf("%d\\n", n1 * n2); break;
        case '/':
            if (n2 == 0) printf("division by zero\\n");
            else         printf("%.2f\\n", (float)n1 / n2);
            break;
        default:  printf("unknown operator\\n");
    }
    return 0;
}
''', run=True, stdin='85\n7 / 2\n', label='input: 85 and then 7 / 2')
s += [H2('8.5 Loops: while, do-while, for')]
s += TABLE([['Feature', 'while', 'do-while', 'for'], ['Type', 'Pre-tested (entry-controlled)', 'Post-tested (exit-controlled)', 'Pre-tested'], ['Minimum iterations', '0', '1 – body always runs once', '0'], ['Condition checked', 'Before the body', 'After the body', 'Before the body'], ['Best for', 'Unknown number of repeats', 'Menus, input validation', 'Known number of repeats']], [1.6, 2, 2, 1.8])
s += SYNTAX('<b>while (condition) { body; update; }</b>   |   <b>do { body; } while (condition);</b>  (note the semicolon)   |   <b>for (init; condition; update) { body; }</b>')
s += BUL(['A `for` loop is equivalent to: `init; while (cond) { body; update; }`. All three parts are optional but the two semicolons are required; `for (;;)` is an infinite loop.', 'Always make sure the condition eventually becomes false – otherwise the loop never ends.'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int n = 5, i = 1, f = 1, k;
    while (i <= n) {                 /* factorial with while */
        f *= i;
        i++;
    }
    printf("%d! = %d\\n", n, f);

    do {                             /* runs once even though condition is false */
        printf("do-while body runs once, n=%d\\n", n);
    } while (n > 10);

    for (k = 1; k <= 5; k++)         /* multiplication table of 7 */
        printf("7 x %d = %d\\n", k, 7 * k);
    return 0;
}
''', run=True)
s += CODE('''
#include <stdio.h>

int main(void) {
    int n;
    do {                                   /* input validation */
        printf("Enter 1-10: ");
        scanf("%d", &n);
    } while (n < 1 || n > 10);
    printf("Valid: %d\\n", n);
    return 0;
}
''', run=True, stdin='15\n0\n7\n', label='input: 15, 0, 7 – the first two are rejected')
s += [H2('8.6 Nested loops and patterns')]
s += [P('A loop inside another loop is a <b>nested loop</b>: the inner loop runs completely for every single iteration of the outer loop. The classic use is printing patterns and tables – the outer loop handles rows, the inner loop handles columns.')]
s += CODE('''
#include <stdio.h>

int main(void) {
    int i, j;
    for (i = 1; i <= 5; i++) {            /* right triangle */
        for (j = 1; j <= i; j++)
            printf("* ");
        printf("\\n");
    }
    printf("\\n");
    for (i = 1; i <= 5; i++) {            /* inverted triangle */
        for (j = 5; j >= i; j--)
            printf("* ");
        printf("\\n");
    }
    printf("\\n");
    for (i = 1; i <= 5; i++) {            /* 5 x 5 multiplication grid */
        for (j = 1; j <= 5; j++)
            printf("%4d", i * j);
        printf("\\n");
    }
    return 0;
}
''', run=True)
s += [H2('8.7 break, continue and goto')]
s += BUL(['<b>break</b> – immediately leaves the <i>innermost</i> loop or switch.', '<b>continue</b> – skips the rest of the current iteration and jumps to the next one (in a `for` loop, to the update step); only for loops.', '<b>goto label;</b> – unconditionally jumps to a labelled statement (`label:`). It makes programs hard to follow ("spaghetti code"), so prefer `break`, `continue` and functions. One accepted use: escaping from deeply nested loops on an error.'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int i, j;
    for (i = 0; i < 3; i++) {                 /* break leaves the INNER loop only */
        printf("i=%d, j=", i);
        for (j = 0; j < 5; j++) {
            if (j == 2) break;
            printf("%d ", j);
        }
        printf("\\n");
    }
    for (i = 0; i < 2; i++) {                 /* continue skips j == 2 */
        printf("i=%d, j=", i);
        for (j = 0; j < 5; j++) {
            if (j == 2) continue;
            printf("%d ", j);
        }
        printf("\\n");
    }
    return 0;
}
''', run=True)
s += CODE('''
#include <stdio.h>

int main(void) {
    int n, c;
    long f = 1;
    scanf("%d", &n);
    if (n < 0) goto end;                 /* skip everything on negative input */
    c = 1;
loop:
    f = f * c;
    c++;
    if (c <= n) goto loop;               /* a hand-made loop */
    printf("Factorial of %d = %ld\\n", n, f);
end:
    return 0;
}
''', run=True, stdin='5\n', label='goto – factorial of 5 (input: 5)')
s += RECALL(['if: block runs when true; if-else: one of two; ladder: first true condition wins.', 'switch: integer/char equality only; `break` stops fall-through; `default` is optional.', 'while: test first (0+ times); do-while: test after (1+ times); for: counted loop.', 'break leaves the innermost loop/switch; continue skips to the next iteration.', '`goto` jumps to a label – avoid it.', 'Never put `;` after `if (...)`, `for (...)` or `while (...)` by mistake.'])
s += QA('g', 'Write a `for` loop that prints the even numbers from 2 to 20.', 'Start at 2 and step by 2.',
        code=CODE('''
#include <stdio.h>

int main(void) {
    for (int i = 2; i <= 20; i += 2)
        printf("%d ", i);
    printf("\\n");
    return 0;
}
''', run=True))
s += QA('y', 'Write a `do-while` loop that keeps asking "Enter a positive number" until the user enters one.', 'The body (prompt + read) must run at least once, which is exactly what do-while guarantees.',
        code=CODE('''
#include <stdio.h>

int main(void) {
    int n;
    do {
        printf("Enter a positive number: ");
        scanf("%d", &n);
    } while (n <= 0);
    printf("You entered %d\\n", n);
    return 0;
}
''', run=True, stdin='-3\n0\n8\n', label='input: -3, 0, 8'))
s += QA('y', 'Explain the difference between `break` and `continue` with a one-line example of each.', [('lines', ['<b>break</b> ends the whole loop: `if (x == 0) break;` stops reading at the first zero.', '<b>continue</b> abandons only the current pass and starts the next one: `if (x < 0) continue;` skips negative values but keeps looping.'])])
s += QA('r', 'Write a program using nested loops that prints the 5 × 5 multiplication table in grid form.', 'The outer loop picks the row i, the inner loop the column j, and `%4d` gives each product a fixed width of 4 so the columns line up. (A run of exactly this program is shown in section 8.6.)')
s += QA('r', 'Write a switch-based calculator for +, −, *, / that handles division by zero.', 'Read two integers and an operator character; switch on the character; in the `/` case test the divisor first. A working program (with a sample run) is shown in section 8.4. Remember the case labels are <i>characters</i> in single quotes: `case \'+\':`.')

# ================================================================= 9
s += H1('9. Mixed Practice — Trace the Output')
s += [P('These questions combine operators, type conversion and control structures, in the style of exam "find the output" problems. Each program was compiled and run to get the real output; try to predict it before reading the answer.')]
s += QA('y', 'Trace: `int x = 5, y, z; y = x++; z = ++x;` – what are x, y and z?', [('work', '''
start:        x = 5
y = x++;      y gets the old x (5), then x becomes 6      ->  x=6  y=5
z = ++x;      x becomes 7 first, then z gets 7             ->  x=7  y=5  z=7
'''), 'Output of the program below: <b>7 5 7</b> (x, y, z).'],
        code=CODE('''
#include <stdio.h>

int main(void) {
    int x = 5, y, z;
    y = x++;
    z = ++x;
    printf("%d %d %d\\n", x, y, z);
    return 0;
}
''', run=True))
s += QA('y', 'What does this loop print? `for (i = 1; i <= 10; i++) { if (i % 2 == 0) continue; if (i > 7) break; printf("%d ", i); }`', [('work', '''
 i   i%2==0 ?        i>7 ?        action
 1   no               no          print 1
 2   yes -> continue
 3   no               no          print 3
 4   yes -> continue
 5   no               no          print 5
 6   yes -> continue
 7   no               no          print 7
 8   yes -> continue
 9   no               yes         break  (loop ends)
'''), 'Output: <b>1 3 5 7</b>.'],
        code=CODE('''
#include <stdio.h>

int main(void) {
    int i;
    for (i = 1; i <= 10; i++) {
        if (i % 2 == 0) continue;
        if (i > 7) break;
        printf("%d ", i);
    }
    printf("\\n");
    return 0;
}
''', run=True))
s += QA('r', 'Predict the output, including the effect of integer division and the missing `break`s.', [('steps', ['n = 2 matches `case 2`, which prints "two" and has <b>no break</b>.', 'Execution falls through into `case 3`, prints "three", and stops at its `break`.', '`7 / 2` is integer division = 3; `7 / 2.0` is real division = 3.5; `7 % 2` = 1.'])],
        code=CODE('''
#include <stdio.h>

int main(void) {
    int n = 2;
    switch (n) {
        case 1: printf("one\\n");
        case 2: printf("two\\n");
        case 3: printf("three\\n"); break;
        default: printf("other\\n");
    }
    printf("%d %.1f %d\\n", 7 / 2, 7 / 2.0, 7 % 2);
    return 0;
}
''', run=True, warn_ok=True))
s += QA('r', 'Write a full program that reads N and prints the sum of its digits (use `%` and `/`).', [('steps', ['Take the last digit with `n % 10` and add it to the sum.', 'Remove that digit with `n = n / 10`.', 'Repeat until n becomes 0.']), 'Trace for 4096: 6 + 9 + 0 + 4 = 19.'],
        code=CODE('''
#include <stdio.h>

int main(void) {
    int n, sum = 0;
    scanf("%d", &n);
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    printf("Sum of digits = %d\\n", sum);
    return 0;
}
''', run=True, stdin='4096\n', label='input: 4096'))
ok = build(sys.argv[1] if len(sys.argv) > 1 else '/home/sleepy/STUDY:)/sem-1/CP/cpclaude/Unit2_Notes.pdf', 2, 'Features of C & Control Structures',
           '', '8 hrs · 20% weightage · C language',
           'Structure of a C program · compilation · constants, variables, data types · operators and expressions · type conversion · precedence and associativity · I/O functions · control structures (if, switch, loops, break/continue, goto)',
           '#e8590c', s)
print('BUILD OK' if ok else 'BUILD HAS PROBLEMS')
