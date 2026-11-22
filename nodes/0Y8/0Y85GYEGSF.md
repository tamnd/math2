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

Every finite-dimensional inner product space has an orthonormal basis, and you may even prescribe its first few vectors, as long as they are orthonormal.
Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, of dimension $n$.

1. $V$ has an [[orthonormal basis|0FWJ0VW561]].
2. Each [[orthonormal family|09VYHEF2VT]] in $V$ has at most $n$ vectors, and it extends to an orthonormal basis of $V$.

The [[proof|6G6ZHPR66X]] extends the family to a basis and runs the [[Gram-Schmidt process|0VT6P0GNQR]].

## Remarks

### Why each hypothesis is needed

Positive definiteness is needed.
Take the semidefinite form $\beta(x, y) = x_1 y_1$ on $\mathbb{R}^2$, and suppose that $e_1, e_2$ were a basis with $\beta(e_i, e_j) = \delta_{ij}$.
Then $\beta(v, v)$ would be the sum of the squared coordinates of $v$ in that basis, which is positive for $v \neq 0$.
But $\beta((0, 1), (0, 1)) = 0$, so no such basis exists.

Finite dimension is needed in the form stated.
In the [[Hilbert space|HM2HHE3J51]] $\ell^2$, no orthonormal family is a basis in the sense of linear algebra, where every vector is a finite combination.
Pick an orthonormal sequence $(f_m)$ inside the family and put $x = \sum_m 2^{-m} f_m$, which converges, with $\ip{x}{f_m} = 2^{-m} \neq 0$ for every $m$.
A finite combination of the family has a nonzero inner product with only finitely many members, so $x$ is not one.

### What it gives you

Each inner product space of dimension $n$ is isometric to $\mathbb{K}^n$ with the standard inner product.
The coordinate map of an orthonormal basis is such an isometry, by [[Parseval's identity|047RFCNVSK]].
So any computation in $V$ can be moved to $\mathbb{K}^n$ and back.

Each subspace $U$ of $V$ is again a finite-dimensional inner product space, so it has an orthonormal basis.
Extend that basis to an orthonormal basis of $V$, and the added vectors span the [[orthogonal complement|0XJXTBCB2T]] of $U$.
This is the start of the sub-area on orthogonality and least squares.
The [[Riesz representation theorem|04GYPXDXNH]] also rests on the theorem: its proof writes a linear form in an orthonormal basis.

### The converse

The converse is false: an inner product space with an orthonormal basis can have infinite dimension.
The real polynomials with $\ip{p}{q} = \int_{-1}^1 p(x) q(x)\, dx$ have the normalized [[Legendre polynomials|QFYGJVA996]] as an orthonormal basis.
Each polynomial of degree $m$ is a finite combination of $e_0, \dots, e_m$, because $e_m$ has degree exactly $m$.

### Generalizations

Each inner product space of countable dimension has an orthonormal basis, by the Gram-Schmidt process applied to a countable basis, as in the polynomial example.
Each Hilbert space has a Hilbert basis, a maximal orthonormal family whose span is dense.
Mathlib proves this as `exists_hilbertBasis`, by [[Zorn's lemma|04RXTQA5ZA]]; that version belongs to functional analysis.

### Try it

Extend $e_1 = \tfrac{1}{\sqrt2}(1, 1)$ to an orthonormal basis of $\mathbb{R}^2$.
Gram-Schmidt on $e_1, (1, 0)$ gives $u_2 = (1, 0) - \tfrac{1}{\sqrt2} e_1 = (\tfrac12, -\tfrac12)$, so $e_2 = \tfrac{1}{\sqrt2}(1, -1)$; the only other answer is $-e_2$.

## Explanations

### L1 human

Every finite-dimensional inner product space has a set of axes that are at right angles and of length $1$.
We build them with the Gram-Schmidt process from any basis.
If we already have some perpendicular unit vectors, we may keep them and add more until the axes are complete.
In the plane, for example, once one axis points along $(3, 4)/5$, the other one must point along $(4, -3)/5$ or its opposite.

### L2 human

Here is a typical problem: extend $e_1 = \tfrac13(1, 2, 2)$ to an orthonormal basis of $\mathbb{R}^3$.
First extend $e_1$ to a basis: $e_1$, $(0, 1, 0)$, $(0, 0, 1)$ is a basis, because $e_1$ has a nonzero first entry.
The process keeps $e_1$, since it is already a unit vector.
For the second vector, $\ip{(0, 1, 0)}{e_1} = \tfrac23$, so
$$u_2 = (0, 1, 0) - \tfrac23 e_1 = \left(-\tfrac29, \tfrac59, -\tfrac49\right), \qquad \norm{u_2} = \tfrac{\sqrt{45}}{9} = \tfrac{\sqrt5}{3}, \qquad e_2 = \tfrac{1}{3\sqrt5}(-2, 5, -4).$$
For the third vector, $\ip{(0, 0, 1)}{e_1} = \tfrac23$ and $\ip{(0, 0, 1)}{e_2} = -\tfrac{4}{3\sqrt5}$, so
$$u_3 = \left(-\tfrac29, -\tfrac49, \tfrac59\right) + \tfrac{4}{45}(-2, 5, -4) = \left(-\tfrac25, 0, \tfrac15\right), \qquad e_3 = \tfrac{1}{\sqrt5}(-2, 0, 1).$$
Check: $e_1 \cdot e_3 = \frac{-2 + 0 + 2}{3\sqrt5} = 0$, $e_2 \cdot e_3 = \frac{4 + 0 - 4}{15} = 0$, and $\norm{e_2}^2 = \frac{4 + 25 + 16}{45} = 1$.
This is how one chooses coordinates adapted to a given direction.
Watch out: extend to a basis before you run the process, since the process needs an independent list of $n$ vectors as input.

### L3 human

The theorem shows that a finite-dimensional inner product space has no invariant except its dimension and its field.
So every statement about such spaces can be checked in $\mathbb{K}^n$ with the standard inner product.
In infinite dimension the existence of a Hilbert basis needs Zorn's lemma in general, and the notion of basis changes to allow convergent series.
The spectral theorems of a later sub-area improve the statement: for a normal operator one can choose the orthonormal basis to consist of eigenvectors.
