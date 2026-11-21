import sys; sys.path.insert(0, '/home/sleepy/STUDY:)/sem-1/CP/cpclaude/_src')
from lib import *
s = []

# ------------------------------------------------------------------ 1
s += H1('1. Introduction to Problem Solving with Computers')
s += [P('A computer is a very fast, very obedient but completely literal-minded machine. It cannot think on its own: it can only follow instructions exactly as they are given. <b>Problem solving with a computer</b> therefore means taking a real-world problem (for example "find the average marks of a student") and turning it into a precise, unambiguous sequence of instructions that a machine can execute.')]
s += [H2('1.1 What is a computer?')]
s += BUL(['An electronic device that takes <b>input</b>, <b>processes</b> it by following stored instructions and produces <b>output</b>.',
          'It is a programmable machine that performs arithmetic and logical operations automatically and at very high speed.',
          'Used in banking, research, education, space, business, engineering, communication, construction, fashion and almost every other field.'])
s += [P('The basic cycle is always <b>Input → Processing → Output</b>, with data and instructions held in memory while the work is going on.')]
s += [H2('1.2 Parts of a computer system')]
s += [P('A complete computer system = <b>Hardware + Software</b>.')]
s += BUL(['<b>Hardware</b> – the physical, touchable parts: CPU, memory chips, keyboard, mouse, printer, circuit boards.',
          '<b>Software</b> – the programs. It is split into <b>System software</b> (keeps the hardware running: OS, BIOS, translators) and <b>Application software</b> (does user-specific work: MS Office, games, banking apps).'])
s += NOTE('Hardware cannot think or decide by itself. It only understands two electrical states, ON and OFF (written 1 and 0). It always needs software, i.e. a set of instructions, to do anything useful.')
s += [H2('1.3 The four functional units of hardware')]
s += [P('<b>1. Central Processing Unit (CPU)</b> – the "brain" of the computer. It has three parts:')]
s += BUL(['<b>Control Unit (CU)</b> – fetches an instruction from memory, decodes it and sends control signals that tell the other parts what to do.',
          '<b>Arithmetic Logic Unit (ALU)</b> – actually performs the arithmetic (+, −, ×, ÷) and logical (AND, OR, NOT, comparisons) operations.',
          '<b>Registers</b> – very small, very fast memory locations <i>inside</i> the CPU holding data/instructions temporarily (Accumulator, Program Counter, Address Register, Instruction Register). Modern CPUs use 64-bit registers.'])
s += [P('<b>2. Memory / Storage unit</b> – holds data and instructions before, during and after processing.')]
s += BUL(['<b>Primary (main) memory</b> – stores data in binary form for immediate use by the CPU: RAM, ROM, PROM, EPROM, EEPROM.',
          ['<b>RAM</b> (Random Access Memory): volatile – contents are lost when power is off; used for the programs and data currently running.',
           '<b>ROM</b> (Read Only Memory): non-volatile – contents are permanent; stores the BIOS/firmware needed to boot.',
           '<b>PROM</b>: can be programmed exactly once after manufacture, never erased.',
           '<b>EPROM</b>: erased using ultraviolet light and reprogrammed many times.',
           '<b>EEPROM</b>: erased and reprogrammed electrically; used in microcontrollers, smart cards, embedded systems.'],
          '<b>Secondary storage</b> – long-term, non-volatile storage: HDD, SSD, flash drive, CD-ROM, cloud. Programs live here and are loaded into RAM only when they are needed.'])
s += [P('<b>3. Input unit</b> – captures data/instructions from the user (keyboard, mouse, scanner) and converts them into binary signals. <b>4. Output unit</b> – converts the computer\'s binary results back into human-readable form (monitor, printer, speaker).')]
s += TABLE([['Memory', 'Volatile?', 'Writable?', 'How it is erased / used'],
            ['RAM', 'Yes', 'Yes (read-write)', 'Working memory of running programs'],
            ['ROM', 'No', 'No (read only)', 'Holds BIOS / firmware'],
            ['PROM', 'No', 'Once', 'Programmed once by the user, cannot be erased'],
            ['EPROM', 'No', 'Yes', 'Erased with UV light, then reprogrammed'],
            ['EEPROM', 'No', 'Yes', 'Erased electrically; used in embedded systems']], [1.1, 1, 1.4, 3.3])
s += [H2('1.4 Computer software')]
s += [P('A <b>program</b> is a set of instructions arranged in a sequence to solve a problem; <b>software</b> is a collection of executable programs. A programmer writes <b>source code</b> in a programming language, and a <b>compiler</b> converts it into <b>object code</b> (machine instructions the hardware understands).')]
s += TABLE([['Type', 'Description', 'Examples'],
            ['System software', 'Lets the hardware run properly; interface between hardware and application software', 'OS, BIOS, compiler, loader'],
            ['BIOS', 'First code run on power-on; performs POST (Power-On Self Test), initialises devices and loads the OS', 'Stored in a ROM chip on the motherboard'],
            ['Operating system', 'Manages CPU, memory and I/O devices efficiently', 'Windows, Linux, macOS, Android'],
            ['System development software', 'Environment to build application software', 'Editors, compilers, interpreters, linkers'],
            ['Application software', 'Does specific user tasks. <i>General purpose</i> (MS Office, browsers) or <i>specific purpose</i> (banking, payment apps, media players)', 'MS Office, games, banking apps']], [1.5, 3.6, 2.2])
s += RECALL(['CPU = CU + ALU + Registers.', 'RAM is volatile; ROM is non-volatile (BIOS lives in ROM).', 'EPROM is erased by UV light, EEPROM electrically.',
             'System software manages the hardware; application software serves the user.', 'Basic computer cycle: Input → Process (CPU) → Output.'])
s += QA('g', 'List the four main functional units of a computer and state one function of each.', [('steps', ['<b>Input unit</b> – takes data and instructions in and converts them to binary.', '<b>CPU</b> – processes data (the CU directs, the ALU computes, registers hold temporary data).', '<b>Memory unit</b> – stores data and instructions (primary = RAM/ROM, secondary = SSD/HDD).', '<b>Output unit</b> – converts processed binary data back to human-readable form.'])])
s += QA('y', 'Differentiate between RAM and ROM and explain why a computer needs both.',
        'RAM is volatile read-write memory used to hold the data and programs the CPU is actively using; it loses its contents when power is switched off. ROM is non-volatile and (practically) read-only; it permanently stores the firmware/BIOS needed to start the computer. A computer needs ROM so it can boot reliably every time (RAM is empty after power-off) and needs RAM so it can run programs quickly once booted, because RAM is far faster than permanent storage.')
