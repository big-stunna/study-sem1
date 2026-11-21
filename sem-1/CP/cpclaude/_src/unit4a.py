from lib import *
s = []

# ================================================================= 1
s += H1('1. Recursion — Concept and the Call Stack')
s += [P('<b>Recursion</b> is a technique in which a function <b>calls itself</b> – directly (A calls A) or indirectly (A calls B, B calls A) – to solve a problem by reducing it to a <i>smaller version of the same problem</i>. It is a different way of thinking from loops: instead of "repeat these steps", you say "the answer for n is built from the answer for a smaller n".')]
s += [P('<b>Everyday picture:</b> to count the people in a queue, ask the person in front "how many are ahead of you?", add 1 to their answer and report it back. The person at the very front, who has nobody ahead, answers 0 straight away – that is the <b>base case</b>.')]
s += [H2('1.1 The two mandatory parts')]
s += TABLE([['Part', 'Meaning', 'If it is missing'], ['<b>Base case</b> (stopping condition)', 'The smallest instance, solved directly without another call', 'Infinite recursion → stack overflow (crash)'], ['<b>Recursive case</b>', 'Expresses the problem through a call with a <i>smaller</i> argument that moves toward the base case', 'The calls never reach the base case']], [2, 3.2, 2.3])
s += CODE('''
type func(args) {
    if (smallest_case)            /* 1. base case: stop here            */
        return base_value;
    return combine(func(smaller_args));   /* 2. recursive case          */
}
''', label='General template')
s += [H2('1.2 The call stack')]
s += [P('Every call creates an <b>activation record</b> (stack frame) on the <b>call stack</b> holding the parameters, the local variables and the return address. The frames are stacked, last-in-first-out. A call that has not yet returned stays on the stack, <i>waiting</i> for the answer of the call it made. When the base case returns, the frames are <b>popped</b> one by one and each waiting call finishes its calculation on the way back.')]
s += CODE('''
fact(4)  waits for fact(3)           <- pushed first, finishes last
  fact(3)  waits for fact(2)
    fact(2)  waits for fact(1)
      fact(1)  waits for fact(0)
        fact(0)  returns 1           <- base case: stack starts to unwind
      fact(1) = 1 * 1 = 1
    fact(2) = 2 * 1 = 2
  fact(3) = 3 * 2 = 6
fact(4) = 4 * 6 = 24
''', label='Stack picture for fact(4): winding (down) then unwinding (up)')
s += WARN('Every frame uses memory. Without a reachable base case (or with a very deep recursion such as `fact(1000000)`) the stack fills up and the program crashes with a <b>stack overflow</b> (segmentation fault). The argument must change toward the base case on every call.')
s += [H2('1.3 Kinds of recursion')]
s += BUL(['<b>Direct</b> – a function calls itself. <b>Indirect (mutual)</b> – A calls B and B calls A.', '<b>Linear</b> – one recursive call per invocation (factorial, power, sum).', '<b>Tree / binary</b> – two or more calls per invocation (Fibonacci, Tower of Hanoi): the number of calls can grow exponentially.', '<b>Tail recursion</b> – the recursive call is the very last thing the function does; some compilers convert it into a loop.'])

