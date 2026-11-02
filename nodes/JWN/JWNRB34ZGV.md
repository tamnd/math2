---
tag: JWNRB34ZGV
kind: statement
role: theorem
name: Fischer decomposition
msc: [31B05, 33C55]
uses: [2C3PAQ7H50, MVYFSYMECG, 0E0B6RA8K0]
about: [MVYFSYMECG]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_polynomial
---

## Statement

Let $n \ge 2$ and $m \ge 2$ be integers, and write $\abs{x}^2 = x_1^2 + \cdots + x_n^2$ for $x \in \R^n$.
Let $p$ be a [[homogeneous polynomial|2C3PAQ7H50]] of degree $m$ in $x_1, \dots, x_n$ with real or complex coefficients.
Then there are unique homogeneous polynomials $h$ of degree $m$ and $q$ of degree $m - 2$ such that $h$ is [[harmonic|MVYFSYMECG]] and
$$p = h + \abs{x}^2 q.$$
Repeating this with $q$ gives the unique expansion
$$p = h_m + \abs{x}^2 h_{m-2} + \abs{x}^4 h_{m-4} + \cdots.$$
Here each $h_j$ is a homogeneous harmonic polynomial of degree $j$, and the sum ends at $j = 0$ or $j = 1$.

## Remarks

Proof idea: on the space $P_m$ of homogeneous polynomials of degree $m$, use the inner product $\langle p, q \rangle = p(\partial) \bar q$, where $p(\partial)$ replaces each $x_i$ by $\partial / \partial x_i$.
For this inner product, multiplication by $\abs{x}^2$ from $P_{m-2}$ to $P_m$ is the adjoint of the [[Laplacian|0E0B6RA8K0]] from $P_m$ to $P_{m-2}$.
So the harmonic polynomials of degree $m$, which form the kernel of the Laplacian, are the orthogonal complement of $\abs{x}^2 P_{m-2}$ in $P_m$.
Example: $x_1^2 = \left(x_1^2 - \tfrac{1}{n}\abs{x}^2\right) + \abs{x}^2 \cdot \tfrac{1}{n}$, and the first term is harmonic since its Laplacian is $2 - \tfrac{2n}{n} = 0$.
Restricted to the unit sphere, where $\abs{x}^2 = 1$, the expansion shows that every polynomial is a finite sum of spherical harmonics.

## Explanations

### L1 human

Every homogeneous polynomial splits into a harmonic part plus a multiple of $\abs{x}^2$.
Repeating the split writes the polynomial as harmonic pieces times powers of $\abs{x}^2$.
On the unit sphere the powers of $\abs{x}^2$ equal $1$, so only harmonic pieces remain.

### L2 human

The decomposition gives the dimension of the space of homogeneous harmonic polynomials of degree $m$: it is $\dim P_m - \dim P_{m-2}$, which is $2m + 1$ in $\R^3$.
It shows that the restrictions of polynomials to the sphere are dense in the continuous functions on the sphere, and that they are sums of spherical harmonics.
This leads to the decomposition of $L^2$ of the sphere into spherical harmonics, which underlies the [[expansion in spherical harmonics|YTPE0GBKWW]].