s += QA('r', 'A student says: "My computer has 16 GB of RAM, so it never forgets anything even after a power cut." Explain why this is wrong and name the memory types that would survive a power cut.',
        'RAM is volatile: it holds data only while electrical power is supplied. The moment power is cut, every bit in RAM is lost, no matter how large it is – 16 GB only says how much it can hold while running, not whether it keeps data. Memory that survives a power cut is non-volatile: ROM (firmware/BIOS), PROM/EPROM/EEPROM, and secondary storage such as SSDs and HDDs where files and installed programs are written permanently (magnetically or in flash).')
s += QA('g', 'Classify as system software or application software: (a) Windows 11, (b) MS Excel, (c) BIOS, (d) a banking mobile app.', [('lines', ['(a) Windows 11 – <b>system software</b> (operating system)', '(b) MS Excel – <b>application software</b> (general purpose)', '(c) BIOS – <b>system software</b>', '(d) Banking app – <b>application software</b> (specific purpose)'])])
# ------------------------------------------------------------------ 2
s += H1('2. Programming Languages — Four Generations')
s += [P('Programming languages are the primary tool for creating software. Over time they have moved from being close to the hardware to being close to human language. There are four generations.')]
s += TABLE([['Generation', 'Style', 'Advantages', 'Disadvantages'],
            ['1GL – Machine language', 'Binary 0s and 1s (ON/OFF states)', 'Fastest execution – no translation needed; very little memory', 'Extremely hard to write and debug; not portable between machines'],
            ['2GL – Assembly language', 'Mnemonics: ADD, CMP, MUL', 'Easier than machine code; still efficient and fast', 'Needs an assembler; not portable; unsuitable for large applications'],
            ['3GL – High-level language', 'English-like statements: C, C++, Java, FORTRAN, COBOL, BASIC', 'Portable; programmer thinks about logic, not hardware; less error-prone', 'Must be compiled or interpreted before execution'],
            ['4GL – Very high-level language', 'Near natural language: SQL, Python, MATLAB, SAS', 'Very few lines of code; non-procedural ("what", not "how"); high productivity', 'Still evolving; costlier to run; may execute slower']], [1.5, 1.7, 2.1, 2.1])
s += NOTE('<b>Procedural</b> language: the programmer specifies every step – <i>how</i> to do the task. <b>Non-procedural</b> language (4GL): the programmer specifies only the goal – <i>what</i> is wanted – and the system works out how. Example (SQL): `SELECT * FROM students WHERE marks > 90;` does not say how to search the table.')
s += RECALL(['1GL = binary; 2GL = mnemonics (assembly); 3GL = English-like (C, Java); 4GL = SQL, Python.', 'Assembly needs an assembler; high-level languages need a compiler or interpreter.', 'Machine language is fastest but not portable; 4GLs need the fewest lines but cost most to run.', 'C is a 3GL: high-level, procedural, compiled.'])
s += QA('g', 'Name one example language from each of the four generations.', '1GL: machine language (pure binary). 2GL: assembly language. 3GL: C / Java / FORTRAN. 4GL: SQL / Python / MATLAB.')
s += QA('y', 'Why is a program written in assembly language not portable, while a C program generally is?',
        'Assembly mnemonics map almost one-to-one onto one particular CPU\'s instruction set (its registers, instruction formats and addressing modes). Different architectures (for example x86 and ARM) have different instruction sets, so assembly code written for one has to be rewritten for another. A C program is written in a standardised high-level syntax; a C compiler for the target machine translates the same source into whatever machine code that CPU needs, so the same .c file can be recompiled with little or no change on many machines. That is what portability means.')
s += QA('r', 'A company must write firmware that runs as fast as possible on an embedded chip with only a few KB of memory, and separately wants a quick one-off script to pull rows from a database. Suggest a language generation for each and justify.',
        'Firmware: a low-level language (assembly, 2GL, or even hand-tuned machine code). Low-level code runs very fast with no translation overhead and needs very little memory, which matches the few-KB constraint; being hard to write and not portable is acceptable for a fixed chip. Database script: a 4GL such as SQL. The task is naturally "what" (certain rows) rather than "how" to search; it needs very few lines, is quick to write and performance is not the constraint, so the 4GL drawbacks (less standardised, costlier to run) do not matter for a one-off script.')

# ------------------------------------------------------------------ 3
s += H1('3. Programming Paradigms')
s += [P('A <b>programming paradigm</b> is a style or underlying philosophy of how you instruct the computer: it guides how a program is designed and implemented.')]
s += [H2('3.1 Imperative vs declarative')]
s += BUL(['<b>Imperative</b> – works by changing the program\'s <i>state</i> through assignment statements, executed step by step (closely tied to the Von Neumann machine). Advantages: simple to understand, supports familiar variables, loops and conditions. Disadvantages: complex problems become hard to manage; less suited to large-scale or parallel programming. Examples: C, FORTRAN, Pascal, BASIC.',
          '<b>Declarative</b> – states <i>what</i> is wanted without describing step-by-step control flow; common in databases and parallel programming. Advantages: cleaner code focused on the result, easier parallelism. Disadvantages: less control over execution and performance tuning; internal execution is harder to debug. Examples: SQL, Haskell, Erlang, Lisp, ML, Clojure.'])
s += TABLE([['Basis', 'Imperative', 'Declarative'],
            ['Approach', 'Tells HOW to do it, step by step', 'Tells WHAT result is wanted'],
            ['State', 'Changes program state via assignments', 'No or minimal mutable state'],
            ['Control flow', 'Explicit: loops and conditionals', 'System decides the execution flow'],
            ['Examples', 'C, FORTRAN, Pascal, BASIC', 'Haskell, Erlang, Lisp, SQL, ML']], [1.2, 2.8, 2.8])
