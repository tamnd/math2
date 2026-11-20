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

Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot.
Let $V^*$ be the [[dual space|0M856Q1AMZ]] of $V$, the space of [[linear forms|0RT96J4D3H]] $f \colon V \to \mathbb{K}$.

1. For each $f \in V^*$ there is exactly one vector $u \in V$ with $f(v) = \ip{v}{u}$ for all $v \in V$.
2. If $e_1, \dots, e_n$ is an [[orthonormal basis|0FWJ0VW561]] of $V$, then $u = \sum_{i=1}^n \overline{f(e_i)}\, e_i$.
3. The map $\Phi \colon V \to V^*$, $\Phi(u) = \ip{\cdot}{u}$, is a bijection. It is additive, and $\Phi(cu) = \overline{c}\, \Phi(u)$ for every scalar $c$.

So $\Phi$ is linear over $\mathbb{R}$, and [[antilinear|BNPDDM95KF]] over $\mathbb{C}$.
The vector $u$ is the Riesz representative of $f$.

## Remarks

### Why each hypothesis is needed

- Finite dimension is needed. On the real polynomials with $\ip{p}{q} = \int_0^1 pq$, the form $f(p) = p(0)$ has no representative $u$. For $p = xu$, a representative would give $\int_0^1 x u^2 = p(0) = 0$, so $u = 0$, but $f(1) = 1 \neq \ip{1}{0}$.
- Positive definiteness is needed. For the semidefinite form $\beta(x, y) = x_1 y_1$ on $\mathbb{R}^2$, every $\beta(\cdot, u)$ vanishes at $(0, 1)$. So $f(x) = x_2$ has no representative, and $u = (0, 1)$ and $u = 0$ both represent $f = 0$.
- The slot matters over $\mathbb{C}$. The map $v \mapsto \ip{u}{v}$ is antilinear in $v$, so it is not an element of $V^*$ unless $u = 0$.

### Consequences

- $\dim V^* = \dim V$, since $\Phi$ is a bijection that is linear over $\mathbb{R}$. Over $\mathbb{C}$, $\Phi$ maps a basis to a basis, since conjugation keeps independence.
- The [[adjoint|0R9NMSM1ZP]] of a linear map $T \colon V \to W$ exists: for fixed $w$, the form $v \mapsto \ip{Tv}{w}$ is $\ip{\cdot}{T^* w}$ for a unique $T^* w$.
- The dual space carries the inner product $\ip{\Phi(u)}{\Phi(u')} = \ip{u'}{u}$, and $\Phi$ maps an orthonormal basis to the dual basis.

### Converse

The theorem is already an equivalence in part 3: $\Phi$ is bijective.
In infinite dimension, $\Phi$ maps $V$ onto the continuous dual exactly when $V$ is complete, that is, a [[Hilbert space|HM2HHE3J51]].

### Generalizations

- The [[Riesz representation theorem|TTC40N49M6]] for Hilbert spaces represents each continuous linear form, and $\norm{f} = \norm{u}$ for the operator norm.
- In physics and in Mathlib the inner product is linear in the second slot. Then $f = \ip{u}{\cdot}$, and in bra-ket notation $f$ is the bra $\langle u|$.
- The Lax-Milgram theorem replaces the inner product by a coercive bilinear form.

## History

According to the Wikipedia article, the theorem for Hilbert spaces is often attributed to Riesz and Fréchet, in 1907.

## Explanations

### L1 human

A linear form eats a vector and returns a number.
In an inner product space, every linear form is the inner product with one fixed vector.
On $\mathbb{R}^3$, the form $x \mapsto 2x_1 - x_2 + 5x_3$ is the dot product with $(2, -1, 5)$.
So in finite dimension, vectors and linear forms match one to one.

### L2 human

Worked example: represent $f(p) = p(0)$ on the real polynomials of degree at most $1$, with $\ip{p}{q} = \int_0^1 p q$.

1. Write $u = a + bx$. The condition $f(p) = \ip{p}{u}$ for $p = 1$ and $p = x$ gives two equations.
2. For $p = 1$: $\int_0^1 (a + bx) = a + \frac{b}{2} = f(1) = 1$.
3. For $p = x$: $\int_0^1 x(a + bx) = \frac{a}{2} + \frac{b}{3} = f(x) = 0$.
4. So $a = -\frac{2b}{3}$ and $-\frac{b}{6} = 1$. This gives $b = -6$, $a = 4$ and $u = 4 - 6x$.
5. Check with $p = 1 + 3x$: $\int_0^1 (1 + 3x)(4 - 6x) = 4 + 3 - 6 = 1 = p(0)$.

Over $\mathbb{C}$, take $f(z) = z_1 + i z_2$ on $\mathbb{C}^2$.
Part 2 gives $u = (\overline{1}, \overline{i}) = (1, -i)$.
A trap: the form $i f$ has the representative $\overline{i}\, u = (-i, -1)$, not $iu$.
This is the antilinearity of part 3.

### L3 human

The theorem identifies $V$ with $V^*$, but over $\mathbb{C}$ the identification is antilinear.
So $V^*$ is naturally the complex conjugate space $\overline{V}$, and this is the reason for the bra-ket notation.
The identification depends on the inner product: a different inner product gives a different map $\Phi$.
In matrix terms, for $\mathbb{C}^n$ with the standard inner product, $\Phi$ sends the column $u$ to the row $u^*$.