# ================================================================= 2
s += H1('2. Factorial Using Recursion')
s += FORMULA('fact(0) = 1 (base case) &nbsp;&nbsp; fact(n) = n × fact(n − 1) for n &gt; 0 (recursive case)'.replace('&nbsp;', ' ').replace('&gt;', '>'))
s += CODE('''
#include <stdio.h>

long fact(int n) {
    if (n == 0)                  /* base case */
        return 1;
    return n * fact(n - 1);      /* recursive case */
}

int main(void) {
    int n = 5;
    printf("%d! = %ld\\n", n, fact(n));
    return 0;
}
''', run=True)
s += NOTE('The base case `n == 0` is mathematically correct (0! = 1). Using `n == 1` also works for n ≥ 1 but fails for n = 0. `fact(n)` creates exactly <b>n + 1</b> stack frames. The iterative equivalent is a simple loop with O(1) extra space.')
s += CODE('''
#include <stdio.h>

long fact_tail(int n, long acc) {         /* tail-recursive: accumulator argument */
    if (n == 0) return acc;
    return fact_tail(n - 1, acc * n);     /* nothing left to do after the call    */
}

int main(void) {
    printf("%ld\\n", fact_tail(5, 1));
    return 0;
}
''', run=True, label='Tail-recursive version')
s += RECALL(['fact(n) = n × fact(n − 1); base case fact(0) = 1.', 'Each pending call waits on the stack until the base case returns.', 'fact(n) uses n + 1 frames; the iterative version needs only a loop.', 'Tail recursion passes the running result as an accumulator argument.'])

# ================================================================= 3
s += H1('3. Fibonacci Series Using Recursion')
s += [P('The series 0, 1, 1, 2, 3, 5, 8, 13, 21, … – each term is the sum of the previous two. It needs <b>two base cases</b> because the recursive case refers back two steps.')]
s += FORMULA('fib(0) = 0 &nbsp; fib(1) = 1 (base cases) &nbsp;&nbsp; fib(n) = fib(n − 1) + fib(n − 2) for n &gt; 1'.replace('&nbsp;', ' ').replace('&gt;', '>'))
s += CODE('''
fib(4)
 +-- fib(3)
 |    +-- fib(2)
 |    |    +-- fib(1) = 1
 |    |    +-- fib(0) = 0
 |    +-- fib(1) = 1
 +-- fib(2)
      +-- fib(1) = 1
      +-- fib(0) = 0

fib(2) = 1 + 0 = 1,  fib(3) = fib(2) + fib(1) = 2,  fib(4) = 2 + 1 = 3
''', label='Call tree for fib(4) – note fib(2) is computed twice')
s += CODE('''
#include <stdio.h>

int calls = 0;

int fib(int n) {
    calls++;
    if (n < 2) return n;                 /* two base cases: fib(0)=0, fib(1)=1 */
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    for (int i = 0; i < 8; i++)
        printf("%d ", fib(i));
    printf("\\n");
    calls = 0;
    fib(5);
    printf("fib(5) needed %d calls\\n", calls);
    calls = 0;
    fib(20);
    printf("fib(20) needed %d calls\\n", calls);
    return 0;
}
''', run=True)
s += WARN('Tree recursion recomputes the same sub-problems: fib(2) is evaluated 3 times inside fib(5). The number of calls grows about 1.6<super>n</super> (exponential – O(2<super>n</super>)), while the stack depth is only O(n). An iterative loop does it in O(n) time and O(1) space; memoisation (storing computed values) also makes the recursive version O(n).')
s += CODE('''
#include <stdio.h>

int main(void) {
    int a = 0, b = 1, next, i, n = 10;
    for (i = 0; i < n; i++) {            /* iterative Fibonacci - O(n) */
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }
    printf("\\n");
    return 0;
}
''', run=True, label='Iterative Fibonacci')
s += RECALL(['Two base cases: fib(0) = 0, fib(1) = 1.', 'Tree recursion recomputes sub-problems → exponential time O(2ⁿ), stack depth O(n).', 'Iterative version: O(n) time, O(1) space.', 'Memoisation brings the recursive version down to O(n).'])

