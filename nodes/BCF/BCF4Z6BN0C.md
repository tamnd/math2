---
tag: BCF4Z6BN0C
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

Let $A = \operatorname{diag}(1, 2, 3)$, the $3 \times 3$ diagonal matrix with diagonal entries $1$, $2$ and $3$.
We compute $\det(A - tI)$ and $\det(tI - A)$ and compare them.

1. The matrix $A - tI$ is diagonal with entries $1 - t$, $2 - t$ and $3 - t$, so the [[determinant of a triangular matrix|0K1KKMFHYH]] gives
$$\det(A - tI) = (1 - t)(2 - t)(3 - t).$$
2. Take a factor $-1$ out of each of the three brackets and expand:
$$(1 - t)(2 - t)(3 - t) = -(t - 1)(t - 2)(t - 3) = -t^3 + 6t^2 - 11t + 6.$$
   Its leading coefficient is $-1$.
3. By the [[definition|039HF58KQ5]], the characteristic polynomial is
$$p_A(t) = \det(tI - A) = (t - 1)(t - 2)(t - 3) = t^3 - 6t^2 + 11t - 6,$$
   which is monic.
4. So $\det(A - tI) = (-1)^3 p_A(t) = -p_A(t)$, and the two polynomials are different.

## Remarks

The two polynomials have the same roots $1$, $2$ and $3$, so either one finds the eigenvalues.
They differ in every coefficient, and that matters as soon as you use the coefficients.
The constant term of $p_A$ is $(-1)^3 \det A = -6$, while the constant term of $\det(A - tI)$ is $\det A = 6$.
A formula such as the Cayley-Hamilton expression for $A^{-1}$ gives a wrong sign if you feed it the coefficients of the wrong polynomial.

Change the size to $2 \times 2$, say $A = \operatorname{diag}(1, 2)$.
Then $\det(A - tI) = (1 - t)(2 - t) = (t - 1)(t - 2) = p_A(t)$, because $(-1)^2 = 1$.
So the two conventions agree for every even size and differ by a sign for every odd size.

## Explanations

### L1 human

Some books use $\det(A - tI)$ and others use $\det(tI - A)$.
For a $3 \times 3$ matrix the two answers are negatives of each other, since each of the three rows changes sign.
Only $\det(tI - A)$ starts with $+t^3$, and that is the one we call the characteristic polynomial.

### L2 human

Before you use a coefficient formula, find out which convention the book uses.
With $\det(tI - A) = t^3 + c_2 t^2 + c_1 t + c_0$, the coefficient $c_2$ is $-\operatorname{tr} A$ and $c_0$ is $-\det A$.
For $\operatorname{diag}(1, 2, 3)$ that gives $c_2 = -6$ and $c_0 = -6$, which matches step 3.
Watch out: the polynomial in step 2 has $+6t^2$ and $+6$, so reading the trace or the determinant from it with the same formulas gives the wrong signs.