s += [H2('3.2 Procedural vs object-oriented vs functional')]
s += TABLE([['Basis', 'Procedural', 'Object-oriented (OOP)', 'Functional'],
            ['Basic unit', 'Procedure / function', 'Object (instance of a class)', 'Pure mathematical function'],
            ['Focus', 'Sequence of steps (HOW)', 'Data and behaviour together', 'Evaluating expressions (WHAT)'],
            ['Design', 'Top-down', 'Bottom-up', 'Function composition'],
            ['Data', 'Separate from functions; often global', 'Encapsulated inside objects', 'Immutable; never changed in place'],
            ['Reuse', 'Function libraries', 'Inheritance + polymorphism', 'Higher-order functions'],
            ['Loops', 'for, while', 'for, while', 'Recursion, map/filter/reduce'],
            ['Security', 'Low – global data accessible', 'High – private/public access', 'High – immutability'],
            ['Languages', 'C, Pascal, FORTRAN', 'C++, Java, Python, C#', 'Haskell, Lisp, Erlang, F#']], [1, 2, 2, 2])
s += [H3('Why C is a procedural language')]
s += BUL(['A program is a collection of functions; execution starts at `main()`.', 'Top-down design: a large problem is broken into smaller functions.', 'There are no classes, objects, inheritance or polymorphism built in.', '`struct` holds data only – no methods are attached to it.', 'Control is structured: sequence, `if`/`switch`, loops.'])
s += CODE('''
#include <stdio.h>

int area(int l, int b) { return l * b; }   /* a procedure */

int main(void) {
    printf("%d\\n", area(4, 5));
    return 0;
}
''', run=True, label='Procedural style in C')
s += RECALL(['Imperative = HOW; declarative = WHAT.', 'Procedural: top-down, functions, data separate (C, Pascal).', 'OOP: objects bundle data and methods; encapsulation, inheritance (Java, C++).', 'Functional: immutable data, recursion, pure functions (Haskell).', 'C = procedural + imperative + 3GL.'])
s += QA('g', 'Is C an imperative or a declarative language? Give one reason.', 'C is imperative: programs are an explicit, ordered sequence of statements that change program state step by step (assignments, loops), which is exactly the imperative paradigm.')
s += QA('y', 'A beginner writes a C program using only sequential assignments and loops and claims it is "declarative because it tells the computer what answer to get". Correct this.',
        'A paradigm is declarative only when the programmer states the desired result or relationship and leaves the execution strategy to the system (an SQL query does not say how to search a table). Writing explicit assignments and loops that manipulate state step by step is the definition of imperative programming, because the programmer dictates <i>how</i> (order, loop control, variable updates), not just <i>what</i>. Every program produces some result; that alone does not make it declarative.')
s += QA('y', 'Differentiate between the procedural, OOP and functional paradigms.', [('lines', ['<b>Procedural:</b> top-down design with functions; data is separate from functions (C).', '<b>OOP:</b> objects bundle data and methods; encapsulation, inheritance, polymorphism (Java, C++).', '<b>Functional:</b> programs are built by composing pure functions on immutable data; recursion replaces loops (Haskell).', '<b>Data handling:</b> procedural – often global; OOP – encapsulated; functional – no mutable state.'])])
# ------------------------------------------------------------------ 4
s += H1('4. Assembler, Compiler, Interpreter, Linker and Loader')
s += [P('A computer only understands machine language, so every program written in any other language must be <b>translated</b>. Three kinds of translators exist, followed by two helper programs, the linker and the loader.')]
s += BUL(['<b>Assembler</b> – translates assembly language (mnemonics) directly into machine language / object code.',
          '<b>Compiler</b> – translates the <i>entire</i> high-level source program into machine code in one go, before execution. It checks the whole program first; if there are errors it lists them all and produces nothing, otherwise it produces an executable. Compiled programs usually run faster.',
          '<b>Interpreter</b> – translates and executes the source <i>line by line</i> without producing a stand-alone executable. Easier to debug interactively, but usually slower because the translation is repeated on every run.'])
s += TABLE([['Basis', 'Compiler', 'Interpreter'],
            ['Translation unit', 'Entire program at once', 'One statement at a time'],
            ['Output', 'Separate executable file (.exe / a.out)', 'No file – executes in place'],
            ['Speed of execution', 'Fast (translated once)', 'Slower (translated on every run)'],
            ['Error reporting', 'All errors listed at the end; nothing runs until fixed', 'Stops at the first error; earlier lines already executed'],
            ['Memory', 'More during compilation (object code is stored)', 'Less – no object code stored'],
            ['Source needed to run?', 'No – only the executable is distributed', 'Yes – source must be present'],
            ['Debugging', 'Harder', 'Easier (line by line)'],
            ['Examples', 'C, C++ (GCC, Clang, Turbo C)', 'Python, Ruby, BASIC, JavaScript']], [1.5, 3, 3])
s += NOTE('Java uses both: `javac` compiles source to <i>bytecode</i>, and the JVM interprets / JIT-compiles the bytecode.')
s += [H2('4.1 Linker and loader')]
s += BUL(['<b>Linker</b> – large programs are split into modules. Each module is compiled to object code (.o); the linker combines all object files <i>and</i> the library code they need into one single executable. It resolves external references (where is `printf` defined?). Static linking embeds library code in the exe; dynamic linking links it at run time (.dll / .so). A missing library gives a link error such as <i>undefined reference to sqrt</i>. The compiler normally invokes the linker automatically as its last step.',
          '<b>Loader</b> – copies the executable (and the libraries it needs) from secondary storage into main memory, sets up the stack, resolves memory addresses and transfers control to `main()`. Only then can the CPU fetch and execute instructions.'])
s += TABLE([['Stage', 'Input → Output', 'Command'], ['Pre-process', '.c → .i (expand macros and headers)', 'gcc -E hello.c -o hello.i'], ['Compile', '.i → .s (assembly)', 'gcc -S hello.i -o hello.s'],
            ['Assemble', '.s → .o (object code)', 'gcc -c hello.s -o hello.o'], ['Link', '.o + libraries → executable', 'gcc hello.o -o hello'], ['Load & run', 'executable → RAM → CPU', './hello']], [1.2, 3.2, 2.6])
