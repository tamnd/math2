---
tag: 46WGVM5VS6
kind: statement
role: theorem
name: Jordan-von Neumann theorem
msc: ["46C15", "39B52"]
topics: [1D4JTZ9VS3]
audience: ug2
uses: [00A0RPAQ8A, 01EK923SKP, 0KG4D8AP6G]
about: [0QVNCJXRY3, 03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelogram_law
    locator: Normed vector spaces satisfying the parallelogram law
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Jordan–von Neumann theorems
formal:
  - system: lean4
    library: mathlib
    decl: InnerProductSpace.ofNorm
    match: weaker
---

## Statement

A norm comes from an inner product exactly when it satisfies the parallelogram law, and then the norm determines the inner product.
Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $(V, \norm{\cdot})$ be a [[normed vector space|00A0RPAQ8A]] over $\mathbb{K}$.
Then the following are equivalent.

1. There is an [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ on $V$ whose [[induced norm|0KG4D8AP6G]] is $\norm{\cdot}$, that is, $\norm{x}^2 = \ip{x}{x}$ for all $x \in V$.
2. The norm satisfies the parallelogram law: $\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2$ for all $x, y \in V$.

When these hold, the inner product is unique, and the [[polarization identity|05FKHRT0B4]] gives it.
For $\mathbb{K} = \mathbb{R}$ it is
$$\ip{x}{y} = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right),$$
and for $\mathbb{K} = \mathbb{C}$, with $\ip{\cdot}{\cdot}$ linear in the first slot and conjugate-linear in the second, it is
$$\ip{x}{y} = \frac14 \sum_{k=0}^{3} i^k \norm{x + i^k y}^2.$$

The [[proof|A67QNADARQ]] treats the real case in full and derives the complex case from it.

## Remarks

### Recovering the dot product from lengths

Suppose that you know only the Euclidean length on $\mathbb{R}^2$.
Take $x = (1, 2)$ and $y = (3, -1)$, so that $x + y = (4, 1)$ and $x - y = (-2, 3)$.
The real formula gives
$$\ip{x}{y} = \frac14\big(\norm{(4, 1)}^2 - \norm{(-2, 3)}^2\big) = \frac14(17 - 13) = 1.$$
Check: the dot product is $1 \cdot 3 + 2 \cdot (-1) = 1$.
The theorem says that this recipe always produces an inner product when the parallelogram law holds, and never when it fails.

### Why each hypothesis is needed

The parallelogram law must hold for all pairs, not for some.
The [[maximum norm on $\mathbb{R}^2$|J5V8HEYXCM]] satisfies it for $x = (1, 0)$ and $y = (2, 0)$, but it fails for $x = (1, 0)$ and $y = (0, 1)$, where it gives $2 \neq 4$.
No inner product induces this norm.

The proof also uses that $\norm{\cdot}$ is a norm, and in particular its triangle inequality.
The law alone gives additivity of the candidate inner product, and additivity gives homogeneity only for rational scalars.
The triangle inequality makes $t \mapsto \norm{tx + y}$ continuous, and continuity extends homogeneity to real scalars.
Some regularity of this kind is needed, because there are [[additive functions|KF719SZD5T]] from $\mathbb{R}$ to $\mathbb{R}$ that are not linear.

### What it gives you

The $p$-norm on $\mathbb{R}^n$ with $n \geq 2$ comes from an inner product only for $p = 2$, since $e_1$ and $e_2$ give
$$\norm{e_1 + e_2}_p^2 + \norm{e_1 - e_2}_p^2 = 2 \cdot 2^{2/p},$$
and this equals $2 + 2 = 4$ only for $p = 2$.
A norm comes from an inner product as soon as its restriction to every subspace of dimension $2$ does, because the law involves only two vectors at a time.
A complete normed space whose norm satisfies the law is a [[Hilbert space|HM2HHE3J51]].

### The converse

The theorem is an equivalence, so the converse of each direction is the other direction.
The direction from 1 to 2 is the [[parallelogram law|026HPGYGS4]] itself, and it follows by expanding two squares.
The direction from 2 to 1 is the real content.

### Generalizations

Several weaker conditions on a norm are also equivalent to condition 1.
One of them is the parallelogram law for unit vectors $x$ and $y$ only.
The same functional equation, $f(x + y) + f(x - y) = 2f(x) + 2f(y)$, is studied for general functions $f$ as the [[quadratic functional equation|7MZGZFQ347]].

## History

Pascual Jordan and John von Neumann published the theorem in 1935.

## Explanations

### L1 human

Some ways to measure length come from an inner product, which also measures angles, and some do not.
The theorem gives a test.
A length comes from an inner product exactly when it obeys the parallelogram law.
For the ordinary length in the plane, the unit square has two diagonals of length $\sqrt{2}$, and $2 + 2 = 2 + 2$, so the test passes.
For the "largest coordinate" length, both diagonals of the unit square have length $1$, and $1 + 1 \neq 2 + 2$, so the test fails.

### L2 human

Here is a typical use: is the taxicab norm $\norm{x}_1 = \abs{x_1} + \abs{x_2}$ on $\mathbb{R}^2$ induced by an inner product?
Try $x = (1, 0)$ and $y = (0, 1)$.
Both have norm $1$, and both diagonals $(1, 1)$ and $(1, -1)$ have norm $2$.
The law would need
$$\norm{x + y}_1^2 + \norm{x - y}_1^2 = 4 + 4 = 8 \quad \text{to equal} \quad 2 \cdot 1 + 2 \cdot 1 = 4,$$
and it does not, so no inner product induces the taxicab norm.
One failing pair settles the question, while a proof that a norm does come from an inner product needs the law for all pairs.

Watch out over $\mathbb{C}$.
The real formula gives only the real part of the complex inner product.
For $x = 1$ and $y = i$ in $\mathbb{C}$ it gives $\frac14(2 - 2) = 0$, while $\ip{1}{i} = 1 \cdot \overline{i} = -i$.

### L3 human

The theorem characterizes Hilbert spaces among Banach spaces, because completeness is a property of the norm alone.
Its proof is a study of a functional equation.
The parallelogram law is the quadratic functional equation for $f(x) = \norm{x}^2$, and the inner product is the associated biadditive form.
Additivity gives linearity over $\mathbb{Q}$, and the continuity of the norm extends it to $\mathbb{R}$, as for the Cauchy functional equation.
Over $\mathbb{C}$, the extra structure is multiplication by $i$, which is an isometry, and this forces the real inner product to be the real part of a complex one.
