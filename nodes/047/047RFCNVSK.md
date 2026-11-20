---
tag: 047RFCNVSK
kind: statement
role: theorem
name: Parseval's identity
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0S9GGTR0EX, 0NB0AWGJBW]
uses: [0FWJ0VW561, 0KG4D8AP6G, 04CYQHN6MC]
sources:
  - url: https://en.wikipedia.org/wiki/Parseval's_identity
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Parseval's_identity
    locator: Generalization of the Pythagorean theorem
  - book: isbn:9783031410253
    locator: Chapter 6
formal:
  - system: lean4
    library: mathlib
    decl: HilbertBasis.tsum_inner_mul_inner
    match: stronger
same_as:
  wikidata: Q944238
  wikipedia: Parseval's identity
---

## Statement

Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$.

1. For all $x, y \in V$, $\ip{x}{y} = \sum_{i=1}^{n} \ip{x}{e_i}\,\overline{\ip{y}{e_i}}$.
2. For all $x \in V$, $\norm{x}^2 = \sum_{i=1}^{n} |\ip{x}{e_i}|^2$.
3. The [[coordinate map|04CYQHN6MC]] $C \colon V \to \mathbb{K}^n$, $C(x) = (\ip{x}{e_1}, \dots, \ip{x}{e_n})$, is a linear bijection with $\ip{Cx}{Cy}_{\mathbb{K}^n} = \ip{x}{y}$, where $\mathbb{K}^n$ has the standard inner product.

## Remarks

### Why each hypothesis is needed

- The family must span $V$. For the orthonormal family $(e_1)$ in $\mathbb{R}^2$ and $x = y = (1, 1)$, the sum is $1$, but $\norm{x}^2 = 2$.
- The family must be orthonormal. For the basis $(1, 1)$, $(1, -1)$ of $\mathbb{R}^2$ and $x = (1, 0)$, the sum is $1 + 1 = 2$, but $\norm{x}^2 = 1$.
- The conjugate must be on the coefficient of $y$. In $\mathbb{C}^2$ with the standard basis, $x = (1, 0)$ and $y = (i, 0)$ give $\ip{x}{y} = -i$, but $\overline{\ip{x}{e_1}}\,\ip{y}{e_1} = i$.

### Consequences

- In coordinates of an orthonormal basis, every inner product space of dimension $n$ looks like $\mathbb{K}^n$ with the standard inner product.
- If $T$ maps an orthonormal basis to an orthonormal basis, then $T$ preserves inner products. The matrix of such a map in orthonormal bases is [[unitary|0AR68JTMDT]], or [[orthogonal|0W02QESPJQ]] over $\mathbb{R}$.
- Part 2 is the equality case of [[Bessel's inequality|0RBT5PB74K]], since every $x$ lies in the span of a basis.

### Converse

The converse is false for families that are not assumed to be orthonormal.
In $\mathbb{R}^2$, let $f_k = \sqrt{2/3}\,(\cos\frac{2\pi k}{3}, \sin\frac{2\pi k}{3})$ for $k = 0, 1, 2$.
Then $\sum_k \ip{x}{f_k} f_k = x$ and $\sum_k \ip{x}{f_k}^2 = \norm{x}^2$ for all $x$, since $\sum_k f_k f_k^\top = I_2$.
But the family has three vectors in a plane, so it is not a basis, and each $f_k$ has norm $\sqrt{2/3}$.
For an orthonormal family, the converse holds.
If part 2 holds for every $x$, then the family spans $V$, by the equality case of Bessel's inequality.

### Generalizations

- In a [[Hilbert space|HM2HHE3J51]] with a Hilbert basis $(e_i)_{i \in I}$, the sums become convergent series. Mathlib states this form.
- For [[Fourier series|G12KXDHPPS]] on $[-\pi, \pi]$, part 2 says that $\frac{1}{2\pi}\int_{-\pi}^{\pi} |f|^2$ is the sum of the squared moduli of the [[Fourier coefficients|5NN2YZZR3V]] of $f$.

## History

According to the Wikipedia article, the identity is named after Parseval.

## Explanations

### L1 human

In an orthonormal basis, a vector is a list of coordinates.
The inner product of two vectors is then the usual dot product of their lists, with conjugates over $\mathbb{C}$.
The squared length is the sum of the squared coordinates, as in Pythagoras.

### L2 human

Worked example: in $\mathbb{R}^2$ take the orthonormal basis $e_1 = (\frac35, \frac45)$, $e_2 = (-\frac45, \frac35)$.

1. Let $x = (1, 2)$ and $y = (2, -1)$. Directly, $\ip{x}{y} = 2 - 2 = 0$.
2. Coordinates of $x$: $\ip{x}{e_1} = \frac{3 + 8}{5} = \frac{11}{5}$ and $\ip{x}{e_2} = \frac{-4 + 6}{5} = \frac25$.
3. Coordinates of $y$: $\ip{y}{e_1} = \frac{6 - 4}{5} = \frac25$ and $\ip{y}{e_2} = \frac{-8 - 3}{5} = -\frac{11}{5}$.
4. Part 1: $\frac{11}{5} \cdot \frac25 + \frac25 \cdot (-\frac{11}{5}) = 0$, as in step 1.
5. Part 2: $\frac{121}{25} + \frac{4}{25} = 5 = \norm{x}^2$.

The typical use is to compute inner products of functions from their coefficients, as in Fourier analysis.
A trap: over $\mathbb{C}$, the conjugate goes on the coefficients of the second vector.

### L3 human

Part 3 says that each orthonormal basis gives an isometric isomorphism $V \cong \mathbb{K}^n$.
So two inner product spaces over the same field are isometric exactly when they have the same dimension.
In infinite dimension, the same statement for a Hilbert basis identifies each separable infinite-dimensional Hilbert space with $\ell^2$.