s += RECALL(['Assembler: assembly → machine code; compiler: HLL → executable; interpreter: line by line.', 'Compiler: fast run, errors listed together; interpreter: slow run, stops at first error.', 'Linker joins object files and libraries; loader puts the exe in RAM and starts it.', 'Build chain: Preprocess → Compile → Assemble → Link → Load.'])
s += QA('g', 'What is the main functional difference between a compiler and an interpreter?', 'A compiler translates the entire program into machine code before any of it runs (errors are reported together); an interpreter translates and executes line by line and stops as soon as it meets an error.')
s += QA('y', 'Why do compiled programs generally run faster than interpreted ones, yet compilers can be "time consuming" for long programs?',
        'All translation work (lexical analysis, parsing, optimisation, code generation) is done once, up front, producing native machine code that the CPU runs directly with no further translation overhead, so every run is fast. But that up-front step must process and optimise every line before producing the executable, so it can take long for very large programs. An interpreter starts immediately, translating each line as it is reached, at the cost of repeating that work on every run.')
s += QA('y', 'Explain the role of the linker and the loader in program execution.', [('lines', ['<b>Linker:</b> combines the object files of all modules plus the library routines they need into one executable, and resolves external references such as where `printf` is defined.', '<b>Loader:</b> copies that executable from disk into RAM, sets up the stack, resolves addresses and jumps to `main()`.'])])
s += QA('r', 'Describe the complete journey of a C program `prog.c` from the moment it is written to the moment its output appears on screen, naming every translator and support program involved.',
        [('steps', ['The programmer writes the source code in `prog.c`.', 'The <b>compiler</b> checks the whole file for syntax/semantic errors. If there are any it lists them and stops; otherwise it translates the source into object code for the target machine.', 'If the program has several modules, each is compiled to its own object file. The <b>linker</b> combines them with the required library routines into a single executable (`a.out` or `.exe`).', 'When the user runs the program, the <b>loader</b> copies the executable from secondary storage into RAM.', 'The CPU fetches instructions from memory (control unit) and executes arithmetic and logic (ALU), using registers for intermediate values.', 'Output instructions such as `printf` send data to the output unit, which converts the binary result into readable characters on the screen.'])])
# ------------------------------------------------------------------ 5
s += H1('5. Process of Programming')
s += [P('Writing a program is not just typing code. The work is divided into two phases: the <b>problem-solving phase</b> (produce an ordered sequence of steps – the algorithm) and the <b>implementation phase</b> (code the algorithm in a real programming language and make it work).')]
s += TABLE([['Step', 'Name', 'What to do'],
            ['1', 'Define and model the problem', 'Identify inputs, outputs, constraints and formulas; clarify exactly what is asked. (Real problems such as the Indian Railways reservation system are huge – in this course problems are defined precisely and kept simple.)'],
            ['2', 'Design the algorithm', 'Break the problem into sub-tasks; write ordered steps top-down; check the logic'],
            ['3', 'Represent the solution', 'Draw a flowchart (visual) or write pseudocode (structured English)'],
            ['4', 'Code', 'Translate the algorithm into C, following the syntax rules'],
            ['5', 'Compile and execute', 'Run the compiler, fix syntax errors, get the executable and run it'],
            ['6', 'Test and debug', 'Test with normal, boundary and invalid data; fix logical and run-time bugs'],
            ['7', 'Document', 'Add comments; write a usage guide for other programmers'],
            ['8', 'Maintain', 'Update the program when requirements change or new bugs are found']], [0.5, 2, 5.3])
s += [H2('5.1 Pseudocode')]
s += [P('<b>Pseudocode</b> is an artificial, informal language very close to everyday English. It lets programmers develop an algorithm without worrying about exact programming syntax. There is no single fixed syntax (some organisations keep a house style), it cannot be executed, and it is language-independent – it bridges the gap between the algorithm and the actual code.')]
s += CODE('''
Input a set of 4 marks
Calculate the average by summing and dividing by 4
If average is below 40
    Print "FAIL"
Else
    Print "PASS"
End
''', label='Pseudocode – final grade of a student (pass mark = 40)')
s += RECALL(['8 steps: Define → Algorithm → Pseudocode/Flowchart → Code → Compile → Test → Document → Maintain.', 'Pseudocode is English-like, has no syntax rules and is language-independent.', 'Test with normal, boundary and invalid data.', 'Maintenance = modifying the program after deployment.'])

# ------------------------------------------------------------------ 6
s += H1('6. Algorithms')
s += [P('An <b>algorithm</b> is a finite, ordered set of well-defined, unambiguous steps that solves a problem. It is universal – independent of any programming language – and it is written <i>before</i> coding begins. It should not contain actual computer code; it should be generic enough to be implemented in many languages.')]
s += [H2('6.1 Qualities of a good algorithm')]
s += TABLE([['Property', 'Meaning'],
            ['Input', 'Takes zero or more well-defined inputs'], ['Output', 'Produces at least one output – the answer'],
            ['Definiteness', 'Every step is precise and unambiguous ("add 5 to X", not "add a little")'], ['Finiteness', 'Must terminate after a finite number of steps – no infinite loops'],
            ['Effectiveness', 'Each step is basic enough to be done by hand in finite time'], ['Correctness', 'Gives the correct output for every valid input'],
            ['Generality', 'Solves a whole class of problems, not one specific case'], ['Efficiency', 'Uses minimum time and memory – the most effective method among possible ways'],
            ['Language independence', 'Can be implemented in any programming language'], ['Simplicity', 'Easy to read, modify and maintain']], [1.6, 5.6])
