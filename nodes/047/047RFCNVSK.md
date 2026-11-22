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

Parseval's identity says that in an orthonormal basis you can compute inner products and lengths from coordinates alone, exactly as with the dot product.
Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot, and let $\norm{\cdot}$ be the [[induced norm|0KG4D8AP6G]].
Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$.

1. For all $x, y \in V$, $\ip{x}{y} = \sum_{i=1}^{n} \ip{x}{e_i}\,\overline{\ip{y}{e_i}}$.
2. For all $x \in V$, $\norm{x}^2 = \sum_{i=1}^{n} \abs{\ip{x}{e_i}}^2$.
3. The [[coordinate map|04CYQHN6MC]] $C \colon V \to \mathbb{K}^n$, $C(x) = (\ip{x}{e_1}, \dots, \ip{x}{e_n})$, is a linear bijection with $\ip{Cx}{Cy} = \ip{x}{y}$ for the standard inner product on $\mathbb{K}^n$.

The [[proof|9A6HKM6K7Z]] expands both vectors in the basis and lets orthonormality remove the mixed terms.

## Remarks

### A first computation

In $\mathbb{R}^2$ with the dot product, take the orthonormal basis $e_1 = (\tfrac35, \tfrac45)$ and $e_2 = (-\tfrac45, \tfrac35)$, and the vectors $x = (1, 2)$ and $y = (2, -1)$.
Directly, $\ip{x}{y} = 2 - 2 = 0$ and $\norm{x}^2 = 5$.
Now compute the coordinates:
$$\ip{x}{e_1} = \frac{3 + 8}{5} = \frac{11}{5}, \quad \ip{x}{e_2} = \frac{-4 + 6}{5} = \frac25, \quad \ip{y}{e_1} = \frac{6 - 4}{5} = \frac25, \quad \ip{y}{e_2} = \frac{-8 - 3}{5} = -\frac{11}{5}.$$
Part 1 multiplies matching coordinates and adds, and part 2 adds the squares:
$$\frac{11}{5} \cdot \frac25 + \frac25 \cdot \left(-\frac{11}{5}\right) = 0, \qquad \frac{121}{25} + \frac{4}{25} = 5.$$
Both answers agree with the direct computation.

### Why each hypothesis is needed

