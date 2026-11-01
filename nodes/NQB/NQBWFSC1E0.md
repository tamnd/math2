---
tag: NQBWFSC1E0
kind: statement
role: theorem
name: Szemerédi–Trotter theorem
msc: [52C10, 52C30, 05D99]
uses: [0XW7V9ZZ05]
about: [0XW7V9ZZ05]
sources:
  - url: https://en.wikipedia.org/wiki/Szemer%C3%A9di%E2%80%93Trotter_theorem
same_as:
  wikidata: Q721695
  wikipedia: Szemerédi–Trotter theorem
---

## Statement

There is an absolute constant $C > 0$ with the following property.
Let $P$ be a finite set of points and $L$ a finite set of lines in the [[Euclidean plane|0XW7V9ZZ05]] $\R^2$.
Let $I(P, L)$ be the number of pairs $(p, \ell) \in P \times L$ with $p \in \ell$.
Then
$$I(P, L) \le C \left( \abs{P}^{2/3} \abs{L}^{2/3} + \abs{P} + \abs{L} \right).$$

## Remarks

Székely gave a short proof with the crossing number inequality.
Draw a graph whose vertices are the points and whose edges join consecutive points on each line.
It has at least $I - \abs{L}$ edges and at most $\abs{L}^2$ crossings, and the crossing number inequality gives the bound.
The bound is sharp up to the constant.
Take the grid $\set{1, \dots, k} \times \set{1, \dots, 2k^2}$ and the lines $y = ax + b$ with $1 \le a \le k$ and $1 \le b \le k^2$.
Each such line meets the grid in $k$ points, so there are $k^4$ incidences, with $2k^3$ points and $k^3$ lines.
The theorem fails over finite fields.
In $\F_q^2$, the $q^2$ points and the $q^2 + q$ lines have $q^3 + q^2$ incidences, which is more than a constant times $q^{8/3}$ for large $q$.

## Explanations

### L1 human

Draw some points and some straight lines in the plane, and count how many times a point lies on a line.
The theorem gives the largest possible count, up to a constant factor.
With $n$ points and $n$ lines, there are at most about $n^{4/3}$ such incidences, far fewer than the trivial $n^2$.

### L2 human

The Szemerédi–Trotter theorem is the basic result of incidence geometry.
A corollary: $n$ points determine at most $O(n^2/k^3 + n/k)$ lines that contain at least $k$ of the points.
It has applications to the [[Erdős distinct distances problem|4H31EM5T0C]] and to sum-product estimates in [[additive combinatorics|3NM362A2JG]].
Its proof uses the topology of the real plane, which explains why it fails over finite fields.
