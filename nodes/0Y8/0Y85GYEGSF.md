---
tag: 0Y85GYEGSF
kind: statement
role: theorem
name: Existence of an orthonormal basis
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0S9GGTR0EX]
uses: [0FWJ0VW561, 0VT6P0GNQR, 09VYHEF2VT]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: Existence
  - book: isbn:9783031410253
    locator: Chapter 6
formal:
  - system: lean4
    library: mathlib
    decl: exists_hilbertBasis
    match: partial
---

## Statement

Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, of dimension $n$.

1. $V$ has an [[orthonormal basis|0FWJ0VW561]].
2. Each [[orthonormal family|09VYHEF2VT]] in $V$ has at most $n$ vectors, and it extends to an orthonormal basis of $V$.

## Remarks

### Why each hypothesis is needed

- Part 1 needs positive definiteness. Take the semidefinite form $\beta(x, y) = x_1 y_1$ on $\mathbb{R}^2$.
  If $e_1, e_2$ were a basis with $\beta(e_i, e_j) = \delta_{ij}$, then $\beta(v, v)$ would be the sum of the squared coordinates of $v$.
  This sum is positive for $v \neq 0$, but $\beta((0, 1), (0, 1)) = 0$.
- Finite dimension is needed in the form stated. In the [[Hilbert space|HM2HHE3J51]] $\ell^2$, no orthonormal family is a basis in the sense of linear algebra.
  For an orthonormal sequence $(f_m)$ in the family, the vector $x = \sum_m 2^{-m} f_m$ has $\ip{x}{f_m} = 2^{-m} \neq 0$ for every $m$.
  A finite combination of the family has a nonzero inner product with only finitely many members, so $x$ is not one.

### Consequences

- Each inner product space of dimension $n$ is isometric to $\mathbb{K}^n$ with the standard inner product. The coordinate map of an orthonormal basis is an isometry, by [[Parseval's identity|047RFCNVSK]].
- Each subspace $U$ of $V$ has an orthonormal basis. Extend it to an orthonormal basis of $V$. The added vectors span the [[orthogonal complement|0XJXTBCB2T]] of $U$.
- Each linear form on $V$ is $\ip{\cdot}{u}$ for a unique $u$, by the [[Riesz representation theorem|04GYPXDXNH]], whose proof uses an orthonormal basis.

### Converse

The converse is false: an inner product space with an orthonormal basis can have infinite dimension.
The real polynomials with $\ip{p}{q} = \int_{-1}^1 pq$ have the normalized [[Legendre polynomials|QFYGJVA996]] as an orthonormal basis, since each polynomial of degree $m$ is a combination of $e_0, \dots, e_m$.

### Generalizations

- Each inner product space of countable dimension has an orthonormal basis, by the Gram-Schmidt process applied to a countable basis.
- Each Hilbert space has a Hilbert basis, a maximal orthonormal family whose span is dense. Mathlib proves this as `exists_hilbertBasis`, by [[Zorn's lemma|04RXTQA5ZA]].

## Explanations

### L1 human

Every finite-dimensional inner product space has a set of axes that are perpendicular and of length $1$.
We build them with the Gram-Schmidt process from any basis.
If we already have some perpendicular unit vectors, we can keep them and add more.

### L2 human

Worked example: extend $e_1 = \frac13(1, 2, 2)$ to an orthonormal basis of $\mathbb{R}^3$.

1. Extend $e_1$ to a basis: $e_1$, $(0, 1, 0)$, $(0, 0, 1)$ is a basis, since $e_1$ has a nonzero first entry.
2. Gram-Schmidt keeps $e_1$. Next, $u_2 = (0, 1, 0) - \frac23 e_1 = (-\frac29, \frac59, -\frac49)$, so $e_2 = \frac{1}{3\sqrt5}(-2, 5, -4)$.
3. Then $u_3 = (0, 0, 1) - \frac23 e_1 - \ip{(0, 0, 1)}{e_2}\, e_2$, with $\ip{(0, 0, 1)}{e_2} = -\frac{4}{3\sqrt5}$.
4. This gives $u_3 = (-\frac29, -\frac49, \frac59) + \frac{4}{45}(-2, 5, -4) = (-\frac{2}{5}, 0, \frac{1}{5})$, so $e_3 = \frac{1}{\sqrt5}(-2, 0, 1)$.
5. Check: $e_1 \cdot e_3 = \frac{-2 + 0 + 2}{3\sqrt5} = 0$ and $e_2 \cdot e_3 = \frac{4 + 0 - 4}{15} = 0$.

The typical use is to choose coordinates adapted to a given direction or subspace.
A trap: the extension to a basis must come before the Gram-Schmidt process, since the process needs a basis as input.

### L3 human

The theorem shows that finite-dimensional inner product spaces have no invariants except the dimension and the field.
So every statement about them can be checked in $\mathbb{K}^n$ with the standard inner product.
In infinite dimension, the existence of a Hilbert basis uses Zorn's lemma, and the notion of basis changes to allow convergent series.