The family must span $V$.
For the orthonormal family $(e_1)$ with $e_1 = (1, 0)$ in $\mathbb{R}^2$ and $x = (1, 1)$, the sum in part 2 is $1$, but $\norm{x}^2 = 2$.
Without spanning, only [[Bessel's inequality|0RBT5PB74K]] survives.

The family must be orthonormal, not just a basis.
For the orthogonal basis $(1, 1)$, $(1, -1)$ of $\mathbb{R}^2$ and $x = (1, 0)$, the sum in part 2 is $1 + 1 = 2$, but $\norm{x}^2 = 1$.

### The complex case

Over $\mathbb{C}$ the conjugate sits on the coordinates of the second vector, the slot in which our inner product is conjugate-linear.
Take the orthonormal basis $e_1 = \tfrac{1}{\sqrt2}(1, i)$, $e_2 = \tfrac{1}{\sqrt2}(1, -i)$ of $\mathbb{C}^2$, with $x = (0, 1)$ and $y = (1, i)$.
Then $\ip{x}{y} = 0 \cdot 1 + 1 \cdot \overline{i} = -i$, and the coordinates are
$$\ip{x}{e_1} = -\tfrac{i}{\sqrt2}, \quad \ip{x}{e_2} = \tfrac{i}{\sqrt2}, \quad \ip{y}{e_1} = \tfrac{1 + i \overline{i}}{\sqrt2} = \sqrt2, \quad \ip{y}{e_2} = \tfrac{1 + i \cdot i}{\sqrt2} = 0.$$
Part 1 gives $\left(-\tfrac{i}{\sqrt2}\right)\sqrt2 + 0 = -i$, as it should.

Watch out.
If you put the conjugate on the coordinates of $x$ instead, you get $\tfrac{i}{\sqrt2} \cdot \sqrt2 = i$, the conjugate of the right answer.
Books that make the inner product linear in the second slot, as physics books and Mathlib do, write $\sum_i \overline{\ip{e_i}{x}}\, \ip{e_i}{y}$, and that is the same number in their notation.

### What it gives you

Part 3 says that each $n$-dimensional inner product space looks exactly like $\mathbb{K}^n$ with the standard inner product, once an orthonormal basis is chosen.
So a linear map that sends one orthonormal basis to another preserves all inner products.
Its matrix in orthonormal bases is [[unitary|0AR68JTMDT]], or [[orthogonal|0W02QESPJQ]] over $\mathbb{R}$.
Part 2 is also the equality case of Bessel's inequality, since every vector lies in the span of a basis.

### The converse

For an orthonormal family, the converse holds: if part 2 holds for every $x$, then the family spans $V$, by the equality case of Bessel's inequality.
For families that are not orthonormal, the converse fails.
In $\mathbb{R}^2$ let $f_k = \sqrt{2/3}\,\left(\cos\tfrac{2\pi k}{3}, \sin\tfrac{2\pi k}{3}\right)$ for $k = 0, 1, 2$.
Because $\sum_k \cos^2\tfrac{2\pi k}{3} = \sum_k \sin^2\tfrac{2\pi k}{3} = \tfrac32$ and $\sum_k \cos\tfrac{2\pi k}{3} \sin\tfrac{2\pi k}{3} = 0$, we get $\sum_k f_k f_k^{\mathsf{T}} = I_2$.
Hence $\sum_k \ip{x}{f_k}^2 = \norm{x}^2$ for every $x$, although three vectors in a plane are not a basis and each has length $\sqrt{2/3}$.

### Beyond finite dimension

In a [[Hilbert space|HM2HHE3J51]] with a Hilbert basis $(e_i)_{i \in I}$, the sums become convergent series, and Mathlib proves this form; it belongs to functional analysis.
For [[Fourier series|G12KXDHPPS]] on $[-\pi, \pi]$, with coefficients $c_m = \tfrac{1}{2\pi}\int_{-\pi}^{\pi} f(t) e^{-imt}\, dt$, the norm form reads $\tfrac{1}{2\pi}\int_{-\pi}^{\pi} \abs{f(t)}^2\, dt = \sum_{m \in \mathbb{Z}} \abs{c_m}^2$.
This is the model for all the finite sums above, and it explains the link to the [[Fourier coefficients|5NN2YZZR3V]].

### Try it

Compute $\norm{(1, 7)}^2$ from its coordinates in the basis $e_1 = (\tfrac35, \tfrac45)$, $e_2 = (-\tfrac45, \tfrac35)$.
The coordinates are $\tfrac{31}{5}$ and $\tfrac{17}{5}$, and $\tfrac{961 + 289}{25} = 50 = 1 + 49$.

## History

The identity is named after the French mathematician Marc-Antoine Parseval, who stated a version of it for series.

## Explanations

### L1 human

In an orthonormal basis a vector is just a list of coordinates.
Parseval's identity says that you can then forget the basis and work with the lists.
The inner product of two vectors is the dot product of their lists, with conjugates when the numbers are complex.
The squared length is the sum of the squared coordinates, as in Pythagoras.
For the list $(3, 4)$ the squared length is $9 + 16 = 25$, in whatever orthonormal basis the list was taken.

### L2 human

Here is a typical use: compute $\int_{-1}^{1} (1 + t)(1 - 2t)\, dt$ without integrating the product.
On polynomials of degree at most $1$ with $\ip{p}{q} = \int_{-1}^{1} p(t) q(t)\, dt$, the polynomials $e_0 = \tfrac{1}{\sqrt2}$ and $e_1 = \sqrt{3/2}\, t$ form an orthonormal basis, as the [[Legendre example|JPDVZM20EX]] shows.
The coordinates of $p = 1 + t$ and $q = 1 - 2t$ are
$$\ip{p}{e_0} = \sqrt2, \quad \ip{p}{e_1} = \sqrt{\tfrac32} \cdot \tfrac23 = \sqrt{\tfrac23}, \quad \ip{q}{e_0} = \sqrt2, \quad \ip{q}{e_1} = \sqrt{\tfrac32} \cdot \left(-\tfrac43\right) = -2\sqrt{\tfrac23}.$$
Part 1 gives
$$\ip{p}{q} = \sqrt2 \cdot \sqrt2 + \sqrt{\tfrac23} \cdot \left(-2\sqrt{\tfrac23}\right) = 2 - \tfrac43 = \tfrac23.$$
Check: $\int_{-1}^{1} (1 - t - 2t^2)\, dt = 2 - 0 - \tfrac43 = \tfrac23$.
This is how Fourier analysis works in practice: once the coefficients are known, inner products and energies are sums of products of coefficients.

### L3 human

Part 3 says that each orthonormal basis gives an isometric isomorphism $V \cong \mathbb{K}^n$, so two finite-dimensional inner product spaces over the same field are isometric exactly when they have the same dimension.
For a separable infinite-dimensional Hilbert space, a countable Hilbert basis gives in the same way an isometric isomorphism with the sequence space $\ell^2$.
On the side of analysis, Parseval's identity for Fourier series and Plancherel's theorem for the Fourier transform are the same statement for other orthonormal systems.
The sub-area on isometries uses part 3 to describe the maps that preserve inner products.
