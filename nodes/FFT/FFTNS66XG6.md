---
tag: FFTNS66XG6
kind: example
name: Discontinuous additive functions via a Hamel basis
msc: [39B22, 15A03]
instance_of: [KF719SZD5T]
uses: [0KCQ9Y3QKA, 0HTGB13FE2, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
---

## Example

View $\R$ as a vector space over the field $\Q$ of rational numbers.
The numbers $1$ and $\sqrt{2}$ are linearly independent over $\Q$, because $\sqrt{2}$ is irrational.
By the [[axiom of choice|0HTGB13FE2]], this independent set extends to a [[basis|0KCQ9Y3QKA]] $B$ of $\R$ over $\Q$, called a Hamel basis.
Every real $x$ is then a unique finite sum $x = \sum_{b \in B} q_b(x)\, b$ with rational coefficients $q_b(x)$, almost all zero.
Define $f \colon \R \to \R$ by $f(x) = q_1(x)$, the coefficient of the basis vector $1$.

Check of additivity: the coefficients of $x + y$ are the sums of the coefficients of $x$ and $y$, so $f(x + y) = f(x) + f(y)$.
So $f$ is an [[additive function|KF719SZD5T]].
It is not of the form $f(x) = cx$: $f(1) = 1$ would force $c = 1$, but $f(\sqrt{2}) = 0 \ne \sqrt{2}$.
Hence $f$ is not [[continuous|0X3WGX95FE]], since every continuous additive function is linear.
One can also see this directly: $f$ takes only rational values, while a continuous function on $\R$ with only rational values is constant, and $f(0) = 0 \ne 1 = f(1)$.

## Explanations

### L1 human

Imagine writing every real number in a strange coordinate system with infinitely many rational coordinates.
The function $f$ just reads off one coordinate.
Reading a coordinate respects addition, so $f$ is additive.
Yet $f$ jumps around wildly and cannot be drawn, because the coordinate system itself comes from the axiom of choice.
