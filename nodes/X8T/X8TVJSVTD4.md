---
tag: X8TVJSVTD4
kind: statement
role: theorem
name: Hilbert's tenth problem
msc: [11U05, 03D35, 11D72]
uses: [08B1RTW7VZ, 07GNX8GCYP, PPGD5KW8JC, TN9G24VABN]
about: [08B1RTW7VZ]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert's_tenth_problem
---

## Statement

Consider polynomials $p(x_1, \ldots, x_n)$ with integer coefficients, in any number $n$ of variables.
There is no algorithm that decides, for every such $p$, whether the [[Diophantine equation|08B1RTW7VZ]] $p(x_1, \ldots, x_n) = 0$ has a solution in integers.

In other words, the set of codes of [[polynomials in several variables|07GNX8GCYP]] over $\Z$ that have an integer zero is not a [[computable set|PPGD5KW8JC]].

## Remarks

The result follows from the Matiyasevich–Robinson–Davis–Putnam (MRDP) theorem.
A set $S \subseteq \N$ is *Diophantine* if there is a polynomial $p(a, y_1, \ldots, y_m)$ with integer coefficients such that $a \in S$ exactly when $p(a, y_1, \ldots, y_m) = 0$ for some $y_1, \ldots, y_m \in \N$.
The MRDP theorem says that the Diophantine sets are exactly the [[computably enumerable sets|TN9G24VABN]].
Taking a Diophantine definition of a c.e. set that is not computable, such as the [[halting problem|Z7TN2B35B0]], shows that solvability cannot be decided.
Matiyasevich completed the proof in 1970 by showing that exponentiation is Diophantine, the last step after work of Davis, Putnam and Julia Robinson.

The question in natural numbers and the question in integers are equivalent.
One direction uses Lagrange's four-square theorem: every natural number is a sum of four squares.
For equations in one variable the problem is decidable, since the integer roots of a nonzero polynomial lie in a finite range bounded in terms of its coefficients.

## Explanations

### L1 human

Hilbert asked in 1900 for a method that tells, for any polynomial equation with whole-number coefficients, whether it has a whole-number solution.
The answer turned out to be no: no computer program can do this for all equations.
The reason is that polynomial equations are expressive enough to describe the run of any computer program.

### L2 human

This is a central example of an undecidable problem from ordinary mathematics, outside of logic.
The key tool is the MRDP theorem, which identifies Diophantine sets with computably enumerable sets.
A consequence is that there is a single polynomial whose positive values, at natural number arguments, are exactly the prime numbers.
Whether the analogous problem over $\Q$ is decidable is still open.