s += [H2('6.2 Algorithm examples')]
s += ALGO_FLOW('Add two numbers', ['Step 1: Start', 'Step 2: Read A, B', 'Step 3: SUM = A + B', 'Step 4: Print SUM', 'Step 5: Stop'], [('start', 'START'), ('io', 'Read A, B'), ('proc', 'SUM = A + B'), ('io', 'Print SUM'), ('stop', 'STOP')])
s += ALGO_FLOW('Larger of two numbers', ['Step 1: Input X, Y', 'Step 2: If (X > Y)', '    Print X', '  else', '    Print Y', 'Step 3: Stop'], [('start', 'START'), ('io', 'Read X, Y'), ('if', 'X > Y ?', 'Print X', 'Print Y'), ('stop', 'STOP')])
s += ALGO_FLOW('Student grade (average of 4 subjects, pass = 40)', ['Step 1: Input M1, M2, M3, M4', 'Step 2: Grade = (M1+M2+M3+M4)/4', 'Step 3: If (Grade < 40)', '    Print "FAIL"', '  else', '    Print "PASS"', 'Step 4: Stop'], [('start', 'START'), ('io', 'Read M1..M4'), ('proc', 'Grade = (M1+..+M4)/4'), ('if', 'Grade < 40 ?', 'Print FAIL', 'Print PASS'), ('stop', 'STOP')])
s += ALGO_FLOW('Sum of first N natural numbers', ['Step 1: Input N', 'Step 2: SUM = 0, COUNT = 1', 'Step 3: If (COUNT <= N)', '    SUM = SUM + COUNT', '    COUNT = COUNT + 1', '    Repeat Step 3', '  else Print SUM', 'Step 4: Stop'],
               [('start', 'START'), ('io', 'Read N'), ('proc', 'SUM = 0, COUNT = 1'), ('loop', 'COUNT <= N ?', [('proc', 'SUM = SUM + COUNT'), ('proc', 'COUNT = COUNT + 1')]), ('io', 'Print SUM'), ('stop', 'STOP')])
s += ALGO_FLOW('Factorial of N', ['Step 1: Input N', 'Step 2: PROD = 1, COUNT = 1', 'Step 3: If (COUNT <= N)', '    PROD = PROD * COUNT', '    COUNT = COUNT + 1', '    Repeat Step 3', '  else Print PROD', 'Step 4: Stop'],
               [('start', 'START'), ('io', 'Read N'), ('proc', 'PROD = 1, COUNT = 1'), ('loop', 'COUNT <= N ?', [('proc', 'PROD = PROD * COUNT'), ('proc', 'COUNT = COUNT + 1')]), ('io', 'Print PROD'), ('stop', 'STOP')])
s += [P('More algorithms from the course slides (the same pattern – a loop with a running total – is reused each time):')]
s += BUL(['<b>Swap two numbers:</b> Step 1 Start; Step 2 Read A, B; Step 3 TEMP = A; A = B; B = TEMP; Step 4 Print A, B; Step 5 Stop.',
          '<b>Largest of three (X, Y, Z):</b> If X > Y then LAR = X else LAR = Y; then if LAR > Z print LAR else print Z. (Find the winner of the first pair, then compare it with the third.)',
          '<b>Sum of squares of first N:</b> same as the sum algorithm but SUM = SUM + COUNT×COUNT.',
          '<b>Sum 1×2 + 2×3 + 3×4 + … (N terms):</b> SUM = SUM + COUNT×(COUNT + 1).'])
s += TABLE([['Basis', 'Algorithm', 'Program'],
            ['Stage', 'Design stage – written first', 'Implementation – written after the algorithm'],
            ['Language', 'Natural language / pseudocode; language-independent', 'A specific language (C, Java) with strict syntax'],
            ['Execution', 'Cannot be executed by a computer directly', 'Compiled / interpreted and executed'],
            ['Termination', 'Must always terminate (finiteness)', 'May run indefinitely (OS, web server)'],
            ['Errors', 'No syntax errors (informal)', 'Must be free of syntax errors to compile'],
            ['Hardware / OS', 'Independent', 'Depends on compiler, OS, hardware']], [1.2, 3, 3])
s += RECALL(['5 essential properties: input, output, definiteness, finiteness, effectiveness.', 'Algorithm = language-independent design; program = language-specific implementation.', 'An algorithm must terminate; a program (e.g. a server) may run forever.', 'The algorithm is written at the design stage, before coding.'])
s += QA('g', 'Write an algorithm to input two numbers and print their sum.', [('lines', ['Step 1: Start', 'Step 2: Input N1, N2', 'Step 3: SUM = N1 + N2', 'Step 4: Print SUM', 'Step 5: Stop'])])
s += QA('g', 'Write an algorithm to find whether a given number is even or odd.', [('lines', ['Step 1: Input N', 'Step 2: REM = N mod 2', 'Step 3: If (REM == 0) Print "EVEN"', '              else Print "ODD"', 'Step 4: Stop'])])
s += QA('y', 'Write an algorithm to calculate simple interest for principal P, rate R and time T.', [('lines', ['Step 1: Input P, R, T', 'Step 2: SI = (P × R × T) / 100', 'Step 3: Print SI', 'Step 4: Stop'])])
s += QA('y', 'Write an algorithm to find the largest of three numbers X, Y, Z.', [('lines', ['Step 1: Input X, Y, Z', 'Step 2: If (X > Y) then LAR = X', '              else LAR = Y', 'Step 3: If (LAR > Z) then Print LAR', '              else Print Z', 'Step 4: Stop']), 'First find the larger of X and Y, then compare that winner with Z.'])
s += QA('r', 'Write a complete algorithm to check whether a number N (N > 1) is prime.', [('lines', ['Step 1: Input N', 'Step 2: FLAG = 1 (assume prime), COUNT = 2', 'Step 3: Repeat while (COUNT <= N/2)', '              If (N mod COUNT == 0) then FLAG = 0 and stop repeating', '              COUNT = COUNT + 1', 'Step 4: If (FLAG == 1) Print "PRIME"', '              else Print "NOT PRIME"', 'Step 5: Stop']), '<i>Reasoning:</i> a number is prime only if no integer from 2 to N/2 divides it exactly. We test every candidate divisor and set FLAG to 0 the moment one divides N.'])
s += QA('r', 'Write the algorithm for the factorial of N and trace it for N = 4.', [('lines', ['Step 1: Input N', 'Step 2: PROD = 1, COUNT = 1', 'Step 3: If (COUNT <= N)', '              PROD = PROD × COUNT', '              COUNT = COUNT + 1', '              Repeat Step 3', '          else Print PROD', 'Step 4: Stop']), '<b>Trace for N = 4:</b>', ('work', '''
COUNT   PROD (after the step)     COUNT <= 4 ?
  1     1 x 1 = 1                 yes
  2     1 x 2 = 2                 yes
  3     2 x 3 = 6                 yes
  4     6 x 4 = 24                yes
  5     (stop)                    no  -> Print PROD = 24
'''), '4! = 4 × 3 × 2 × 1 = 24, which matches the trace.'])
# ------------------------------------------------------------------ 7
s += H1('7. Flowcharts')
s += [P('A <b>flowchart</b> is a graphical representation of an algorithm. It uses standard symbols (boxes of different shapes) joined by arrows to show the order of operations and the control flow.')]
s += TABLE([['Symbol', 'Name', 'Use'],
            ['Oval / rounded rectangle', 'Terminal', 'Start or Stop of the flowchart'],
            ['Parallelogram', 'Input / Output', 'Read input from the user or print output'],
            ['Rectangle', 'Process', 'Calculations and assignments (SUM = A + B)'],
            ['Diamond', 'Decision', 'A condition check with Yes/No (True/False) exits'],
            ['Arrow', 'Flow line', 'Shows the direction of control flow'],
            ['Circle', 'Connector', 'Joins parts of a flowchart, e.g. across pages']], [2, 1.5, 3.7])
