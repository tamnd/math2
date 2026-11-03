---
tag: NEA5V51H3S
kind: definition
name: Reciprocal lattice
msc: [82D25, 11H06]
defines: KNAK0TTVTY
uses: [2ASPT0SP6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_lattice
---

## Definition

Let $\Lambda \subset \R^n$ be a [[Bravais lattice|2ASPT0SP6Z]] and let $k \cdot x$ be the standard inner product on $\R^n$.
The *reciprocal lattice* of $\Lambda$ is
$$\Lambda^* = \set{k \in \R^n : e^{i k \cdot R} = 1 \text{ for all } R \in \Lambda} = \set{k \in \R^n : k \cdot R \in 2\pi\Z \text{ for all } R \in \Lambda}.$$
If $a_1, \dots, a_n$ are primitive vectors of $\Lambda$, then $\Lambda^*$ is the Bravais lattice with primitive vectors $b_1, \dots, b_n$ fixed by $a_i \cdot b_j = 2\pi \delta_{ij}$.

## Remarks

In dimension $3$, $b_1 = 2\pi \dfrac{a_2 \times a_3}{a_1 \cdot (a_2 \times a_3)}$, and $b_2, b_3$ follow by cyclic permutation.
The reciprocal of $\Lambda^*$ is $\Lambda$, and the primitive cells have volumes related by $V^* = (2\pi)^n / V$.
Mathematicians often use the dual lattice $\set{k : k \cdot R \in \Z}$, which is $\Lambda^*$ divided by $2\pi$.

Example: for $\Lambda = a\Z^n$ with $a > 0$, $\Lambda^* = (2\pi/a)\Z^n$.
Indeed $k \cdot (a e_j) = a k_j \in 2\pi\Z$ for every $j$ holds exactly when each $k_j$ is a multiple of $2\pi/a$.

Non-example: for $\Lambda = \Z^2$, the vector $k = (\pi, 0)$ is not in $\Lambda^*$, because $k \cdot (1, 0) = \pi \notin 2\pi\Z$.
The wave $e^{i\pi x_1}$ changes sign under the shift by $(1, 0)$.
