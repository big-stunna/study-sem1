import sys
from lib import *
from unit2a import s

# ================================================================= 5
s += H1('5. Type Conversion')
s += [P('Operands of an operator should ideally have the same type, and the result then has that type too. When they differ but are compatible, the compiler converts them to a common type automatically (<b>implicit</b> conversion), or the programmer forces a conversion (<b>explicit</b> conversion / type casting).')]
s += [H2('5.1 Implicit (automatic) conversion')]
s += BUL(['`char` and `short` operands are first promoted to `int`.', 'In a mixed expression the "lower" type is converted to the "higher" type and the result has the higher type.', 'Hierarchy (low → high): <b>char → short → int → long → float → double</b>.', 'Mixing signed and unsigned operands can give unintuitive results.'])
s += CODE('''
int i; short s; float f; double d; long l;
d + f      /* f is converted to double before the addition        */
i / s      /* s is converted to int before the division           */
l / i      /* i is converted to long; the result is long          */
''', label='Examples (declarations assumed)')
s += WARN('<b>The classic bug:</b> `c = (9/5) * (f - 32);` – both 9 and 5 are `int`, so `9/5` is integer division = 1 and the formula is wrong for every f. Force floating-point division: `c = (9.0/5) * (f - 32);` (only one operand needs to be float).')
s += [H2('5.2 Explicit conversion (type casting)')]
s += SYNTAX('<b>(type_name) expression</b>   e.g. <b>(float) 9 / 5</b> gives 1.8. The cast applies to the operand immediately after it, <i>before</i> the division happens.')
s += TABLE([['Conversion', 'Effect', 'Example'], ['float → int', 'Truncates (drops) the fraction – does not round', '(int)3.9 = 3,  (int)(−9.7) = −9'], ['double → float', 'Rounds; loses precision', '(float)3.14159265358979…'],
            ['long → int', 'Drops high-order bits; may overflow silently', 'large values wrap around'], ['int → float', 'Exact unless the number is huge', '(float)5 = 5.0']], [1.4, 3.4, 2.7])
