---
tag: KHD2QMNR7R
kind: definition
name: Mutually orthogonal Latin squares
msc: [05B15]
defines: H6TN6BADVY
uses: [44HTG620GB]
sources:
  - url: https://en.wikipedia.org/wiki/Mutually_orthogonal_Latin_squares
---

## Definition

Let $n$ be a positive integer.
Let $L = (L_{ij})$ and $M = (M_{ij})$ be [[Latin squares|44HTG620GB]] of order $n$, on symbol sets $S$ and $T$ with $n$ elements each.
The squares $L$ and $M$ are orthogonal if the $n^2$ ordered pairs $(L_{ij}, M_{ij})$, for $1 \le i, j \le n$, are pairwise distinct.
A family of Latin squares of order $n$ is mutually orthogonal if each two distinct squares of the family are orthogonal.

## Remarks

Since $S \times T$ has $n^2$ elements, orthogonality means that every pair in $S \times T$ occurs exactly once.
Example of order $3$: for $i, j \in \Z/3\Z$, let $L_{ij} = i + j$ and $M_{ij} = 2i + j$.
If $(L_{ij}, M_{ij}) = (s, t)$, then $i = t - s$ and $j = 2s - t$, so each pair $(s, t)$ comes from exactly one cell, and $L$ and $M$ are orthogonal.
Non-example: a Latin square of order $n \ge 2$ is never orthogonal to itself, because only the $n$ pairs $(s, s)$ occur.
There are no orthogonal Latin squares of order $2$, and there is no orthogonal pair of order $6$; this answers [[Euler's thirty-six officers problem|WXJAVQKFR6]].
For a prime power $q$ and the [[finite field|08RTDHX1SK]] $\F_q$, the squares $L^{(a)}_{xy} = ax + y$ for $a \in \F_q \setminus \set{0}$ form $q - 1$ mutually orthogonal Latin squares of order $q$.