# ================================================================= 4
s += H1('4. Ackermann Function')
s += [P('The <b>Ackermann function</b> is the standard example of a function that is not <i>primitive recursive</i>: it grows faster than any loop-based formula. It has two arguments and the recursion nests <b>inside its own argument</b> (double recursion).')]
s += FORMULA('A(0, n) = n + 1<br/>A(m, 0) = A(m − 1, 1) &nbsp; for m &gt; 0<br/>A(m, n) = A(m − 1, A(m, n − 1)) &nbsp; for m, n &gt; 0'.replace('&nbsp;', ' ').replace('&gt;', '>'))
s += CODE('''
A(1,2) = A(0, A(1,1))             inner call first:  A(1,1)
A(1,1) = A(0, A(1,0))                                A(1,0)
A(1,0) = A(0, 1)       = 1 + 1   = 2
A(1,1) = A(0, 2)       = 2 + 1   = 3
A(1,2) = A(0, 3)       = 3 + 1   = 4
''', label='Hand trace of A(1, 2)')
s += CODE('''
#include <stdio.h>

int ackermann(int m, int n) {
    if (m == 0) return n + 1;
    if (n == 0) return ackermann(m - 1, 1);
    return ackermann(m - 1, ackermann(m, n - 1));
}

int main(void) {
    printf("A(1,2) = %d\\n", ackermann(1, 2));
    printf("A(2,3) = %d\\n", ackermann(2, 3));
    printf("A(3,2) = %d\\n", ackermann(3, 2));
    printf("A(3,3) = %d\\n", ackermann(3, 3));
    return 0;
}
''', run=True)
s += NOTE('Values explode: A(3,3) = 61, but A(4,1) = 65533 and A(4,2) has 19,729 digits. Never call it with m ≥ 4 in practice – the stack depth alone would overflow. It is used to stress-test compilers and recursion depth.')

# ================================================================= 5
s += H1('5. More Recursion Examples')
s += [P('Most recursive solutions follow one recipe: <b>(1)</b> find the base case, <b>(2)</b> express the answer for n using the answer for something smaller, <b>(3)</b> make sure every call moves toward the base case.')]
s += CODE('''
#include <stdio.h>
#include <string.h>

/* b^e: power(b,0) = 1, power(b,e) = b * power(b,e-1) */
int power(int b, int e) {
    if (e == 0) return 1;
    return b * power(b, e - 1);
}

/* Euclid: gcd(m,0) = m, gcd(m,n) = gcd(n, m%n) */
int gcd(int m, int n) {
    if (n == 0) return m;
    return gcd(n, m % n);
}

int digit_sum(int n) {                       /* sum of digits */
    if (n == 0) return 0;
    return n % 10 + digit_sum(n / 10);
}

int is_palin(const char *s, int l, int r) {  /* palindrome check */
    if (l >= r) return 1;                    /* empty or one character left */
    if (s[l] != s[r]) return 0;
    return is_palin(s, l + 1, r - 1);
}

int main(void) {
    printf("2^10 = %d\\n", power(2, 10));
    printf("gcd(48,18) = %d\\n", gcd(48, 18));
    printf("digit_sum(4096) = %d\\n", digit_sum(4096));
    printf("madam: %d, hello: %d\\n", is_palin("madam", 0, 4), is_palin("hello", 0, 4));
    return 0;
}
''', run=True)
s += CODE('''
gcd(48,18) -> gcd(18,12) -> gcd(12,6) -> gcd(6,0) = 6      (each step: gcd(n, m mod n))
''', label='Trace of the Euclidean algorithm')
s += [H2('5.1 Tower of Hanoi')]
s += [P('Move n disks from the left peg to the right peg using the centre peg, one disk at a time, never placing a larger disk on a smaller one. <b>Recursive idea:</b> (1) move the top n − 1 disks left → centre; (2) move the biggest disk left → right; (3) move the n − 1 disks centre → right. The minimum number of moves is <b>2<super>n</super> − 1</b>.')]
s += CODE('''
#include <stdio.h>

void hanoi(int n, char from, char to, char tmp) {
    if (n == 0) return;                          /* base case: nothing to move */
    hanoi(n - 1, from, tmp, to);                 /* 1. top n-1 disks out of the way */
    printf("Move disk %d: %c -> %c\\n", n, from, to);   /* 2. biggest disk */
    hanoi(n - 1, tmp, to, from);                 /* 3. n-1 disks onto it */
}

int main(void) {
    hanoi(3, 'L', 'R', 'C');                     /* 2^3 - 1 = 7 moves */
    return 0;
}
''', run=True)
s += [H2('5.2 Recursion vs iteration')]
s += TABLE([['Aspect', 'Recursion', 'Iteration'], ['Termination', 'Base case reached', 'Loop condition becomes false'], ['State storage', 'Call stack (implicit)', 'Loop variables (explicit)'], ['Readability', 'Very clear for divide-and-conquer and tree problems', 'Clear for simple sequential steps'],
            ['Overhead', 'A function call (and frame) per step', 'Minimal'], ['Memory', 'O(depth) stack space', 'O(1) usually'], ['Risk', 'No base case / wrong reduction → stack overflow', 'Wrong condition → infinite loop'], ['Prefer for', 'Tree/graph traversal, divide and conquer, Hanoi', 'Simple counting, summing']], [1.5, 3.2, 2.8])