s += CODE('''
#include <stdio.h>

int main(void) {
    float f1 = 123.125f, f2;
    int i1, i2 = -150;
    i1 = f1;                              /* float -> int: truncates        */
    printf("%f assigned to an int gives %d\\n", f1, i1);
    f2 = i2 / 100;                        /* int / int = -1, then widened   */
    printf("i2/100        = %f\\n", f2);
    f2 = (float) i2 / 100;                /* cast first -> real division    */
    printf("(float)i2/100 = %f\\n", f2);
    f2 = i2 / 100.0;
    printf("i2/100.0      = %f\\n", f2);
    printf("9/5 = %d, 9.0/5 = %.1f, (float)9/5 = %.1f\\n", 9 / 5, 9.0 / 5, (float)9 / 5);
    return 0;
}
''', run=True)
s += RECALL(['Implicit: lower type → higher type in mixed expressions.', 'Hierarchy: char → short → int → long → float → double.', 'Explicit: `(type) expression`.', 'float → int truncates (3.9 → 3), it does not round.', 'Cast <i>before</i> dividing to get a real result: `(float)a / b`.'])
s += QA('g', 'What is printed by `int a = 7, b = 2; float c = a / b; printf("%f", c);`?', [('steps', ['`a / b` is int / int, so integer division: 7 / 2 = 3.', 'The integer 3 is then converted to float: 3.0.', 'Output: <b>3.000000</b>.'])])
s += QA('y', 'Fix this temperature conversion so it gives a correct real result: `c = (9/5) * (f - 32);`', [('steps', ['`9/5` is int / int = 1, so the expression is wrong for every value of f.', 'Force floating-point division: `c = (9.0/5) * (f - 32);` or `c = ((float)9/5) * (f - 32);`.', '<b>Also check the formula itself:</b> Fahrenheit → Celsius is `c = (f - 32) * 5.0 / 9` – the 9 and 5 were the wrong way round. (9/5 is the factor for Celsius → Fahrenheit.)'])])
s += QA('r', 'Predict the values: `int i = 7; float f = 2; double d = i / 2 + f / 4;` and say which conversions occur.', [('steps', ['`i / 2` is int / int = 3 (integer division).', '`f / 4` is float / int: 4 is converted to float, giving 0.5.', '`3 + 0.5`: the int 3 is converted to float, giving 3.5 (float).', 'The float result is widened to double when stored in d.'] ), 'So d = <b>3.5</b>.'])
s += H1('6. Precedence and Associativity')
s += [P('When an expression has several operators, <b>precedence</b> decides which is applied first (higher precedence binds tighter). When two operators have the <i>same</i> precedence, <b>associativity</b> (left-to-right or right-to-left) decides the order. Parentheses have the highest priority of all and can override both.')]
s += TABLE([['Priority', 'Operators', 'Associativity'], ['1 (highest)', '`( )  [ ]  .  ->`', 'Left → Right'], ['2', '`!  ~  ++  --  +  -  (type)  sizeof  *  &` (unary)', 'Right → Left'], ['3', '`*  /  %`', 'Left → Right'],
            ['4', '`+  -`', 'Left → Right'], ['5', '`<<  >>`', 'Left → Right'], ['6', '`<  <=  >  >=`', 'Left → Right'], ['7', '`==  !=`', 'Left → Right'], ['8', '`&` (bitwise AND)', 'Left → Right'],
            ['9', '`^` (bitwise XOR)', 'Left → Right'], ['10', '`|` (bitwise OR)', 'Left → Right'], ['11', '`&&`', 'Left → Right'], ['12', '`||`', 'Left → Right'], ['13', '`?:`', 'Right → Left'],
            ['14', '`=  +=  -=  *=  /=  %=`', 'Right → Left'], ['15 (lowest)', '`,`', 'Left → Right']], [1.3, 4, 1.7])
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = 10 + 20 * 30;                  /* * before +  -> 10 + 600 = 610      */
    int b = 100 / 10 * 10;                 /* same level, left to right -> 100    */
    int e1 = 100 + 200 / 10 - 3 * 10;      /* 100 + 20 - 30 = 90                  */
    int e2 = (100 + 200) / 10 - 3 * 10;    /* 300/10 - 30 = 0                     */
    int x, y, z;
    x = y = z = 5;                         /* right to left: all three become 5   */
    printf("%d %d %d %d | %d %d %d\\n", a, b, e1, e2, x, y, z);
    printf("%d\\n", (2 + 3 > 4 && 1) || 0);   /* (2+3)>4 -> 1; 1&&1 -> 1; 1||0 -> 1 */
    return 0;
}
''', run=True)
s += WARN('Expressions such as `a++ * ++a` modify a variable twice with no sequence point between the changes, so the result is <b>undefined behaviour</b> – different compilers print different answers. Never write them; use separate statements. The order in which function arguments are evaluated is also unspecified.')
s += RECALL(['Higher precedence is evaluated first; equal precedence uses associativity (mostly left → right).', '`()` has the highest priority – use it to force an order and for clarity.', 'Unary operators (`!`, `~`, `++`, `--`) and assignment are right → left.', '`a = b = c = 5` works because assignment is right → left.'])
s += QA('g', 'Evaluate `5 + 3 * 2 - 1`.', [('work', '''
5 + 3 * 2 - 1
Step 1:  3 * 2 = 6          (* has higher precedence than + and -)
Step 2:  5 + 6 = 11         (+ and - left to right)
Step 3:  11 - 1 = 10
'''), 'Answer: <b>10</b>.'])
s += QA('y', 'What does `a = b = c = 5;` do and which property allows it?', [('steps', ['Assignment is <b>right-to-left</b> associative.', '`c = 5` happens first and yields the value 5.', 'Then `b = 5` (using that value), then `a = 5`.', 'All three variables become 5.'])])
s += QA('r', 'What is the output of `int a = 10; printf("%d", a++ * ++a);`? Explain.', 'The result is <b>undefined</b>: `a` is modified twice (by `a++` and by `++a`) between two sequence points, so the C standard gives no guarantee about the value. Avoid such code; use separate statements.')

# ================================================================= 7
s += H1('7. Input and Output Functions')
s += [H2('7.1 Unformatted I/O: getchar() and putchar()')]
s += [P('`getchar()` reads a single character from standard input (the keyboard) and returns it as an `int` (or `EOF` on end of input). `putchar(c)` writes a single character to standard output. No format string is needed.')]
s += CODE('''
#include <stdio.h>

