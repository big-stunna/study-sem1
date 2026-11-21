import sys
from lib import *
from unit5a import s

# ================================================================= 6
s += H1('6. Dynamic Memory Allocation')
s += [P('Ordinary (automatic) variables and arrays live on the <b>stack</b>, and their size must be known when the program is compiled – `int a[100];` wastes space if you need 5 and fails if you need 101. <b>Dynamic memory allocation</b> asks the system for memory from the <b>heap</b> <i>while the program is running</i>, so you can allocate exactly what is needed, and release it when finished. All the functions are declared in `<stdlib.h>`.')]
s += TABLE([['Basis', 'Stack (automatic)', 'Heap (dynamic)'], ['Size fixed', 'At compile time', 'At run time, as needed'], ['Lifetime', 'Until the function returns', 'Until you call `free()` (or the program ends)'], ['Managed by', 'Compiler (automatic)', 'Programmer (`malloc` / `free`)'], ['Typical use', 'Local variables, fixed arrays', 'Arrays sized by user input, linked lists, large data']], [1.4, 3, 3.1])
s += [H2('6.1 malloc() — memory allocation')]
s += SYNTAX('<b>ptr = (cast_type *) malloc(byte_size);</b> – allocates one contiguous block of `byte_size` bytes and returns a `void *` to it (cast it to the type you need). The memory is <b>not initialised</b> (it holds garbage). If the request fails, `malloc` returns <b>NULL</b> – always check.')
s += CODE('''
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, i;
    int *arr;
    scanf("%d", &n);
    arr = (int *) malloc(n * sizeof(int));        /* n ints, uninitialised */
    if (arr == NULL) {                            /* allocation can fail   */
        printf("Allocation failed\\n");
        return 1;
    }
    for (i = 0; i < n; i++) arr[i] = i * i;       /* use it like an array  */
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\\n");
    free(arr);                                    /* give it back          */
    arr = NULL;                                   /* avoid a dangling pointer */
    return 0;
}
''', run=True, stdin='6\n', label='input: 6')
s += [H2('6.2 calloc() — contiguous allocation')]
s += SYNTAX('<b>ptr = (cast_type *) calloc(n, element_size);</b> – allocates <b>n</b> blocks of `element_size` bytes each and <b>sets every byte to zero</b>. Two arguments instead of malloc\'s one. Example: `arr = (float *) calloc(25, sizeof(float));` gives 25 floats, all 0.0.')
s += [H2('6.3 realloc() and free()')]
s += BUL(['<b>realloc(ptr, new_size)</b> resizes a block you already allocated. Existing data is preserved (up to the smaller size); any new bytes are uninitialised. The block may be <i>moved</i>, so always use the returned pointer. If it fails it returns NULL and the <b>old block is still valid</b> – so assign to a temporary first.', '<b>free(ptr)</b> returns the block to the heap. Free each block <b>exactly once</b>.'])
s += CODE('''
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int i;
    int *a = (int *) calloc(5, sizeof(int));          /* five zeros          */
    if (a == NULL) return 1;
    printf("calloc: ");
    for (i = 0; i < 5; i++) printf("%d ", a[i]);
    printf("\\n");

    for (i = 0; i < 5; i++) a[i] = (i + 1) * 10;
    int *tmp = (int *) realloc(a, 8 * sizeof(int));   /* grow to 8 ints      */
    if (tmp == NULL) { free(a); return 1; }           /* old block still valid */
    a = tmp;
    for (i = 5; i < 8; i++) a[i] = (i + 1) * 10;      /* new part is uninitialised */
    printf("realloc: ");
    for (i = 0; i < 8; i++) printf("%d ", a[i]);
    printf("\\n");

    free(a);
    return 0;
}
''', run=True)
s += TABLE([['Basis', 'malloc()', 'calloc()'], ['Arguments', '1 (total bytes)', '2 (count, element size)'], ['Initialisation', 'No – contains garbage', 'Yes – all bytes zero'], ['Speed', 'Slightly faster', 'Slightly slower (zeroes the block)'], ['Syntax', '`malloc(n * sizeof(T))`', '`calloc(n, sizeof(T))`']], [1.5, 3, 3])
s += [H2('6.4 Dynamic array of structures')]
s += CODE('''
#include <stdio.h>
#include <stdlib.h>

struct student { int roll; float cgpa; };

int main(void) {
    int n = 3, i;
    struct student *st = (struct student *) malloc(n * sizeof(struct student));
    if (st == NULL) return 1;
    for (i = 0; i < n; i++) {               /* st[i] works like an array element */
        st[i].roll = 100 + i;
        st[i].cgpa = 7.5f + i * 0.5f;
    }
    for (i = 0; i < n; i++)
        printf("%d %.1f\\n", st[i].roll, st[i].cgpa);
    free(st);
    return 0;
}
''', run=True)
s += TABLE([['Memory error', 'What happens', 'Prevention'], ['<b>Memory leak</b>', 'Allocated block is never freed; the program slowly eats memory', 'Pair every `malloc` with one `free`'], ['<b>Dangling pointer</b>', 'Using a pointer after `free(ptr)`', 'Set `ptr = NULL` after free'], ['<b>Double free</b>', '`free(ptr)` called twice – undefined behaviour', 'Free once; NULL the pointer'], ['<b>Buffer overflow</b>', 'Writing beyond the n elements allocated', 'Respect the size: valid indices 0 … n−1'], ['<b>Unchecked NULL</b>', 'Using the result of a failed `malloc`', '`if (p == NULL) …` right after allocating']], [1.6, 3.4, 2.5])
s += RECALL(['Stack = fixed size at compile time; heap = sized at run time through `malloc`/`calloc`/`realloc`.', '`malloc(n*sizeof(T))` – 1 argument, uninitialised; `calloc(n, sizeof(T))` – 2 arguments, zeroed.', 'Both return `void *` and NULL on failure – always check.', '`free(p)` once; then set `p = NULL`.', '`realloc` may move the block and can fail without freeing the old one.'])
s += QA('g', 'Allocate an integer array of size n (read from the user) with `malloc`, fill it with squares (arr[i] = i × i), print it and free the memory.', [('steps', ['Read n, then `arr = (int *) malloc(n * sizeof(int));`.', 'If `arr == NULL` report the failure and stop.', 'Fill with a loop `arr[i] = i * i;` and print it.', '`free(arr);` at the end.']), 'The first program of this chapter is exactly this solution (for n = 6 it prints 0 1 4 9 16 25).'])
s += QA('y', 'Compare `calloc` and `malloc` with a snippet that allocates 5 ints with each and explain the difference.', [('steps', ['`calloc(5, sizeof(int))` returns 5 ints whose bytes are all zero.', '`malloc(5 * sizeof(int))` returns 5 ints with <b>indeterminate</b> (garbage) contents.', 'Reading the malloc\'d values before writing them gives unpredictable output; the calloc\'d values are always 0.']), 'The calloc line of the realloc program above prints 0 0 0 0 0.'],
        code=CODE('''
int *a = (int *) calloc(5, sizeof(int));      /* a[0..4] are all 0       */
int *b = (int *) malloc(5 * sizeof(int));     /* b[0..4] are unpredictable */
'''))
s += QA('r', 'Why must `realloc`\'s result be stored in a temporary pointer first?', [('steps', ['If `realloc` fails it returns NULL but leaves the original block allocated.', 'Writing `a = realloc(a, n)` would overwrite `a` with NULL and lose the only pointer to the old block – a memory leak.', 'So: `tmp = realloc(a, n); if (tmp == NULL) { /* handle error, a still valid */ } else a = tmp;`.'])])