s += RECALL(['Always: base case + a recursive call that moves toward it.', 'Recursion is natural for self-similar problems; loops are cheaper for simple repetition.', 'GCD: gcd(m, n) = gcd(n, m % n), base gcd(m, 0) = m.', 'Hanoi needs 2ⁿ − 1 moves.', 'Ackermann grows faster than any primitive recursive function.'])
s += QA('g', 'Write a recursive function `power(base, exp)` that returns base^exp.', [('steps', ['Base case: power(x, 0) = 1.', 'Recursive case: power(x, n) = x × power(x, n − 1).', 'Each call reduces the exponent by 1, so the base case is always reached.']), 'Trace for power(2, 3):', ('work', '''
power(2,3) = 2 * power(2,2)
           = 2 * (2 * power(2,1))
           = 2 * (2 * (2 * power(2,0)))
           = 2 * 2 * 2 * 1
           = 8
''')], code=CODE('''
int power(int b, int e) {
    if (e == 0) return 1;
    return b * power(b, e - 1);
}
'''))
s += QA('y', 'Trace the call tree for `fib(5)` and count how many times `fib(2)` is called and how many calls are made in all.', [('steps', ['fib(5) calls fib(4) and fib(3).', 'fib(4) calls fib(3) and fib(2); fib(3) calls fib(2) and fib(1).', 'In total fib(3) is evaluated 2 times and <b>fib(2) is evaluated 3 times</b>.', 'Counting every call (the program in section 3 confirms it): <b>15 calls</b>.'])])
s += QA('r', 'Write a recursive function that checks whether a string is a palindrome, handling the base cases carefully.', [('steps', ['Compare the first and last characters (indices l and r).', 'Base case 1: if `l >= r` the string is empty or one character in the middle – it is a palindrome, return 1.', 'Base case 2: if `s[l] != s[r]` – return 0 immediately.', 'Recursive case: check the inside part, `is_palin(s, l + 1, r - 1)`.', 'Call as `is_palin(str, 0, strlen(str) - 1)`.']), 'The function `is_palin` and its test run are shown in section 5.'])
s += QA('y', 'What happens if the base case is missing from a recursive function?', [('steps', ['Each call makes another call and none ever returns.', 'Every call adds a stack frame, so the stack keeps growing.', 'Eventually the stack is exhausted: a <b>stack overflow</b> / segmentation fault.'])])
s += QA('r', 'Evaluate A(2, 1) using the Ackermann definition, showing every step.', [('work', '''
A(2,1) = A(1, A(2,0))
A(2,0) = A(1, 1)
A(1,1) = A(0, A(1,0))
A(1,0) = A(0, 1) = 2
A(1,1) = A(0, 2) = 3
A(2,0) = A(1,1) = 3
A(2,1) = A(1, 3) = A(0, A(1,2)) = A(0, 4) = 5
        [A(1,2) = A(0, A(1,1)) = A(0, 3) = 4]
'''), 'Answer: A(2,1) = <b>5</b>. (Shortcut: A(2, n) = 2n + 3.)'])
