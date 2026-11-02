---
tag: VDQX55E7D4
kind: definition
name: Betti number
msc: [55N10]
defines: ST71ZV3FES
uses: [M0Q5CFJ7ZH, EMCTDD3HZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Betti_number
---

## Definition

Let $X$ be a topological space, let $k \ge 0$ be an integer, and let $H_k(X)$ be the $k$-th [[singular homology|M0Q5CFJ7ZH]] group of $X$ with integer coefficients.
The *$k$-th Betti number* of $X$ is the [[rank|EMCTDD3HZ1]] of the abelian group $H_k(X)$:
$$b_k(X) = \rank H_k(X) = \dim_{\Q} \left( H_k(X) \otimes_{\Z} \Q \right),$$
a nonnegative integer or $\infty$.

## Remarks

When $H_k(X)$ is finitely generated, it is isomorphic to $\Z^{b_k} \oplus T$ with $T$ finite, so $b_k$ is the number of copies of $\Z$.
By the [[universal coefficient theorem|GTA8ZFGZ3N]], $b_k(X) = \dim_{\Q} H_k(X; \Q)$.
Torsion is invisible to Betti numbers.

Example: for the torus $T^2 = S^1 \times S^1$, $H_0 = \Z$, $H_1 = \Z^2$ and $H_2 = \Z$, so $b_0 = 1$, $b_1 = 2$, $b_2 = 1$.

Non-example of a finite Betti number: an infinite discrete space $X$ has $H_0(X)$ free abelian of infinite rank, so $b_0(X) = \infty$.
For the real projective plane, $H_1 = \Z/2$ is nonzero but has rank $0$, so $b_1 = 0$.
