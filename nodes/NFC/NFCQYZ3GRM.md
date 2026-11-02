---
tag: NFCQYZ3GRM
kind: statement
role: theorem
name: Orlicz–Pettis theorem
msc: [46B15, 40A05]
uses: [0BDTTM24DP, 2ME9M61TJK, WN6M8B3ZKB]
about: [WN6M8B3ZKB, 2ME9M61TJK]
sources:
  - url: https://en.wikipedia.org/wiki/Orlicz%E2%80%93Pettis_theorem
same_as:
  wikidata: Q1621180
  wikipedia: Orlicz–Pettis theorem
---

## Statement

Let $X$ be a [[Banach space|0BDTTM24DP]] over $\R$ or $\C$, and let $X'$ be the space of continuous linear functionals on $X$.
Let $(x_n)_{n \ge 1}$ be a sequence in $X$.
Assume that for every strictly increasing sequence $n_1 < n_2 < \cdots$ of indices there is $y \in X$ with
$$\varphi(y) = \sum_{k=1}^{\infty} \varphi(x_{n_k}) \quad \text{for all } \varphi \in X'.$$
Then for every such sequence of indices the series $\sum_{k} x_{n_k}$ converges in norm.
In particular, the series $\sum_n x_n$ is [[unconditionally convergent|2ME9M61TJK]] in norm.

## Remarks

The hypothesis says that every subseries converges in the weak topology; the conclusion says that every subseries converges in norm.
The theorem needs all subseries: in $\ell^2$, the series $e_1 + (e_2 - e_1) + (e_3 - e_2) + \cdots$ has partial sums $e_n$, which tend to $0$ weakly but not in norm.
The theorem also holds in Hausdorff locally convex spaces, with the weak topology given by the continuous dual.

## Explanations

### L1 human

In an infinite-dimensional space, weak convergence is in general much weaker than convergence in norm.
For series, the theorem says that this gap closes as soon as one asks for every subseries.
If each subseries converges when tested by every continuous linear functional, then each subseries already converges in norm.

### L2 human

The theorem is a basic tool for [[series in Banach spaces|WN6M8B3ZKB]] and for vector measures.
A countably additive vector measure is defined by convergence of $\sum \mu(A_n)$ for disjoint sets $A_n$, and every subfamily of disjoint sets gives a subseries.
So the theorem shows that a weakly countably additive vector measure is countably additive in norm.
It is also used in the Bochner and Pettis theories of integration of vector-valued functions.
