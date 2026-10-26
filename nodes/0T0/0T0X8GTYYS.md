---
tag: 0T0X8GTYYS
kind: statement
role: proposition
name: Determinant is a coefficient of the characteristic polynomial
msc: [15A15, 15A18]
uses: [039HF58KQ5, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Statement

Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
Then the constant coefficient of the [[characteristic polynomial|0VSSPAFM2C]] $p_A(t) = \det(t I_n - A)$ is
$$p_A(0) = (-1)^n \det A,$$
where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

The proof sets $t = 0$: $p_A(0) = \det(-A) = (-1)^n \det A$.
So, over a field, $0$ is an eigenvalue of $A$ if and only if $\det A = 0$.

## Explanations

### L1 human

The constant term of the characteristic polynomial is the determinant, up to a sign.
This follows when we put $t = 0$.
So a matrix with determinant zero has the eigenvalue $0$.
