---
tag: Q7CB3ET9P8
kind: statement
role: theorem
name: Equivalence of Turing machines and partial recursive functions
msc: [03D10, 03D20, 68Q04]
uses: [W6ESDYBF8Z, 4DQGSSWREK]
about: [758EYCN27B, HBK5QHC1GC]
sources:
  - url: https://en.wikipedia.org/wiki/Church–Turing_thesis
---

## Statement

Let $k \ge 1$ and let $f \colon \N^k \rightharpoonup \N$ be a partial function.
Code a tuple $(x_1, \dots, x_k)$ as the input string $1^{x_1} 0 1^{x_2} 0 \cdots 0 1^{x_k}$, and code an output $y$ as the string $1^y$.
Then the following are equivalent.

1. The function $f$ is [[partial recursive|4DQGSSWREK]].
2. There is a [[Turing machine|W6ESDYBF8Z]] $M$ with the following property for every $x \in \N^k$: $M$ halts on the code of $x$ exactly when $f(x)$ is defined.
   In that case $M$ halts with the code of $f(x)$ on its tape.

## Remarks

From recursive functions to machines: one builds machines for the zero, successor and projection functions, and shows that Turing-computable functions are closed under composition, primitive recursion and minimisation.
Minimisation is a loop that tests $y = 0, 1, 2, \dots$ in turn and stops at the first zero.
From machines to recursive functions: configurations are coded as numbers, and the step function on codes is primitive recursive.
Then $f(x)$ is obtained by searching with $\mu$ for the first halting time and decoding the output, as in [[Kleene's T predicate|S9DK13K5PS]].
In particular, every partial recursive function is obtained with at most one use of minimisation.
The theorem is part of the evidence for the [[Church–Turing thesis|RWRNBS3Z7B]], but it is a theorem about two formal models, while the thesis is not a formal statement.
The choice of unary coding is not essential: any of the usual codings, such as binary numerals, gives the same class of functions.

## Explanations

### L1 human

There are two very different ways to say what a computable function on numbers is.
One builds functions from simple ones by composition, recursion and search.
The other runs a machine with a tape.
The theorem says that both ways give exactly the same functions.

### L2 human

The theorem lets one move freely between programs and recursive definitions.
To show that a function is computable, it is often easier to write a recursive definition than to design a machine.
To show that a set is undecidable, one argues with machines, for example with the [[halting problem|Z7TN2B35B0]], and then transfers the result to recursive functions.
The same method of coding configurations by numbers shows that [[register machines|BSPVYC28BY]] and the [[lambda calculus|BD756KR8FM]] define the same class.
