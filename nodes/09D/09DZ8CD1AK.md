---
tag: 09DZ8CD1AK
kind: statement
role: theorem
name: Coordinates in an orthonormal basis
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0S9GGTR0EX, 04CYQHN6MC]
uses: [0FWJ0VW561, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: Basic formula
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Statement

Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$.
Then, for each $v \in V$:

1. $v = \sum_{i=1}^{n} \ip{v}{e_i}\, e_i$, so the [[coordinate vector|04CYQHN6MC]] of $v$ is $(\ip{v}{e_1}, \dots, \ip{v}{e_n})$;
2. $\norm{v}^2 = \sum_{i=1}^{n} |\ip{v}{e_i}|^2$, where $\norm{\cdot}$ is the [[induced norm|0KG4D8AP6G]].

## Remarks

### Why each hypothesis is needed

- The basis must be normalized. For the orthogonal basis $(1, 1)$, $(1, -1)$ of $\mathbb{R}^2$ and $v = (3, 1)$, the formula gives $2v$, as the [[non-example|72YCTDMG60]] shows.
- The family must span $V$. For the orthonormal family $(e_1)$ in $\mathbb{R}^2$ and $v = (1, 1)$, the sum is $\ip{v}{e_1} e_1 = (1, 0) \neq v$, and $1 < 2 = \norm{v}^2$.
- The slots matter over $\mathbb{C}$. With $\ip{e_i}{v}$ in place of $\ip{v}{e_i}$, the [[basis of $\mathbb{C}^2$|V2B3V8T8TX]] gives $-v$ for $v = (0, 1)$.

### Consequences

- The coordinates of $v$ need no linear system: each one is a single inner product.
- The map $V \to \mathbb{K}^n$, $v \mapsto (\ip{v}{e_i})_i$, preserves norms, and by the [[polarization identity|05FKHRT0B4]] it preserves inner products. This is [[Parseval's identity|047RFCNVSK]].
- If $T \colon V \to V$ is linear, then the entry $(i, j)$ of its matrix in this basis is $\ip{T e_j}{e_i}$.
- If $v \perp e_i$ for every $i$, then $v = 0$.

### Converse

The converse of part 1 is true for a basis.
If a basis $(e_1, \dots, e_n)$ satisfies part 1 for every $v$, then for $v = e_j$ we get $e_j = \sum_i \ip{e_j}{e_i} e_i$.
Coordinates in a basis are unique, so $\ip{e_j}{e_i} = \delta_{ij}$, and the basis is orthonormal.
Let an orthonormal family satisfy part 2 for every $v$, without the assumption that it is a basis.
Then it spans $V$, by the equality case of [[Bessel's inequality|0RBT5PB74K]].

### Generalizations

- For an orthogonal basis $(u_1, \dots, u_n)$ of nonzero vectors, $v = \sum_i \frac{\ip{v}{u_i}}{\norm{u_i}^2} u_i$.
- For an orthonormal family that does not span $V$, the sum $\sum_i \ip{v}{e_i} e_i$ is the [[orthogonal projection|0B8KZRT28M]] of $v$ onto the span.
- In a [[Hilbert space|HM2HHE3J51]] with an orthonormal basis, part 1 becomes a convergent series. For periodic functions this is the [[Fourier series|G12KXDHPPS]], and the numbers $\ip{v}{e_i}$ are the [[Fourier coefficients|5NN2YZZR3V]].

## Explanations

### L1 human

In an orthonormal basis, each coordinate of a vector is one inner product.
For the axes $(1, 0)$ and $(0, 1)$ of the plane, the coordinates of $(3, 4)$ are $3$ and $4$.
After a rotation of the axes, the coordinates are still inner products, only with the new axes.
The squared length of the vector is the sum of the squared coordinates, as in Pythagoras.

### L2 human

Worked example: Fourier coefficients of a trigonometric polynomial.

1. Let $V$ be the span of $e^{-it}$, $1$ and $e^{it}$ in the complex functions on $[-\pi, \pi]$, with $\ip{f}{g} = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(t)\overline{g(t)}\, dt$.
2. For integers $j, k$, $\ip{e^{ijt}}{e^{ikt}} = \frac{1}{2\pi}\int_{-\pi}^{\pi} e^{i(j - k)t}\, dt$, which is $1$ for $j = k$ and $0$ for $j \neq k$. So the three functions form an orthonormal basis of $V$.
3. Let $f(t) = \cos t = \frac12 e^{it} + \frac12 e^{-it}$. The coefficient for $e^{it}$ is $\ip{f}{e^{it}} = \frac{1}{2\pi}\int_{-\pi}^{\pi} \cos t\, e^{-it}\, dt = \frac12$.
4. In the same way, $\ip{f}{e^{-it}} = \frac12$ and $\ip{f}{1} = 0$.
5. Part 2: $\norm{f}^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} \cos^2 t\, dt = \frac12$, and $|\frac12|^2 + 0 + |\frac12|^2 = \frac12$.

The typical use is in signal processing, where the coefficients measure the amount of each frequency.
A trap: with the convention of physics or of Mathlib, the coefficient is written $\ip{e_i}{v}$, but it has the same value.

### L3 human

The theorem says that an orthonormal basis turns $V$ into $\mathbb{K}^n$ with the standard inner product, by an isometry.
The coordinate functionals $v \mapsto \ip{v}{e_i}$ are the [[dual basis|0ZD2CF6ZS0]] of $(e_1, \dots, e_n)$, so an orthonormal basis is its own dual basis under the [[Riesz representation|04GYPXDXNH]].
In infinite dimension the formula is the expansion in a Hilbert basis, and Fourier series on $[-\pi, \pi]$ are the model case.