# ================================================================= 7
s += H1('7. File Management')
s += [P('Variables disappear when a program ends. A <b>file</b> is a named collection of data on secondary storage (disk) that <b>persists</b> after the program finishes. C accesses files through a <b>file pointer</b>, `FILE *fp`, declared in `<stdio.h>`; all file functions take it as an argument.')]
s += TABLE([['Basis', 'Text file', 'Binary file'], ['Data', 'ASCII characters', 'Raw bytes, exactly as in memory'], ['Readable by', 'Any text editor', 'Only a program that knows the layout'], ['Examples', '.txt, .c, .csv', '.bin, .dat, images, executables'], ['Numbers', 'Stored as digit characters ("146")', 'Stored as raw 4-byte int / float'], ['Size', 'Usually larger', 'Usually smaller'], ['Functions', '`fprintf`, `fscanf`, `fgets`, `fputs`, `fgetc`, `fputc`', '`fread`, `fwrite`']], [1.4, 3, 3.1])
s += [H2('7.1 Opening and closing — fopen() and fclose()')]
s += SYNTAX('<b>FILE *fp = fopen("filename", "mode");</b> – returns NULL if the file cannot be opened (always test it). <b>fclose(fp);</b> flushes the buffers and releases the file – forgetting it can lose data.')
s += TABLE([['Mode', 'Meaning', 'If the file exists', 'If it does not exist'], ['"r"', 'Read only', 'Opens at the start', 'Returns NULL'], ['"w"', 'Write only', '<b>Truncated to length 0</b> (old content lost)', 'Created'], ['"a"', 'Append (write at the end)', 'Writes after existing data', 'Created'], ['"r+"', 'Read and write', 'Opens, keeps content', 'Returns NULL'], ['"w+"', 'Write and read', 'Truncated', 'Created'], ['"a+"', 'Append and read', 'Reads anywhere, writes at end', 'Created'], ['add "b"', 'Binary mode, e.g. "rb", "wb"', 'same as above', 'same as above']], [0.9, 2.2, 2.4, 2])
s += NOTE('Three streams are always open: `stdin` (keyboard), `stdout` (screen) and `stderr` (error output). So `printf(...)` ≡ `fprintf(stdout, ...)` and `scanf(...)` ≡ `fscanf(stdin, ...)`. `exit(0)` (from `<stdlib.h>`) ends the program from any function – 0 means success, non-zero means failure.')
s += [H2('7.2 File I/O functions')]
s += TABLE([['Function', 'Direction', 'Description'], ['`fgetc(fp)`', 'Read', 'One character; returns an `int` (EOF at the end)'], ['`fputc(c, fp)`', 'Write', 'One character'], ['`fgets(s, n, fp)`', 'Read', 'Up to n−1 characters, stops after `\\n`, adds `\\0`; returns NULL at the end'], ['`fputs(s, fp)`', 'Write', 'A string (no newline added)'],
            ['`fscanf(fp, ...)`', 'Read', 'Formatted read like `scanf`; returns the number of items read, or EOF'], ['`fprintf(fp, ...)`', 'Write', 'Formatted write like `printf`'], ['`feof(fp)`', 'Query', 'True only <i>after</i> a read has tried to go past the end'], ['`ferror(fp)`', 'Query', 'True if a file error occurred'],
            ['`fseek(fp, off, whence)`', 'Seek', 'Move the position: `SEEK_SET` (start), `SEEK_CUR`, `SEEK_END`'], ['`ftell(fp)`', 'Query', 'Current byte position'], ['`rewind(fp)`', 'Seek', 'Back to the start (≡ `fseek(fp, 0, SEEK_SET)`)'], ['`fread` / `fwrite`', 'Binary', 'Read / write whole blocks of bytes']], [1.8, 0.9, 4.8])