s += [H2('7.1 The four basic structures')]
s += TABLE([['Structure', 'Description', 'C equivalent'],
            ['Sequence', 'Steps executed one after another', '`a = 1; b = 2; c = a + b;`'],
            ['Decision (selection)', 'One of two paths chosen by a condition', '`if (cond) {...} else {...}`'],
            ['Repetition (loop)', 'Steps repeated while a condition holds', '`for`, `while`, `do-while`'],
            ['Case', 'One of several paths chosen by the value of a variable', '`switch-case`']], [1.6, 3.2, 2.4])
s += [H2('7.2 Flowchart + algorithm + C program')]
s += [P('Every flowchart in the previous section converts directly to C: a sequence becomes consecutive statements, a decision becomes `if-else` and a loop becomes `while`/`for`. The three programs below were compiled and run, so the outputs are real.')]
s += CODE('''
#include <stdio.h>

int main(void) {
    int a, b, sum;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    sum = a + b;
    printf("Sum = %d\\n", sum);
    return 0;
}
''', run=True, stdin='12 30\n', label='Add two numbers (input: 12 30)')
s += CODE('''
#include <stdio.h>

int main(void) {
    int n, sum = 0, i = 1;
    scanf("%d", &n);
    while (i <= n) {          /* the loop in the flowchart */
        sum += i;
        i++;
    }
    printf("Sum = %d\\n", sum);
    return 0;
}
''', run=True, stdin='5\n', label='Sum of first N natural numbers (input: 5)')
s += CODE('''
#include <stdio.h>

int main(void) {
    float m1, m2, m3, m4, g;
    scanf("%f %f %f %f", &m1, &m2, &m3, &m4);
    g = (m1 + m2 + m3 + m4) / 4;
    if (g < 40)
        printf("FAIL (avg=%.1f)\\n", g);
    else
        printf("PASS (avg=%.1f)\\n", g);
    return 0;
}
''', run=True, stdin='50 60 30 70\n', label='Student grade (input: 50 60 30 70)')
s += [H2('7.3 Flowchart vs algorithm')]
s += TABLE([['Basis', 'Algorithm', 'Flowchart'],
            ['Form', 'Textual (words / pseudocode)', 'Graphical (boxes, diamonds, arrows)'],
            ['Ease of creation', 'Quick to write and edit', 'Time-consuming to draw and modify'],
            ['Understanding', 'Harder to visualise the flow', 'Easy to follow at a glance'],
            ['Complex logic', 'Handles large problems well', 'Becomes cluttered for big problems'],
            ['Branches / loops', 'Written as words: "If … go to Step 3"', 'Shown by diamonds and loop-back arrows'],
            ['Debugging', 'Step numbers make errors easy to locate', 'Flow errors such as infinite loops are visible, but large charts are hard to edit'],
            ['Rules', 'No strict symbols', 'Uses standard ANSI/ISO symbols']], [1.3, 3, 3])
