---
tag: ~fba77cf4
kind: statement
role: proposition
name: Trace is a coefficient of the characteristic polynomial
msc: [15A15, 15A18]
uses: [~ebbd8e12, ~5bc48bd1]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Statement

Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
Then the coefficient of $t^{n-1}$ in the [[characteristic polynomial|~14b846dc]] $p_A(t) = \det(t I_n - A)$ is $-\tr A$, where $\tr$ is the [[trace|~c290a0d4]].
So $p_A(t) = t^n - (\tr A)\, t^{n-1} + \cdots$.

## Remarks

In the Leibniz expansion of $\det(t I_n - A)$, only the product of the diagonal entries $(t - a_{11}) \cdots (t - a_{nn})$ contributes to $t^{n-1}$.
For $n = 2$, $p_A(t) = t^2 - (\tr A) t + \det A$.
Together with [[the constant coefficient|~d755b09d]], it shows that $\tr$ and $\det$ are invariants of similarity.

## Explanations

### L1 human

The characteristic polynomial contains the trace as its second coefficient, with a minus sign.
For a $2 \times 2$ matrix, the full polynomial is $t^2 - (\text{trace})\,t + \text{determinant}$.
So the trace and the determinant are part of the information of the characteristic polynomial.
