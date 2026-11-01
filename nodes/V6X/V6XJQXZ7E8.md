---
tag: V6XJQXZ7E8
kind: statement
role: theorem
name: Schur's theorem
msc: [05D10, 11B75]
uses: [00TQV3F5S4]
about: [G5TWXV565S]
sources:
  - url: https://en.wikipedia.org/wiki/Schur's_theorem
---

## Statement

Let $r \ge 1$ be an integer.
Then there is a positive integer $N$ with the following property.
For every colouring of $\set{1, \ldots, N}$ with $r$ colours, there are $x, y, z \in \set{1, \ldots, N}$ of the same colour with $x + y = z$.
Here $x$ and $y$ need not be distinct.

## Remarks

Let $N + 1$ be at least the Ramsey number for $r$ colours and triangles, given by [[Ramsey's theorem|00TQV3F5S4]].
Colour the edge $\set{i, j}$ of the complete graph on $\set{1, \ldots, N + 1}$ with the colour of $\abs{i - j}$.
A monochromatic triangle $i < j < k$ gives $x = j - i$, $y = k - j$ and $z = k - i$ of the same colour with $x + y = z$.

The least such $N$ is $S(r) + 1$, where the Schur number $S(r)$ is the largest $n$ for which $\set{1, \ldots, n}$ can be split into $r$ [[sum-free sets|7SHV2SPYP6]].
For example $S(2) = 4$: the colouring $\set{1, 4}$, $\set{2, 3}$ has no monochromatic solution, while every $2$-colouring of $\set{1, \ldots, 5}$ has one.
Known values are $S(1) = 1$, $S(2) = 4$, $S(3) = 13$, $S(4) = 44$ and $S(5) = 160$.

## Explanations

### L1 human

However you colour the numbers $1$ to $N$ with a fixed number of colours, if $N$ is large enough, some colour contains two numbers together with their sum.
For two colours, $N = 5$ is enough.
It is one of the first results of [[Ramsey theory|G5TWXV565S]] in the integers.

### L2 human

Schur proved the theorem in 1916 while studying Fermat's equation modulo primes.
It implies that for each $n$ and all large enough primes $p$, the congruence $x^n + y^n \equiv z^n \pmod p$ has a solution with $xyz \not\equiv 0$.
The proof is a direct reduction to [[Ramsey's theorem|00TQV3F5S4]] for triangles.
[[Rado's theorem|BZSGRCTFH4]] extends it to all linear equations whose monochromatic solutions are forced in this way.
