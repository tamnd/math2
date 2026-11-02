---
tag: 96MQARP0N4
kind: definition
name: Δ-complex
msc: [55U10, 57Q05]
defines: ZFCMCXA71M
uses: [0CNQXVBHCX, 0SY9ECQ19Q]
sources:
  - url: https://en.wikipedia.org/wiki/Delta_set
---

## Definition

For $n \ge 0$ let $\Delta^n$ be the standard $n$-simplex with ordered vertices $e_0, \dots, e_n$, and let $\mathring{\Delta}^n$ be its interior.
For $0 \le i \le n$ with $n \ge 1$, let $\delta^i \colon \Delta^{n-1} \to \Delta^n$ be the affine map onto the $i$-th face that sends $e_0, \dots, e_{n-1}$ in order to the vertices $e_0, \dots, \widehat{e_i}, \dots, e_n$.
Let $X$ be a [[topological space|0CNQXVBHCX]].
A *$\Delta$-complex structure* on $X$ is a family of [[continuous maps|0SY9ECQ19Q]] $\sigma_\alpha \colon \Delta^{n_\alpha} \to X$ such that:

1. Each $\sigma_\alpha$ is injective on $\mathring{\Delta}^{n_\alpha}$, and each point of $X$ lies in $\sigma_\alpha(\mathring{\Delta}^{n_\alpha})$ for exactly one $\alpha$.
2. For each $\alpha$ with $n_\alpha \ge 1$ and each $i$, the map $\sigma_\alpha \circ \delta^i$ is $\sigma_\beta$ for some $\beta$ with $n_\beta = n_\alpha - 1$.
3. A subset $A \subseteq X$ is open if and only if $\sigma_\alpha^{-1}(A)$ is open in $\Delta^{n_\alpha}$ for every $\alpha$.

A *$\Delta$-complex* is a space with a $\Delta$-complex structure.

## Remarks

Every $\Delta$-complex is a CW complex whose cells are the open simplices $\sigma_\alpha(\mathring{\Delta}^{n_\alpha})$.
The combinatorial data of a $\Delta$-complex, the sets of $n$-simplices with the face maps $d_i$ given by clause 2, form a semi-simplicial set.

Example: the circle $S^1$ with one $0$-simplex $\sigma_0 \colon \Delta^0 \to S^1$ onto a point $p$ and one $1$-simplex $\sigma_1 \colon \Delta^1 \to S^1$ that wraps once around, sending both ends to $p$.
Clause 1 holds since $\sigma_1$ is injective on the open interval and misses only $p$.
Clause 2 holds since both faces of $\sigma_1$ equal $\sigma_0$, and clause 3 holds since $S^1$ is a quotient of $\Delta^1$.

Non-example: the circle with one $0$-simplex at $p$ and one $1$-simplex that wraps twice around fails clause 1, since the map is not injective on the open interval.
