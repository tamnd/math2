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

Let $Q_1 = x^2 + y^2$ and $Q_2 = x^2 + 2y^2$ on $\Q^2$.

1. Their matrices are $\operatorname{diag}(1, 1)$ and $\operatorname{diag}(1, 2)$, with determinants $1$ and $2$.
2. The quotient $2 / 1 = 2$ is not the square of a rational number, since $\sqrt 2$ is irrational.
3. So the [[discriminants|MZFRXECCMC]] $1$ and $2$ are different square classes of $\Q^\times$.
4. By [[the invariance theorem|WYQGZK8GFT]], $Q_1$ and $Q_2$ are not equivalent over $\Q$.

## Remarks

The same argument in matrix form is in [[the example on congruence over the rationals|R4ZDJG99Q0]].
Over $\R$ the two forms are equivalent: with $y' = \sqrt 2\, y$, $Q_2 = x^2 + y'^2$.
Both have signature $(2, 0, 0)$, and both discriminants are positive, which is the only square class condition over $\R$.
Over $\F_7$ they are also equivalent, since $2 = 3^2 = 9$ there is a square.
Over $\F_3$ they are not equivalent, since $2$ is not a square in $\F_3$.
So the same pair of forms is equivalent or not according to the field, and the discriminant detects the difference.

## Explanations

### L1 human

To turn $x^2 + 2y^2$ into $x^2 + y^2$ we would need to replace $y$ by $\sqrt 2\, y$.
Over the rational numbers this is not allowed, because $\sqrt 2$ is not rational.
The discriminant turns this idea into a proof: no change of variables at all can work.

### L2 human

The typical use: one determinant computation proves non-equivalence over $\Q$.
A trap: the test only works in one direction.
Equal discriminants over $\Q$ do not prove equivalence; $x^2 + 3y^2$ and $2x^2 + 6y^2$ have equal discriminants and are not equivalent.