s += RECALL(['Oval = terminal, parallelogram = I/O, rectangle = process, diamond = decision, circle = connector.', 'Four structures: sequence, decision, repetition, case.', 'A diamond has two exits: Yes and No.', 'Flowchart is best for small/medium logic and teaching; algorithm for large, complex problems.'])
s += QA('g', 'State two advantages of a flowchart over a plain algorithm and one advantage of an algorithm over a flowchart.', [('lines', ['<b>Flowchart:</b> (1) easier to understand at a glance because it is a diagram; (2) branching and looping are visually obvious (diamonds and loop-back arrows).', '<b>Algorithm:</b> quicker to write and edit, and handles large complex problems without the clutter of a big diagram.'])])
s += QA('y', 'Write an algorithm (and note the flowchart shape) for the roots of ax² + bx + c = 0, given d = √(b² − 4ac), x1 = (−b + d)/2a and x2 = (−b − d)/2a.',
        [('lines', ['Step 1: Input a, b, c', 'Step 2: D = b×b − 4×a×c', 'Step 3: If (D < 0) Print "No real roots" and Stop', 'Step 4: d = sqrt(D)', 'Step 5: x1 = (−b + d) / (2×a);  x2 = (−b − d) / (2×a)', 'Step 6: Print x1, x2', 'Step 7: Stop']),
         '<b>Flowchart shape:</b> START → Input a, b, c → Compute D → decision (D < 0 ?). Yes → print "no real roots" → STOP. No → compute d, x1, x2 → print x1, x2 → STOP.'],
        code=CODE('''
#include <stdio.h>
#include <math.h>

int main(void) {
    float a, b, c, D, d, x1, x2;
    scanf("%f %f %f", &a, &b, &c);
    D = b * b - 4 * a * c;
    if (D < 0) {
        printf("No real roots\\n");
        return 0;
    }
    d = sqrt(D);
    x1 = (-b + d) / (2 * a);
    x2 = (-b - d) / (2 * a);
    printf("x1 = %.2f, x2 = %.2f\\n", x1, x2);
    return 0;
}
''', run=True, stdin='1 -5 6\n', label='C code (input: 1 -5 6)'))
s += QA('r', 'Write an algorithm and C code to grade students: ≥90 → Ex, 80–89 → A, 70–79 → B, 60–69 → C, 50–59 → D, 35–49 → P, below 35 → F.',
        [('lines', ['Step 1: Input Marks', 'Step 2: If (Marks >= 90) Grade = "Ex"', '        else if (Marks >= 80) Grade = "A"', '        else if (Marks >= 70) Grade = "B"', '        else if (Marks >= 60) Grade = "C"', '        else if (Marks >= 50) Grade = "D"', '        else if (Marks >= 35) Grade = "P"', '        else Grade = "F"', 'Step 3: Print Grade', 'Step 4: Stop']),
         '<i>Reasoning:</i> conditions are checked from the highest cut-off downward. Because it is a strict else-if chain the first true condition decides the grade, so the order matters.'],
        code=CODE('''
#include <stdio.h>

int main(void) {
    int m;
    scanf("%d", &m);
    if (m >= 90)      printf("Ex\\n");
    else if (m >= 80) printf("A\\n");
    else if (m >= 70) printf("B\\n");
    else if (m >= 60) printf("C\\n");
    else if (m >= 50) printf("D\\n");
    else if (m >= 35) printf("P\\n");
    else              printf("F\\n");
    return 0;
}
''', run=True, stdin='73\n', label='C code (input: 73)'))
s += QA('r', 'Write an algorithm and C code for SUM = 1×2 + 2×3 + 3×4 + … up to N terms.',
        [('lines', ['Step 1: Input N', 'Step 2: SUM = 0, COUNT = 1', 'Step 3: While (COUNT <= N)', '              SUM = SUM + COUNT × (COUNT + 1)', '              COUNT = COUNT + 1', 'Step 4: Print SUM', 'Step 5: Stop']), 'Check for N = 3: 1×2 + 2×3 + 3×4 = 2 + 6 + 12 = 20.'],
        code=CODE('''
#include <stdio.h>

int main(void) {
    int n, sum = 0, i = 1;
    scanf("%d", &n);
    while (i <= n) {
        sum += i * (i + 1);
        i++;
    }
    printf("%d\\n", sum);
    return 0;
}
''', run=True, stdin='3\n', label='C code (input: 3)'))
# ------------------------------------------------------------------ 8
s += H1('8. Machine Representation — Binary and ASCII')
s += [P('A computer stores and processes everything – numbers, characters, instructions, images – using only two electrical states, written <b>0</b> and <b>1</b>. This is the <b>binary</b> (base-2) number system, which is why bits and bytes are fundamental to understanding how a computer "sees" data.')]
s += [H2('8.1 Bits, bytes and units')]
s += BUL(['<b>Bit</b> – a single binary digit, 0 or 1; the smallest unit of data.', '<b>Nibble</b> – 4 bits (values 0–15).', '<b>Byte</b> – 8 consecutive bits (values 0–255). Maximum unsigned value in 1 byte = 11111111₂ = 255 = 2⁸ − 1; a byte has 2⁸ = 256 distinct values.',
          '<b>Word</b> – the natural data unit of a processor (16 / 32 / 64 bits). Largest unsigned 32-bit value = 2³² − 1 = 4294967295.', '1 KB = 1024 bytes; 1 MB = 1024 KB; 1 GB = 1024 MB.'])
s += FORMULA('With n bits you can represent 2<super>n</super> different values; the unsigned range is 0 to 2<super>n</super> − 1. If one bit is used as a sign bit, the magnitude range is 0 to 2<super>n−1</super> − 1.')
s += [H2('8.2 Decimal ↔ binary')]
s += [P('<b>Decimal</b> (base 10) uses digits 0–9 with weights 10⁰, 10¹, 10², …, e.g. 723 = 7×10² + 2×10¹ + 3×10⁰. <b>Binary</b> (base 2) uses digits 0 and 1 with weights 2⁰, 2¹, 2², … from the right.')]
s += [H3('Decimal to binary – repeated division by 2')]
s += [P('Divide the number by 2 again and again, note each remainder, and read the remainders from <b>bottom to top</b>.')]
s += CODE('''
Convert 25 to binary
25 / 2 = 12  remainder 1   (LSB)
12 / 2 =  6  remainder 0
 6 / 2 =  3  remainder 0
 3 / 2 =  1  remainder 1
 1 / 2 =  0  remainder 1   (MSB)
Read bottom to top: 11001      so  (25)10 = (11001)2
''')
s += [H3('Binary to decimal – positional notation')]
s += CODE('''
(11001)2 = 1x2^4 + 1x2^3 + 0x2^2 + 0x2^1 + 1x2^0
         = 16 + 8 + 0 + 0 + 1
         = 25                          so  (11001)2 = (25)10
''')
s += TABLE([['Decimal', 'Binary', 'Working'], ['5', '101', '4 + 0 + 1'], ['10', '1010', '8 + 0 + 2 + 0'], ['13', '1101', '8 + 4 + 0 + 1'], ['15', '1111', '8 + 4 + 2 + 1'],
            ['25', '11001', '16 + 8 + 0 + 0 + 1'], ['50', '110010', '32 + 16 + 0 + 0 + 2 + 0'], ['57', '111001', '32 + 16 + 8 + 0 + 0 + 1'], ['100', '1100100', '64 + 32 + 0 + 0 + 4 + 0 + 0'], ['128', '10000000', '2⁷'], ['255', '11111111', 'all 8 bits set = 2⁸ − 1']], [1, 1.6, 4])