int main(void) {
    char ans;
    printf("Enter any character: ");
    ans = getchar();
    printf("The character entered = ");
    putchar(ans);
    putchar('\\n');
    return 0;
}
''', run=True, stdin='K\n')
s += [H2('7.2 Formatted output: printf()')]
s += SYNTAX('<b>printf("format string", var1, var2, ...);</b> – the format string contains (a) ordinary text printed as it is, (b) format specifiers starting with <b>%</b> and (c) escape sequences starting with <b>\\</b>. There must be one specifier per argument, of the right type.')
s += TABLE([['Spec', 'Type', 'Example', 'Output'], ['%d  %i', 'signed decimal int', '`printf("%d", 42)`', '42'], ['%u', 'unsigned int', '`printf("%u", 42)`', '42'], ['%f', 'float / double', '`printf("%f", 3.14)`', '3.140000 (6 decimals)'],
            ['%e', 'scientific notation', '`printf("%e", 3.14)`', '3.140000e+00'], ['%c', 'character', '`printf("%c", 65)`', 'A'], ['%s', 'string', '`printf("%s", "hi")`', 'hi'], ['%o', 'octal', '`printf("%o", 8)`', '10'],
            ['%x  %X', 'hexadecimal', '`printf("%x", 255)`', 'ff  (FF for %X)'], ['%p', 'pointer address', '`printf("%p", &a)`', 'machine dependent'], ['%%', 'a literal percent sign', '`printf("%%")`', '%']], [1, 1.9, 2.6, 2])
s += [H3('Width, precision and flags:  %[flags][width][.precision]specifier')]
s += TABLE([['Format', 'Value', 'Output (| marks the edges)', 'Explanation'], ['%5d', '42', '|   42|', 'right-aligned in 5 columns'], ['%-5d', '42', '|42   |', 'left-aligned in 5 columns'], ['%05d', '42', '|00042|', 'zero-padded to 5'],
            ['%10.4f', '98.7654', '|   98.7654|', 'width 10, 4 decimals'], ['%-10.2f', '2.34', '|2.34      |', 'left-aligned, 2 decimals'], ['%8.2f', '3.14159', '|    3.14|', 'width 8, 2 decimals, rounded'], ['%10s', '"Delhi"', '|     Delhi|', 'right-aligned string'], ['%-10s', '"Delhi"', '|Delhi     |', 'left-aligned string'], ['%.3s', '"Delhi"', '|Del|', 'only 3 characters']], [1.2, 1.2, 2.6, 2.6])
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = 10, c = 20;
    float b = 1.23f, d = 2.34f;
    printf("a = %d, b = %10.4f|\\n", a, b);
    printf("c = %-5d|d = %-10.2f|\\n", c, d);
    printf("[%8.2f] [%-8s] [%8s] [%05d] [%x] [%o]\\n", 3.14159, "Hi", "Bye", 42, 255, 8);
    printf("%d%%  %c  %s\\n", 95, 65, "done");
    return 0;
}
''', run=True)
s += [H2('7.3 Formatted input: scanf()')]
s += SYNTAX('<b>scanf("format string", &var1, &var2, ...);</b> – the <b>&amp;</b> (address-of) operator passes the address of each variable so scanf can store the value there. Arrays (strings) need no &amp; because the array name already is an address.'.replace('&amp;', '&'))
s += BUL(['Whitespace in the format string (and in the input) matches any amount of whitespace, so `"%d %d"` reads two integers separated by spaces, tabs or newlines.', '`%d` and `%f` skip leading whitespace automatically, but `%c` does <b>not</b> – it reads the very next character, even a leftover newline. Write `" %c"` (a space before %c) to skip whitespace.', 'Use `%lf` for `double` in scanf (but `%f` in printf).', '`scanf` returns the number of items successfully read – check it for robust programs.'])
s += CODE('''
#include <stdio.h>

int main(void) {
    int a; float b; char ch; char name[10];
    int n = scanf("%d %f %c %9s", &a, &b, &ch, name);   /* no & before name */
    printf("items read = %d\\n", n);
    printf("%d %f %c %s\\n", a, b, ch, name);
    return 0;
}
''', run=True, stdin='10 3.14 X Alice\n')
s += WARN('Forgetting the `&`: `scanf("%d", a);` is undefined behaviour (scanf treats the <i>value</i> of a as an address) and usually crashes. Using the wrong specifier (`%d` for a float) gives garbage.')
s += RECALL(['`getchar()` / `putchar()` handle a single character, with no format string.', 'printf format: `%[flags][width][.precision]specifier`; `-` = left-align, `0` = zero pad.', '`scanf` needs `&` for every non-array variable.', 'Common specifiers: `%d` int, `%f` float, `%lf` double (scanf), `%c` char, `%s` string.', '`%c` in scanf reads whitespace too – use `" %c"`.'])
s += QA('g', 'Write a printf that prints 3.14159 with 2 decimal places, right-aligned in 8 columns.', '`printf("%8.2f", 3.14159);` prints four spaces then 3.14 (width 8 in total).')
s += QA('y', 'Write a scanf that reads two integers separated by a space into `a` and `b`.', '`scanf("%d %d", &a, &b);` – each non-array variable needs the address-of operator.')
s += QA('r', 'What does `printf("%-8s|%8s", "Hi", "Bye");` print?', '`%-8s` left-aligns "Hi" in 8 columns (Hi + 6 spaces); `%8s` right-aligns "Bye" in 8 columns (5 spaces + Bye). Output: <b>Hi      |     Bye</b>',
        code=CODE('''
#include <stdio.h>

int main(void) {
    printf("%-8s|%8s\\n", "Hi", "Bye");
    return 0;
}
''', run=True))
