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

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $(V, \norm{\cdot})$ be a [[normed vector space|00A0RPAQ8A]] over $\mathbb{K}$.
Then the following are equivalent.

1. There is an [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ on $V$ whose [[induced norm|0KG4D8AP6G]] is $\norm{\cdot}$, that is, $\norm{x}^2 = \ip{x}{x}$ for all $x \in V$.
2. The norm satisfies the parallelogram law: $\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2$ for all $x, y \in V$.

When these hold, the inner product is unique, and the [[polarization identity|05FKHRT0B4]] gives it.
For $\mathbb{K} = \mathbb{R}$ it is
$$\ip{x}{y} = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right),$$
and for $\mathbb{K} = \mathbb{C}$, with $\ip{\cdot}{\cdot}$ linear in the first argument, it is
$$\ip{x}{y} = \frac14 \sum_{k=0}^{3} i^k \norm{x + i^k y}^2.$$

The [[proof|A67QNADARQ]] gives all details of the real case and derives the complex case from it.

## Remarks

### Why each hypothesis is needed

- The parallelogram law must hold for all pairs. The [[maximum norm on $\mathbb{R}^2$|J5V8HEYXCM]] satisfies it for $x = (1, 0)$ and $y = (2, 0)$, but it fails for $x = (1, 0)$ and $y = (0, 1)$, and no inner product induces this norm.
- The triangle inequality of the norm is used in the proof, to show that $t \mapsto \norm{tx + y}$ is continuous. Without some regularity, additivity alone does not give homogeneity over $\mathbb{R}$, since there are additive functions $\mathbb{R} \to \mathbb{R}$ that are not linear.

### Consequences

- The $p$-norm on $\mathbb{R}^n$ with $n \geq 2$ comes from an inner product only for $p = 2$.
- A norm comes from an inner product as soon as its restriction to every subspace of dimension $2$ does. The reason is that the law involves only two vectors.
- A Banach space whose norm satisfies the law is a [[Hilbert space|HM2HHE3J51]].

### Converse

The theorem is an equivalence, so the converse of each direction is the other direction.
The direction from 1 to 2 is the [[parallelogram law|026HPGYGS4]].

### Generalizations

The Wikipedia article on the polarization identity lists other conditions on a norm that are equivalent to condition 1.
An example is the parallelogram law for unit vectors only.

## History

The theorem carries the names of Jordan and von Neumann.

## Explanations

### L1 human

Some ways to measure length come from an inner product, which also measures angles, and some do not.
This theorem gives a test: a length comes from an inner product exactly when it obeys the parallelogram law.
For the ordinary length in the plane, the unit square has diagonals of length $\sqrt{2}$, and $2 + 2 = 2 + 2$, so the test passes.
For the "largest coordinate" length, both diagonals have length $1$, and $1 + 1 \neq 2 + 2$, so the test fails.

### L2 human

Worked example: we recover the dot product of $\mathbb{R}^2$ from the Euclidean norm.

1. Let $x = (1, 2)$ and $y = (3, -1)$. Then $x + y = (4, 1)$ and $x - y = (-2, 3)$.
2. The norms are $\norm{x + y}^2 = 16 + 1 = 17$ and $\norm{x - y}^2 = 4 + 9 = 13$.
3. The formula gives $\ip{x}{y} = \frac14(17 - 13) = 1$.
4. The dot product is $1 \cdot 3 + 2 \cdot (-1) = 1$, the same value.

The typical use is to prove that a normed space, such as $\ell^p$ for $p \neq 2$, is not an inner product space.
Another use is to build an inner product from a norm that has the law.
A trap: over $\mathbb{C}$ the real formula is not enough.
It gives only the real part of the inner product.

### L3 human

The theorem characterizes Hilbert spaces among Banach spaces, because completeness is a property of the norm alone.
The proof is a study of a functional equation.
The parallelogram law is the [[quadratic functional equation|7MZGZFQ347]] for $f(x) = \norm{x}^2$, and the inner product is the associated biadditive form.
Additivity gives linearity over $\mathbb{Q}$, and the continuity of the norm extends it to $\mathbb{R}$, as for the Cauchy functional equation of [[additive functions|KF719SZD5T]].
Over $\mathbb{C}$, the extra structure is the multiplication by $i$, which is an isometry.
This forces the real inner product to be the real part of a complex one.
