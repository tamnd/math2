---
tag: 3BBE4XY4E9
kind: definition
name: Twelvefold way
msc: [05A15, 05A18, 05A17]
defines: 1J16RVRHYS
uses: [0XHDTE5YMZ, 0PVG1CRAJN, 0XKH881BZ7, 0515A6D2Y1, 0JCQGPY8Z4, 0JV30XN73Z, 0N5M924N3P]
sources:
  - url: https://en.wikipedia.org/wiki/Twelvefold_way
---

## Definition

Let $N$ and $X$ be finite sets with $\abs{N} = n$ and $\abs{X} = x$.
Consider the [[functions|0XHDTE5YMZ]] $f \colon N \to X$ in one of three classes: all functions, [[injective functions|0PVG1CRAJN]], or [[surjective functions|0XKH881BZ7]].
Count them in one of four ways:

1. as functions;
2. up to permutations of $N$, so $f$ and $f \circ \sigma$ count as the same for every permutation $\sigma$ of $N$;
3. up to permutations of $X$, so $f$ and $\tau \circ f$ count as the same for every permutation $\tau$ of $X$;
4. up to permutations of both, so $f$ and $\tau \circ f \circ \sigma$ count as the same for all such $\sigma$ and $\tau$.

The *twelvefold way* is the list of these $3 \cdot 4 = 12$ counting problems with their answers.

## Remarks

Write $x^{\underline{n}}$ for the [[falling factorial|0N5M924N3P]], $S(n, k)$ for the [[Stirling numbers of the second kind|0JCQGPY8Z4]], and $p_k(m)$ for the number of [[partitions|0JV30XN73Z]] of $m$ into exactly $k$ parts.
Write $[n \le x]$ for $1$ if $n \le x$ and $0$ otherwise.
The answers, with $n$ balls $N$ and $x$ boxes $X$, are as follows.

| count | all functions | injective | surjective |
|---|---|---|---|
| as functions | $x^n$ | $x^{\underline{n}}$ | $x!\, S(n, x)$ |
| up to permutations of $N$ | $\binom{x + n - 1}{n}$ | $\binom{x}{n}$ | $\binom{n - 1}{x - 1}$ |
| up to permutations of $X$ | $\sum_{k=0}^{x} S(n, k)$ | $[n \le x]$ | $S(n, x)$ |
| up to both | $\sum_{k=0}^{x} p_k(n)$ | $[n \le x]$ | $p_x(n)$ |

The entry $\binom{n-1}{x-1}$ needs $n \ge 1$; for $n = x = 0$ there is exactly one surjection, the empty map.

Example: take $n = 3$ and $x = 2$, counted up to permutations of $N$.
A class of functions is then fixed by how many balls go into each box, so the classes are $(3, 0)$, $(2, 1)$, $(1, 2)$ and $(0, 3)$.
This gives $4 = \binom{4}{3}$, as in the table.

Non-example: counting functions up to a permutation of $N$ that is not arbitrary, for instance only up to cyclic rotations of $N$, is not one of the twelve problems.
It leads to necklace counting, which is handled by the [[Pólya enumeration theorem|MPYQ39P01F]].

The second row is the theory of [[combinations with repetition|0VQQCVG8WA]].
The first entry of the first row is the [[number of functions between finite sets|08QQH9F7G0]], and the second is the [[number of injections|0X0N833FF8]].
