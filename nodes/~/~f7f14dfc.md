---
tag: ~f7f14dfc
kind: example
name: The polynomial det(A - tI) for a 3 by 3 matrix
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
not_instance_of:
  - target: 0VSSPAFM2C
    note: For odd n, det(A - tI) has leading coefficient -1, so it is not the monic characteristic polynomial det(tI - A)
uses: [039HF58KQ5, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Formal definition
---

## Example

Let $A = \operatorname{diag}(1, 2, 3)$.

1. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det(A - tI) = (1 - t)(2 - t)(3 - t)$.
2. $(1 - t)(2 - t)(3 - t) = -(t - 1)(t - 2)(t - 3) = -t^3 + 6t^2 - 11t + 6$. Its leading coefficient is $-1$.
3. By the [[definition|039HF58KQ5]], $p_A(t) = \det(tI - A) = (t - 1)(t - 2)(t - 3) = t^3 - 6t^2 + 11t - 6$, which is monic.
4. So $\det(A - tI) = (-1)^3 p_A(t) = -p_A(t)$, and $\det(A - tI) \ne p_A(t)$.

## Remarks

- The two polynomials have the same roots, so both give the eigenvalues $1, 2, 3$.
- For even $n$ they are equal, since $(-1)^n = 1$.
- The sign matters for the coefficients: the constant term of $p_A$ is $(-1)^n \det A$.

## Explanations

### L1 human

Some books use $\det(A - tI)$ and others use $\det(tI - A)$.
For a $3 \times 3$ matrix, the two differ by a sign.
Only $\det(tI - A)$ has leading coefficient $1$.

### L2 human

The typical lesson is to fix one convention before using the coefficient formulas.
A trap is to apply the Cayley-Hamilton inverse formula with the coefficients of $\det(A - tI)$ for odd $n$.