s += [H2('8.3 Character representation – ASCII')]
s += [P('Characters are not stored as pictures of letters; they are stored as small integers using a standard called <b>ASCII</b> (American Standard Code for Information Interchange). It maps letters, digits and symbols to 7-bit codes (0–127); extended ASCII uses 8 bits (0–255). Letters are consecutive, so A=65, B=66, C=67, D=68 …')]
s += TABLE([['Character', 'ASCII', 'Character', 'ASCII'], ["'A' – 'Z'", '65 – 90', "'a' – 'z'", '97 – 122'], ["'0' – '9'", '48 – 57', 'space', '32'], ["'\\n' (newline)", '10', "'@'", '64']], [1.3, 1.2, 1.3, 1.2])
s += NOTE('Lowercase = uppercase + 32 (e.g. \'A\' = 65, \'a\' = 97). In C, `char c = \'A\'; printf("%d", c);` prints 65 – characters are just small integers and can be compared and manipulated using their ASCII values.')
s += CODE('''
#include <stdio.h>

int main(void) {
    char c = 'A';
    printf("%c = %d\\n", c, c);
    printf("%c\\n", c + 32);      /* lower-case equivalent */
    return 0;
}
''', run=True, label='ASCII demo')
s += RECALL(['1 byte = 8 bits; unsigned byte range 0–255; n bits → 2ⁿ values.', 'Decimal → binary: divide by 2, read remainders bottom to top.', 'Binary → decimal: add bit × 2^position (rightmost position is 0).', "ASCII: 'A' = 65, 'a' = 97, '0' = 48; lowercase = uppercase + 32."])
s += QA('g', 'Convert the binary number 1010 to decimal.', [('work', '''
1010 (binary)  =  1 x 2^3  +  0 x 2^2  +  1 x 2^1  +  0 x 2^0
               =  8  +  0  +  2  +  0
               =  10
'''), 'Answer: 1010₂ = 10₁₀.'])
s += QA('g', 'Convert 13 (decimal) to binary.', ['Divide repeatedly by 2 and note the remainders:', ('work', '''
13 / 2 = 6   remainder 1    (last bit)
 6 / 2 = 3   remainder 0
 3 / 2 = 1   remainder 1
 1 / 2 = 0   remainder 1    (first bit)
Read the remainders bottom to top:  1101
Check: 8 + 4 + 0 + 1 = 13
'''), 'Answer: 13₁₀ = 1101₂.'])
s += QA('g', 'How many bits are in 3 bytes and what is the largest unsigned value they can hold?', [('steps', ['Bits = 3 × 8 = 24.', 'Largest unsigned value = 2²⁴ − 1 = 16,777,216 − 1 = <b>16,777,215</b>.'])])
s += QA('g', "If the ASCII value of 'A' is 65, what is the ASCII value of 'D'?", [('work', '''
A = 65
B = 66
C = 67
D = 68      (65 + 3)
'''), 'Consecutive uppercase letters have consecutive codes, so D = 68.'])
s += QA('y', 'Convert 57 (decimal) to binary using the division method.', [('work', '''
57 / 2 = 28   remainder 1    (last bit)
28 / 2 = 14   remainder 0
14 / 2 =  7   remainder 0
 7 / 2 =  3   remainder 1
 3 / 2 =  1   remainder 1
 1 / 2 =  0   remainder 1    (first bit)
Read the remainders bottom to top:  111001
Check: 32 + 16 + 8 + 0 + 0 + 1 = 57
'''), 'Answer: 57₁₀ = 111001₂.'])
s += QA('y', 'Convert 11111111₂ to decimal and explain why it is the largest value storable in 1 byte.', [('work', '''
11111111 = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
         = 255
'''), 'A byte has exactly 8 bit positions. Setting every position to 1 (the largest binary digit) gives the maximum value, 2⁸ − 1 = 255.'])
s += QA('y', "The ASCII code of 'a' is 97 and of 'A' is 65. What is the difference between any lowercase letter and its uppercase form? Verify with 'z' (122).", [('steps', ["Difference = 97 − 65 = <b>32</b>.", "Verify: 'z' = 122, so 'Z' should be 122 − 32 = 90.", "90 is indeed the ASCII code of 'Z'."]), 'This is why subtracting 32 converts a lowercase letter to uppercase in C (or use `toupper()`).'])
s += QA('y', 'Convert 1010₂ to decimal and 50₁₀ to binary.', [('work', '''
Part 1:  1010 (binary) = 1x8 + 0x4 + 1x2 + 0x1 = 8 + 0 + 2 + 0 = 10

Part 2:  50 / 2 = 25   remainder 0    (last bit)
         25 / 2 = 12   remainder 1
         12 / 2 =  6   remainder 0
          6 / 2 =  3   remainder 0
          3 / 2 =  1   remainder 1
          1 / 2 =  0   remainder 1    (first bit)
         Read bottom to top:  110010
         Check: 32 + 16 + 0 + 0 + 2 + 0 = 50
'''), 'Answers: 1010₂ = 10₁₀ and 50₁₀ = 110010₂.'])
s += QA('r', 'A sensor reports readings in exactly 2 bytes, unsigned. (a) What is the maximum reading? (b) If one bit is reserved as a sign bit to allow negatives, what is the new maximum magnitude and why is it about half of (a)?',
        [('lines', ['<b>(a)</b> 2 bytes = 16 bits, so the maximum is 2¹⁶ − 1 = <b>65,535</b>.', '<b>(b)</b> One bit now holds the sign, leaving 15 bits for the magnitude: 2¹⁵ − 1 = <b>32,767</b>.']),
         'Each bit doubles the range, so giving up one bit roughly halves the largest magnitude – in exchange, negative values can now be represented.'])
s += QA('y', 'Write an algorithm and C code for the area and perimeter of a rectangle.',
        [('lines', ['Step 1: Read L, B', 'Step 2: AREA = L × B', 'Step 3: PERI = 2 × (L + B)', 'Step 4: Print AREA, PERI', 'Step 5: Stop'])],
        code=CODE('''
#include <stdio.h>

int main(void) {
    float l, b;
    scanf("%f %f", &l, &b);
    printf("Area = %.2f\\n", l * b);
    printf("Perimeter = %.2f\\n", 2 * (l + b));
    return 0;
}
''', run=True, stdin='4 5\n', label='C code (input: 4 5)'))
ok = build('/home/sleepy/STUDY:)/sem-1/CP/cpclaude/Unit1_Notes.pdf' if len(sys.argv) < 2 else sys.argv[1], 1, 'Basics of Programming',
      '', '6 hrs · 15% weightage · C language',
      'Hardware / software · programming languages (4 generations) · paradigms · assembler / compiler / interpreter / linker / loader · process of programming · algorithms · flowcharts · machine representation',
      '#5b3fd6', s)
print('BUILD OK' if ok else 'BUILD HAS PROBLEMS')
