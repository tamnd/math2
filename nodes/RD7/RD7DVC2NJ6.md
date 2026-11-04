---
tag: RD7DVC2NJ6
kind: definition
name: Weierstrass polynomial
msc: [32B05, 13J07]
defines: SDCKNWSWNM
uses: [EVPZ7ZG1HB, 0C3QBCR46M]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_preparation_theorem
  - url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L14364
    locator: scv.tex:14364
---

## Definition

Let $n \ge 1$, write $z' = (z_1, \dots, z_{n-1})$, and let $\mathcal{O}_{n-1} = \C\{z'\}$ be the [[ring of convergent power series|EVPZ7ZG1HB]] in $n - 1$ variables.
Let $d \ge 0$ be an integer.
A *Weierstrass polynomial* of degree $d$ in $z_n$ is a [[monic polynomial|0C3QBCR46M]]
$$P(z', z_n) = z_n^d + a_{d-1}(z')\, z_n^{d-1} + \cdots + a_1(z')\, z_n + a_0(z')$$
with coefficients $a_0, \dots, a_{d-1} \in \mathcal{O}_{n-1}$ such that $a_j(0) = 0$ for every $j$.

## Remarks

Equivalently, $P \in \mathcal{O}_{n-1}[z_n]$ is monic of degree $d$ and $P(0, z_n) = z_n^d$.
The only Weierstrass polynomial of degree $0$ is $P = 1$.
Example: $P = z_2^3 - z_1 z_2 + z_1^2$ is a Weierstrass polynomial of degree $3$ in $z_2$, since $a_2 = 0$, $a_1 = -z_1$ and $a_0 = z_1^2$ all vanish at $0$.
Non-example: $Q = z_2^2 + z_2 + z_1$ is monic in $z_2$, but its coefficient $a_1 = 1$ does not vanish at $0$; indeed $Q(0, z_2) = z_2^2 + z_2 \ne z_2^2$.
The same definition is used with $\mathcal{O}_{n-1}$ replaced by the ring of holomorphic functions on a neighbourhood of $0 \in \C^{n-1}$.
