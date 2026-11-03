---
tag: 7SZTTSG2FH
kind: definition
name: Low-density parity-check code
msc: [94B05, 94B35]
defines: JJH68RANFH
uses: [E85KREWV60, Y4JB44WWFG, 0PHDYNR24D, M2X88AXM17]
sources:
  - url: https://en.wikipedia.org/wiki/Low-density_parity-check_code
---

## Definition

Let $w_c, w_r \ge 2$ be integers.
Let $H$ be an $m \times n$ matrix over $\F_2$ with exactly $w_c$ ones in each column and exactly $w_r$ ones in each row.
The [[null space|0PHDYNR24D]]
$$C = \set{x \in \F_2^n : H x^{T} = 0}$$
is a *$(w_c, w_r)$-regular low-density parity-check code*; it is a binary [[linear code|E85KREWV60]].
More generally, consider a family of binary linear codes $C_n$ with lengths $n \to \infty$.
It is a family of *low-density parity-check codes* if each $C_n$ is the null space of a [[parity-check matrix|Y4JB44WWFG]] $H_n$ with few ones.
This means that the numbers of ones per row and per column of $H_n$ are bounded by a constant independent of $n$.

## Remarks

Counting the ones of $H$ by rows and by columns gives $n w_c = m w_r$.
Since $H$ has $m$ rows, the rate of $C$ is at least $1 - m/n = 1 - w_c/w_r$, with equality when the rows of $H$ are independent.
Gallager's original examples are the $(3, 6)$-regular codes, of rate at least $1/2$.
The code depends only on the row space of $H$, but decoding uses the particular sparse matrix $H$.

Example: let $H$ be the $4 \times 6$ incidence matrix of the complete graph $K_4$, rows indexed by vertices and columns by edges.
Each column has $2$ ones and each row has $3$ ones, so the code is $(2, 3)$-regular.
A codeword is a set of edges meeting every vertex an even number of times, that is, an edge-disjoint union of cycles.
The code has dimension $6 - 4 + 1 = 3$, and its [[minimum distance|M2X88AXM17]] is $3$, the length of a triangle.

Non-example: every nonzero word of the dual of the binary [[Hamming code|D68NF1S2NW]] of length $2^r - 1$ has weight $2^{r-1}$.
The rows of a parity-check matrix of the Hamming code lie in this dual, so each nonzero row has weight $2^{r-1}$.
Hence the Hamming codes do not form a low-density family.
