---
tag: C18PABZVSN
kind: example
name: The forms x² + y² and x² + 2y² have different discriminants over Q
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug2
instance_of: [MZFRXECCMC]
illustrates: [WYQGZK8GFT]
uses: [MZFRXECCMC, WYQGZK8GFT, R4ZDJG99Q0]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Example

The forms $Q_1 = x^2 + y^2$ and $Q_2 = x^2 + 2y^2$ on $\mathbb{Q}^2$ have different [[discriminants|MZFRXECCMC]], so no rational change of variables turns one into the other.

1. The matrices are $\operatorname{diag}(1, 1)$ and $\operatorname{diag}(1, 2)$, with determinants $1$ and $2$.
2. The quotient $2 / 1 = 2$ is not the square of a rational number, because $\sqrt 2$ is irrational.
3. So the discriminants $1$ and $2$ are different elements of $\mathbb{Q}^\times / \mathbb{Q}^{\times 2}$.
4. By [[the invariance theorem|WYQGZK8GFT]], equivalent forms have the same discriminant, so $Q_1$ and $Q_2$ are not equivalent over $\mathbb{Q}$.

## Remarks

### What the example shows

The argument needs no search over substitutions.
One determinant each and one irrationality fact rule out every invertible rational matrix $P$ at once.
The same argument in matrix language appears in [[the example on congruence over the rationals|R4ZDJG99Q0]], which shows that $I$ and $\operatorname{diag}(1, 2)$ are not congruent over $\mathbb{Q}$.

### What changes with the field

Over $\mathbb{R}$ the two forms are equivalent: with $y' = \sqrt 2 \, y$ we get $Q_2 = x^2 + y'^2$.
Both are positive definite with two positive squares, and over $\mathbb{R}$ the only square class condition is the sign, which is positive for both.
Over $\mathbb{F}_7$ they are also equivalent, since $3^2 = 9 = 2$ there, so $2$ is a square.
Over $\mathbb{F}_3$ they are not equivalent, since the only nonzero square of $\mathbb{F}_3$ is $1$.
So the same pair of forms is equivalent or not according to the field, and in each case the discriminant gives the answer.

## Explanations

### L1 human

To turn $x^2 + 2y^2$ into $x^2 + y^2$, you would like to replace $y$ by $\sqrt 2 \, y$.
Over the rational numbers this is not allowed, because $\sqrt 2$ is not a fraction.
The discriminant turns this idea into a proof that no change of variables with fractions can work.

### L2 human

The typical use is one determinant computation that proves non-equivalence over $\mathbb{Q}$.
For example, $x^2 + 5y^2$ and $x^2 + 10y^2$ have determinants $5$ and $10$, and $10/5 = 2$ is not a rational square, so they are not equivalent.
Watch out: the test works in one direction only.
The forms $x^2 + 3y^2$ and $2x^2 + 6y^2$ have determinants $3$ and $12$, whose quotient $4$ is a square, but they are still not equivalent: the second takes the value $2$ at $(1, 0)$ and the first never does, as the [[discriminant|MZFRXECCMC]] page proves.
