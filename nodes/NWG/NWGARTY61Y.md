---
tag: NWGARTY61Y
kind: definition
name: Enumerative combinatorics
msc: [05A15, 05A16, 05A99]
defines: EX382NQTGP
uses: [0JKW7W7XFR, 0BBTH3YSZA, 0PHAC833JF, 0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Enumerative_combinatorics
---

## Definition

Let $(S_n)_{n \ge 0}$ be a family of [[finite sets|0BBTH3YSZA]] given by a combinatorial rule, such as the subsets of $\set{1, \ldots, n}$ or the trees with $n$ vertices.
*Enumerative combinatorics* is the branch of [[combinatorics|0JKW7W7XFR]] that determines the counting function $n \mapsto \abs{S_n}$.
An answer is one of the following:

1. an explicit formula for $\abs{S_n}$;
2. a [[recurrence relation|0FYX44GP92]] that computes $\abs{S_n}$ from earlier values;
3. a closed form for a [[generating function|0PHAC833JF]] of the sequence $\abs{S_n}$;
4. an asymptotic estimate of $\abs{S_n}$ as $n \to \infty$.

## Remarks

Example: let $S_n$ be the set of subsets of $\set{1, \ldots, n}$ with no two consecutive elements.
A set in $S_n$ either avoids $n$, or contains $n$ and avoids $n - 1$.
This gives the recurrence $\abs{S_n} = \abs{S_{n-1}} + \abs{S_{n-2}}$, with $\abs{S_0} = 1$ and $\abs{S_1} = 2$, so $\abs{S_n}$ is the Fibonacci number $F_{n+2}$.

Non-example: the question whether a finite projective plane of order $10$ exists is a question of existence, not of counting.
It belongs to the theory of [[combinatorial designs|PAJTMQ604P]].

The parameter $n$ may be replaced by several parameters, as in the [[binomial coefficient|0GBZM0MT0F]] $\binom{n}{k}$.
