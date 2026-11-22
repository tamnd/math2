---
tag: 04GYPXDXNH
kind: statement
role: theorem
name: Riesz representation theorem in finite dimensions
msc: ["46C05", "15A04"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [07YQ1C78G0, 07JBSZE0V4]
uses: [01EK923SKP, 0RT96J4D3H, 0M856Q1AMZ, 0FWJ0VW561, BNPDDM95KF]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_representation_theorem
    locator: Example in finite dimensions using matrix transformations
  - url: https://en.wikipedia.org/wiki/Riesz_representation_theorem
    locator: Mathematics vs. physics notations and definitions of inner product
  - url: https://en.wikipedia.org/wiki/Riesz_representation_theorem
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Statement

In a finite-dimensional inner product space, every linear form is the inner product with one fixed vector, and that vector is unique.
Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot and conjugate-linear in the second.
Let $V^*$ be the [[dual space|0M856Q1AMZ]] of $V$, the space of [[linear forms|0RT96J4D3H]] $f \colon V \to \mathbb{K}$.

1. For each $f \in V^*$ there is exactly one vector $u \in V$ with $f(v) = \ip{v}{u}$ for all $v \in V$.
2. If $e_1, \dots, e_n$ is an [[orthonormal basis|0FWJ0VW561]] of $V$, then this vector is $u = \sum_{i=1}^n \overline{f(e_i)}\, e_i$.
3. The map $\Phi \colon V \to V^*$, $\Phi(u) = \ip{\cdot}{u}$, is a bijection. It is additive, and $\Phi(c u) = \overline{c}\, \Phi(u)$ for every scalar $c$.

So $\Phi$ is linear over $\mathbb{R}$ and [[antilinear|BNPDDM95KF]] over $\mathbb{C}$.
The vector $u$ is called the Riesz representative of $f$.
The [[proof|7MN6S22S2Q]] builds $u$ from an orthonormal basis.

## Remarks

### A first representation

On $\mathbb{R}^3$ with the dot product, the form $f(x) = 2x_1 - x_2 + 5x_3$ is the dot product with $u = (2, -1, 5)$, and part 2 reads off the entries as $f(e_1) = 2$, $f(e_2) = -1$ and $f(e_3) = 5$.
Over $\mathbb{C}^2$ the conjugates appear.
For $f(z) = z_1 + i z_2$, part 2 gives $u = (\overline{1}, \overline{i}) = (1, -i)$, and the check is
$$\ip{z}{u} = z_1 \overline{1} + z_2 \overline{(-i)} = z_1 + i z_2 = f(z).$$
The form $i f$ then has the representative $\overline{i}\, u = -i (1, -i) = (-i, -1)$, not $i u$; this is the antilinearity of part 3.

### Why each hypothesis is needed

Finite dimension is needed.
On all real polynomials with $\ip{p}{q} = \int_0^1 p q \, dx$, the form $f(p) = p(0)$ has no representative.
If $u$ were one, then $p = x u$ would give $\int_0^1 x\, u(x)^2 \, dx = f(x u) = 0$, so $u = 0$; but then $f(1) = 1 \ne 0 = \ip{1}{0}$.

Positive definiteness is needed.
For the semidefinite form $\beta(x, y) = x_1 y_1$ on $\mathbb{R}^2$, every form $\beta(\cdot, u)$ vanishes at $(0, 1)$, so $f(x) = x_2$ has no representative.
Uniqueness fails too, since $u = (0, 1)$ and $u = 0$ both represent $f = 0$.

The slot matters over $\mathbb{C}$.
With our convention, the map $v \mapsto \ip{u}{v}$ is conjugate-linear in $v$, so it is not a linear form unless $u = 0$.

### What it gives you

The [[adjoint|0R9NMSM1ZP]] of a linear map $T \colon V \to W$ comes from the theorem.
For fixed $w \in W$, the map $v \mapsto \ip{T v}{w}$ is a linear form on $V$, so it equals $\ip{\cdot}{T^* w}$ for exactly one vector $T^* w$, and this defines $T^*$.
The theorem also gives $\dim V^* = \dim V$ once more, since $\Phi$ is a bijection that is linear over $\mathbb{R}$, and over $\mathbb{C}$ it sends a basis to a basis.
Finally, $\Phi$ sends an orthonormal basis $e_1, \dots, e_n$ to its [[dual basis|0ZD2CF6ZS0]], since $\Phi(e_j)(e_i) = \ip{e_i}{e_j}$ is $1$ for $i = j$ and $0$ otherwise.

### The converse and the infinite case

Part 3 already contains the converse: every vector $u$ gives a linear form $\ip{\cdot}{u}$, and different vectors give different forms.
In infinite dimension the statement needs two changes, which belong to functional analysis.
Only continuous linear forms can be represented, and every continuous linear form is represented exactly when the space is complete, that is, a [[Hilbert space|HM2HHE3J51]].
That is the [[Riesz representation theorem|TTC40N49M6]] for Hilbert spaces, which adds that the norm of $f$ as an operator equals $\norm{u}$.

### Other conventions

In physics and in Mathlib the inner product is linear in the second slot.
Then the theorem reads $f = \ip{u}{\cdot}$, and in the bra-ket notation of physics the form $f$ is the bra $\langle u \rvert$ of the ket $\lvert u \rangle$.
Both versions say the same thing, and in both the map from vectors to forms is conjugate-linear.

## History

The theorem for spaces of square-integrable functions is due to Frigyes Riesz and Maurice Fréchet, who found it independently in 1907.

## Explanations

### L1 human

A linear form eats a vector and returns a number, in a way that respects sums and multiples.
The theorem says that every such rule is a dot product with one fixed vector.
On $\mathbb{R}^3$, the rule "twice the first entry, minus the second, plus five times the third" is the dot product with $(2, -1, 5)$.
So a rule that measures vectors can always be replaced by an arrow that you measure against.

### L2 human

Here is a typical use where no coordinates are given: represent $f(p) = p(0)$ on the real polynomials of degree at most $1$, with $\ip{p}{q} = \int_0^1 p q \, dx$.
Write $u = a + b x$, and test the condition $f(p) = \ip{p}{u}$ on the basis $1, x$.
For $p = 1$ and for $p = x$ it gives
$$a + \frac{b}{2} = f(1) = 1, \qquad \frac{a}{2} + \frac{b}{3} = f(x) = 0.$$
The second equation gives $a = -\frac{2b}{3}$, and then the first gives $-\frac{b}{6} = 1$, so $b = -6$, $a = 4$ and $u = 4 - 6x$.
Check with $p = 1 + 3x$:
$$\int_0^1 (1 + 3x)(4 - 6x) \, dx = \int_0^1 (4 + 6x - 18x^2) \, dx = 4 + 3 - 6 = 1 = p(0).$$
So evaluation at $0$, which does not look like an inner product at all, is the inner product with $4 - 6x$.
Watch out: the representative depends on the inner product, and with $\int_{-1}^1$ in place of $\int_0^1$ you get a different $u$.

### L3 human

The theorem gives an isomorphism of $V^*$ with the conjugate space $\overline{V}$, the same set with the scalar action $c \cdot u = \overline{c} u$.
Over $\mathbb{R}$ it is a linear isomorphism $V \cong V^*$, but it is not canonical: it depends on the inner product, while the isomorphism $V \cong V^{**}$ of the sub-area on [[duality|9K7FFF26QR]] does not.
For $\mathbb{C}^n$ with the standard inner product, $\Phi$ sends the column $u$ to the row $u^*$, since $\ip{z}{u} = u^* z$.
The same idea, with a coercive bilinear form in place of the inner product, is the Lax-Milgram theorem of the theory of partial differential equations.
The sub-area on [[adjoints and normal operators|3YM9EK6VMB]] builds on the definition of $T^*$ above.
