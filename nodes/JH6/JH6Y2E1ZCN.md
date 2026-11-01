---
tag: JH6Y2E1ZCN
kind: statement
role: theorem
name: Catalan's conjecture
msc: [11D61, 11D41]
uses: [08B1RTW7VZ, 0MWKJ44V5A, NN77VYSGXR, WMBJSNG57F]
about: [08B1RTW7VZ]
sources:
  - url: https://en.wikipedia.org/wiki/Catalan%27s_conjecture
same_as:
  wikidata: Q174955
  wikipedia: Catalan's conjecture
---

## Statement

Let $x$, $y$, $a$, $b$ be [[natural numbers|0MWKJ44V5A]] with $x > 1$, $y > 1$, $a > 1$ and $b > 1$.
If $x^a - y^b = 1$, then $x = 3$, $a = 2$, $y = 2$ and $b = 3$.

## Remarks

The result is also called Mihăilescu's theorem: Eugène Catalan conjectured it in 1844, and Preda Mihăilescu proved it in 2002.
Robert Tijdeman had shown in 1976, with [[Baker's theorem|WMBJSNG57F]] on linear forms in logarithms, that the [[Diophantine equation|08B1RTW7VZ]] has only finitely many solutions.
Mihăilescu's proof reduces to odd prime exponents and then uses the arithmetic of [[cyclotomic fields|NN77VYSGXR]].
Equivalently: $8$ and $9$ are the only two consecutive integers that are both perfect powers.
The hypothesis $a, b > 1$ is needed, since for $b = 1$ every $x^a - 1$ is a valid $y$.
Euler had settled the special case $x^2 - y^3 = 1$, whose only positive solution is $(3, 2)$.

## Explanations

### L1 human

Perfect powers are numbers such as $4, 8, 9, 16, 25, 27, 32$.
Among them, $8$ and $9$ sit right next to each other.
Catalan guessed that this never happens again, and Mihăilescu proved it about one and a half centuries later.

### L2 human

The equation $x^a - y^b = 1$ is an exponential Diophantine equation, with unknown exponents.
Tijdeman's finiteness result is typical of Baker's method: it bounds the solutions, but the bound was far too large to search.
Mihăilescu's proof avoids computation and works with units and class groups of cyclotomic fields, a theme shared with work on Fermat's Last Theorem.
The more general Pillai conjecture, that each positive integer occurs only finitely often as a difference of perfect powers, remains open.
