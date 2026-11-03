---
tag: NHDWBESKG3
kind: definition
name: L-infinity algebra
msc: [17B55, 18M70, 55P62]
defines: 572DS8WXEH
uses: [04C5ZBG1WT, 000AYPA9AJ, 0515A6D2Y1, D5XH66A8RP]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_Lie_algebra
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] of characteristic $0$.
Let $L = \bigoplus_{i \in \Z} L^i$ be a $\Z$-graded [[vector space|000AYPA9AJ]] over $F$, and write $\abs{x} = i$ for $x \in L^i$.
For homogeneous $x_1, \ldots, x_n$ and a permutation $\sigma$ in the [[symmetric group|0515A6D2Y1]] $S_n$, let $\chi(\sigma) = \chi(\sigma; x_1, \ldots, x_n)$ be the sign defined by two rules.
The sign of a transposition of neighbours $x_k, x_{k+1}$ is $-(-1)^{\abs{x_k}\abs{x_{k+1}}}$, and $\chi$ is multiplicative along products of such transpositions.
An *$(i, n - i)$-unshuffle* is a permutation $\sigma \in S_n$ with $\sigma(1) < \cdots < \sigma(i)$ and $\sigma(i + 1) < \cdots < \sigma(n)$.

An *$L_\infty$-algebra* structure on $L$ is a family of multilinear maps $l_k \colon L^{\otimes k} \to L$, for $k \ge 1$, such that:

1. $l_k$ has degree $2 - k$, that is, it maps $L^{i_1} \otimes \cdots \otimes L^{i_k}$ into $L^{i_1 + \cdots + i_k + 2 - k}$;
2. $l_k(x_{\sigma(1)}, \ldots, x_{\sigma(k)}) = \chi(\sigma)\, l_k(x_1, \ldots, x_k)$ for all homogeneous $x_j$ and all $\sigma \in S_k$;
3. for each $n \ge 1$ and all homogeneous $x_1, \ldots, x_n$,
$$\sum_{i + j = n + 1} \sum_{\sigma} \chi(\sigma) (-1)^{i(j - 1)}\, l_j\big(l_i(x_{\sigma(1)}, \ldots, x_{\sigma(i)}), x_{\sigma(i + 1)}, \ldots, x_{\sigma(n)}\big) = 0,$$
where $i, j \ge 1$ and $\sigma$ runs over the $(i, n - i)$-unshuffles.

## Remarks

For $n = 1$, clause 3 says $l_1 \circ l_1 = 0$, so $(L, l_1)$ is a cochain complex.
For $n = 2$, it says $l_1 l_2(x_1, x_2) = l_2(l_1 x_1, x_2) + (-1)^{\abs{x_1}} l_2(x_1, l_1 x_2)$, so $l_1$ is a derivation of $l_2$.
For $n = 3$, it says that the graded Jacobi identity for $l_2$ holds up to terms built from $l_1$ and $l_3$.

Example: a [[differential graded Lie algebra|D5XH66A8RP]] $(L, [\cdot, \cdot], d)$ gives an $L_\infty$-algebra with $l_1 = d$, $l_2 = [\cdot, \cdot]$ and $l_k = 0$ for $k \ge 3$.
Clause 2 for $k = 2$ is graded antisymmetry, and clause 3 for $n = 3$ becomes the graded Jacobi identity.

Non-example: a Lie algebra $\mathfrak{g}$ in degree $0$ with $l_2$ its bracket and $l_1 = \id$ fails clause 1, since $l_1$ must raise the degree by one.

Sign conventions vary between authors; some use a lower grading in which $l_k$ has degree $k - 2$.