s += CODE('''
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("notes.txt", "w");
    if (fp == NULL) { printf("cannot open file\\n"); return 1; }
    fprintf(fp, "Line one\\n");
    fputs("Line two\\n", fp);
    fprintf(fp, "Total = %d\\n", 3 * 14);
    fclose(fp);                                    /* flush and close */

    char line[50];
    fp = fopen("notes.txt", "r");
    if (fp == NULL) return 1;
    while (fgets(line, sizeof line, fp) != NULL)   /* returns NULL at end of file */
        printf("read: %s", line);
    fclose(fp);
    return 0;
}
''', run=True, label='Write a text file, then read it back line by line')
s += CODE('''
#include <stdio.h>

int main(void) {
    FILE *in, *out;
    int c;                                      /* int, NOT char - EOF is -1 */

    out = fopen("source.txt", "w");             /* create a sample source file */
    if (out == NULL) return 1;
    fputs("Copy me, character by character.\\n", out);
    fclose(out);

    in  = fopen("source.txt", "r");
    out = fopen("copy.txt", "w");
    if (in == NULL || out == NULL) { printf("file error\\n"); return 1; }
    while ((c = fgetc(in)) != EOF)              /* copy until end of file */
        fputc(c, out);
    fclose(in);
    fclose(out);

    in = fopen("copy.txt", "r");
    while ((c = fgetc(in)) != EOF) putchar(c);
    fclose(in);
    return 0;
}
''', run=True, label='Copy a file with fgetc / fputc')
s += NOTE('`fgetc` returns an <b>int</b>, so the variable that stores it must be an `int`. If you store it in a `char`, the value 255 (a real character on some systems) is confused with EOF (−1), and on platforms where `char` is unsigned the loop never ends.')
s += [H2('7.3 Detecting the end of a file')]
s += CODE('''
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *fp = fopen("input.txt", "w");                 /* create sample numbers */
    if (fp == NULL) exit(1);
    fputs("12 7 25 30\\n8 19 40 5\\n", fp);
    fclose(fp);

    fp = fopen("input.txt", "r");
    if (fp == NULL) exit(1);
    int x, sum = 0, n = 0;
    while (fscanf(fp, "%d", &x) == 1) {           /* CORRECT: test the return value */
        sum += x;
        n++;
    }
    fclose(fp);
    printf("Sum = %d, Count = %d\\n", sum, n);
    return 0;
}
''', run=True, label='Sum all integers in a file')
s += WARN('<b>`while (!feof(fp))` is wrong.</b> `feof` becomes true only <i>after</i> a read has failed at the end, so the loop body runs one extra time and processes the last value twice (or processes garbage). Test the <b>return value</b> of the read function instead: `fscanf(...) == 1`, `fgets(...) != NULL`, `(c = fgetc(fp)) != EOF`.')
s += [H2('7.4 Random access — fseek, ftell, rewind')]
s += [P('Normally a file is read sequentially: each call moves the position forward. `fseek(fp, offset, whence)` jumps to any byte position, `ftell(fp)` reports the current position, and `rewind(fp)` returns to the start.')]
s += CODE('''
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("alpha.txt", "w+");           /* write + read */
    if (fp == NULL) return 1;
    fputs("ABCDEFGHIJ", fp);

    long pos;
    int ch;
    rewind(fp);                                    /* back to the start */
    pos = ftell(fp);  ch = fgetc(fp);
    printf("position = %ld, char = %c\\n", pos, ch);        /* 0, 'A' */
    fseek(fp, 4, SEEK_SET);                        /* 4 bytes from start -> 'E' */
    pos = ftell(fp);  ch = fgetc(fp);
    printf("position = %ld, char = %c\\n", pos, ch);
    fseek(fp, 2, SEEK_CUR);                        /* skip 2 more         -> 'H' */
    pos = ftell(fp);  ch = fgetc(fp);
    printf("position = %ld, char = %c\\n", pos, ch);
    fseek(fp, -1, SEEK_END);                       /* last byte           -> 'J' */
    pos = ftell(fp);  ch = fgetc(fp);
    printf("position = %ld, char = %c\\n", pos, ch);
    fseek(fp, 0, SEEK_END);
    printf("file size = %ld bytes\\n", ftell(fp));
    fclose(fp);
    return 0;
}
''', run=True)
s += [H2('7.5 Binary files — fwrite and fread')]
s += [P('`fwrite(&data, size, count, fp)` copies `count` items of `size` bytes straight from memory to the file; `fread` does the reverse. A whole structure or array is stored in one call – compact and fast, but not human-readable and not portable between machines with different layouts.')]
s += CODE('''
#include <stdio.h>

struct student { int roll; float cgpa; };

int main(void) {
    struct student out[3] = {{1, 8.2f}, {2, 9.1f}, {3, 7.4f}}, in[3];
    FILE *fp = fopen("students.dat", "wb");
    if (fp == NULL) return 1;
    fwrite(out, sizeof(struct student), 3, fp);        /* 3 records in one call */
    fclose(fp);

    fp = fopen("students.dat", "rb");
    if (fp == NULL) return 1;
    size_t got = fread(in, sizeof(struct student), 3, fp);
    fclose(fp);
    for (size_t i = 0; i < got; i++)
        printf("%d %.1f\\n", in[i].roll, in[i].cgpa);
    return 0;
}
''', run=True)
s += RECALL(['`FILE *fp = fopen(name, mode);` – always check `fp != NULL`; always `fclose(fp)`.', '"r" read, "w" write (truncates!), "a" append; "+" allows both; "b" = binary.', '`fgetc`/`fputc` – character; `fgets`/`fputs` – line/string; `fscanf`/`fprintf` – formatted; `fread`/`fwrite` – blocks.', 'Test the <i>return value</i> (EOF / NULL / count) to find the end – never `while (!feof(fp))`.', '`fseek` + `ftell` + `rewind` give random access.'])
s += QA('g', 'Write a program that creates `data.txt`, writes the integers 1 to 5 one per line with `fprintf`, closes it, reopens it for reading and prints the numbers.', [('steps', ['`fopen("data.txt", "w")` and check for NULL.', 'Loop `fprintf(fp, "%d\\n", i)` for i = 1…5; `fclose(fp)`.', '`fopen("data.txt", "r")`; loop `while (fscanf(fp, "%d", &x) == 1)` and print x.', '`fclose(fp)`.'])],
        code=CODE('''
#include <stdio.h>

int main(void) {
    FILE *fp;
    int i, x;
    fp = fopen("data.txt", "w");
    if (fp == NULL) return 1;
    for (i = 1; i <= 5; i++)
        fprintf(fp, "%d\\n", i);
    fclose(fp);
    fp = fopen("data.txt", "r");
    if (fp == NULL) return 1;
    while (fscanf(fp, "%d", &x) == 1)
        printf("%d\\n", x);
    fclose(fp);
    return 0;
}
''', run=True))
s += QA('r', 'Write a program that counts the lines and words in a text file, reading with `fgetc`.', [('steps', ['Read characters until EOF (store them in an `int`).', 'Every `\\n` is one more line.', 'Track whether we are inside a word: a space, tab or newline sets `inWord = 0`; the first non-space character after that starts a new word, so count it and set `inWord = 1`.', 'Print the two counters.'])],
        code=CODE('''
#include <stdio.h>

int main(void) {
    FILE *fp = fopen("essay.txt", "w");                 /* create a sample file */
    if (fp == NULL) return 1;
    fputs("The quick brown fox\\njumps over\\nthe lazy dog\\n", fp);
    fclose(fp);

    fp = fopen("essay.txt", "r");
    if (fp == NULL) { printf("Error\\n"); return 1; }
    int c, lines = 0, words = 0, inWord = 0;
    while ((c = fgetc(fp)) != EOF) {
        if (c == '\\n') lines++;
        if (c == ' ' || c == '\\n' || c == '\\t')
            inWord = 0;
        else if (!inWord) {
            words++;
            inWord = 1;
        }
    }
    fclose(fp);
    printf("Lines: %d  Words: %d\\n", lines, words);
    return 0;
}
''', run=True))
s += QA('y', 'What is the difference between opening a file with "w" and with "a"?', [('lines', ['<b>"w"</b> – creates the file, or <b>truncates an existing file to zero length</b>, destroying its old content.', '<b>"a"</b> – creates the file if missing, otherwise keeps the content and writes <b>after</b> it (at the end).'])])

ok = build(sys.argv[1] if len(sys.argv) > 1 else '/home/sleepy/STUDY:)/sem-1/CP/cpclaude/Unit5_Notes.pdf', 5, 'Structures, Memory & Files', '', '10 hrs · 20% weightage · C language',
           'Structures · nested structures · array of structures · structures with functions · unions · dynamic memory allocation (malloc, calloc) · file management and its functions', '#c2255c', s)
print('BUILD OK' if ok else 'BUILD HAS PROBLEMS')
